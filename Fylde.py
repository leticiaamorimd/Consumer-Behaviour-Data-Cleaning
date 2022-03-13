# -*- coding: utf-8 -*-

# -- Sheet --

!pip install pandas
!pip install petl

import pandas as pd
import numpy as np
import petl as etl
import matplotlib.pyplot as plt

############FYLDE OUTLET 
fylde = pd.read_csv('2010-2020_Fylde_outlet.csv')
fylde = fylde.rename(columns={'sku': 'products','total_quantity_purchased':'quantity'})


table = etl.fromdataframe(fylde)
table = etl.select(table, 'quantity', lambda quantity: quantity.isnumeric())
etl.stats(table, 'quantity')

table3 = etl.convert(table, 'quantity', int) #converter all quantity column to int 

etl.tocsv(table, 'fylde_fixed.csv')
fylde = pd.read_csv('fylde_fixed.csv')

fylde_updated = fylde.pivot_table(index='products', columns=None, values='quantity', aggfunc=np.sum)

fylde_updated = fylde_updated.reset_index()

fylde_updated.to_csv("fylde.csv")

top_5_fylde = fylde_updated.head(5)
least_5_fylde = fylde_updated.tail(5)

