![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-v2.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Scientific Computing](https://img.shields.io/badge/Scientific_Computing-Python-blueviolet)
![Status](https://img.shields.io/badge/Status-Active-success)

# Pulsar Signal Analysis

Python pipeline for simulating and analyzing pulsar signals using modern signal-processing techniques, including Fourier analysis, phase folding, pulse profile extraction, signal-to-noise estimation, and Monte Carlo validation.

The project supports both synthetic pulsar simulations and real pulsar observations from the European Pulsar Network (EPN) database through a unified analysis pipeline.

---

# Overview

Pulsars are rapidly rotating neutron stars that emit beams of electromagnetic radiation.

When one of these beams crosses Earth's line of sight, a pulse is detected. Recovering the pulsar's rotational period and pulse properties from noisy observations is a fundamental task in radio astronomy.

This project implements a complete scientific analysis pipeline that automatically:

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
- Analysis of real pulsar observations (EPN)
- Interactive command-line interface
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

├── data/
│   ├── simulated/
│   └── real/
│
├── results/
│   ├── simulation/
│   └── real_data/
│
├── src/
│   ├── config.py
│   ├── simulate.py
│   ├── real_data.py
│   ├── pipeline.py
│   ├── eda.py
│   ├── period_search.py
│   ├── folding.py
│   ├── profile.py
│   ├── peak_detection.py
│   ├── plotting.py
│   ├── monte_carlo.py
│   └── io_utils.py
│
├── main.py
├── requirements.txt
└── README.md
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

# Analysis Pipeline

```text
                 +------------------------+
                 | Synthetic Simulation   |
                 +------------------------+
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
                    Pulse Measurements
                            │
                            ▼
                  Monte Carlo Validation


                 +------------------------+
                 | Real Pulsar Observation|
                 +------------------------+
                            │
                            ▼
                   Mean Pulse Profile
                            │
                            ▼
                    Pulse Measurements
```

---

# Example Results

The pipeline automatically estimates:

- Pulsar period
- Pulse phase
- Pulse amplitude
- Pulse prominence
- Pulse width (FWHM)
- Pulse duration
- Signal-to-Noise Ratio (SNR)

### Synthetic Simulation

```text
Estimated period: 1.0000 s

Peak phase: 0.5100
Pulse width: 0.0794 phase
Signal amplitude: 0.925
SNR: 22.3
```

### Real Observation

```text
Pulsar: PSR B0329+54
Observation Frequency: 10.55 GHz

Peak phase: 0.4047
Peak flux: 2.4520
Peak prominence: 2.5464
SNR: 31.78
```

---

# Real Data Validation

In addition to synthetic simulations, the analysis pipeline has been validated using a real pulsar observation from the European Pulsar Network (EPN) database.

**Observed Pulsar**

- **PSR B0329+54**
- Observation Frequency: **10.55 GHz**
- Source: **European Pulsar Network (EPN)**

The same analysis pipeline is applied without modifying the core algorithms. Only the input data format is adapted, demonstrating that the software can process both simulated and real astronomical observations through a common workflow.

This validates the modular architecture of the project and demonstrates its extensibility to additional pulsar datasets.

---

# Monte Carlo Validation

The project includes a Monte Carlo framework that repeatedly simulates independent pulsar observations with different realizations of random noise.

This allows quantitative evaluation of:

- Detection stability
- Period estimation accuracy
- Signal-to-Noise Ratio distribution
- Algorithm robustness

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
- Radio Pulsar Observations

---

# Future Work

Planned extensions include:

- Interactive simulation parameter configuration
- Support for additional pulsars from the EPN database
- Detection of multiple pulse components
- Harmonic analysis
- Comparison of synthetic and real pulsar observations
- Unit testing of analysis modules
- Export of publication-ready analysis reports

---

# Author

Developed as a scientific software portfolio project focused on computational physics, signal processing, and radio astronomy.

The project emphasizes reproducible scientific workflows, modular software architecture, and modern Python development practices while demonstrating the analysis of both simulated and real pulsar observations.