# pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# built on top of the Python programming language.

import pandas as pd
# pip install pandas

# tworzymy tabelki
writer = pd.ExcelWriter('empty_excel.xlsx')

empty_dataframe = pd.DataFrame()  # tabele/macierze w pandas

# zapisanie danych
empty_dataframe.to_excel(writer, sheet_name='empty')
writer.close()