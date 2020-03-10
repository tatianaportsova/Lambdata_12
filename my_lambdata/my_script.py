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