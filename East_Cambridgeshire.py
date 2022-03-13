# -*- coding: utf-8 -*-

# -- Sheet --

!pip install pandas
!pip install petl

import pandas as pd
import petl as etl
import numpy as np

east_camb = pd.read_csv('2010-2020_East_Cambridgeshire_outlet.csv')

east_camb = east_camb.rename(columns={'product': 'products','total_quantity': 'quantity'})
east_camb

table = etl.fromdataframe(east_camb)


table2 = etl.convert(table, 'quantity', int) #converter all quantity column to int 

table = etl.select(table, 'quantity', lambda quantity: quantity.isnumeric())
etl.stats(table, 'quantity')

etl.tocsv(table, 'east_camb_fixed.csv')

east_camb_updated = east_camb.pivot_table(index='products', columns=None, values='quantity', aggfunc=np.sum)
east_camb_updated = east_camb_updated.reset_index()

east_camb_updated.to_csv("East_Cambridgeshire.csv")

