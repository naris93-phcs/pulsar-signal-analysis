def print_summary_statistics(data):
    """
    Print basic summary statistics for the pulsar signal.
    """

    print("Signal summary")
    print("----------------")
    print(f"Number of samples: {len(data)}")
    print(f"Mean flux: {data['flux'].mean():.4f}")
    print(f"Median flux: {data['flux'].median():.4f}")
    print(f"Standard deviation: {data['flux'].std():.4f}")
    print(f"Minimum flux: {data['flux'].min():.4f}")
    print(f"Maximum flux: {data['flux'].max():.4f}")
