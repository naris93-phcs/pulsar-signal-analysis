from pathlib import Path

import matplotlib.pyplot as plt


def _finalize_figure(fig, output_path=None, show=True):
    """
    Save, optionally display, and close a Matplotlib figure.
    """
    fig.tight_layout()

    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=300)

    if show:
        plt.show()

    plt.close(fig)


def plot_signal(data, output_path=None, show=True):
    """
    Plot flux as a function of time.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame containing time and flux columns.
    output_path : str, pathlib.Path or None
        If provided, save the figure to this path.
    show : bool
        Whether to display the figure interactively.
    """
    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(
        data["time"],
        data["flux"],
        linewidth=0.8,
    )

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Flux")
    ax.set_title("Simulated Pulsar Signal")

    _finalize_figure(
        fig,
        output_path=output_path,
        show=show,
    )


def plot_flux_histogram(data, output_path=None, show=True):
    """
    Plot a histogram of the simulated flux values.
    """
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.hist(
        data["flux"],
        bins=60,
        edgecolor="black",
        alpha=0.8,
    )

    ax.set_xlabel("Flux")
    ax.set_ylabel("Count")
    ax.set_title("Flux Distribution")

    _finalize_figure(
        fig,
        output_path=output_path,
        show=show,
    )


def plot_folded_signal(data, output_path=None, show=True):
    """
    Plot the folded pulsar signal.
    """
    fig, ax = plt.subplots(figsize=(10, 4))

    ax.scatter(
        data["phase"],
        data["flux"],
        s=5,
    )

    ax.set_xlabel("Phase")
    ax.set_ylabel("Flux")
    ax.set_title("Folded Pulsar Signal")

    _finalize_figure(
        fig,
        output_path=output_path,
        show=show,
    )


def plot_mean_pulse_profile(
    profile,
    output_path=None,
    show=True,
):
    """
    Plot the mean folded pulse profile.

    Parameters
    ----------
    profile : pandas.DataFrame
        DataFrame containing phase_center and mean_flux columns.
    output_path : str, pathlib.Path or None
        If provided, save the figure to this path.
    show : bool
        Whether to display the figure interactively.
    """
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(
        profile["phase_center"],
        profile["mean_flux"],
        marker="o",
        markersize=3,
        linewidth=1.5,
    )

    ax.set_xlabel("Phase")
    ax.set_ylabel("Mean Flux")
    ax.set_title("Mean Folded Pulse Profile")

    _finalize_figure(
        fig,
        output_path=output_path,
        show=show,
    )


def plot_pulse_measurements(
    profile,
    peak,
    pulse_width,
    snr_result,
    output_path=None,
    title="Pulse Profile Measurements",
    show=True,
):
    """
    Plot a pulse profile with peak, baseline, and FWHM measurements.
    """
    phase = profile["phase_center"].to_numpy()
    flux = profile["mean_flux"].to_numpy()

    if len(phase) < 2:
        raise ValueError(
            "At least two phase values are required for plotting."
        )

    phase_step = phase[1] - phase[0]

    left_phase = (
        phase[0]
        + pulse_width["left"] * phase_step
    )

    right_phase = (
        phase[0]
        + pulse_width["right"] * phase_step
    )

    half_height = (
        peak["flux"] + snr_result["baseline"]
    ) / 2

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        phase,
        flux,
        marker="o",
        markersize=3,
        linewidth=1.5,
        label="Pulse profile",
    )

    ax.scatter(
        peak["phase"],
        peak["flux"],
        s=60,
        label="Detected peak",
        zorder=3,
    )

    ax.axhline(
        snr_result["baseline"],
        linestyle="--",
        linewidth=1,
        label="Baseline",
    )

    ax.hlines(
        half_height,
        left_phase,
        right_phase,
        linewidth=2,
        label="FWHM",
    )

    ax.axvline(
        left_phase,
        linestyle=":",
        linewidth=1,
    )

    ax.axvline(
        right_phase,
        linestyle=":",
        linewidth=1,
    )

    ax.set_xlabel("Phase")
    ax.set_ylabel("Mean Flux")
    ax.set_title(title)
    ax.legend()

    _finalize_figure(
        fig,
        output_path=output_path,
        show=show,
    )


def plot_real_pulse_profile(
    profile,
    output_path=None,
    pulsar_name="PSR B0329+54",
    frequency_ghz=10.55,
    show=True,
):
    """
    Plot a real pulsar pulse profile.

    Parameters
    ----------
    profile : pandas.DataFrame
        Profile containing phase_center and mean_flux columns.
    output_path : str, pathlib.Path or None
        If provided, save the figure to this path.
    pulsar_name : str
        Pulsar identifier displayed in the title.
    frequency_ghz : float
        Observation frequency in GHz.
    show : bool
        Whether to display the figure interactively.
    """
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        profile["phase_center"],
        profile["mean_flux"],
        linewidth=1.2,
    )

    ax.set_xlabel("Phase")
    ax.set_ylabel("Mean Flux")
    ax.set_title(
        f"Real Pulsar Profile ({pulsar_name})\n"
        f"Observation Frequency: {frequency_ghz:.2f} GHz"
    )

    ax.grid(alpha=0.3)

    _finalize_figure(
        fig,
        output_path=output_path,
        show=show,
    )


def plot_off_pulse_noise(
    profile,
    peak,
    pulse_width,
    output_path=None,
    exclusion_factor=2.0,
    show=True,
):
    """
    Plot the flux distribution outside the detected pulse region.

    Parameters
    ----------
    profile : pandas.DataFrame
        Profile containing phase_center and mean_flux columns.
    peak : dict
        Peak measurement returned by find_pulse_peak.
    pulse_width : dict
        Pulse-width result returned by measure_pulse_width.
    output_path : str, pathlib.Path or None
        If provided, save the figure to this path.
    exclusion_factor : float
        Multiplier controlling the excluded region around the pulse.
    show : bool
        Whether to display the figure interactively.
    """
    half_exclusion_width = (
        exclusion_factor
        * pulse_width["width_phase"]
        / 2
    )

    phase_distance = abs(
        profile["phase_center"] - peak["phase"]
    )

    off_pulse_flux = profile.loc[
        phase_distance > half_exclusion_width,
        "mean_flux",
    ]

    if off_pulse_flux.empty:
        raise ValueError(
            "No off-pulse samples remain after pulse exclusion."
        )

    baseline = off_pulse_flux.mean()

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(
        off_pulse_flux,
        bins=30,
        edgecolor="black",
        alpha=0.8,
    )

    ax.axvline(
        baseline,
        linestyle="--",
        label=f"Baseline = {baseline:.4f}",
    )

    ax.set_xlabel("Off-Pulse Flux")
    ax.set_ylabel("Count")
    ax.set_title("Off-Pulse Noise Distribution")
    ax.legend()
    ax.grid(alpha=0.3)

    _finalize_figure(
        fig,
        output_path=output_path,
        show=show,
    )