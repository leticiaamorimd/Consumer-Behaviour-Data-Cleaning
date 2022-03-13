# -*- coding: utf-8 -*-

# -- Sheet --

!pip install pandas
!pip install petl

import pandas as pd
import numpy as np
import petl as etl

belfast = pd.read_csv('2011-2020_Belfast_branch.csv')
belfast = belfast.rename(columns={'item':'products', 'total_quantity': 'quantity'})

belfast

table = etl.fromdataframe(belfast)
table = etl.select(table, 'quantity', lambda quantity: quantity.isnumeric())
etl.stats(table, 'quantity')

table2 = etl.convert(table, 'quantity', int) #converter all quantity column to int 

etl.tocsv(table, 'belfast_fixed.csv')
belfast = pd.read_csv('belfast_fixed.csv')

belfast_updated = belfast.pivot_table(index='products', columns=None, values=['quantity','amount_in_gbp'], aggfunc=np.sum)
belfast_updated = belfast_updated.reset_index()

sort_top_5 = belfast_updated.sort_values('quantity', ascending=False)
sort_top_5.head(5)

sort_top_5.to_csv("belf_top5.csv")

sort_least_5 = belfast_updated.sort_values('quantity', ascending=False)
sort_least_5.tail(5)

