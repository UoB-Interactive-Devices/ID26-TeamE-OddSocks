# Scientific and Physiological Justification for Sleep Stage Detection

## 1. Introduction and Clinical Context
Current clinical gold-standard sleep tracking utilizes Polysomnography (PSG), tracking brainwaves (EEG), eye movement (EOG), and muscle tone (EMG). However, research extensively proves that consumer-grade wearable devices utilizing strictly Photoplethysmography (PPG) and accelerometry (Actigraphy) can accurately estimate 4-stage sleep cycles (Wake, Light, Deep, and REM) by proxying autonomic and musculoskeletal changes.

Our Bangle.js implementation operates on a distilled, computationally-efficient model derived from published algorithms (such as SLAMSS and Philips' bidirectional LSTM pipelines) and clinical Heart Rate Variability (HRV) studies.

## 2. Physiological Markers by Sleep Stage
The architecture of this application targets critical transitions in the autonomic nervous system over dense 60-second observation epochs.

### 2.1 Deep Sleep (NREM Stage 3)
Deep sleep, or slow-wave sleep, is physically restorative. Physiologically, this stage is characterized by substantial parasympathetic (vagal) dominance.
*   **Sensory Proxies:** 
    *   *Heart Rate:* Noticeable autonomic suppression, driving the heart rate to the lowest percentiles of the night's distribution.
    *   *HRV:* Increased High-Frequency (HF) variability due to stable respiratory sinus arrhythmia, resulting in low variance in time-domain metrics.
    *   *Movement:* Near-absolute gross body stillness.
*   **Implementation:** The algorithm tags epochs as candidate Deep Sleep when wrist activity approaches zero (`< A_DEEP_MAX`) and the mean Heart Rate falls into the bottom quintile (`hrP20`).

### 2.2 REM Sleep
Rapid Eye Movement (REM) sleep is defined clinically by vivid dreaming, muscle atonia (paralysis), and a highly active brain. Unlike deep sleep, REM exhibits fluctuating autonomic instability—rapid shifts between sympathetic and parasympathetic systemic dominance.
*   **Sensory Proxies:**
    *   *Heart Rate:* A dramatic elevation compared to NREM, typically exceeding the median nightly heart rate (`hrP50`) and approximating wakeful cardiac rhythms.
    *   *HRV:* Due to the autonomic instability, standard deviation of heart rate (sdHR) or RMSSD sharply spikes. Short-term epoch-to-epoch variances are exceptionally high.
    *   *Movement:* Muscle atonia visually mimics the extreme stillness of Deep Sleep (though small peripheral twitching occasionally bypasses wrist accelerometers).
    *   *Timing:* By circadian rule, the first REM phases rarely occur before 60-90 minutes post-sleep onset (REM latency).
*   **Implementation:** The sleep architecture leverages a heuristic modeled precisely on Yoon et al.’s HRV-only REM estimation framework. An epoch is classified as REM if movement remains intensely suppressed, HR accelerates past the median percentile, beat-to-beat variability (`sdHR` > 2.0) indicates autonomic chaos, and hard-coded latency constraints are met.

## 3. Minimal Viable Feature Set Architecture
While enterprise vendors (e.g., Fitbit, Firstbeat) utilize heavy Convolutional Neural Networks (CNN) or end-to-end deep learning, Song et al.'s SLAMSS model proves that an immense simplification of features (`Activity`, `Mean HR`, `HRSD`) firmly retains a ~70% accuracy ceiling against PSG. 

The constrained Bangle.js implementation adheres strictly to this validated minimal viable feature set:
1.  **Movement (Mean Absolute Deviation):** A computationally cheap $O(N)$ mathematical substitute for dedicated clinical actigraphy counts.
2.  **Mean HR:** Summarized efficiently using beat-to-beat (R-R) intervals over the epoch.
3.  **Standard Deviation of HR (`sdHR`):** Safely proxies complex frequency-domain HRV (like LF/HF ratios) without requiring costly Fast Fourier Transforms (FFTs) on the constrained nRF52840 microcontroller array.

## 4. The 60-Second Epoch Imperative
Traditional "dumb" fitness trackers average data over 5-to-10 minute blocks. However, clinically validated sleep algorithms universally operate on 30-to-60 second polling windows for an inflexible biological reason: Autonomic variations defining REM sleep (sudden heart rate acceleration, abrupt micro-awakenings) operate on extremely short biological timeframes. Averaging sensor data over 10 minutes permanently destroys the HRV variance required to discriminate REM from Light Sleep. 

By operating entirely within a continuous 60-second sliding epoch architecture, the Bangle.js application successfully approximates standard 30-second AASM clinical sleep scoring blocks while retaining extreme battery efficiency (discarding raw 25Hz PPG data out of RAM essentially in real-time).

## 5. Performance Expectations
Using similar features on PPG/ACT data, independent scientific research shows top-tier machine learning models achieving around 65–75% Kappa agreement for REM versus PSG. As a strictly heuristic and rule-based translation designed for un-tethered streaming on constrained 256kB RAM hardware, this embedded algorithm focuses on structural classification (high specificity and logical temporal smoothing) over perfect generalized precision, yielding an incredibly capable and physiologically-backed offline wearable tracker.

---

### References Used in Architectural Design
*   **Wulterkens et al. (2021)** - *It is All in the Wrist: Wearable Sleep Staging in a Clinical Population.* Utilizes PPG/Actigraphy LSTM Sleep Classification strategies.
*   **Song et al. (2023)** - *AI-Driven sleep staging from actigraphy and heart rate.* Introduces the SLAMSS strategy, proving viability of coarse heart rate data + actigraphy.
*   **Fonseca et al. (2023)** - *A computationally efficient algorithm for wearable sleep staging.* Definitively demonstrates that instantaneous 10Hz HR and 30s actigraphy is the minimal requirement for 4-class sleep tracking.
*   **Yoon et al. (2017)** - *REM sleep estimation based on autonomic dynamics using R-R intervals.* Specifically models the adaptive-thresholding of autonomic dynamic features used in the Bangle REM classifier.
