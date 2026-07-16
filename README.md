![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-v2.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Scientific Computing](https://img.shields.io/badge/Scientific_Computing-Python-blueviolet)
![Status](https://img.shields.io/badge/Status-Active-success)

# Pulsar Signal Analysis

A scientific Python pipeline for simulating and analyzing pulsar signals using modern signal-processing techniques, including Fourier analysis, phase folding, pulse profile extraction, signal-to-noise estimation, and Monte Carlo validation.

The project supports both **synthetic pulsar simulations** and **real pulsar observations** from the **European Pulsar Network (EPN)** through a unified and modular analysis pipeline.

---

<p align="center">
<img src="assets/banner.png" width="900">
</p>

---

# Scientific Background

Pulsars are among the most fascinating objects in modern astrophysics.

They are **rapidly rotating neutron stars**, formed during the gravitational collapse of massive stars after supernova explosions.

Although only about 20 kilometers in diameter, a neutron star typically contains more mass than the Sun, making it one of the densest forms of matter known in the Universe.

Because neutron stars possess extremely strong magnetic fields, charged particles are accelerated along their magnetic poles, producing narrow beams of electromagnetic radiation that sweep across space as the star rotates.

If one of these beams intersects Earth's line of sight, an observer detects a highly regular sequence of pulses, similar to the light emitted by a rotating lighthouse.

Recovering these pulses from noisy observations is one of the fundamental tasks in radio astronomy and provides valuable information about neutron stars, their environments, and the physics governing ultra-dense matter.

---

# Project Overview

This project implements a complete scientific analysis pipeline capable of processing both simulated and real pulsar observations.

The software automatically

- simulates realistic pulsar observations
- estimates the rotational period using Fast Fourier Transform (FFT)
- folds the signal into rotational phase
- constructs the mean pulse profile
- detects the pulse automatically
- measures pulse properties
- estimates the Signal-to-Noise Ratio (SNR)
- validates the complete pipeline through Monte Carlo simulations
- analyzes real pulsar observations from the European Pulsar Network (EPN)

---

# Features

✔ Synthetic pulsar signal generation

✔ Analysis of real pulsar observations

✔ Interactive command-line interface

✔ Exploratory Data Analysis (EDA)

✔ FFT-based period estimation

✔ Phase folding

✔ Mean pulse profile construction

✔ Automatic pulse peak detection

✔ Pulse width (FWHM) measurement

✔ Signal-to-Noise Ratio estimation

✔ Monte Carlo validation

✔ Automatic CSV export

✔ Publication-quality figures

✔ Modular scientific software architecture

---

# Gallery

## Simulated Pulsar Signal

<p align="center">
<img src="assets/gallery/simulated_signal.png" width="900">
</p>

---

## Folded Pulsar Signal

<p align="center">
<img src="assets/gallery/folded_signal.png" width="900">
</p>

---

## Pulse Profile Measurements

<p align="center">
<img src="assets/gallery/pulse_measurements.png" width="850">
</p>

---

## Real Pulsar Observation (PSR B0329+54)

<p align="center">
<img src="assets/gallery/psr_b0329_54_profile.png" width="900">
</p>

---

# Project Structure

```text
pulsar-signal-analysis/

├── assets/
│   ├── banner.png
│   ├── pulsar_image.png
│   └── gallery/
│
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
│   ├── pipeline.py
│   ├── simulate.py
│   ├── real_data.py
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

```
                     Synthetic Signal
                             │
                             ▼
                 Exploratory Data Analysis
                             │
                             ▼
                    FFT Period Estimation
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


                      Real Observation
                             │
                             ▼
                 Mean Pulse Profile
                             │
                             ▼
                    Pulse Measurements
```

---

# Example Results

The pipeline automatically estimates

- Rotational period
- Pulse phase
- Pulse amplitude
- Pulse prominence
- Pulse width (FWHM)
- Pulse duration
- Signal-to-Noise Ratio (SNR)

### Synthetic Signal

```text
Estimated period: 1.0000 s

Peak phase: 0.5100

Pulse width: 0.0794 phase

Signal amplitude: 0.925

SNR: 22.3
```

### Real Observation

```text
PSR B0329+54

Observation Frequency: 10.55 GHz

Peak phase: 0.4047

Peak flux: 2.4520

Peak prominence: 2.5464

SNR: 31.78
```

---

# Real Data Validation

The analysis pipeline has also been validated using a real observation of **PSR B0329+54** obtained from the **European Pulsar Network (EPN)** database.

The same analysis algorithms developed for the simulated observations are applied directly to the real dataset without modifying the core processing workflow.

This demonstrates the flexibility, modularity, and reproducibility of the software architecture while highlighting its applicability to real astronomical observations.

---

# Monte Carlo Validation

A dedicated Monte Carlo framework repeatedly generates independent pulsar observations with different realizations of random noise.

This enables quantitative evaluation of

- detection stability

- robustness against noise

- period estimation accuracy

- Signal-to-Noise Ratio distribution

The Monte Carlo implementation provides a solid foundation for future statistical studies under increasingly challenging observational conditions.

---

# Scientific Techniques

This project demonstrates several techniques widely used in

- Radio Astronomy

- Scientific Computing

- Computational Physics

- Signal Processing

including

- Fast Fourier Transform (FFT)

- Phase Folding

- Pulse Profile Analysis

- Peak Detection

- Full Width at Half Maximum (FWHM)

- Signal-to-Noise Ratio (SNR)

- Monte Carlo Simulation

---

# Future Work

Future extensions include

- Interactive simulation parameter configuration

- Automatic parameter optimization

- Multiple pulsar support

- Harmonic analysis

- Comparison between synthetic and real observations

- Bayesian parameter estimation

- Unit testing

- Continuous Integration (CI)

- Interactive visualization dashboard

---

# Author

Developed as part of a scientific software portfolio focused on

- Computational Physics

- Particle Physics

- Astrophysics

- Scientific Computing

- Signal Processing

The primary goal of this repository is to demonstrate the development of reproducible, modular, and well-documented scientific software using modern Python tools while applying real-world data analysis techniques commonly used in observational astrophysics.