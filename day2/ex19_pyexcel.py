import pyexcel

# pip install pyexcel pyexcel-xlsx

data = [
    ['Imie', "Wiek"],
    ['Tomek', "38"],
    ['Kasia', "34"],
]

sheet = pyexcel.Sheet(data)
sheet.save_as('wyniki.xlsx')

# wczytanie
sheet = pyexcel.get_sheet(file_name='wyniki.xlsx')
print(sheet)
# pyexcel sheet:
# +-------+------+
# | Imie  | Wiek |
# +-------+------+
# | Tomek | 38   |
# +-------+------+
# | Kasia | 34   |
# +-------+------+

print(sheet.columns())
# <generator object Matrix.columns at 0x000001E6D7337E60>

for i in sheet.columns():
    print(i)
# ['Imie', 'Tomek', 'Kasia']
# ['Wiek', '38', '34']