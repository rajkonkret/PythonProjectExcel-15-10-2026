import openpyxl

from openpyxl.styles import Font, colors, PatternFill, Border, Side

filename = 'video2.xlsx'
wb = openpyxl.load_workbook(filename)
ws = wb.active

print(ws.title)

# zmiana nazwy arkusza
ws.title = "Video Games Sales Data"

wb.save(filename)
wb.close()