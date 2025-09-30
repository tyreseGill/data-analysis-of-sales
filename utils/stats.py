import numpy as np
import pandas as pd
from .charts import generate_chart
from .tables import generate_table


def calc_stats(og_data, show_chart, mean=False, median=False, std=False, prob=False):
    """
    Handles statistical calculations and chart/table generation.
    
    Args:
        og_data (np.ndarray): Represents the entire raw dataset.
        show_chart (bool): Determines whether a bar chart or a table will display the data.
        mean (bool): Indicates if mean statistics are to be calculated.
        median (bool): Indicates if median statistics are to be calculated.
        std (bool): Indicates if standard deviation statistics are to be calculated.
        prob (bool): Indicates if probability statistics are to be calculated.

    Returns:
         None if the user generates a chart. Otherwise, returns a DataFrame object representing a table of the statistical data.
    """
    stats: list[float] = []
    x_label = 'Year'

    # Ensures a single statistic is provided to calculate
    num_of_stats_selected = sum([mean, median, std, prob])
    assert num_of_stats_selected == 1, f"One and only one statistic was expected, {num_of_stats_selected} inputted."
    
    for year in range(2001, 2021):
        # Filters data to retrieve sales from a given year and build a temporary list of the sales from that year
        data_from_some_year = og_data[og_data[:, 0] == year]

        # Using the data from a given year, calculates the corresponding statistic
        if mean:
            title = 'Mean Price of Residential Units by Year'
            y_label = 'Mean Sale Price'
            stat_from_some_year: float = data_from_some_year[:, 1].mean()
        elif median:
            title = 'Median Price of Residential Units by Year'
            y_label = 'Median Sale Price'
            stat_from_some_year: float = np.median(data_from_some_year[:, 1])
        elif std:
            title = 'Standard Deviation of Residential Units by Year'
            y_label = 'Standard Deviation in Sale Pricing (in Millions)'
            stat_from_some_year: float = data_from_some_year[:, 1].std()
        else:
            title = 'Probability of \\$200K–\\$300K Prices by Year'
            y_label = 'Probability (\\$200K–\\$300K)'
            data_in_range_from_some_year = data_from_some_year[(200_000 <= data_from_some_year[:, 1]) &
                                                            (data_from_some_year[:, 1] <= 300_000)]
            stat_from_some_year: float = len(data_in_range_from_some_year) / len(data_from_some_year)

        # Adds those yearly statistics to a list for reference when creating the y-axis of bar graph
        stats.append(
            stat_from_some_year
        )

    # Determines whether to present the statistics with a chart or a table
    if show_chart:
        generate_chart(stats, x_label, y_label, title)
    else:
        if prob:
            return generate_table(stats, [x_label, y_label], True)
        else:
            return generate_table(stats, [x_label, y_label])


def calc_multiple_stats(og_data, mean=False, median=False, std=False, prob=False):
    """
    Calculates multiple statistics from the dataset and organizes them into a single table to view.

    Args:
        og_data (np.ndarray): Represents the entire raw dataset.
        mean (bool): Indicates if mean statistics are to be calculated.
        median (bool): Indicates if median statistics are to be calculated.
        std (bool): Indicates if standard deviation statistics are to be calculated.
        prob (bool): Indicates if probability statistics are to be calculated.

    Returns:
        pd.Dataframe: The table summarizing the statistics of the data over time.
    """
    years: list[int] = [ year for year in range(2001, 2021) ]
    mean_sale_stats: list[float] = []
    std_sale_stats: list[float] = []
    prob_sale_stats: list[float] = []
    median_sale_stats: list[float] = []
    
    for year in range(2001, 2021):
        # Filters data to retrieve sales from a given year and build a temporary list of the sales from that year
        data_from_some_year = og_data[og_data[:, 0] == year]
        
        # Using the data from that year, calculates the mean, median, std, and probability of a sale falling between $200K-300K
        if mean:
            mean_from_some_year: float = data_from_some_year[:, 1].mean()
        if median:
            median_from_some_year: float = np.median(data_from_some_year[:, 1])
        if std:
            std_from_some_year: float = data_from_some_year[:, 1].std()
        if prob:
            data_in_range_from_some_year = data_from_some_year[(200_000 <= data_from_some_year[:, 1]) &
                                                               (data_from_some_year[:, 1] <= 300_000)]
            prob_from_some_year: float = len(data_in_range_from_some_year) / len(data_from_some_year)
    
        # Adds those yearly statistics to a list for reference when creating the y-axis of bar graph
        if mean:
            mean_sale_stats.append(mean_from_some_year)
        if median:
            median_sale_stats.append(median_from_some_year)
        if std:
            std_sale_stats.append(std_from_some_year)
        if prob:
            prob_sale_stats.append(prob_from_some_year)

    # Creates 5-column matrix representing years and statistics
    column_values = np.array([
            years,
            [ f"${mean_from_some_year:,.2f}" for mean_from_some_year in mean_sale_stats ],
            [ f"${median_from_some_year:,.2f}" for median_from_some_year in median_sale_stats ],
            [ f"${std_from_some_year:,.2f}" for std_from_some_year in std_sale_stats ],
            [ f"{prob_from_some_year:.2%}" for prob_from_some_year in prob_sale_stats ]
        ]).T
    
    df = pd.DataFrame(column_values, columns=['Year', 'Mean Sales', 'Median Sales', 'Standard Deviation of Sales', 'Probability of Sale Being Between \\$200K and \\$300K'])
    return df
