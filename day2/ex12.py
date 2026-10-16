import pandas as pd

data = pd.read_excel('course_participants.xlsx')
print(data)

#    numer   imię  wiek    kraj  ocena kontynent
# 0   1001   Mark    55  Włochy    4.5    Europa
# 1   1000   John    33     USA    6.7   Ameryka
# 2   1002    Tim    41     USA    3.9   Ameryka
# 3   1003  Jenny    12  Niemcy    9.0    Europa

data.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 6 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   numer      4 non-null      int64
#  1   imię       4 non-null      str
#  2   wiek       4 non-null      int64
#  3   kraj       4 non-null      str
#  4   ocena      4 non-null      float64
#  5   kontynent  4 non-null      str
# dtypes: float64(1), int64(2), str(3)
# memory usage: 324.0 bytes

data = [
    ['Mark', 55, "Włochy", 4.5, "Europa"],
    ['John', 45, "USA", 4.5, "Ameryka"],
    ['Tim', 75, "USA", 4.5, "Ameryka"],
    ['Jenny', 33, "Niemcy", 4.5, "Europa"],
]

df = pd.DataFrame(
    data=data,
    columns=["imie", 'wiek', 'kraj', 'ocena', 'kontynent'],
    index=[1001, 1000, 1002, 1003]
)
print(df)
# memory usage: 324.0 bytes
#        imie  wiek    kraj  ocena kontynent
# 1001   Mark    55  Włochy    4.5    Europa
# 1000   John    45     USA    4.5   Ameryka
# 1002    Tim    75     USA    4.5   Ameryka
# 1003  Jenny    33  Niemcy    4.5    Europa

df.info()
# Data columns (total 5 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   imie       4 non-null      str
#  1   wiek       4 non-null      int64
#  2   kraj       4 non-null      str
#  3   ocena      4 non-null      float64
#  4   kontynent  4 non-null      str
# dtypes: float64(1), int64(1), str(3)
# memory usage: 192.0 bytes

print(df.index)  # Index([1001, 1000, 1002, 1003], dtype='int64')

df.index.name = 'numer'
print(df)

#         imie  wiek    kraj  ocena kontynent
# numer
# 1001    Mark    55  Włochy    4.5    Europa
# 1000    John    45     USA    4.5   Ameryka
# 1002     Tim    75     USA    4.5   Ameryka
# 1003   Jenny    33  Niemcy    4.5    Europa

# sortowanie danych
print(df.sort_values(['wiek']))
# numer
# 1003   Jenny    33  Niemcy    4.5    Europa
# 1000    John    45     USA    4.5   Ameryka
# 1001    Mark    55  Włochy    4.5    Europa
# 1002     Tim    75     USA    4.5   Ameryka

print(df.sort_values(['kontynent', 'wiek']))
# numer
# 1000    John    45     USA    4.5   Ameryka
# 1002     Tim    75     USA    4.5   Ameryka
# 1003   Jenny    33  Niemcy    4.5    Europa
# 1001    Mark    55  Włochy    4.5    Europa
