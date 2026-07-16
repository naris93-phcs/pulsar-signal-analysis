from pathlib import Path

import pandas as pd


def load_epn_profile(file_path):
    """
    Load a total-power pulsar profile from the EPN database.

    Parameters
    ----------
    file_path : str or pathlib.Path
        Path to the EPN ASCII profile.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing time, flux, and normalized phase.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"EPN profile not found: {file_path}"
        )

    profile = pd.read_csv(
        file_path,
        sep=r"\s+",
        skiprows=2,
        header=None,
        names=["time", "flux"],
    )

    if profile.empty:
        raise ValueError("The EPN profile contains no data.")

    time_start = profile["time"].min()
    time_end = profile["time"].max()
    profile_duration = time_end - time_start

    if profile_duration <= 0:
        raise ValueError(
            "The profile time range must be greater than zero."
        )

    profile["phase"] = (
        profile["time"] - time_start
    ) / profile_duration

    return profile[["time", "phase", "flux"]]