# -*- coding: utf-8 -*-

# -- Sheet --

!pip install pandas
!pip install petl

import pandas as pd
import numpy as np
import petl as etl
import matplotlib.pyplot as plt
import plotly.express as px

nyorkshire = pd.read_csv('2011-2020_North_Yorkshire_outlet (1).csv')
nyorkshire = nyorkshire.rename(columns={'sku':'products', 'total_quantity': 'quantity'})
nyorkshire

table = etl.fromdataframe(nyorkshire)
table = etl.select(table, 'quantity', lambda quantity: quantity.isnumeric())
#etl.stats(table, 'quantity')

table2 = etl.convert(table, 'quantity', int) #converter all quantity column to int 

etl.tocsv(table, 'nyorkshire_fixed.csv')
nyorkshire = pd.read_csv('nyorkshire_fixed.csv')

nyorkshire_updated = nyorkshire.pivot_table(index='products', columns=None, values=['quantity', 'amount_in_gbp'], aggfunc=np.sum)
nyorkshire_updated = nyorkshire_updated.reset_index()

#1

sort_top_5 = nyorkshire_updated.sort_values('quantity', ascending=False)
sort_top_5.head(5)

sort5_nyorkshire = sort_top_5.head(5)

sort5_nyorkshire.plot.bar(x='products', y=['quantity'])
plt.xlabel('Products')
plt.ylabel('Quantity')

plt.savefig('sort5_nyorkshire.png')

sort_least_5 = nyorkshire_updated.sort_values('quantity', ascending=False)
sort_least_5.tail(5)

sort_least_5_nyorkshire = sort_top_5.tail(5)

sort_least_5_nyorkshire.plot.bar(x='products', y=['quantity'])
plt.xlabel('Products')
plt.ylabel('Quantity')
plt.savefig('sort_least_5_nyorkshire.png')

#track the best performing branches overall per region and per city (performance is
#measured in both item quantity sold and monetary value of sales made, limit to best
#0 and worst 10)


#Sum the item quantity sold
#Sum the total amount

nyorkshire_updated.to_csv('nyorkshire_updated.csv')
nyorkshire_updated['quantity'].sum()

nyorkshire_updated['amount_in_gbp'].sum()

