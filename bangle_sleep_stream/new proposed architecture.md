## 1. Context and goals
### 1.1. Current implementation (what exists now)

From the README you supplied, the current system works as follows:[^1]

- On the **watch**:
    - A boot service (`sleepstream.boot.js`) listens to Bangle.js 2 “health” events roughly every 10 minutes.
    - When a health event fires, it runs a simple on‑watch classifier (essentially the same as the official `sleeplog` app) using:
        - Movement,
        - Heart rate (BPM),
        - Consecutive sleep tracking,
        - HRM‑based wear detection.
    - It classifies into 5 states:
        - 0 = unknown
        - 1 = not_worn
        - 2 = awake
        - 3 = light_sleep
        - 4 = deep_sleep
    - It sends a JSON packet over BLE UART, e.g.:
`{"t":"sleepstream","v":1,"seq":1,"ts":1773846600,"status":2,"consecutive":0,"source_mode":0,"movement":595,"bpm":56}`
- On the **receiver** side:
    - A Python script subscribes to UART notifications, decodes the JSON, and writes each row into SQLite (`sleepstream.db`).[^1]

Key constraints:

- Hardware: Bangle.js 2, with 3‑axis accelerometer and PPG heart‑rate sensor, nRF52840 MCU, 256 kB RAM.[^2][^3]
- Processing: JavaScript on Espruino, so algorithms must be simple, streaming, and efficient.
- Current temporal resolution: effectively 10‑minute “snapshots” driven by the health event.


### 1.2. Target: 4‑stage sleep with REM

The new target is to classify 4 sleep stages:

- wake
- light (N1/N2)
- deep (N3)
- REM

using **only** wrist accelerometer and PPG, without EEG, and without heavy ML models. The classifier must:

- Run **on‑watch** in JavaScript.
- Use short‑timescale features (30–60‑second epochs), not just 10‑minute averages.
- Use a very small set of features:
    - Movement (activity count),
    - Mean HR,
    - Very simple HRV measures (e.g., RMSSD, SDNN‑like), computed from beat‑to‑beat intervals.

The BLE protocol and receiver can stay mostly the same: the boot service remains the single source of truth for current sleep stage and continues to send JSON packets; we only change how `status` is computed and optionally add fields.

***

## 2. Base research: what works for wrist PPG + accelerometer sleep staging

### 2.1. What published algorithms use

Several research‑grade and commercial algorithms achieve multi‑stage sleep classification using wrist accelerometer + PPG‑derived HR/HRV:

- **Philips “It is All in the Wrist” (Wulterkens et al., 2021)**
    - Wrist device with 3‑axis accelerometer (128 Hz) and green PPG (32 Hz).[^4]
    - Pipeline:
        - Extract inter‑beat intervals (IBIs) from PPG.
        - Compute a large set of HRV features per 30‑s epoch.
        - Combine with an accelerometer activity count per epoch.
        - Feed to a bidirectional LSTM network.
    - Results (292 mostly clinical recordings):
        - 4‑class (wake, N1+N2, N3, REM) κ ≈ 0.62, overall accuracy ≈ 76%.[^4]
        - REM vs non‑REM: κ ≈ 0.69, sensitivity ≈ 78%, specificity ≈ 95%.[^4]
- **Computationally efficient PPG‑based staging (Fonseca et al., 2023)**
    - Similar sensors, but replace manual feature extraction with an end‑to‑end neural net.[^5]
    - Inputs to the model:
        - Instantaneous HR (IHR) time series at 10 Hz (from PPG IBIs),
        - A 30‑s accelerometer activity count.
    - Results (394 recordings):
        - 4‑class median κ ≈ 0.64, accuracy ≈ 77.8%.[^5]
        - REM vs rest κ ≈ 0.75, sensitivity ≈ 77.5%, specificity ≈ 97.6%.[^5]
- **SLAMSS (Song et al., 2023)**
    - Designed to use only **coarse** HR features that PPG wearables can provide.[^6]
    - Input per 30‑s epoch:
        - Actigraphy activity count.
        - Mean heart rate (HRM).
        - Standard deviation of HR within epoch (HRSD).
    - With these three signals and an LSTM over short windows, they achieve:
        - ~70–72% accuracy for 4‑stage (wake / light / deep / REM),
        - REM sensitivity in the ~63–70% range.[^6]
- **Fitbit and Firstbeat devices**
    - Combine accelerometer + PPG HR/HRV (and sometimes respiratory rate) in proprietary models.[^7][^8]
    - Validation reports:
        - Fitbit Charge devices: good REM accuracy (~0.82–0.86), decent deep‑sleep accuracy (~0.78), but poorer performance distinguishing light sleep stages.[^9][^10]
        - Firstbeat: excellent specificity and good accuracy for REM and slow‑wave sleep, weaker on light NREM.[^8]
- **HRV‑only, rule‑based REM and slow‑wave sleep estimators**
    - Yoon et al. (2017) propose a REM estimator using only ECG R‑R intervals.[^11]
        - They compute a set of HRV parameters per 30‑s epoch, combine them into an “autonomic dynamics” feature, and detect REM via an adaptive threshold + time‑of‑night rules.
        - Achieved κ ≈ 0.61–0.63 and ≈87% accuracy for REM vs non‑REM (binary).[^12][^11]
    - A companion algorithm detects slow‑wave sleep using a stability metric from R‑R intervals plus simple rules about when SWS usually occurs in the night, with κ ≈ 0.56 and ~90% accuracy for SWS vs others.[^13]


### 2.2. Key physiological signals for REM vs NREM

Studies of HRV and autonomic regulation across sleep stages show the following:[^14][^15][^16][^17]

- **NREM (especially deep N3)**:
    - Lower mean HR (longer R‑R intervals).
    - High parasympathetic (vagal) tone, low sympathetic tone.
    - Higher high‑frequency (HF) HRV power, indicating stable, restful autonomic state.[^16][^17]
- **REM**:
    - Mean HR elevated relative to NREM, closer to wake values.
    - Autonomic instability: fluctuating sympathetic and parasympathetic activity, reflected as larger and more frequent HR accelerations and decelerations.[^18][^16]
    - In HRV metrics, increased low‑frequency power and LF/HF ratio, and more irregular, burst‑like changes.

In time‑domain terms:

- **RMSSD** (root mean square of successive RR differences):
    - Measures beat‑to‑beat variance in HR, reflecting short‑term parasympathetic activity.[^19][^20][^15][^14]
    - Straightforward to compute from IBIs, widely used in wearables.
- **SDNN / SDRR** (standard deviation of RR intervals):
    - Captures overall variability (short and long term).[^20][^15][^19]

REM tends to show:

- Higher **mean HR** vs NREM,
- Often elevated RMSSD/SDNN vs N3 because the autonomic system is more unstable,
- Distinct epoch‑to‑epoch HR swings compared with stable N3.


### 2.3. Why 30–60‑second epochs are essential

Every successful wearable sleep‑staging algorithm works at about **30–60‑second resolution**, not 10 minutes:[^11][^6][^4][^5]

- Sleep scoring standards (AASM) define 30‑s epochs, and stage transitions are annotated at that granularity.[^21]
- Autonomic changes (e.g., REM onset, arousals) and movement bursts occur over tens of seconds, not tens of minutes.

Using 10‑minute averages of HR and motion:

- **Erases temporal structure**: quick HR accelerations/decelerations and short REM bouts are smoothed away.
- **Breaks HRV**: HRV time‑domain measures like RMSSD and SDNN must be computed from beat‑to‑beat intervals over relatively short, roughly stationary segments (1–5 minutes).[^17][^20][^14]
- **Overlaps multiple stages**: a 10‑minute window may contain N2→N3 or N2→REM transitions, making any single label meaningless.

Therefore, to detect REM at all, you must switch from 10‑minute to ~30–60‑second windows and access beat‑level RR intervals (or at least per‑second HR) during the night.

***

## 3. Design reasoning: mapping research → Bangle.js‑compatible plan

Given:

- Hardware: Bangle.js 2 with accelerometer + PPG and modest MCU.[^3][^2]
- Environment: Espruino JS, limited CPU/RAM, best for streaming, low‑complexity computations.
- Existing app: `sleepstream.boot.js` doing 10‑minute snapshots and sending JSON over BLE.[^1]

The design aims to:

1. **Add an internal, 30–60‑second sleep staging pipeline** that runs continuously at night:
    - Works like actigraphy + HRV research systems, but with very few features.
    - Implementation purely in JS with integer/fixed‑point friendly operations.
2. **Expose the resulting stage through your existing 10‑minute health event**:
    - Instead of recomputing stage from scratch at each health event, the handler reads the latest 30‑s stage from the new classifier and sends it in the JSON.
3. **Preserve your BLE protocol and receiver** as much as possible:
    - Optionally extend `status` to include REM or a `rem` flag, but not break existing consumers drastically.

### 3.1. Minimum viable feature set

Following research like SLAMSS and Philips/Firstbeat work, the minimal per‑epoch feature set that can separate REM, deep, light, and wake is:[^12][^6][^11][^4]

- **Movement (activity)**:
    - An activity count or variance of accelerometer magnitude across the epoch.[^6][^4][^5]
    - REM and deep: very low; wake: high; light: in‑between.
- **Mean HR**:
    - Calculated from RR intervals in the epoch; deep N3: lowest HR; REM: higher HR, near wake; light NREM: mid‑range.[^16][^17]
- **Simple HRV measures**:
    - **RMSSD** – beat‑to‑beat variation.[^19][^20][^14]
    - **SDNN‑like** – overall variability (using SD of RR or SD of HR within the epoch).[^20][^19][^6]
- **Context**:
    - Time since sleep onset (REM latency constraint: no REM before ~60–70 min; more REM later).[^22][^23][^24]

These choices are grounded directly in literature but are **computationally cheap**: sums, differences, squares, square roots, and absolute values—well within Bangle.js capabilities.

***

## 4. Proposed on‑watch architecture

### 4.1. New continuous “sleep monitoring” mode

Add to `sleepstream.boot.js`:

- A **sleep monitoring state** that:
    - Activates during a configured window (e.g., 21:00–09:00) or when simple heuristics indicate probable sleep.
    - Deactivates on clear wakefulness or user interaction.

When active:

- Configure **accelerometer** at ~25 Hz.
- Enable **HRM** for continuous beats or per‑second HR.[^25][^26]

Maintain per‑epoch buffers:

- `accelMagBuffer`: array of accelerometer magnitude samples (e.g., |x|+|y|+|z|).
- `ibiBuffer`: array of inter‑beat intervals in ms (or per‑second HR samples if IBIs are not directly available).

And an epoch manager:

- `epochStartTime` (Unix timestamp).
- `epochLen` (e.g., 30 s).

When `now - epochStartTime >= epochLen`:

- Pass the buffers to the **feature extractor**.
- Reset the buffers.
- Advance `epochStartTime`.


### 4.2. Feature extraction module

In `sleepstream.js`, implement a module like:

```js
function computeEpochFeatures(epochStart, accelMagBuffer, ibiBufferOrHr) {
  // returns { epochStart, activity, meanHR, rmssd, sdRR, validBeats, flags }
}
```


#### 4.2.1. Activity (movement)

Approximating actigraphy activity count:[^4][^5][^6]

1. Compute mean magnitude:
$m = \frac{1}{N} \sum_i mag_i$.
2. Activity = Σ |mag_i − m| (or mean absolute deviation).

This is O(N) and uses only subtraction and abs; it produces a scalar “how much movement” score per epoch.

#### 4.2.2. Mean HR

With IBIs in ms:

- Mean RR: $\overline{RR} = \frac{1}{N} Σ RR_i$.
- Mean HR (bpm): $HR = 60000 / \overline{RR}$.[^15][^20]

Fallback: if only HR per second is available, average those.

#### 4.2.3. RMSSD

Time‑domain HRV measure defined as the root mean square of successive RR differences.[^14][^15][^19][^20]

- Take successive differences: $d_i = RR_{i} − RR_{i-1}$.
- Compute mean of squared differences: $\frac{1}{N-1} Σ d_i^2$.
- RMSSD = square root of that.[^19][^20]

RMSSD reflects short‑term, beat‑to‑beat variability, strongly linked to parasympathetic activity and widely used in wearable HRV apps.[^27][^14][^19]

#### 4.2.4. SDNN‑like metric

To get a coarser “overall variability” measure similar to SDNN:[^20][^14][^19]

- Compute standard deviation of RR intervals in the epoch:
$SDNN ≈ \sqrt{ \frac{1}{N} Σ (RR_i − \overline{RR})^2 }$.

Or if using 1‑s HR samples, compute SD of HR within the epoch.

#### 4.2.5. Validity flags

Mark epochs where HR/IBI data is insufficient or too noisy:

- `lowBeats`: if fewer than some minimum count (e.g., <10 RR intervals in 30 s).
- `noisy`: if RMSSD or SDNN is absurd (above some hard cap) or IBIs contain many outliers.

The classifier can fall back to movement‑only heuristics or mark these epochs as wake/unknown.

### 4.3. Night‑level statistics and context

Maintain, over the course of the night:

- `sleepStartTime`: timestamp of first confirmed sleep epoch.
- HR distribution during sleep:
    - E.g., a histogram of HR values (binned in 1‑bpm buckets) updated per epoch when `meanHR` is valid.
    - From that histogram, periodically estimate:
        - HR 20th percentile (`hrP20`),
        - HR 50th percentile (`hrP50`),
        - HR 80th percentile (`hrP80`).

Use these as “adaptive thresholds” for deep vs REM:

- Deep tends to occupy the lowest HR quantiles.[^13][^16]
- REM tends to have HR nearer or above median sleep HR.[^17][^16]

Also compute `minutesSinceSleepOnset = (epochStart - sleepStartTime) / 60000` and use it for REM latency constraints.[^23][^24][^22]

***

## 5. Rule‑based 4‑stage classifier

Implement a state machine in `sleepstream.js` that outputs a stage label per epoch, using:

```text
0 = UNKNOWN
1 = NOT_WORN
2 = WAKE
3 = LIGHT
4 = DEEP
5 = REM   (new)
```

(You can either map this `5` into a new `status` code or surface it in an extra field.)

### 5.1. Wear vs not_worn

Reuse your current wear detection logic (likely based on very low variance HR and accelerometer, or built‑in HRM status):[^1]

- If the watch isn’t being worn (HRM indicates off‑skin, accelerometer nearly static in an odd orientation):
    - Stage = `NOT_WORN`.
    - Skip further classification for that epoch.


### 5.2. Wake vs sleep

Within worn epochs, first determine if the user is awake or asleep using movement + HR:

- If activity > `A_WAKE_HIGH` (threshold) → WAKE.
- Else if meanHR is close to daytime baseline (e.g., > `hrWakeThreshold`) → WAKE.
- Else → candidate sleep.

This parallels actigraphy + HR methods where high activity and high HR reliably indicate wakefulness.[^5][^4]

To avoid jitter:

- Require K consecutive “candidate sleep” epochs before switching from WAKE → SLEEP.
- Require K consecutive “wake‑like” epochs before switching back.


### 5.3. Deep vs non‑deep sleep

Within sleep, identify deep N3 using:

- Very low activity (`activity < A_DEEP_MAX`).
- Low HR relative to night distribution (`meanHR < hrP20`).[^13][^16]
- Optionally, HRV indicating a stable, vagal‑dominated state:
    - RMSSD and SDNN not extremely high (indicating stable rhythm).

Heuristic:

- If `activity` is below `A_DEEP_MAX` and `meanHR` is below `hrP20`, and no obviously bad HRV flags, mark epoch as deep candidate.
- Require ≥ 2 consecutive deep candidates to call it `DEEP`, to avoid misclassifying occasional still epochs.

This reflects that slow‑wave sleep episodes are typically clusters of low‑HR, low‑movement epochs.[^16][^13]

### 5.4. REM vs light sleep

Among sleep epochs not classified as deep, decide REM vs light:

REM signatures:

- Movement: very low (muscle atonia), but not necessarily quite as “flat” as deep.
- HR: elevated vs N3 and often vs median NREM; close to or above median HR across sleep epochs.[^17][^16]
- Autonomic instability: more frequent HR accelerations/decelerations, reflected in higher RMSSD/SDNN and sometimes larger epoch‑to‑epoch HR jumps.[^18][^16][^4]
- Timing: REM typically does **not** appear in the first 60–70 minutes, and its proportion increases later in the night.[^24][^28][^22][^23]

Heuristic for REM candidate:

- `activity < A_REM_MAX` (stillness requirement).
- `minutesSinceSleepOnset ≥ MIN_REM_LATENCY` (e.g., 60–70).[^22][^23][^24]
- `meanHR > hrP50` or `meanHR` higher than a non‑REM baseline.
- RMSSD or SDNN ≥ thresholds indicating more variability (relative to NREM).
- Optional: `|meanHR_now − meanHR_prevEpoch| > ΔHR_REM_MIN` to capture HR surges.

If a sleep epoch is:

- Not deep,
- Meets movement + HR + HRV + timing criteria,

then classify as REM. Otherwise classify as **light**.

To stabilize:

- Only confirm REM when ≥ 2 consecutive REM candidates appear; isolated REM candidates can be downgraded to light.

This rule‑based design echoes Yoon’s HRV‑only REM detector, which uses an HRV‑derived “autonomic dynamics” feature, an adaptive threshold, and time‑of‑night rules, and achieved κ ≈ 0.61 and 87% accuracy for REM vs non‑REM.[^11][^12]

### 5.5. Temporal smoothing and cycle logic

Sleep stages are not random; they follow ultradian cycles (~90 minutes) and have some structural rules.[^28][^22]

Add a simple smoothing layer:

- Maintain a ring buffer of last N epoch decisions (e.g., N=4–6).
- Apply:
    - **Minimum segment lengths**:
        - REM: require at least 2 contiguous REM epochs.
        - DEEP: require at least 2 contiguous deep epochs.
    - **Transition constraints**:
        - Avoid direct single‑epoch DEEP ↔ REM transitions; if one epoch flips, but neighbors disagree, relabel it as LIGHT.
    - **Cycle‑based prior (optional)**:
        - Before ~60–70 minutes: strongly penalize REM candidates.
        - After ~3 hours: relax REM criteria slightly to allow longer REM bouts.[^23][^28][^22]

This turns raw, noisy per‑epoch decisions into a more plausible hypnogram without requiring ML.

***

## 6. Integration with your existing `sleepstream` app

### 6.1. Where the new logic lives

- `sleepstream.boot.js`:
    - Responsible for:
        - Enabling/disabling sleep monitoring mode.
        - Configuring sensors.
        - Buffering raw data into epochs.
        - Calling feature extraction + classifier each epoch.
        - Holding the “current stage” and latest epoch features in module‑level variables.
        - Handling the 10‑minute health event and sending BLE JSON.
- `sleepstream.js`:
    - Contains:
        - Constants and default thresholds.
        - Settings load/save.
        - Feature extraction functions (`computeActivity`, `computeMeanHR`, `computeRMSSD`, `computeSDRR`).[^15][^14][^19][^20]
        - `SleepClassifier` object or functions that maintain night‑level context and return `currentStage`.
- `sleepstream.settings.js`:
    - Adds user‑visible settings for:
        - Epoch length.
        - Night‑time window (start/end hour).
        - Main threshold values and REM latency (or “Auto” mode).
- `sleepstream.app.js`:
    - Debug UI for:
        - Current stage (A/L/D/R).
        - Latest epoch features.
        - Basic hypnogram view.


### 6.2. Health event → BLE JSON mapping

Currently, the 10‑minute health event recomputes sleep state and then sends a JSON with `status` and some health values.[^1]

After the upgrade:

- The 10‑minute handler **does not** perform its own classification; instead it:
    - Reads `SleepClassifier.currentStage` (or similar).
    - Accesses the latest epoch features for `movement` and `bpm`.
    - Builds the packet:

```json
{
  "t": "sleepstream",
  "v": 1,
  "seq": ...,
  "ts": ...,
  "status": <mapped stage>,
  "consecutive": ...,
  "source_mode": ...,
  "movement": ...,
  "bpm": ...,
  "rem": 0/1,           // optional extra field
  "epoch_len": 30,      // optional
  "rmssd": <value>,     // optional
  "sdrr": <value>       // optional
}
```

- `status` could:
    - Be extended to 5=rem_sleep, updating receiver mapping accordingly, or
    - Stay as 0–4 with an additional `rem`/`stage4` field for REM, preserving backward compatibility.

The Python receiver only needs to be updated to recognize:

- New `status` code for REM, or
- New `rem`/`stage4` field if you choose that route.

***

## 7. Why this is realistic on Bangle.js 2

Bangle.js 2 hardware is capable enough for this approach:

- nRF52840, 64 MHz ARM Cortex‑M4, 256 kB RAM.[^2][^3]
- All HRV operations are O(N) with simple integer arithmetic and one or two `Math.sqrt` calls per epoch, which is trivial workload.
- Memory footprint:
    - Per epoch at 25 Hz, 30 s ⇒ ~750 accel samples, plus tens of RR intervals — easily held in RAM.
    - Only a small ring buffer of recent features and stage labels needs to be kept.

The design purposely avoids:

- Neural networks or heavy ML inference on watch.
- Frequency‑domain HRV (FFT), which is more computationally expensive and not clearly necessary for this use case.
- Long‑term raw data storage; raw samples are discarded once features are computed.

Yet it adheres closely to:

- The **feature types** used in validated wearable algorithms (activity + mean HR + simple HRV).[^6][^4][^5]
- The **temporal resolution** and **REM latency constraints** used in research and clinical sleep scoring.[^21][^22][^23][^11][^13]

***

## 8. Summary for another AI model

When you give this to an implementation model, you can highlight the main tasks:

1. **Add continuous night‑time sampling** in `sleepstream.boot.js`:
    - Configure accelerometer and HRM when in a “sleep window”.
    - Maintain per‑epoch buffers of accel magnitude and IBIs/HR.
    - Every 30–60 s, call `computeEpochFeatures`.
2. **Implement feature extraction** in `sleepstream.js` based on HRV literature:
    - `activity` as mean absolute deviation of accel magnitude.[^4][^5][^6]
    - `meanHR = 60000 / meanRR`.[^15][^20]
    - `rmssd` from successive RR differences.[^14][^19][^20]
    - `sdRR` ≈ standard deviation of RR intervals or HR.
3. **Implement a `SleepClassifier` with night‑level context**:
    - Tracks HR histograms to get `hrP20`, `hrP50`.
    - Tracks `sleepStartTime` and `minutesSinceSleepOnset`.
    - For each epoch, applies:
        - Wear detection → NOT_WORN vs worn.
        - Wake vs sleep via activity and HR.
        - Deep vs non‑deep via low HR + low activity.
        - REM vs light via low activity, elevated HR vs baseline, high variability, and REM latency constraints.[^12][^22][^11][^6][^4]
4. **Add temporal smoothing**:
    - Ring buffer of last N epoch stages.
    - Enforce minimum run lengths for DEEP and REM.
    - Avoid single‑epoch DEEP ↔ REM flips.
5. **Wire classifier output into health event handler**:
    - Use `currentStage` instead of old threshold classifier.
    - Adjust `status` value and optionally extend JSON schema.
6. **Expose thresholds and epoch settings in `sleepstream.settings.js`**:
    - Provide defaults and allow user tuning.
7. **Extend `sleepstream.app.js` for debugging**:
    - Show current stage and latest features.
    - Optionally display a scrolling hypnogram.

This gives the other model a clear mapping from research evidence → feature design → rule logic → code structure, all within your existing `bangle_sleep_stream` architecture.
<span style="display:none">[^29][^30][^31][^32][^33][^34]</span>

<div align="center">⁂</div>

[^1]: README.md

[^2]: https://shop.pimoroni.com/products/bangle-js-2-smart-watch

[^3]: https://shop.espruino.com/banglejs2

[^4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8253894/

[^5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10244431/

[^6]: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0285703

[^7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8255273/

[^8]: https://mhealth.jmir.org/2021/2/e24704

[^9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8527385/

[^10]: https://jnnp.bmj.com/content/93/Suppl_1/A59.1

[^11]: https://pubmed.ncbi.nlm.nih.gov/28248198/

[^12]: https://www.bohrium.com/paper-details/rem-sleep-estimation-based-on-autonomic-dynamics-using-r-r-intervals/811054885922406400-4105

[^13]: https://pubmed.ncbi.nlm.nih.gov/28600268/

[^14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5624990/

[^15]: https://en.wikipedia.org/wiki/Heart_rate_variability

[^16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1978378/

[^17]: https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2017.01100/full

[^18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3081328/

[^19]: https://tryterra.co/blog/measuring-hrv-sdnn-and-rmssd-3a9b962f7314

[^20]: https://www.kubios.com/blog/hrv-analysis-methods/

[^21]: https://www.ncbi.nlm.nih.gov/books/NBK526132/

[^22]: https://www.sleepfoundation.org/stages-of-sleep

[^23]: https://www.healthline.com/health/how-much-deep-sleep-do-you-need

[^24]: https://www.sciencedirect.com/science/article/abs/pii/S1389945702001545

[^25]: https://www.espruino.com/Bangle.js2+Technical

[^26]: https://www.espruino.com/ReferenceBANGLEJS2

[^27]: https://spikeapi.com/understanding-hrv-metrics-a-deep-dive-into-sdnn-and-rmssd/

[^28]: https://en.wikipedia.org/wiki/Sleep_cycle

[^29]: https://circuitpython.org/board/espruino_banglejs2/

[^30]: https://help.elitehrv.com/article/68-what-are-hrv-score-rmssd-ln-rmssd-sdnn-nn50-and-pnn50

[^31]: https://marcoaltini.substack.com/p/heart-rate-variability-hrv-numbers

[^32]: https://thepihut.com/products/bangle-js-2

[^33]: https://www.espruino.com/Bangle.js2

[^34]: https://welltory.com/rmssd-and-other-hrv-measurements/

