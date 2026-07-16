from src.config import ANALYSIS_CONFIG
from src.peak_detection import (
    compute_snr,
    find_pulse_peak,
    measure_pulse_width,
)
from src.plotting import plot_pulse_measurements
from src.real_data import load_epn_profile


def main():
    real_profile = load_epn_profile(
        "data/real/b0329_54_10550mhz.asc"
    )

    mean_profile = real_profile.rename(
        columns={"flux": "mean_flux"}
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
        exclusion_factor=ANALYSIS_CONFIG[
            "snr_exclusion_factor"
        ],
    )

    pulse_duration = (
        pulse_width["width_phase"]
        * (
            real_profile["time"].max()
            - real_profile["time"].min()
        )
    )

    print()
    print("Real pulsar measurements")
    print("------------------------")
    print(f"Peak phase: {peak['phase']:.4f}")
    print(f"Peak flux: {peak['flux']:.4f}")
    print(f"Peak prominence: {peak['prominence']:.4f}")
    print(
        f"Pulse width (phase): "
        f"{pulse_width['width_phase']:.4f}"
    )
    print(f"Pulse duration: {pulse_duration:.6f} s")
    print(f"Baseline: {snr_result['baseline']:.4f}")
    print(
        f"Noise standard deviation: "
        f"{snr_result['noise_std']:.4f}"
    )
    print(
        f"Signal amplitude: "
        f"{snr_result['signal_amplitude']:.4f}"
    )
    print(f"SNR: {snr_result['snr']:.2f}")

    plot_pulse_measurements(
        mean_profile,
        peak,
        pulse_width,
        snr_result,
        output_path=(
            "results/figures/"
            "real_b0329_54_pulse_measurements.png"
        ),
    )


if __name__ == "__main__":
    main()