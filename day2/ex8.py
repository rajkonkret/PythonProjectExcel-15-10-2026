import openpyxl

from openpyxl.styles import Font, colors, PatternFill, Border, Side

filename = 'video2.xlsx'
wb = openpyxl.load_workbook(filename)
ws = wb.active

print(ws.title)

# zmiana nazwy arkusza
ws.title = "Video Games Sales Data"

# wb.save(filename)
# wb.close()

sheet_names = wb.sheetnames
print(sheet_names)
# ['Video Games Sales Data', 'Total Sales by Genre', 'Breakdown of Sales by Genre', 'Breakdown of Sales by Year']

sheet = wb[sheet_names[1]]
wb.active = wb.index(sheet)

# wb.save(filename)
# wb.close()

ws = wb.active
print(ws.title)