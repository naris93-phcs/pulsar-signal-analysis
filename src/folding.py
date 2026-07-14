def fold_signal(data, period):
    """
    Fold the pulsar signal using the estimated period.

    Parameters
    ----------
    data : pandas.DataFrame
        Input signal.
    period : float
        Pulsar period in seconds.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing phase and flux.
    """

    folded = data.copy()

    folded["phase"] = (folded["time"] % period) / period

    folded = folded.sort_values("phase")

    return folded
