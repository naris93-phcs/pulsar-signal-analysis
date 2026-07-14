import pandas as pd
import numpy as np


def mean_pulse_profile(folded_data, bin_width=0.02):
    """
    Calculate the mean folded pulse profile.

    Parameters
    ----------
    folded_data : pandas.DataFrame
        DataFrame containing phase and flux columns.
    bin_width : float
        Width of each phase bin.

    Returns
    -------
    pandas.DataFrame
        Table containing phase-bin centers and mean flux values.
    """

    profile = folded_data.copy()

    bin_edges = np.arange(0, 1 + bin_width, bin_width)

    profile["phase_bin"] = pd.cut(
        profile["phase"],
        bins=bin_edges,
        include_lowest=True,
    )

    mean_profile = (
        profile.groupby("phase_bin", observed=True)["flux"]
        .mean()
        .reset_index(name="mean_flux")
    )

    mean_profile["phase_center"] = mean_profile["phase_bin"].apply(
        lambda interval: interval.mid
    )

    return mean_profile[["phase_center", "mean_flux"]]
