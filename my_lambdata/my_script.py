import pandas
import numpy as np
import requests
from sklearn.model_selection import train_test_split
# my_lambdata/my_script.py

from my_mod import enlarge

print("HELLO WORLD")

df = pandas.DataFrame({"State": ['CT', "CO", "CA", "TX"]})
print(df.head())

print("--------")

x = 5
print("NUMBER", x)
print("ENLARGED NUMBER", enlarge(x))  # invoking our function!!

df1 = pandas.read_csv('https://raw.githubusercontent.com/ryanleeallred/datasets/master/Ames%20Housing%20Data/train.csv')

df1['LotFrontage'].head(5)

# Split train into train & val
train, test = train_test_split(df1, train_size=0.85, test_size=0.15,
                               random_state=42)
train, val = train_test_split(df, train_size=0.80, test_size=0.20,
                              random_state=42)

train.shape, val.shape, test.shape

# Check for NaN values in the dataset
train.isna().sum()
