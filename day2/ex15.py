import pandas as pd
import csv

with open('height_file.csv', "r") as f:
    data = csv.Sniffer().sniff(f.read(1024))
    delimiter = data.delimiter
    quata = data.quotechar
    print(delimiter)
    print(quata)
    # ,
    # "
    f.seek(0)  # powrót na początek pliku

# df = pd.read_csv('height_file.csv', delimiter=",")
df = pd.read_csv('height_file.csv', delimiter=delimiter)
print(df)
#        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167

writer = pd.ExcelWriter("excel_from_csv.xlsx", engine="xlsxwriter")

df.to_excel(writer, sheet_name='first_name', index=False)
writer.close()

