import numpy as np
import pandas as pd


def simulate_pulsar_signal(
    duration=10.0,
    sampling_rate=1000,
    period=0.5,
    pulse_width=0.03,
    pulse_amplitude=1.0,
    noise_level=0.2,
):
    """
    Simulate a simple pulsar signal.

    Parameters
    ----------
    duration : float
        Total observation time in seconds.
    sampling_rate : int
        Number of measurements per second.
    period : float
        Pulsar rotation period in seconds.
    pulse_width : float
        Width of each pulse in phase units.
    pulse_amplitude : float
        Height of the pulsar pulse.
    noise_level : float
        Standard deviation of Gaussian noise.

    Returns
    -------
    pandas.DataFrame
        Table with time and flux columns.
    """

    time = np.arange(0, duration, 1 / sampling_rate)

    phase = (time % period) / period

    pulse = pulse_amplitude * np.exp(-0.5 * ((phase - 0.5) / pulse_width) ** 2)

    noise = np.random.normal(0, noise_level, size=len(time))

    flux = pulse + noise

    data = pd.DataFrame({"time": time, "flux": flux})

    return data
