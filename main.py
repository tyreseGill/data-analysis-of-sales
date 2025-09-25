import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Loads text file
file_name = 'Sales_01_20.csv'
# Skips first row
og_data = np.loadtxt(file_name, delimiter=',', skiprows=1)

mean_sale_stats: list[float] = []
std_sale_stats: list[float] = []
prob_sale_stats: list[float] = []

for year in range(2001, 2021):
    # Filters data to retrieve sales from a given year and build a temporary list of the sales from that year
    data_from_some_year = og_data[og_data[:, 0] == year]
    # Using the data from that year, calculates the mean, std, and probability of a sale falling between $200K-300K
    mean_from_some_year: float = data_from_some_year[:, 1].mean()
    std_from_some_year: float = data_from_some_year[:, 1].std()
    data_in_range_from_some_year = data_from_some_year[(200_000 <= data_from_some_year[:, 1]) &
                                                       (data_from_some_year[:, 1] <= 300_000)]
    prob_from_some_year: float = len(data_in_range_from_some_year) / len(data_from_some_year)

    # Adds those yearly statistics to a list for reference when creating the y-axis of bar graph
    mean_sale_stats.append(
        mean_from_some_year
        )
    std_sale_stats.append(
        std_from_some_year
        )
    prob_sale_stats.append(
        prob_from_some_year
        )

# Creates a list of the years from 2001-2020 for the x-axis of the bar graph
years: list[int] = [year for year in range(2001, 2021)]

column_values = np.array([
    years,
    [ f"${mean_from_some_year:,.2f}" for mean_from_some_year in mean_sale_stats ],
    [ f"${std_from_some_year:,.2f}" for std_from_some_year in std_sale_stats ],
    [ f"{prob_from_some_year:.2%}" for prob_from_some_year in prob_sale_stats ]
    ]).T

df = pd.DataFrame(column_values, columns=['Year', 'Mean Sales', 'Standard Deviation of Sales', 'Probability of Sale Being Between $200K and $300K'])
print(df)

'''Figure 1: Mean Prices'''
fig, ax = plt.subplots()
ax.bar(years, mean_sale_stats)
ax.set_xlabel('Year')
ax.set_ylabel('Price')
ax.set_title('Mean Price of Residential Units by Year')
plt.show()

'''Figure 2: Standard Deviations'''
fig_2, ax_2 = plt.subplots()
ax_2.bar(years, std_sale_stats)
ax_2.set_xlabel('Year')
ax_2.set_ylabel('Standard Deviation (in Millions)')
ax_2.set_title('Standard Deviation of Residential Units by Year')
plt.show()

'''Figure 3: Probabilities'''
fig_3, ax_3 = plt.subplots()
ax_3.bar(years, prob_sale_stats)
ax_3.set_xlabel('Year')
ax_3.set_ylabel('Probability of Price being Between 200k and 300k')
ax_3.set_title('Probability of Price Ranging from 200K-300K for Residential Units by Year')
plt.show()
