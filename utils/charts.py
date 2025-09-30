import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def generate_chart(stats, x_label, y_label, title):
    """
    Creates a bar chart representing changes to the statistical data over time.

    Args: 
        stats (list[float]): The statistical data to be displayed.
        x_label (str): Describes the independent variable plotted along the x-axis.
        y_label (str): Describes the dependent variable plotted along the y-axis.
        title (str): The name of the chart.
    """
    years: list[int] = [ year for year in range(2001, 2021) ]
    
    fig, ax = plt.subplots()
    ax.bar(years, stats)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    plt.plot(years, stats, color="orange", marker="o", linewidth=1)
    x, m, b = get_best_fit_vars(years, stats)
    plt.plot(years, m * x + b, color="red", label=f"y = {m:.2f}x + {b:.2f}", linestyle="dashed")
    ax.set_xticks([2000, 2005, 2010, 2015, 2020])
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    plt.xticks(rotation=45)
    plt.show()


def get_best_fit_vars(X, Y):
    """
    Obtains slope and y-intercept values for the line of best fit.

    Args:
        X (list): Represents the x-coordinates.
        Y (list): Represents the y-coordinates.

    Returns:
        tuple: An numpy array of X and the slope and intercept.
    """
    x = np.array(X)
    y = Y
    m, b = np.polyfit(x, y, 1)
    return x, m, b
