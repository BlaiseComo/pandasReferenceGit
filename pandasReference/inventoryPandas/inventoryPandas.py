import pandas as pd

# Reads data from csv file to pd dataframe
inventory = pd.read_csv('inventory.csv')

# selects first ten rows of inventory
staten_island = inventory.head(10)

# selects all the product descriptions from staten island
product_request = staten_island.product_description

# selects all rows from inventory with location as brooklyn and product type as seeds
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

# Adds a new column 'in_stock'
# Axis=1 applys this to every row
inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis=1)

# Adds a new column 'total_value'
inventory['total_value'] = inventory.apply(lambda row: row.price * row.quantity, axis=1)

# Lambda function to print a string
combine_lambda = lambda row: \
  '{} - {}'.format(row.product_type, row.product_description)

# Adds a new column 'full_description' using combine_lambda
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory)
