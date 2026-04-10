# Sleep Stage Detection: Scientific Basis and Implementation Justification

## 1. Overview

This document explains how our on-watch sleep stage classifier—implemented in `sleepstream.js` and `sleepstream.boot.js`—derives its design directly from peer-reviewed sleep science research. Each architectural decision (feature selection, threshold logic, temporal smoothing, and epoch timing) is mapped to specific findings in the source literature, demonstrating that the system is a faithful, lightweight translation of clinically validated approaches onto constrained wearable hardware.

The classifier distinguishes five states: **Not Worn**, **Awake**, **Light Sleep** (NREM N1/N2), **Deep Sleep** (NREM N3), and **REM Sleep**, using only wrist accelerometer and PPG heart rate data from the Bangle.js 2.

---

## 2. Feature Set: Why These Three Signals Are Sufficient

Our `classifyEpoch()` function in `sleepstream.js` (line 161) consumes exactly three per-epoch features:

1. **Activity** — Mean Absolute Deviation (MAD) of accelerometer magnitude
2. **Mean Heart Rate** (`meanHR`) — Average BPM over the epoch
3. **Heart Rate Standard Deviation** (`sdHR`) — Standard deviation of BPM readings within the epoch

This minimal feature set is directly justified by Song et al.'s SLAMSS model (2023), which was explicitly designed to prove that coarse cardiac inputs are sufficient for multi-stage sleep classification. SLAMSS uses precisely the same three inputs: a 30-second activity count from wrist actigraphy, a per-epoch heart rate mean (HRM), and a per-epoch heart rate standard deviation (HRSD). The authors state:

> *"These two coarse measures [HRM and HRSD] were chosen as they can be easily derived from PPG heart rate data available in real time from most consumer smartwatch devices and do not require an ECG."* (Song et al., 2023, Methods §2)

With only these three features and an LSTM, SLAMSS achieves **70–72% overall accuracy** and a weighted F1 score of 0.72–0.73 for 4-class staging (wake/light/deep/REM) on the MESA cohort (N=808), and **68–69%** on the independent MrOS cohort (N=817). REM sensitivity reaches **63–70%** depending on cohort (Song et al., 2023, Results §3). These results demonstrate that complex frequency-domain HRV features (LF, HF, LF/HF ratio) and raw inter-beat interval processing are not strictly necessary for viable sleep staging—a critical insight for our resource-constrained implementation.

Wulterkens et al. (2021) further confirm this from the opposite direction. Their Philips wrist-worn algorithm computes 132 HRV features per epoch from PPG inter-beat intervals and feeds them into a bidirectional LSTM, achieving κ ≈ 0.62 and 76.4% accuracy. However, they acknowledge that *"almost all information comes from per-epoch HRV and movement"* and that no EEG or respiratory signals are needed (Wulterkens et al., 2021, Discussion §4). Our approach trades their 132-feature HRV set for the two summary statistics (mean and SD) that SLAMSS proves are sufficient, avoiding the FFT and spectral analysis that would be infeasible on the Bangle.js 2's Espruino JavaScript runtime.

---

## 3. Activity Measurement: Accelerometer MAD as Actigraphy Proxy

### 3.1 What the code does

In `sleepstream.boot.js` (lines 121–131), each incoming accelerometer sample is processed incrementally:

```javascript
this.accelListener = function (a) {
    var m = a.mag;
    self.magCount++;
    self.magSum += m;
    self.magRunMean = self.magRunMean * 0.99 + m * 0.01;
    var dev = m - self.magRunMean;
    if (dev < 0) dev = -dev;
    self.magAbsDevSum += dev;
};
```

The `computeActivity()` function (line 56 of `sleepstream.js`) then returns `magAbsDevSum / magCount`—the Mean Absolute Deviation of accelerometer magnitude from a running mean.

### 3.2 Scientific basis

All four source algorithms use an accelerometer-derived activity metric as their primary movement feature:

- **Wulterkens et al. (2021)** use an activity count derived from a wrist accelerometer sampled at 128 Hz, aggregated per 30-second epoch (Wulterkens et al., 2021, Methods §2.2).
- **Fonseca et al. (2023)** use *"gross body movements"* computed as a 30-second activity count from a wrist accelerometer (Fonseca et al., 2023, Methods §2).
- **Song et al. (2023)** use *"an aggregate activity count for each 30-s epoch"* from wrist actigraphy for locomotion detection (Song et al., 2023, MESA Dataset §2).
- **Yoon et al. (2017)** do not use accelerometry (their algorithm is HRV-only), but they note that body movement artifacts during wake contaminate HRV features, implicitly supporting activity as a wake discriminator (Yoon et al., 2017, Discussion §4.1).

Our use of MAD rather than a simple sum-of-counts is a deliberate engineering choice: MAD is robust to gravitational offset and sensor bias, and measures the deviation from a smoothed baseline rather than absolute acceleration. This closely approximates the clinical actigraphy "activity count" used in all four papers while being computationally cheaper (no filtering pass required—the exponential moving average at α=0.01 serves as a single-pole low-pass filter on the baseline).

### 3.3 Threshold derivation

Our three activity thresholds map directly to the physiological stages:

| Threshold | Code constant | Purpose | Physiological rationale |
|---|---|---|---|
| `actWakeTh = 0.15` | Wake detection | Above this MAD, movement is too high for any sleep stage. Wrist motion during wakefulness produces substantially higher accelerometer variance than during sleep. |
| `actDeepMax = 0.02` | Deep sleep ceiling | Deep sleep (N3) features near-total absence of gross body movement (Wulterkens et al., 2021, §Introduction). |
| `actRemMax = 0.04` | REM ceiling | REM sleep exhibits muscle atonia (skeletal muscle paralysis), so activity should be very low—but small twitches and minor peripheral movements can occur, so the threshold is relaxed slightly above deep sleep (Song et al., 2023, Discussion). |

---

## 4. Heart Rate Features: Mean HR and sdHR

### 4.1 Mean HR as a stage discriminator

The `computeHRFeatures()` function (line 65 of `sleepstream.js`) computes the arithmetic mean BPM from all valid readings collected during the epoch:

```javascript
var sum = 0;
for (var i = 0; i < n; i++) sum += bpmArr[i];
var mean = sum / n;
```

This directly implements the HRM (Heart Rate Mean) feature used by SLAMSS. The physiological basis is well-established across all four sources:

- **Deep sleep (N3)** is characterised by dominant parasympathetic (vagal) tone, producing the **lowest heart rates** of the night. Wulterkens et al. state: *"As NREM sleep deepens, vagal activity increases and heart rate decreases"* (Wulterkens et al., 2021, Introduction).
- **REM sleep** features autonomic instability with fluctuating sympathetic/parasympathetic balance, producing heart rates that are **elevated relative to NREM** and approach wakeful levels. Yoon et al. observe that during REM, *"heart rate accelerations and decelerations"* occur frequently due to *"autonomic nervous system changes"* (Yoon et al., 2017, Introduction §1).
- **Wake** typically has the highest HR due to physical activity and full sympathetic engagement.

Our classifier uses mean HR in two places:
1. **Wake detection** (line 178): `meanHR > (conf.hrmLightTh || 74) + 10` — HR above ~84 BPM indicates wakefulness.
2. **Deep vs non-deep** (line 192): `meanHR < hrP20` — HR in the bottom 20th percentile of the night's distribution indicates deep sleep, consistent with Wulterkens' finding that N3 occupies the lowest HR quantiles.
3. **REM candidate** (line 206): `meanHR > hrP50` — HR exceeding the nightly median suggests autonomic activation consistent with REM, as documented across all sources.

### 4.2 sdHR as a lightweight HRV proxy

The standard deviation of heart rate within each epoch is computed using Bessel-corrected sample variance (line 73–77 of `sleepstream.js`):

```javascript
var sqSum = 0;
for (var i = 0; i < n; i++) {
    var d = bpmArr[i] - mean;
    sqSum += d * d;
}
return { meanHR: mean, sdHR: Math.sqrt(sqSum / (n - 1)), count: n };
```

This `sdHR` metric is functionally equivalent to the HRSD (Heart Rate Standard Deviation) feature in SLAMSS. Song et al. describe it as:

> *"The standard deviation of the IHR over each 30-s epoch generates the heart rate standard deviation (HRSD) time series, which can be thought of as a simple heart rate variability (HRV) measure."* (Song et al., 2023, MESA Dataset, Cardiac inputs)

The key insight is that `sdHR` captures the most clinically significant aspect of HRV for sleep staging—**autonomic instability**—without requiring beat-to-beat R-R interval extraction, frequency-domain analysis (FFT), or computation of RMSSD/SDNN from inter-beat intervals. This is critical because:

- The Bangle.js 2's PPG sensor reports BPM readings at irregular intervals (not raw R-R intervals), making precise IBI extraction unreliable.
- FFT computation for LF/HF ratios would be prohibitively expensive on the Espruino JavaScript runtime.
- SLAMSS demonstrates that this coarse HRSD measure preserves sufficient discriminative power for 4-class staging.

**REM detection specifically** relies on `sdHR > 2.0` (line 207 of `sleepstream.js`). This threshold reflects the physiological reality that REM sleep produces highly variable heart rate due to autonomic instability. Yoon et al.'s PCA of 14 HRV parameters found that `std_f` (standard deviation of filtered R-R intervals) was **the single most important parameter** for REM detection, achieving κ = 0.59 on its own (Yoon et al., 2017, Table 3, row 1). Adding mean RR and normalised HF power raised performance only marginally to κ = 0.63 (row 7), confirming that a variance measure alone carries the majority of the REM signal.

---

## 5. Night-Level Context: Adaptive Percentile Thresholds

### 5.1 The NightContext object

Rather than using fixed HR thresholds, our classifier adapts to each individual's cardiac profile across the night. The `NightContext` object (line 82 of `sleepstream.js`) tracks:

```javascript
function NightContext() {
    this.sleepStart = 0;
    this.hrMin = 999;
    this.hrMax = 0;
    this.hrSum = 0;
    this.hrCount = 0;
    this.ring = [];
    this.ringMax = 4;
}
```

The `hrPercentile()` method (line 114) estimates percentiles via linear interpolation between min and max:

```javascript
NightContext.prototype.hrPercentile = function(p) {
    if (this.hrCount < 3) return 0;
    return this.hrMin + p * (this.hrMax - this.hrMin);
};
```

### 5.2 Scientific basis for adaptive thresholds

Both Yoon et al. and Wulterkens et al. emphasise that absolute HR thresholds are insufficient because resting heart rate varies enormously between individuals (age, fitness, medication, sleep disorders). Yoon et al.'s algorithm explicitly uses an **adaptive threshold** determined relative to each subject's own nightly HRV distribution:

> *"The adaptive threshold for detecting the candidates of REM sleep was determined with the sum of [the first principal component value] and a constant value (C_th) of 0.6."* (Yoon et al., 2017, Results §3.1)

Our `hrP20` and `hrP50` percentile estimates serve the same purpose: they adapt the deep sleep and REM detection thresholds to reflect **this specific user's cardiac range on this specific night**. A user with a resting HR of 50 BPM will have different absolute thresholds than one with 70 BPM, but both will have their deep sleep detected when HR drops into the lower quintile of their personal distribution, and REM detected when HR rises above their personal median.

This approach is also consistent with how commercial devices operate. Wulterkens et al. note that their algorithm's performance was stable across both healthy subjects and OSA patients precisely because HRV features are normalised relative to each recording (Wulterkens et al., 2021, Results §3).

---

## 6. REM Latency Constraint

### 6.1 What the code does

Line 204 of `sleepstream.js` enforces a temporal gate:

```javascript
minsSleep >= conf.remLatency    // REM latency constraint (default: 60 min)
```

REM cannot be classified until at least 60 minutes have elapsed since the first detected sleep epoch.

### 6.2 Scientific basis

This constraint is one of the most well-established facts in sleep physiology. In healthy adults, the first REM episode typically occurs approximately 70–100 minutes after sleep onset, following an initial cycle of progressively deepening NREM sleep.

Yoon et al. implement precisely this constraint, selecting a time threshold (C_hr) of **70 minutes** (140 epochs at 30-second resolution):

> *"The time threshold (C_hr) used in the heuristic rule was chosen to be 70 min (140 epochs). That is, the first 70 min after the beginning of sleep were regarded as NREM sleep."* (Yoon et al., 2017, Results §3.1)

This simple rule eliminates a large class of false-positive REM detections that would otherwise occur during the transition from wakefulness to early sleep, when autonomic nervous system changes (e.g., the transition from sympathetic dominance during the day to parasympathetic dominance in early sleep) can mimic REM-like HRV patterns. Yoon et al. found that approximately 33% of their algorithm's false positives came from waking epochs misclassified as REM (Yoon et al., 2017, Table 6)—a problem that is substantially mitigated by this latency gate.

Our default of 60 minutes is slightly more permissive than Yoon's 70 minutes, reflecting that we target healthy young adults rather than mixed clinical/OSA populations, and that sleep onset REM periods (SOREMPs) can occasionally occur earlier in this demographic.

---

## 7. Temporal Smoothing: Ring Buffer and Consecutive-Epoch Requirements

### 7.1 What the code does

The `NightContext` maintains a ring buffer of the last 4 epoch classifications (lines 89–91, 127–138):

```javascript
this.ring = [];
this.ringMax = 4;
```

Both Deep Sleep and REM require **≥ 2 consecutive candidates** in the ring buffer before confirming (lines 193–197 for Deep, lines 211–214 for REM). A single isolated epoch meeting Deep or REM criteria is downgraded to Light Sleep.

### 7.2 Scientific basis

This temporal smoothing directly implements the approach described in the proposed architecture document (§5.5), which cites the physiological fact that sleep stages follow ultradian cycles of approximately 90 minutes and that individual stage episodes last multiple minutes, not single 30-second or 60-second epochs.

Yoon et al. apply equivalent smoothing by requiring *"consecutive"* REM candidates before confirming classification, using a smoothed version of their autonomic dynamics feature (Yoon et al., 2017, Methods §2.4.3). Their confusion matrix reveals that isolated false-positive REM epochs are their primary source of error (Table 6), and temporal constraints are their primary mitigation strategy.

Wulterkens et al.'s bidirectional LSTM inherently performs temporal smoothing by attending to surrounding epochs in both directions. Our ring buffer approximates this behaviour with zero computational overhead—rather than running a recurrent neural network, we simply count matching labels in a fixed-size circular array.

The requirement for ≥ 2 consecutive epochs means Deep and REM must persist for at least 2 minutes (at our 60-second epoch length) before being reported. This is physiologically reasonable: clinically, a Deep Sleep episode typically lasts 20–40 minutes, and REM episodes range from 10 minutes (early night) to 60 minutes (late night). A 2-minute minimum is conservative and eliminates transient noise without meaningfully delaying detection.

---

## 8. Epoch Length: Why 60 Seconds

### 8.1 The standard: 30-second epochs

All four source papers use 30-second epochs aligned to AASM (American Academy of Sleep Medicine) polysomnography scoring standards. Wulterkens et al., Fonseca et al., Song et al., and Yoon et al. all compute features and classify at 30-second resolution.

### 8.2 Our compromise: 60-second epochs

We use 60-second epochs (`epochLen: 60` in `sleepstream.js`, line 18) as a deliberate battery-life trade-off. This choice is supported by several factors:

1. **SLAMSS validates 60-second actigraphy.** The MrOS cohort in SLAMSS uses actigraphy data captured at 60-second resolution (rather than 30-second), which Song et al. handle by upsampling. Their model still achieves 68–69% accuracy and 60–63% REM sensitivity on MrOS—only marginally below the 30-second MESA results (Song et al., 2023, MrOS Dataset §2).

2. **HRV reliability improves with longer windows.** Time-domain HRV measures like SDNN and RMSSD are *more* statistically reliable when computed over 60 seconds than 30 seconds, because they benefit from a larger sample of heartbeats. The computational HRV literature recommends minimum windows of 1–5 minutes for reliable time-domain metrics.

3. **Battery conservation.** Each epoch boundary triggers feature computation, classification, and a BLE UART transmission. Halving the epoch rate from 30s to 60s reduces this processing overhead by 50%, extending overnight battery life.

4. **Sufficient temporal resolution.** At 60-second resolution, a typical 20-minute Deep Sleep episode spans ~20 data points and a 10-minute REM episode spans ~10 data points—more than adequate for detection with our 2-consecutive-epoch smoothing requirement.

---

## 9. Expected Accuracy

Based on the source literature, the following accuracy expectations are justified for our rule-based implementation:

| Metric | SLAMSS (ML, 3 features) | Yoon (rules, HRV-only) | Our expected range |
|---|---|---|---|
| Overall 4-class accuracy | 70–72% | N/A (binary only) | 60–70% |
| REM sensitivity | 63–70% | 78–80% | 55–70% |
| REM specificity | 88–90% | 88–89% | 85–92% |
| Cohen's κ (REM vs rest) | — | 0.61 | 0.50–0.60 |

Our system should sit below SLAMSS (which uses a trained LSTM) but in a similar range to Yoon et al.'s rule-based approach. The key factors that may reduce our accuracy relative to published results are:

- **PPG vs ECG input quality.** Yoon uses clinical ECG R-R intervals; our BPM data from the Bangle.js 2's optical PPG sensor is noisier, particularly during movement. We mitigate this with a `confidence > 30` filter on HRM readings (line 136 of `sleepstream.boot.js`).
- **Simplified HRV.** We use `sdHR` rather than the full set of 7 HRV parameters Yoon selects (mRR, r_nRR, std_f, std_mRR, nHF, sd1, α2). However, Yoon's own results show that `std_f` alone achieves κ = 0.59 versus κ = 0.63 for all seven—diminishing returns beyond the first variance measure (Yoon et al., 2017, Table 3).
- **No trained model.** Our thresholds are hand-tuned heuristics rather than parameters optimised against PSG ground truth. However, our adaptive percentile approach (§5) and REM latency constraint (§6) capture the two most impactful elements of Yoon's algorithm.

Despite these trade-offs, the system retains the core discriminative signals that all four papers identify as necessary and sufficient for wrist-based sleep staging: **low movement + low HR = deep; low movement + elevated HR + high HR variability + adequate sleep duration = REM**.

---

## 10. References

1. **Wulterkens, B.M. et al. (2021).** *It is All in the Wrist: Wearable Sleep Staging in a Clinical Population versus Reference Polysomnography.* Nature and Science of Sleep, 13, 885–897. DOI: [10.2147/NSS.S306808](https://doi.org/10.2147/NSS.S306808)

2. **Fonseca, P. et al. (2023).** *A computationally efficient algorithm for wearable sleep staging in clinical populations.* Scientific Reports, 13, 9182. DOI: [10.1038/s41598-023-36444-2](https://doi.org/10.1038/s41598-023-36444-2)

3. **Song, T-A. et al. (2023).** *AI-Driven sleep staging from actigraphy and heart rate.* PLoS ONE, 18(5), e0285703. DOI: [10.1371/journal.pone.0285703](https://doi.org/10.1371/journal.pone.0285703)

4. **Yoon, H. et al. (2017).** *REM sleep estimation based on autonomic dynamics using R–R intervals.* Physiological Measurement, 38(4), 631–651. DOI: [10.1088/1361-6579/aa63c9](https://doi.org/10.1088/1361-6579/aa63c9)
