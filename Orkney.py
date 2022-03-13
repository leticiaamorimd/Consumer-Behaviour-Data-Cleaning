# -*- coding: utf-8 -*-

# -- Sheet --

!pip install pandas
!pip install petl

import pandas as pd
import numpy as np
import petl as etl
import matplotlib.pyplot as plt
import plotly.express as px

orkney = pd.read_csv('2010-2020_Orkney_store.csv')
orkney = orkney.rename(columns={'sku':'products', 'total_quantity_purchased': 'quantity'})

orkney

table = etl.fromdataframe(orkney)
etl.convert(table, 'quantity', int) 

table = etl.select(table, 'quantity', lambda quantity: quantity.isnumeric())
#etl.stats(table, 'quantity')

etl.tocsv(table, 'orkney_fixed.csv')
peeble = pd.read_csv('orkney_fixed.csv')

orkney_updated = orkney.pivot_table(index='products', columns=None, values=['quantity','amount_in_gbp'], aggfunc=np.sum)
orkney_updated = orkney_updated.reset_index()

orkney_updated.to_csv('peeble_updated.csv')

#1

sort_top_5 = orkney_updated.sort_values('quantity', ascending=False)
sort_top_5.head(5)

top5_orkney = sort_top_5.head(5)

top5_orkney.plot.bar(x='products', y=['quantity'])
plt.xlabel('Products')
plt.ylabel('Quantity')

plt.savefig('top5_peeble.png')

sort_least_5 = orkney_updated.sort_values('quantity', ascending=False)
sort_least_5.tail(5)

sort_least_5_orkney = sort_top_5.tail(5)

sort_least_5_orkney.plot.bar(x='products', y=['quantity'])
plt.xlabel('Products')
plt.ylabel('Quantity')
plt.savefig('sort_least_5_peeble.png')

