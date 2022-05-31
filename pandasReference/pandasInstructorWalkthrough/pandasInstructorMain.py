import pandas as pd


#DO NOT RUN THiS FILE

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
for index, row in df.iterrows():
    print(index, row['Name'])

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
df['Total'] = df.iloc[:, 4:10].sum(axis=1) # :, selects all rows     4:9 selects certain rows    axis=1 adds horizontally

# Moves columns around
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]


## Saving our data

df.to_csv('modified.csv', index=False) #Index = False erases the index column

df.to_csv('modified.txt', index=False, sep='\t') # sep denotes a delimiter

## Filtering Data

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df = new_df.reset_index(drop=True, inplace=True) # drop removes all instances of old indices if true

## Shows all columns of names that include Mega, if you add a squigly line in front of df['Name'], it will remove all names with Mega

df.loc[df['Name'].str.contains('Mega')]


import re

# Filters data using regex
df.loc[df['Name'].str.contains('fire | grass', regex=True, flags=re.I)]

# Picks out data using loc
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

# Would change the generation and legendary column of the table to test value if the pokemon had a total over 500
# You could specify generation to become ['Test 1'] and legendary to become ['Test 2'] if you replaced 'test value' with ['Test 1', 'Test 2']
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'

# Gets all the averages for the data of each type of 'Type 1', with the main first column being which type 1 it is
df.groupby(['Type 1']).mean()

# This does the same as above but sorts the rows by the defense column values
df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)



print(df.head())

