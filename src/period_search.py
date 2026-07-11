import numpy as np


def find_dominant_period(data):
    """
    Estimate the dominant period of the signal using FFT.
    """

    time = data["time"].values
    flux = data["flux"].values

    dt = time[1] - time[0]

    flux_centered = flux - np.mean(flux)

    spectrum = np.fft.rfft(flux_centered)
    frequencies = np.fft.rfftfreq(len(flux_centered), d=dt)

    power = np.abs(spectrum) ** 2

    power[0] = 0

    best_index = np.argmax(power)
    best_frequency = frequencies[best_index]
    best_period = 1 / best_frequency

    return best_period, frequencies, power