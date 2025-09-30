import numpy as np
import pandas as pd


def generate_table(sale_stats, table_cols, percentile=False):
    """
    Creates a table representing changes to the statistical data over time.
    
    Args:
        sale_stats (list[float]): The statistical data to be displayed.
        table_cols (list[str]): The names of the columns in the matrix.
        percentile (bool): Indicates whether the data should be displayed as a percentile or not.

    Returns:
        pd.DataFrame: A structure to visualize the data in an organized format.
    """
    years: list[int] = [ year for year in range(2001, 2021) ]

    # Determines whether stats should be formated percentile or 2-point float
    if percentile:
        stats = [ f"{stat_from_some_year:.2%}" for stat_from_some_year in sale_stats ]
    else:
        stats = [ f"${stat_from_some_year:,.2f}" for stat_from_some_year in sale_stats ]

    # Creates two-column matrix
    column_values = np.array([
        years,
        stats
    ]).T

    df = pd.DataFrame(column_values, columns=table_cols)
    return df
