# Lightweight REM and 4‑stage sleep classification from wrist PPG and accelerometer

## Executive summary

Research on wrist‑worn PPG + accelerometer devices shows that 4‑stage sleep staging (wake, light N1–N2, deep N3, REM) is feasible with moderate accuracy using only movement and heart‑rate–derived features, but nearly all high‑performing systems rely on machine‑learning models running off‑device.  The minimum viable feature set for distinguishing REM from other stages is: (1) an actigraphy measure of movement per 30‑s epoch and (2) at least one short‑term heart‑rate variability (HRV) measure (e.g., per‑epoch heart rate standard deviation or RMSSD) plus mean heart rate, computed from beat‑to‑beat intervals.  Ten‑minute averaged BPM and movement are too coarse; all published algorithms that detect REM work at approximately 30‑s resolution and use beat‑level R‑R (or PPG inter‑beat interval) data.[^1][^2][^3][^4]

Across multiple validation studies versus polysomnography (PSG), best‑in‑class wrist algorithms achieve roughly 65–80% epoch‑level accuracy for REM and Cohen’s κ around 0.6–0.7 for 4‑class or 3‑class staging, approaching human inter‑scorer agreement but still clearly imperfect.  Purely rule‑based HRV+movement REM detectors exist and can reach κ ≈ 0.6 for REM vs non‑REM using an adaptive threshold on an HRV‑derived “autonomic dynamics” feature, but they are binary (REM vs not‑REM) and still require beat‑to‑beat intervals and per‑epoch HRV computation.  A practical path for a constrained Bangle.js‑class device is therefore: compute a very small set of HR/HRV + movement features on‑device over 30–60‑s windows, apply simple heuristics and temporal rules to approximate REM, and accept that accuracy will likely sit in the 60–70% REM sensitivity range at best.[^5][^2][^3][^4][^6][^1]


## Published wrist algorithms using actigraphy + PPG

### PPG‑HRV + accelerometer, feature‑based model (Philips “It is all in the Wrist”)

Wulterkens et al. developed a 4‑class sleep staging algorithm using a wrist device with 3‑axis accelerometer (128 Hz) and green‑LED PPG (32 Hz). The pipeline: extract inter‑beat intervals (IBIs) from PPG, build a 4 Hz IBI time series, compute 132 HRV features for each 30‑s epoch, combine with a gross body‑movement activity count from the accelerometer, and feed this into a bidirectional LSTM classifier.  On a large clinical population (292 patients, many with sleep disorders), they achieved κ ≈ 0.62 and 76.4% accuracy for 4‑class staging (wake, N1+N2, N3, REM), with REM one‑vs‑rest κ ≈ 0.69, sensitivity ≈ 78%, specificity ≈ 95%.[^1]

Although the feature set is large, almost all information comes from per‑epoch HRV and movement; there are no EEG or respiratory signals, confirming that autonomic and movement signals alone can distinguish REM reasonably well.[^1]

### PPG‑HRV + accelerometer, end‑to‑end neural network (computationally efficient model)

Fonseca et al. later replaced the 132‑feature HRV front‑end with an end‑to‑end convolutional + recurrent network that takes as input: (a) instantaneous heart rate (IHR) time series derived from PPG inter‑beat intervals, resampled at 10 Hz, and (b) 30‑s activity counts from the accelerometer.  The model (PPG–NN) achieved median κ ≈ 0.64 and accuracy ≈ 77.8% for 4‑class sleep staging, with REM one‑vs‑rest κ ≈ 0.75 and sensitivity ≈ 77.5% on a 394‑recording clinical validation set.[^2]

Importantly for your use case, the input features at the classifier boundary are still only: a 10 Hz IHR series and a single movement count per 30‑s epoch, showing that you do not need complex feature engineering if you can afford an ML model—but also implying that the “signal content” needed for REM lies in short‑timescale HR dynamics plus low movement.[^2]

### Activity counts + coarse heart‑rate statistics (SLAMSS)

Song et al.’s SLAMSS model performs 3‑class (wake / NREM / REM) and 4‑class (wake / light / deep / REM) staging using only: wrist actigraphy counts per 30‑s epoch and two “coarse” heart‑rate measures per epoch—mean heart rate (HRM) and the standard deviation of heart rate (HRSD), both derived from ECG R‑R intervals but explicitly chosen to be implementable with PPG.  With these three time series (activity, HRM, HRSD) and a 6‑minute sequence‑to‑sequence LSTM, they reach roughly 70–72% overall 4‑class accuracy and REM sensitivity of ~63–70% across two large cohorts.[^3]

SLAMSS thus demonstrates that for REM vs NREM, it is sufficient to have per‑epoch mean HR and a simple variance‑like HRV metric plus actigraphy; no frequency‑domain HRV is strictly required, although performance could potentially improve with richer features.[^3]

### Commercial Fitbit / Firstbeat multi‑stage algorithms

Several studies have validated proprietary multi‑stage algorithms from Fitbit and Firstbeat that use wrist accelerometry plus PPG‑derived HR/HRV.  Menghini et al. found that the Fitbit Charge 3, which integrates accelerometer, PPG‑derived HR and HRV into a multi‑sensor classifier, achieved higher accuracy for REM and deep sleep than for light sleep, with REM classification strongly influenced by the magnitude of heart‑rate accelerations/decelerations between consecutive epochs.  Kuula et al. evaluated the Firstbeat method, which uses HRV (including HRV‑derived respiratory rate), movement, and time‑of‑day; they found excellent specificity and good accuracy for REM and slow‑wave sleep, but poorer performance for light sleep.[^7][^8]

Fitbit Charge 2/4 validation in clinical and disease cohorts shows REM sensitivities in the mid‑70% range and high specificity (~95%), with more difficulty distinguishing N3 than REM.  These vendors do not publish rule sets, but published descriptions and analyses consistently emphasize HRV‑derived autonomic markers plus low movement as the core signals for REM.[^9][^5]


## HRV and autonomic signatures of REM vs NREM

### Physiological differences

Classic HRV literature and Philips’ introduction summarize autonomic patterns across stages: during deep NREM (N3), parasympathetic (vagal) activity is high, sympathetic activity low, and heart rate is reduced; this appears as lower mean HR and increased high‑frequency (HF) HRV power.  In REM, autonomic activity is unstable with fluctuating sympathetic and parasympathetic tone, leading to elevated average HR compared with NREM and increased low‑frequency (LF) power and LF/HF ratio, as well as abrupt heart‑rate changes.[^10][^11][^1]

Time‑domain HRV metrics such as SDNN (standard deviation of all NN intervals) capture overall variability, whereas RMSSD (root mean square of successive differences) reflects short‑term beat‑to‑beat variability driven mainly by vagal activity.  Studies consistently report longer R‑R intervals (lower HR) and higher HF power in NREM than REM, while REM shows shorter R‑R intervals and higher LF/HF ratios, indicating a shift toward sympathetic dominance.  These contrasts are the basis for HRV‑only REM detectors.[^12][^13][^14][^10]

### HRV‑only REM estimators

Yoon et al. developed a REM estimation algorithm that uses only ECG R‑R intervals: several HRV parameters are computed each 30‑s epoch, then combined into a single “autonomic dynamics” feature that reflects the major autonomic variation across the sleep cycle; REM is then detected by an adaptive threshold on this feature.  In 26 training and 25 validation subjects (healthy and OSA), they achieved κ ≈ 0.61–0.63 and 87% epoch‑level accuracy for REM vs non‑REM classification.[^4][^6]

A companion algorithm from the same group detects slow‑wave sleep (SWS/N3) using a stability metric derived from R‑R intervals (autonomic “stability” characteristic of SWS) plus heuristic thresholds and rules based on expected distribution across the night, reaching κ ≈ 0.56 and ~90% accuracy for SWS vs other stages.  These works demonstrate that state‑machine logic plus a few HRV features (no accelerometer) can achieve reasonably strong binary classification for REM and N3.[^15]


## Minimum viable feature set for REM vs light vs deep

### Evidence from SLAMSS and PPG‑based work

SLAMSS shows that the combination of:

- Actigraphy: 30‑s activity counts (movement intensity per epoch)
- Mean HR: average beats per minute over 30 s (HRM)
- HR variability: standard deviation of HR within 30 s (HRSD)

is sufficient to drive a deep model to ~70% 4‑class accuracy and ~63–70% REM sensitivity, even though the cardiac inputs are deliberately “coarse.”  Wulterkens and Fonseca’s Philips work achieves slightly higher κ (~0.62–0.64) partly by adding a large number of HRV features on IBIs and possibly benefiting from clinical training data, but the discrimination between REM, light, and deep still fundamentally comes from HR level/variability and low movement.[^2][^3][^1]

Yoon’s REM‑only and SWS‑only algorithms further indicate that only a handful of HRV metrics (e.g., LF, HF, LF/HF, SDNN, RMSSD) plus a time‑of‑night prior can separate REM, N3, and other stages.  Commercial systems like Fitbit and Firstbeat also rely on HRV, HR‑derived respiratory rate, movement, and circadian/time‑of‑night features, without EEG.[^8][^7][^4][^15]

### Practical minimum feature set for Bangle.js‑class device

Given your constraints, a realistic “minimal but useful” on‑device feature set per 30‑ or 60‑s epoch would be:

- Movement
  - Activity count or variance of accelerometer magnitude over the epoch (proxy for actigraphy count).[^1][^2]
  - Optional: a binary “still vs moving” flag based on thresholded activity.[^1]
- Heart rate
  - Mean HR over the epoch; lower in N3, intermediate in N2, higher in REM and wake.[^14][^10]
- Very small HRV set
  - Short‑term variability: RMSSD or equivalent computed from beat‑to‑beat intervals in the epoch.[^13][^12]
  - Overall variability: SDNN (standard deviation of NN intervals) or simply the standard deviation of instantaneous HR within the epoch.[^12][^3]
- Context
  - Time since sleep onset / approximate sleep cycle index, leveraging that first REM typically occurs ~70–100 minutes after sleep onset and REM proportion increases later in the night.[^16][^17]

All of these can be computed with simple integer arithmetic from R‑R intervals and accelerometer magnitude in JavaScript, keeping CPU usage low. Frequency‑domain HRV (LF/HF) adds complexity and may be too heavy on a microcontroller; the literature suggests that time‑domain measures (mean HR, SDNN, RMSSD) already contain most of the discriminative power for wearable‑grade staging.[^4][^12][^3]


## Can 10‑minute averages work?

All of the above algorithms, including the “coarse” SLAMSS model and the HRV‑only REM estimators, operate on epochs of about 30 seconds (occasionally 60 s).  The reason is that sleep scoring standards define 30‑s epochs, and both autonomic changes and body movements associated with stage transitions occur on this timescale.[^6][^18][^3][^2][^1]

Ten‑minute averaging of heart rate and movement will:

- Blur out transient accelerations/decelerations in HR that distinguish REM from NREM.[^7][^10]
- Obscure short REM bouts and short N3 episodes that may last only a few minutes within a 90‑minute cycle.[^17][^16]
- Render time‑domain HRV measures like RMSSD meaningless, because reliable HRV requires beat‑to‑beat data over short, stationary segments (typically 1–5 minutes), not long multi‑stage mixtures.[^14][^12]

In practice, no published algorithm demonstrates good REM detection using 10‑minute averaged BPM and movement alone; even SLAMSS, which is explicitly designed to use low‑information inputs, still needs HR mean and SD at 30‑s resolution.  For any REM detection beyond a trivial probabilistic “REM happens later in the night” prior, you will need higher‑frequency sampling at least in intermittent bursts to compute per‑epoch HR and HRV.[^3]


## Realistic accuracy ceiling for REM with wrist PPG + accelerometer

### Performance of state‑of‑the‑art wrist algorithms

Across multiple PPG+accelerometer algorithms validated against PSG:

- Wulterkens et al. (PPG‑HRV + accelerometer + LSTM) report κ ≈ 0.62 and 76.4% accuracy for 4‑class staging in a mixed clinical population; REM one‑vs‑rest κ ≈ 0.69, sensitivity ≈ 78%, specificity ≈ 95%.[^1]
- Fonseca et al. (PPG–NN end‑to‑end network) achieve median κ ≈ 0.64 and 77.8% accuracy for 4‑class staging; REM κ ≈ 0.75, sensitivity ≈ 77.5%, specificity ≈ 97.6%.[^2]
- SLAMSS (activity + HRM + HRSD only) reaches 70–72% 4‑class accuracy and ~63–70% REM sensitivity depending on cohort.[^3]
- Fitbit devices show overall REM accuracies around 0.82–0.86 and deep‑sleep (N3) accuracies ~0.78 when compared to PSG, but with lower accuracy for light sleep (N1+N2).[^19][^5]

These κ values around 0.6–0.7 are in the same ballpark as human inter‑scorer agreement for PSG sleep staging, which is typically reported around κ ≈ 0.76 for 5‑stage scoring (with worst agreement between N1 and N2).  However, wearable staging tends to misclassify between neighboring NREM stages and occasionally confuse REM with wake or light sleep, especially in people with fragmented or disordered sleep.[^18][^2][^1]

Given that these results already use sophisticated ML (LSTMs, CNNs, attention) and high‑quality pre‑processing, a realistic **upper bound** for 4‑class wrist‑only staging is probably in the ~0.65–0.7 κ and ~75–80% REM sensitivity range on diverse populations; a very lightweight rule‑based implementation on a Bangle‑class device should expect noticeably lower performance.

### HRV‑only rule‑based ceiling

Yoon’s HRV‑only REM detector (adaptive threshold on an autonomic dynamics feature, using only R‑R intervals) achieved κ ≈ 0.61 and 87% accuracy for REM vs non‑REM, even in OSA patients.  Their SWS detector achieved κ ≈ 0.56 and ~90% accuracy for SWS vs others.  These figures suggest that for **binary** decisions (REM vs not, or N3 vs not), simple feature combinations and thresholds can approach κ ≈ 0.6 with good accuracy, but full 4‑stage classification would require additional logic and will likely reduce κ somewhat.[^6][^15]


## Simple rule‑based heuristics for “good‑enough” REM

No widely‑used consumer algorithm publishes a fully rule‑based REM classifier, but Yoon’s work and standard physiology suggest a practical heuristic state machine combining HR, HRV, movement, and time‑of‑night.[^16][^4][^6]

A plausible on‑device rule set (conceptually inspired by these papers) could be:

1. **Compute per‑epoch features (30–60 s):**
   - Activity count A (e.g., sum of |accel| deviations).
   - Mean heart rate HR.
   - Short‑term HRV V1 (e.g., RMSSD or SD of HR).
   - Optionally long‑term trend of HR over the last 5–10 minutes.
2. **Classify coarse state (wake vs sleep):**
   - If A above threshold or HR within X% of daytime baseline: classify as wake.
   - Else, treat as candidate sleep.
3. **Deep vs non‑deep during sleep:**
   - If HR is in the lowest Y percentile of the night and V1 relatively high (strong vagal tone), and movement is extremely low for several consecutive epochs, classify as N3.[^10][^1]
4. **REM vs light NREM within non‑deep sleep:**
   - Among non‑N3, low‑movement epochs, mark as **probable REM** if:
     - Movement A is low (no gross body movement), and
     - HR is elevated relative to preceding N3 baseline, and
     - V1 or epoch‑to‑epoch HR change exceeds a variability threshold (reflecting unstable autonomic activity), and
     - Time since sleep onset is > 60–90 minutes or in the second half of the sleep period.[^17][^10][^16]
   - Otherwise classify as light NREM.
5. **Enforce sleep‑cycle constraints:**
   - Do not allow REM before a minimum REM‑latency (e.g., 60–70 minutes after sleep onset) except as a low‑confidence tag, since healthy REM typically begins after ~70–100 minutes.[^20][^16]
   - Encourage REM bouts to cluster near expected ultradian cycle peaks (around 90‑minute multiples), and to lengthen in later cycles; penalize isolated one‑epoch REM tags in early night.[^21][^16]

This state machine mirrors the approach in Yoon’s algorithms, which use an HRV‑derived feature plus adaptive thresholds and heuristic rules about expected REM and SWS distribution across the night.  On a constrained device you can implement all of this with simple integer operations and a few running statistics (nightly HR baseline, percentile estimates, exponentially weighted moving averages), trading fine‑grained accuracy for transparency and compute efficiency.[^15][^4]


## Sampling rate and data resolution vs battery

### What published systems use

- Philips wrist sensor: accelerometer at 128 Hz, PPG at 32 Hz, then downsampled to IBIs and 30‑s activity counts; HRV features computed per 30‑s epoch.[^1]
- PPG–NN: similar PPG sampling, IBIs converted to instantaneous HR sampled at 10 Hz plus 30‑s activity counts.[^2]
- SLAMSS: source ECG sampled at standard PSG rates, but final features are only 30‑s HRM and HRSD plus 30‑ or 60‑s activity counts.[^3]
- Fitbit and Firstbeat: do not publish exact on‑device sampling, but validation papers mention 1‑s HR sampling and 30‑s epoch staging.[^9][^5][^8]

All of these systems therefore follow a common pattern: **high‑frequency raw sampling for PPG/accelerometer, but feature extraction and staging at 30‑s epochs synchronized to PSG scoring.**

### Practical trade‑offs for Bangle.js‑class hardware

For your Bangle.js 2 (nRF52840, JavaScript via Espruino), a reasonable compromise is:

- **PPG sampling:** 25–50 Hz in bursts during detected rest/sleep; enough to resolve IBIs and filter motion artifacts.[^2][^1]
- **Accelerometer sampling:** 25–50 Hz; downsample to 1‑Hz movement magnitude and then to 30‑s activity counts.
- **Feature window:** 30‑s (aligned to standard epochs); 60‑s could work but will blur short transitions and slightly hurt staging temporal resolution.[^18]
- **Duty cycling:** Keep sensors at high rate only during likely sleep, or even only during low‑movement periods (detected from accelerometer alone), to save battery.
- **On‑device compute:** After each 30‑ or 60‑s window, compute mean HR, SDNN/HRSD, RMSSD (or a simpler proxy), and activity count, then discard raw data.

Attempting to stage sleep using only 10‑minute averages to save battery will almost certainly miss REM physiology and cannot exploit HRV; instead, the evidence suggests collecting higher‑rate data but aggressively summarizing and discarding it in short windows is the best accuracy‑to‑battery trade‑off.[^3][^2][^1]


## Recommendations for your implementation

Based on the literature and your constraints, a pragmatic roadmap is:

1. **Increase temporal resolution of inputs:** Move from 10‑min to 30‑s or at worst 60‑s epochs at night; compute per‑epoch features (activity count, mean HR, short‑term HRV measure).[^3][^1]
2. **Implement a simple HRV pipeline:** From PPG, detect peaks to get IBIs, then compute mean HR, SDNN or HRSD, and RMSSD over each epoch using integer/fixed‑point math.[^13][^12]
3. **Adopt a rule‑based REM detector:** Start with a distilled version of Yoon‑style logic: low movement, HR elevated vs N3 baseline, higher short‑term variability, and appropriate time‑of‑night constraints, with some smoothing over neighboring epochs.[^4][^6][^16]
4. **Treat deep vs light NREM mostly via HR level and stability:** Very low HR plus stable HRV and minimal movement over multiple epochs → deep; other sleep epochs → light, unless they meet REM criteria.[^15][^1]
5. **Evaluate against an external reference:** If you cannot run PSG, you can at least compare your hypnograms qualitatively to those from a validated device (Fitbit, Apple Watch with a research app, or a phone app that uses Firstbeat‑style HRV) on the same nights to tune thresholds.

With this approach, you stay close to the feature sets and heuristics that have been shown to work in the literature, while keeping computation and memory demands small enough for Bangle.js‑class hardware.

---

## References

1. [It is All in the Wrist: Wearable Sleep Staging in a Clinical ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC8253894/) - There is great interest in unobtrusive long-term sleep measurements using wearable devices based on ...

2. [A computationally efficient algorithm for wearable sleep ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC10244431/) - This study describes a computationally efficient algorithm for 4-class sleep staging based on cardia...

3. [AI-Driven sleep staging from actigraphy and heart rate](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0285703) - by TA Song · 2023 · Cited by 31 — In this paper, we present an artificial intelligence (AI) techniqu...

4. [REM sleep estimation based on autonomic dynamics using R–R ...](https://www.bohrium.com/paper-details/rem-sleep-estimation-based-on-autonomic-dynamics-using-r-r-intervals/811054885922406400-4105) - Read the abstract for REM sleep estimation based on autonomic dynamics using R–R. Generate BibTeX, A...

5. [Validation of Fitbit Charge 2 Sleep and Heart Rate Estimates ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC8527385/) - by B Stucky · 2021 · Cited by 70 — We observed that Fitbit uses 30-second intervals to classify the ...

6. [REM sleep estimation based on autonomic dynamics using R-R intervals - PubMed](https://pubmed.ncbi.nlm.nih.gov/28248198/) - The current algorithm only using R-R intervals can be applied to mobile and wearable devices that ac...

7. [Performance of Fitbit Charge 3 against polysomnography in ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC8255273/) - by L Menghini · 2021 · Cited by 53 — The magnitude of the heart rate acceleration/deceleration betwe...

8. [Heart Rate Variability and Firstbeat Method for Detecting ...](https://mhealth.jmir.org/2021/2/e24704) - by L Kuula · 2021 · Cited by 32 — The method uses a neural network–based algorithm with HRV, HRV-der...

9. [F63 Validation of fitbit charge 4 for sleep monitoring in participants with Huntington’s disease](https://jnnp.bmj.com/content/93/Suppl_1/A59.1) - Background Wearable devices enable long-term home sleep monitoring, allowing changes in sleep qualit...

10. [Cardiac Autonomic Regulation During Sleep in Idiopathic ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC1978378/) - To assess cardiac autonomic and respiratory changes from stage 2 non-rapid eye movement sleep (NREM)...

11. [Heart rate variability, sleep and sleep disorders. | Semantic Scholar](https://www.semanticscholar.org/paper/Heart-rate-variability,-sleep-and-sleep-disorders.-Stein-Pu/6f4ca0c2355459aa430ed434366979c73957fe13) - Semantic Scholar extracted view of "Heart rate variability, sleep and sleep disorders." by P. Stein ...

12. [HRV analysis methods - How is HRV calculated - Kubios](https://www.kubios.com/blog/hrv-analysis-methods/) - Introducing the HRV analysis methods available in Kubios HRV software products. Time-domain, frequen...

13. [RMSSD, pNN50, SDNN and other HRV measurements](https://welltory.com/rmssd-and-other-hrv-measurements/) - Welltory is a scientifically proven way to measure HRV and stress. In this article we explain how we...

14. [Reproducibility of Heart Rate Variability Is Parameter and ...](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2017.01100/full) - by D Herzig · 2018 · Cited by 76 — Good reproducibility within and across nights was found for heart...

15. [Slow-Wave Sleep Estimation for Healthy Subjects and OSA Patients Using R-R Intervals - PubMed](https://pubmed.ncbi.nlm.nih.gov/28600268/) - We developed an automatic slow-wave sleep (SWS) detection algorithm that can be applied to groups of...

16. [Stages of Sleep: What Happens in a Normal Sleep Cycle?](https://www.sleepfoundation.org/stages-of-sleep) - Healthy sleep consists of four stages. We break down the traits of both REM and NREM stages, how the...

17. [How Much Deep, Light, and REM Sleep Do You Need?](https://www.healthline.com/health/how-much-deep-sleep-do-you-need) - Sleep is essential to health, and deep sleep is the most important of all for feeling rested and sta...

18. [Physiology, Sleep Stages - StatPearls - NCBI Bookshelf - NIH](https://www.ncbi.nlm.nih.gov/books/NBK526132/) - The human body cycles through 2 phases of sleep, (1) rapid eye movement (REM) and (2) nonrapid eye m...

19. [Fitbit Research Library](https://fitabase.com/research-library/?searchString=&category=Validation&data=Sleep) - Validation of Fitbit Charge 2 and Fitbit Alta HR Against Polysomnography for Assessing Sleep in Adul...

20. [Review Elicitation of sleep-onset REM periods in normal individuals using the sleep interruption technique (SIT)](https://www.sciencedirect.com/science/article/abs/pii/S1389945702001545) - Use of the sleep interruption technique (SIT) to elicit sleep onset REM periods (SOREMPs) in normal ...

21. [Sleep cycle - Wikipedia](https://en.wikipedia.org/wiki/Sleep_cycle)

