import openpyxl
from openpyxl.chart import Reference, BarChart
from openpyxl.chart.axis import ChartLines
from openpyxl.chart.layout import Layout, ManualLayout

filename = 'video2.xlsx'
wb = openpyxl.load_workbook(filename)
ws = wb['Total Sales by Genre']

# dane wykres
values = Reference(
    ws,
    min_col=2,
    max_col=2,
    min_row=1,
    max_row=13
)

cats = Reference(
    ws,
    min_col=1,
    max_col=1,
    min_row=2,
    max_row=13
)
