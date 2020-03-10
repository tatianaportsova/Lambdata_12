import pandas
import requests
# my_lambdata/my_script.py

from my_mod import enlarge

print("HELLO WORLD")

df = pandas.DataFrame({"State" : ['CT', "CO", "CA", "TX"]})
print(df.head())

print("--------")

x = 5
print("NUMBER", x)
print("ENLARGED NUMBER", enlarge(x))  # invoking our function!!

df = pandas.read_csv('https://raw.githubusercontent.com/ryanleeallred/datasets/master/Ames%20Housing%20Data/train.csv')

df['LotFrontage'].head(5)

# Split train into train & val
import numpy as np
from sklearn.model_selection import train_test_split

train, test = train_test_split(df, train_size=0.85, test_size=0.15, 
                               random_state=42)
train, val = train_test_split(df, train_size=0.80, test_size=0.20, 
                               random_state=42)

train.shape, val.shape, test.shape

# Check for NaN values in the dataset
df.isna().sum() 