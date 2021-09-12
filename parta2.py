import pandas as pd
import argparse
import matplotlib.pyplot as plt

# read in data to needed columns
df = pd.read_csv('owid-covid-data.csv',
                 usecols=['location', 'date', 'new_cases', 'new_deaths'])

# Select only dates in 2020
df = df[(df['date'] >= '2020-01-01') & (df['date'] <= '2020-12-31')]

# group by location and sum columns
grouped_df = df.groupby(['location']).sum()

# Add new case fatality rate column
grouped_df['case_fatality_rate'] = grouped_df['new_deaths'] / grouped_df['new_cases']

# Re-order columns
grouped_df = grouped_df[['case_fatality_rate', 'new_cases']]

# remove rows with NA data entries
final_df = grouped_df.dropna()

# Creates initial Scatter plot
plt.scatter(final_df.new_cases, final_df.case_fatality_rate)

# Rename Labels
plt.xlabel('New Cases')
plt.ylabel('Case Fatality Rate')

# Save plot a before changing x scale
plt.savefig('scatter-a.png')

# Change x scale
ax = plt.gca()
ax.set_xscale('log')

# Save plot b
plt.savefig('scatter-b.png')
