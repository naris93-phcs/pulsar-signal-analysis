import matplotlib.pyplot as plt


def plot_signal(data, output_path=None):
    """
    Plot flux as a function of time.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame containing time and flux columns.
    output_path : str or None
        If given, save the figure to this path.
    """

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(data["time"], data["flux"], linewidth=0.8)

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Flux")
    ax.set_title("Simulated Pulsar Signal")

    fig.tight_layout()

    if output_path is not None:
        fig.savefig(output_path, dpi=300)

    plt.show()


def plot_flux_histogram(data, output_path=None):
    """
    Plot a histogram of the flux values.
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.hist(data["flux"], bins=60)

    ax.set_xlabel("Flux")
    ax.set_ylabel("Counts")
    ax.set_title("Flux Distribution")

    fig.tight_layout()

    if output_path is not None:
        fig.savefig(output_path, dpi=300)

    plt.show()


def plot_folded_signal(data, output_path=None):
    """
    Plot folded pulsar signal.
    """

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.scatter(data["phase"], data["flux"], s=5)

    ax.set_xlabel("Phase")
    ax.set_ylabel("Flux")
    ax.set_title("Folded Pulsar Signal")

    fig.tight_layout()

    if output_path is not None:
        fig.savefig(output_path, dpi=300)

    plt.show()


def plot_mean_pulse_profile(profile, output_path=None):
    """
    Plot the mean folded pulse profile.

    Parameters
    ----------
    profile : pandas.DataFrame
        DataFrame containing phase_center and mean_flux columns.
    output_path : str or None
        Path where the figure will be saved.
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

    fig.tight_layout()

    if output_path is not None:
        fig.savefig(output_path, dpi=300)

    plt.show()


def plot_pulse_measurements(
    profile,
    peak,
    pulse_width,
    snr_result,
    output_path=None,
):
    """
    Plot the mean pulse profile with peak, baseline,
    and FWHM measurements.
    """

    phase = profile["phase_center"].to_numpy()
    flux = profile["mean_flux"].to_numpy()

    phase_step = phase[1] - phase[0]

    left_phase = phase[0] + pulse_width["left"] * phase_step
    right_phase = phase[0] + pulse_width["right"] * phase_step

    half_height = (peak["flux"] + snr_result["baseline"]) / 2

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        phase,
        flux,
        marker="o",
        markersize=3,
        linewidth=1.5,
        label="Mean pulse profile",
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
    ax.set_title("Pulse Profile Measurements")

    ax.legend()

    fig.tight_layout()

    if output_path is not None:
        fig.savefig(output_path, dpi=300)

    plt.show()
