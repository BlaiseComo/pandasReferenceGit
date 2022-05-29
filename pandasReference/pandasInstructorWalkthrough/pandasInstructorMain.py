import pandas as pd


# Reading data from various sources
df = pd.read_csv('pokemon.csv')

df_xlsx = pd.read_excel('pokemon_data.xlsx')

df_tabs = pd.read_csv('pokemon.txt', delimiter='\t')


# Read Headers
df.columns

# Read each Column
df[['Name', 'Type 1', 'HP']][0:5]

# Read Each Row
df.iloc[1] # 1 represents the index of the row

## Way to look at data that isn't limited
#for index, row in df.iterrows():
    #print(index, row['Name'])

# Print all rows with a type 1 column of fire
df.loc[df['Type 1'] == "Fire"]

# Read a specific Location (Row, Column)
df.iloc[2,1]

# Sort data
df.sort_values('Name', ascending=False) # Name is the name of a column, you can also pass in a list as the first argument 

# Adding new Column
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# Deleting a column
df = df.drop(columns=['Total'])

# Adding a column
df['Total'] = df.iloc[:, 4:9].sum(axis=1) # :, selects all rows     4:9 selects certain rows    axis=1 adds horizontally

# Moves columns around
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]






print(df.head())

