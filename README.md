![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-v1.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Scientific Computing](https://img.shields.io/badge/Scientific_Computing-Python-blueviolet)
![Status](https://img.shields.io/badge/Status-Stable-success)

# Pulsar Signal Analysis

Python pipeline for simulating and analyzing pulsar signals using signal processing techniques such as Fourier analysis, phase folding, pulse profile extraction, and Monte Carlo validation.

---

# Overview

Pulsars are rapidly rotating neutron stars that emit beams of electromagnetic radiation.

When one of these beams crosses Earth's line of sight, a pulse is detected. Recovering the pulsar's rotational period and pulse properties from noisy observations is a fundamental task in radio astronomy.

This project simulates pulsar observations and implements a complete analysis pipeline that automatically:

- estimates the pulsar period using Fast Fourier Transform (FFT)
- folds the signal in phase
- constructs the mean pulse profile
- detects the pulse automatically
- measures pulse properties
- evaluates the detection using Signal-to-Noise Ratio (SNR)
- validates the pipeline using Monte Carlo simulations

---

# Features

- Synthetic pulsar signal generation
- Exploratory Data Analysis (EDA)
- FFT-based period estimation
- Phase folding
- Mean pulse profile construction
- Automatic pulse peak detection
- Pulse width (FWHM) measurement
- Signal-to-Noise Ratio (SNR) estimation
- Monte Carlo validation
- Automatic CSV export of measurements
- Publication-quality plots

---

# Project Structure

```text
pulsar-signal-analysis/

├── main.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── config.py
│   ├── simulate.py
│   ├── eda.py
│   ├── period_search.py
│   ├── folding.py
│   ├── profile.py
│   ├── peak_detection.py
│   ├── plotting.py
│   ├── monte_carlo.py
│   └── io_utils.py
│
└── results/
    ├── figures/
    ├── measurements.csv
    └── tables/
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/naris93-phcs/pulsar-signal-analysis.git
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

# Example Analysis Pipeline

```
Simulated Signal
        │
        ▼
Exploratory Statistics
        │
        ▼
FFT Period Search
        │
        ▼
Phase Folding
        │
        ▼
Mean Pulse Profile
        │
        ▼
Peak Detection
        │
        ▼
Pulse Width (FWHM)
        │
        ▼
Signal-to-Noise Ratio
        │
        ▼
Monte Carlo Validation
```

---

# Example Results

The analysis automatically estimates:

- Pulsar period
- Pulse phase
- Pulse amplitude
- Pulse prominence
- Pulse width (FWHM)
- Pulse duration
- Signal-to-Noise Ratio (SNR)

Example output

```text
Estimated period: 1.0000 s

Peak phase: 0.5100
Pulse width: 0.0794 phase
Signal amplitude: 0.925
SNR: 22.3
```

---

# Monte Carlo Validation

The project includes a Monte Carlo framework that repeatedly simulates independent pulsar observations with different realizations of random noise.

This allows quantitative evaluation of:

- detection stability
- period estimation accuracy
- Signal-to-Noise Ratio distribution
- algorithm robustness

The Monte Carlo framework also provides the foundation for future validation studies under increasingly challenging noise conditions.

---

# Scientific Background

The project demonstrates several techniques commonly used in astronomy, signal processing, and scientific computing, including:

- Fast Fourier Transform (FFT)
- Phase Folding
- Gaussian Pulse Profiles
- Full Width at Half Maximum (FWHM)
- Signal-to-Noise Ratio (SNR)
- Monte Carlo simulations

---

# Future Work

Planned extensions include:

- Analysis of real pulsar observations
- Automatic harmonic detection
- Multiple pulse components
- Parameter estimation under different noise conditions
- Detection efficiency studies
- Interactive visualization dashboard

---

# Author

Developed as part of a scientific computing portfolio focused on particle physics, astrophysics, and data analysis.

The goal of this repository is both educational and scientific: to build reproducible, well-documented analysis pipelines using modern Python tools and software engineering practices.