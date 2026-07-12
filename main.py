from src.simulate import simulate_pulsar_signal
from src.eda import print_summary_statistics
from src.period_search import find_dominant_period
from src.folding import fold_signal
from src.profile import mean_pulse_profile
from src.peak_detection import (find_pulse_peak,measure_pulse_width,compute_snr)
from src.plotting import (plot_signal,plot_flux_histogram,plot_folded_signal,plot_mean_pulse_profile,plot_pulse_measurements)
from src.io_utils import save_measurements
from src.config import (SIMULATION_CONFIG,ANALYSIS_CONFIG,MONTE_CARLO_CONFIG,)
from src.monte_carlo import run_monte_carlo

# Easier dataset for development
data = simulate_pulsar_signal(
    **SIMULATION_CONFIG,
)

# Basic exploratory statistics
print_summary_statistics(data)

# Estimate the pulsar period using FFT
best_period, frequencies, power = find_dominant_period(data)

print()
print(f"Estimated period: {best_period:.4f} s")

# Fold the signal using the estimated period
folded = fold_signal(data, best_period)

# Calculate the mean pulse profile
mean_profile = mean_pulse_profile(
    folded,
    bin_width=ANALYSIS_CONFIG["bin_width"],
)


peak = find_pulse_peak(
    mean_profile,
    min_prominence=ANALYSIS_CONFIG["min_prominence"],
)
pulse_width = measure_pulse_width(
    mean_profile,
    peak,
)

snr_result = compute_snr(
    mean_profile,
    peak,
    pulse_width,
    exclusion_factor=ANALYSIS_CONFIG["snr_exclusion_factor"],
)

pulse_duration = pulse_width["width_phase"] * best_period


save_measurements(
    best_period,
    peak,
    pulse_width,
    pulse_duration,
    snr_result,
    output_path="results/measurements.csv",
)

# Plot the original simulated signal
plot_signal(
    data,
    output_path="results/figures/simulated_signal.png",
)

# Plot the flux distribution
plot_flux_histogram(
    data,
    output_path="results/figures/flux_histogram.png",
)

# Plot all folded data points
plot_folded_signal(
    folded,
    output_path="results/figures/folded_signal.png",
)

# Plot the averaged pulse profile
plot_mean_pulse_profile(
    mean_profile,
    output_path="results/figures/mean_pulse_profile.png",
)
plot_pulse_measurements(
    mean_profile,
    peak,
    pulse_width,
    snr_result,
    output_path="results/figures/pulse_measurements.png",
)


print()
print("Pulse measurements")
print("------------------")
print(f"Peak phase: {peak['phase']:.4f}")
print(f"Peak flux: {peak['flux']:.4f}")
print(f"Peak prominence: {peak['prominence']:.4f}")
print(f"Pulse width (phase): {pulse_width['width_phase']:.4f}")
print(f"Pulse duration: {pulse_duration:.4f} s")
print(f"Baseline: {snr_result['baseline']:.4f}")
print(f"Noise standard deviation: {snr_result['noise_std']:.4f}")
print(f"Signal amplitude: {snr_result['signal_amplitude']:.4f}")
print(f"SNR: {snr_result['snr']:.2f}")

monte_carlo_results = run_monte_carlo(
    simulation_config=SIMULATION_CONFIG,
    analysis_config=ANALYSIS_CONFIG,
    n_simulations=MONTE_CARLO_CONFIG["n_simulations"],
)

monte_carlo_results.to_csv(
    "results/tables/monte_carlo_results.csv",
    index=False,
)

successful_runs = monte_carlo_results[
    monte_carlo_results["success"]
]

print()
print("Monte Carlo summary")
print("-------------------")
print(f"Total runs: {len(monte_carlo_results)}")
print(f"Successful runs: {len(successful_runs)}")
print(
    f"Mean estimated period: "
    f"{successful_runs['estimated_period'].mean():.4f} s"
)
print(
    f"Period standard deviation: "
    f"{successful_runs['estimated_period'].std():.4f} s"
)
print(
    f"Mean SNR: "
    f"{successful_runs['snr'].mean():.2f}"
)
print(
    f"SNR standard deviation: "
    f"{successful_runs['snr'].std():.2f}"
)