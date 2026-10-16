import openpyxl

filename = 'video2.xlsx'
wb = openpyxl.load_workbook(filename)
# ws = wb.active
ws = wb['vgsales']

# dodanie nowego wiersza
new_row = (1, "The Legend of Zelda", 'Wii', 1986, 'Action', 'Nintendo', 3.74, 0.93, 1.69, 0.14, 6.51)
