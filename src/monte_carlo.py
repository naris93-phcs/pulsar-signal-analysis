import pandas as pd

from src.simulate import simulate_pulsar_signal
from src.period_search import find_dominant_period
from src.folding import fold_signal
from src.profile import mean_pulse_profile
from src.peak_detection import (
    find_pulse_peak,
    measure_pulse_width,
    compute_snr,
)


def run_monte_carlo(
    simulation_config,
    analysis_config,
    n_simulations=100,
):
    """
    Run repeated pulsar simulations and collect the measurements.

    Parameters
    ----------
    simulation_config : dict
        Parameters used to generate each simulated pulsar signal.
    analysis_config : dict
        Parameters used by the analysis pipeline.
    n_simulations : int
        Number of independent simulations.

    Returns
    -------
    pandas.DataFrame
        One row per successful simulation, containing the measured values.
    """

    results = []

    for run_number in range(1, n_simulations + 1):
        try:
            data = simulate_pulsar_signal(
                **simulation_config,
            )

            best_period, _, _ = find_dominant_period(data)

            folded = fold_signal(
                data,
                best_period,
            )

            mean_profile = mean_pulse_profile(
                folded,
                bin_width=analysis_config["bin_width"],
            )

            peak = find_pulse_peak(
                mean_profile,
                min_prominence=analysis_config["min_prominence"],
            )

            pulse_width = measure_pulse_width(
                mean_profile,
                peak,
            )

            snr_result = compute_snr(
                mean_profile,
                peak,
                pulse_width,
                exclusion_factor=analysis_config["snr_exclusion_factor"],
            )

            pulse_duration = pulse_width["width_phase"] * best_period

            results.append(
                {
                    "run": run_number,
                    "estimated_period": best_period,
                    "peak_phase": peak["phase"],
                    "peak_flux": peak["flux"],
                    "peak_prominence": peak["prominence"],
                    "pulse_width_phase": pulse_width["width_phase"],
                    "pulse_duration": pulse_duration,
                    "baseline": snr_result["baseline"],
                    "noise_std": snr_result["noise_std"],
                    "signal_amplitude": snr_result["signal_amplitude"],
                    "snr": snr_result["snr"],
                    "success": True,
                }
            )

        except ValueError:
            results.append(
                {
                    "run": run_number,
                    "estimated_period": None,
                    "peak_phase": None,
                    "peak_flux": None,
                    "peak_prominence": None,
                    "pulse_width_phase": None,
                    "pulse_duration": None,
                    "baseline": None,
                    "noise_std": None,
                    "signal_amplitude": None,
                    "snr": None,
                    "success": False,
                }
            )

    return pd.DataFrame(results)
