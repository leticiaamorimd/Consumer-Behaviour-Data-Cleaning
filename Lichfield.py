# -*- coding: utf-8 -*-

# -- Sheet --

!pip install pandas
!pip install petl

import pandas as pd
import numpy as np
import petl as etl

lichfield = pd.read_csv('2010-2020_Lichfield_outlet.csv')
lichfield = lichfield.rename(columns={'item':'products'})

lichfield

table = etl.fromdataframe(lichfield)
table = etl.select(table, 'quantity', lambda quantity: quantity.isnumeric())
#etl.stats(table, 'quantity')

table2 = etl.convert(table, 'quantity', int) #converter all quantity column to int 

etl.tocsv(table, 'lichfield_fixed.csv')
lichfield = pd.read_csv('lichfield_fixed.csv')

lichfield_updated = lichfield.pivot_table(index='products', columns=None, values=['quantity', 'amount_in_gbp'], aggfunc=np.sum)
lichfield_updated = lichfield_updated.reset_index()

#Export data updated
lichfield_updated.to_csv('lichfield_updated.csv')

#1

top_5 = lichfield_updated.sort_values('quantity', ascending=False)
top_5.head(5)

top_5_lichfield = top_5.head(5)

sort_least_5 = lichfield_updated.sort_values('quantity', ascending=False)
sort_least_5.tail(5)

lichfield_updated.to_csv('lichfield_updated.csv')
lichfield_updated['quantity'].sum()

