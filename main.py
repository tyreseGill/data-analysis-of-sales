import numpy as np
from utils import calc_stats, calc_multiple_stats


def main(mean_stats=False, median_stats=False, std_stats=False, prob_stats=False, show_chart=True):
    """
    Manages which statistics to calculate and display.

    Args:
        mean_stats (bool): Indicates if mean statistics are to be calculated.
        median_stats (bool): Indicates if median statistics are to be calculated.
        std_stats (bool): Indicates if standard deviation statistics are to be calculated.
        prob_stats (bool): Indicates if probability statistics are to be calculated.
        show_chart (bool): Determines whether a bar chart or a table will display the data.

    Returns:
        None if show_chart is True. Otherwise, a Dataframe object is returned.
    """
    
    # Loads text file
    file_name = 'Sales_01_20.csv'
    # Skips first row
    og_data = np.loadtxt(file_name, delimiter=',', skiprows=1)

    # Ensures that one and only one stat will be displayed
    num_of_stats_selected = sum([mean_stats, median_stats, std_stats, prob_stats])
    assert num_of_stats_selected != 0, "Please specify at least one statistic to showcase."

    # Outputs table of multiple stats if more than one is inputted
    if num_of_stats_selected > 1:
        df = calc_multiple_stats(og_data, mean_stats, median_stats, std_stats, prob_stats)
    # Otherwise, outputs table representing an individual stat
    elif mean_stats:
        df = calc_stats(og_data, show_chart, mean=True)
    elif median_stats:
        df = calc_stats(og_data, show_chart, median=True)
    elif std_stats:
        df = calc_stats(og_data, show_chart, std=True)
    elif prob_stats:
        df = calc_stats(og_data, show_chart, prob=True)

    if df is not None:
        print(df)


main(mean_stats=True, median_stats=True, std_stats=True, prob_stats=True)
main(mean_stats=True, show_chart=True)
main(median_stats=True, show_chart=True)
main(std_stats=True, show_chart=True)
main(prob_stats=True, show_chart=True)
