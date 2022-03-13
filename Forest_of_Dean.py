# -*- coding: utf-8 -*-

# -- Sheet --

!pip install pandas
!pip install petl

import pandas as pd
import numpy as np
import petl as etl
import matplotlib.pyplot as plt

forest = pd.read_csv('2010-2020_Forest_of_Dean_store.csv')

forest = forest.rename(columns={'item':'products'})
forest

table = etl.fromdataframe(forest)
table2 = etl.convert(table, 'quantity', int) #converter all quantity column to int 


table = etl.select(table, 'quantity', lambda quantity: quantity.isnumeric())
etl.stats(table, 'quantity')


etl.tocsv(table, 'forest_fixed.csv')

forest_updated = forest.pivot_table(index='products', columns=None, values='quantity', aggfunc=np.sum)
forest_updated = forest_updated.reset_index()

forest_updated.to_csv("forest.csv")

top_5_forest = forest_updated.head(5)
top_5_forest

