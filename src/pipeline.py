from pathlib import Path

from src.config import (
    ANALYSIS_CONFIG,
    MONTE_CARLO_CONFIG,
    SIMULATION_CONFIG,
)
from src.eda import print_summary_statistics
from src.folding import fold_signal
from src.io_utils import save_measurements
from src.monte_carlo import run_monte_carlo
from src.peak_detection import (
    compute_snr,
    find_pulse_peak,
    measure_pulse_width,
)
from src.period_search import find_dominant_period
from src.plotting import (
    plot_flux_histogram,
    plot_folded_signal,
    plot_mean_pulse_profile,
    plot_off_pulse_noise,
    plot_pulse_measurements,
    plot_real_pulse_profile,
    plot_signal,
)
from src.profile import mean_pulse_profile
from src.real_data import load_epn_profile
from src.simulate import simulate_pulsar_signal


def run_simulation_analysis():
    """
    Run the complete synthetic pulsar analysis pipeline.
    """
    simulation_results_dir = Path("results/simulation")
    simulation_results_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    data = simulate_pulsar_signal(
        **SIMULATION_CONFIG,
    )

    print_summary_statistics(data)

    best_period, _, _ = find_dominant_period(data)

    print()
    print(f"Estimated period: {best_period:.4f} s")

    folded = fold_signal(
        data,
        best_period,
    )

    mean_profile = mean_pulse_profile(
        folded,
        bin_width=ANALYSIS_CONFIG["bin_width"],
    )

    peak = find_pulse_peak(
        mean_profile,
        min_prominence=ANALYSIS_CONFIG[
            "min_prominence"
        ],
    )

    pulse_width = measure_pulse_width(
        mean_profile,
        peak,
    )

    snr_result = compute_snr(
        mean_profile,
        peak,
        pulse_width,
        exclusion_factor=ANALYSIS_CONFIG[
            "snr_exclusion_factor"
        ],
    )

    pulse_duration = (
        pulse_width["width_phase"] * best_period
    )

    save_measurements(
        best_period,
        peak,
        pulse_width,
        pulse_duration,
        snr_result,
        output_path=(
            simulation_results_dir
            / "measurements.csv"
        ),
    )

    plot_signal(
        data,
        output_path=(
            simulation_results_dir
            / "simulated_signal.png"
        ),
        show=True,
    )

    plot_flux_histogram(
        data,
        output_path=(
            simulation_results_dir
            / "flux_histogram.png"
        ),
        show=True,
    )

    plot_folded_signal(
        folded,
        output_path=(
            simulation_results_dir
            / "folded_signal.png"
        ),
        show=True,
    )

    plot_mean_pulse_profile(
        mean_profile,
        output_path=(
            simulation_results_dir
            / "mean_pulse_profile.png"
        ),
        show=True,
    )

    plot_pulse_measurements(
        mean_profile,
        peak,
        pulse_width,
        snr_result,
        output_path=(
            simulation_results_dir
            / "pulse_measurements.png"
        ),
        title="Synthetic Pulse Profile Measurements",
        show=True,
    )

    print_measurements(
        peak,
        pulse_width,
        pulse_duration,
        snr_result,
    )

    monte_carlo_results = run_monte_carlo(
        simulation_config=SIMULATION_CONFIG,
        analysis_config=ANALYSIS_CONFIG,
        n_simulations=MONTE_CARLO_CONFIG[
            "n_simulations"
        ],
    )

    monte_carlo_results.to_csv(
        simulation_results_dir
        / "monte_carlo_results.csv",
        index=False,
    )

    print_monte_carlo_summary(
        monte_carlo_results
    )


def run_real_data_analysis():
    """
    Analyze a real EPN pulse profile for PSR B0329+54.
    """
    real_results_dir = Path("results/real_data")
    real_results_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    real_profile = load_epn_profile(
        "data/real/b0329_54_10550mhz.asc"
    )

    mean_profile = real_profile.rename(
        columns={
            "phase": "phase_center",
            "flux": "mean_flux",
        }
    )

    peak = find_pulse_peak(
        mean_profile,
        min_prominence=ANALYSIS_CONFIG[
            "min_prominence"
        ],
    )

    pulse_width = measure_pulse_width(
        mean_profile,
        peak,
    )

    snr_result = compute_snr(
        mean_profile,
        peak,
        pulse_width,
        exclusion_factor=ANALYSIS_CONFIG[
            "snr_exclusion_factor"
        ],
    )

    profile_duration = (
        real_profile["time"].max()
        - real_profile["time"].min()
    )

    pulse_duration = (
        pulse_width["width_phase"]
        * profile_duration
    )

    plot_real_pulse_profile(
        mean_profile,
        output_path=(
            real_results_dir
            / "real_b0329_54_profile.png"
        ),
        pulsar_name="PSR B0329+54",
        frequency_ghz=10.55,
        show=True,
    )

    plot_off_pulse_noise(
        mean_profile,
        peak,
        pulse_width,
        output_path=(
            real_results_dir
            / "real_b0329_54_off_pulse_noise.png"
        ),
        exclusion_factor=ANALYSIS_CONFIG[
            "snr_exclusion_factor"
        ],
        show=True,
    )

    plot_pulse_measurements(
        mean_profile,
        peak,
        pulse_width,
        snr_result,
        output_path=(
            real_results_dir
            / "real_b0329_54_pulse_measurements.png"
        ),
        title=(
            "Real Pulsar Profile "
            "(PSR B0329+54)"
        ),
        show=True,
    )

    print()
    print("Real pulsar profile")
    print("-------------------")
    print("Pulsar: PSR B0329+54")
    print("Frequency: 10.55 GHz")
    print("Source: EPN Database")

    print_measurements(
        peak,
        pulse_width,
        pulse_duration,
        snr_result,
    )


def print_measurements(
    peak,
    pulse_width,
    pulse_duration,
    snr_result,
):
    """
    Print the measured pulse properties.
    """
    print()
    print("Pulse measurements")
    print("------------------")
    print(f"Peak phase: {peak['phase']:.4f}")
    print(f"Peak flux: {peak['flux']:.4f}")
    print(
        f"Peak prominence: "
        f"{peak['prominence']:.4f}"
    )
    print(
        f"Pulse width (phase): "
        f"{pulse_width['width_phase']:.4f}"
    )
    print(
        f"Pulse duration: "
        f"{pulse_duration:.6f} s"
    )
    print(
        f"Baseline: "
        f"{snr_result['baseline']:.4f}"
    )
    print(
        f"Noise standard deviation: "
        f"{snr_result['noise_std']:.4f}"
    )
    print(
        f"Signal amplitude: "
        f"{snr_result['signal_amplitude']:.4f}"
    )
    print(f"SNR: {snr_result['snr']:.2f}")


def print_monte_carlo_summary(
    monte_carlo_results,
):
    """
    Print summary statistics from Monte Carlo simulations.
    """
    successful_runs = monte_carlo_results[
        monte_carlo_results["success"]
    ]

    print()
    print("Monte Carlo summary")
    print("-------------------")
    print(
        f"Total runs: "
        f"{len(monte_carlo_results)}"
    )
    print(
        f"Successful runs: "
        f"{len(successful_runs)}"
    )
    print(
        "Mean estimated period: "
        f"{successful_runs['estimated_period'].mean():.4f} s"
    )
    print(
        "Period standard deviation: "
        f"{successful_runs['estimated_period'].std():.4f} s"
    )
    print(
        "Mean SNR: "
        f"{successful_runs['snr'].mean():.2f}"
    )
    print(
        "SNR standard deviation: "
        f"{successful_runs['snr'].std():.2f}"
    )