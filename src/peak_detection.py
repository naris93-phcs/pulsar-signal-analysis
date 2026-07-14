import numpy as np
from scipy.signal import find_peaks, peak_widths


def find_pulse_peak(profile, min_prominence=0.1):
    """
    Find the dominant peak in the mean pulse profile.

    Parameters
    ----------
    profile : pandas.DataFrame
        DataFrame containing phase_center and mean_flux columns.
    min_prominence : float
        Minimum prominence required for a detected peak.

    Returns
    -------
    dict
        Peak index, phase, flux, and prominence.
    """

    flux = profile["mean_flux"].to_numpy()

    peaks, properties = find_peaks(
        flux,
        prominence=min_prominence,
    )

    if len(peaks) == 0:
        raise ValueError("No pulse peak was detected.")

    strongest_peak_position = np.argmax(properties["prominences"])
    peak_index = peaks[strongest_peak_position]

    peak_phase = profile["phase_center"].iloc[peak_index]
    peak_flux = profile["mean_flux"].iloc[peak_index]
    peak_prominence = properties["prominences"][strongest_peak_position]

    return {
        "index": peak_index,
        "phase": float(peak_phase),
        "flux": float(peak_flux),
        "prominence": float(peak_prominence),
    }


def measure_pulse_width(profile, peak):
    """
    Measure the width of the detected pulse.

    Parameters
    ----------
    profile : pandas.DataFrame
        Mean pulse profile.

    peak : dict
        Output dictionary from find_pulse_peak().

    Returns
    -------
    dict
        Pulse width in bins and phase units.
    """

    flux = profile["mean_flux"].to_numpy()

    widths, _, left_ips, right_ips = peak_widths(
        flux,
        [peak["index"]],
        rel_height=0.5,
    )

    phase_step = profile["phase_center"].iloc[1] - profile["phase_center"].iloc[0]

    width_phase = widths[0] * phase_step

    return {
        "width_bins": float(widths[0]),
        "width_phase": float(width_phase),
        "left": float(left_ips[0]),
        "right": float(right_ips[0]),
    }


def compute_snr(
    profile,
    peak,
    pulse_width,
    exclusion_factor=1.5,
):
    """
    Estimate the signal-to-noise ratio of the pulse.

    Parameters
    ----------
    profile : pandas.DataFrame
        Mean pulse profile containing phase_center and mean_flux.
    peak : dict
        Output from find_pulse_peak().
    pulse_width : dict
        Output from measure_pulse_width().
    exclusion_factor : float
        Size of the region excluded around the pulse,
        expressed in pulse-width units.

    Returns
    -------
    dict
        Signal-to-noise ratio, baseline, and noise standard deviation.
    """

    phase = profile["phase_center"].to_numpy()
    flux = profile["mean_flux"].to_numpy()

    half_exclusion_width = exclusion_factor * pulse_width["width_phase"] / 2

    pulse_start = peak["phase"] - half_exclusion_width
    pulse_end = peak["phase"] + half_exclusion_width

    off_pulse_mask = (phase < pulse_start) | (phase > pulse_end)
    off_pulse_flux = flux[off_pulse_mask]

    baseline = off_pulse_flux.mean()
    noise_std = off_pulse_flux.std(ddof=1)

    signal_amplitude = peak["flux"] - baseline
    snr = signal_amplitude / noise_std

    return {
        "snr": float(snr),
        "baseline": float(baseline),
        "noise_std": float(noise_std),
        "signal_amplitude": float(signal_amplitude),
    }
