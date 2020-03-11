
# my_lambdata/my_frames.py

import pandas

# State abbreviation -> Full Name and visa versa.
# FL -> Florida, etc. (Handle Washington DC and territories like Puerto Rico etc.)

df1 = pandas.DataFrame({"State": ['CT', "CO", "CA", "TX"]})
print(df1.head())

df2 = pandas.DataFrame({"State": ['AZ', 'DC', "CO", "MI", "WI"]})
print(df2.head())