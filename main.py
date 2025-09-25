import numpy as np
import matplotlib.pyplot as plt

# Loads text file
file_name = 'Sales_01_20.csv'
# Skips first row
og_data = np.loadtxt(file_name, delimiter=',', skiprows=1)

mean_sale_statistics: list[float] = []
std_sale_statistics: list[float] = []
prob_sale_statistics: list[float] = []

for year in range(2001, 2021):
    # Filters data to retrieve sales from a given year and build a temporary list of the sales from that year
    data_from_some_year = og_data[og_data[:, 0] == year]
    # Using the data from that year, calculates the mean, std, and probability of a sale falling between $200K-300K
    mean_from_some_year: float = data_from_some_year[:, 1].mean()
    std_from_some_year: float = data_from_some_year[:, 1].std()
    data_in_range_from_some_year = data_from_some_year[(200_000 <= data_from_some_year[:, 1]) &
                                                       (data_from_some_year[:, 1] <= 300_000)]
    prob_from_some_year: float = len(data_in_range_from_some_year) / len(data_from_some_year)

    print(f'********************** {year} Statistics ***********************')
    print(f'{year} Data Mean: ${mean_from_some_year:,.2f}')
    print(f'{year} Data Standard Deviation: ${std_from_some_year:,.2f}')
    print(f'{year} Data Probability of being Between $200K and $300K: {prob_from_some_year:.2%}\n')

    # Adds those yearly statistics to a list for reference when creating the y-axis of bar graph
    mean_sale_statistics.append(mean_from_some_year)
    std_sale_statistics.append(std_from_some_year)
    prob_sale_statistics.append(prob_from_some_year)

# Creates a list of the years from 2001-2020 for the x-axis of the bar graph
years: list[int] = [year for year in range(2001, 2021)]

'''Figure 1: Mean Prices'''
fig, ax = plt.subplots()
ax.bar(years, mean_sale_statistics)
ax.set_xlabel('Year')
ax.set_ylabel('Price')
ax.set_title('Mean Price of Residential Units by Year')
plt.show()

'''Figure 2: Standard Deviations'''
fig_2, ax_2 = plt.subplots()
ax_2.bar(years, std_sale_statistics)
ax_2.set_xlabel('Year')
ax_2.set_ylabel('Standard Deviation (in Millions)')
ax_2.set_title('Standard Deviation of Residential Units by Year')
plt.show()

'''Figure 3: Probabilities'''
fig_3, ax_3 = plt.subplots()
ax_3.bar(years, prob_sale_statistics)
ax_3.set_xlabel('Year')
ax_3.set_ylabel('Probability of Price being Between 200k and 300k')
ax_3.set_title('Probability of Price Ranging from 200K-300K for Residential Units by Year')
plt.show()
