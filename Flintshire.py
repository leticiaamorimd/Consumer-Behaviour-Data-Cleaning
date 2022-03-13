# -*- coding: utf-8 -*-

# -- Sheet --

!pip install pandas
!pip install petl

import pandas as pd
import numpy as np
import petl as etl
import matplotlib.pyplot as plt
import plotly.express as px

flinshire = pd.read_csv('2010-2020_Flintshire_branch.csv')
flinshire = flinshire.rename(columns={'sku':'products', 'quantity_purchased': 'quantity'})

flinshire

table = etl.fromdataframe(flinshire)
table = etl.select(table, 'quantity', lambda quantity: quantity.isnumeric())
etl.stats(table, 'quantity')

table2 = etl.convert(table, 'quantity', int) #converter all quantity column to int 

flinshire = pd.read_csv('flinshire_fixed.csv')

flinshire_updated = flinshire.pivot_table(index='products', columns=None, values=['quantity', 'amount_in_gbp'], aggfunc=np.sum)
flinshire_updated = flinshire_updated.reset_index()

flinshire_updated.to_csv('flinshire_updated.csv')

#1

sort_top_5 = flinshire_updated.sort_values('quantity', ascending=False)
sort_top_5.head(5)

top5_flinshire = sort_top_5.head(5)

top5_flinshire.plot.bar(x='products', y=['quantity'])
plt.xlabel('Products')
plt.ylabel('Quantity')
plt.savefig('top5_flinshire.png')

least5_flinshire = flinshire_updated.sort_values('quantity', ascending=False)
least5_flinshire.tail(5)

least5_flinshire = least5_flinshire.tail(5)

least5_flinshire.plot.bar(x='products', y=['quantity'])
plt.xlabel('Products')
plt.ylabel('Quantity')
plt.savefig('least5_flinshire.png')

