# -*- coding: utf-8 -*-

# -- Sheet --

!pip install pandas
!pip install petl

import pandas as pd
import numpy as np
import petl as etl
import matplotlib.pyplot as plt
import plotly.express as px

islington = pd.read_csv('2011-2020_Islington_branch.csv')
islington = islington.rename(columns={'item':'products', 'total_quantity_purchased': 'quantity'})

islington

table = etl.fromdataframe(islington)
table = etl.select(table, 'quantity', lambda quantity: quantity.isnumeric())
etl.stats(table, 'quantity')

table2 = etl.convert(table, 'quantity', int) #converter all quantity column to int 


etl.tocsv(table, 'islington_fixed.csv')
islington = pd.read_csv('islington_fixed.csv')

islington_updated = islington.pivot_table(index='products', columns=None, values=['quantity', 'amount_in_gbp'], aggfunc=np.sum)
islington_updated = islington_updated.reset_index()

#Export data updated
islington_updated.to_csv('islington_updated.csv')

#1

sort_top_5 = islington_updated.sort_values('quantity', ascending=False)
sort_top_5.head(5)

sort5_islington = sort_top_5.head(5)

sort5_islington.plot.bar(x='products', y=['quantity'])
plt.xlabel('Products')
plt.ylabel('Quantity')

plt.savefig('sort5_islington.png')

sort_least_5 = islington_updated.sort_values('quantity', ascending=False)
sort_least_5.tail(5)

sort_least_5_islington = sort_top_5.tail(5)

sort_least_5_islington.plot.bar(x='products', y=['quantity'])
plt.xlabel('Products')
plt.ylabel('Quantity')
plt.savefig('sort_least_5_islington.png')

