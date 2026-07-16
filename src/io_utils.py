import pandas as pd


def save_measurements(
    best_period,
    peak,
    pulse_width,
    pulse_duration,
    snr_result,
    output_path,
):
    """
    Save pulse measurements to a CSV file.
    """

    results = pd.DataFrame(
        {
            "Quantity": [
                "Estimated Period",
                "Peak Phase",
                "Peak Flux",
                "Peak Prominence",
                "Pulse Width (phase)",
                "Pulse Duration (s)",
                "Baseline",
                "Noise Std",
                "Signal Amplitude",
                "SNR",
            ],
            "Value": [
                best_period,
                peak["phase"],
                peak["flux"],
                peak["prominence"],
                pulse_width["width_phase"],
                pulse_duration,
                snr_result["baseline"],
                snr_result["noise_std"],
                snr_result["signal_amplitude"],
                snr_result["snr"],
            ],
        }
    )

    results.to_csv(
        output_path,
        index=False,
    )
