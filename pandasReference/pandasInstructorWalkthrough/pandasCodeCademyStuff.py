import pandas as pd

sales = pd.read_csv('sales.csv')
#print(sales)
targets = pd.read_csv('targets.csv')
#print(targets)

# sales_vs_targets is a dataframe with columns months, revenue, target
sales_vs_targets = pd.merge(sales, targets)
#print(sales_vs_targets)

# crushing_it is the sales_vs_targets dataframe but only with rows where revenue exceeded the target
crushing_it = sales_vs_targets.loc[(sales_vs_targets['revenue'] > sales_vs_targets['target'])]

men_women = pd.read_csv('men_women_sales.csv')
#print(men_women)

# all_data is a data frame of all data frames merged together
all_data = sales.merge(targets).merge(men_women)
#print(all_data)

# results is a data frame from all_data but only the rows where revenue exceeds target and women shirts are bought more than mens
results = all_data.loc[(all_data['revenue'] > all_data['target']) & (all_data['women'] > all_data['men'])]

# IMPORTANT NOTE: Merge usually sorts data frames based off a column that both data frames have, for exmaple, the above data frames are being sorted based on the column 'months'

orders = pd.read_csv('orders.csv')
#print(orders)
products = pd.read_csv('products.csv')
#print(products)

# orders_products is a data frame of orders and products, but the id in products was renamed to product_id to match the column in orders#
orders_products = pd.merge(orders, products.rename(columns={'id': 'product_id'}))
#print(orders_products)

