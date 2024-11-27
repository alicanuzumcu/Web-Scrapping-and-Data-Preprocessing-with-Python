# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:20:56 2024

@author: ALI CAN
"""
import pandas as pd

dataset = pd.read_csv("cost_of_living_csv.csv")
#%%

#Get transpose of the dataset
data = dataset.transpose()

#Seperate city names 
cities = data.index.tolist()
cities.remove(cities[0]) 
cities_df = pd.DataFrame(cities, columns=['City'])

data.columns = data.iloc[0]
data = data[1:].reset_index(drop=True)

#Create new column
data["City"] = cities_df
#%%

#Move the City column to the 1st
cols = data.columns.tolist()
cols = cols[-1:] + cols[:-1]
data = data[cols]
#%%

#Save as csv
data.to_csv("updated_data.csv",index=False)