import openpyxl
from openpyxl.chart import Reference, BarChart
from openpyxl.chart.axis import ChartLines
from openpyxl.chart.layout import Layout, ManualLayout

filename = 'video2.xlsx'
wb = openpyxl.load_workbook(filename)
ws = wb['Total Sales by Genre']
