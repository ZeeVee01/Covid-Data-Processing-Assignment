import pandas as pd
import argparse

# read in data to needed columns
df = pd.read_csv('owid-covid-data.csv',
                 usecols=['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths'])

# Select only dates in 2020
df = df[(df['date'] >= '2020-01-01') & (df['date'] <= '2020-12-31')]

# Make new column just containing months
df['month'] = pd.DatetimeIndex(df['date']).month

# reorder dataframe and remove date column with the addition of month
df = df[['location', 'month', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]

# group by location and month and aggregate remaining columns
grouped_df = df.groupby(['location', 'month']).agg('mean')

# Add new case fatality rate column
grouped_df['case_fatality_rate'] = grouped_df['new_deaths'] / grouped_df['new_cases']

# Re order columns
grouped_df = grouped_df[['case_fatality_rate', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]

# remove rows with NA data entries
final_df = grouped_df.dropna(thresh=2)

# Write to csv
final_df.to_csv('owid-covid-data-2020-monthly.csv')

# obtain first 5 rows for print
result = final_df.head(5)
print(result)
