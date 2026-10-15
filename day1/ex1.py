#
# Najważniejsze funkcje
#
# • Instalacja: Za pomocą menedżera pakietów: pip install openpyxl.
# • Tworzenie i zapis: Inicjalizacja skoroszytu przez Workbook() oraz zapis metodą wb.save("plik.xlsx").
# • Odczyt danych: Otwieranie istniejącego pliku za pomocą load_workbook("plik.xlsx").
# • Praca z komórkami: Odczyt i zapis przez indeksowanie (np. ws['A1']) lub iterację (iter_rows()).
# • Formatowanie i style: Obsługa czcionek, obramowań, wyrównania oraz formuł w komórkach.
# • Wykresy: Tworzenie prostych wykresów bezpośrednio w arkuszach.
# • Dokumentację oraz przykłady znajdziesz na oficjalnej stronie openpyxl ReadTheDocs.

from openpyxl import Workbook, load_workbook

wb = Workbook()  # tworzy szkielet pliku excel
ws = wb.active  # ustawia arkusz pliku

ws['A1'] = 42
ws['A2'] = 42
ws['A3'] = 42

ws.append([1, 2, 3])
ws.append([4, 5, 6])

wb.save('sample.xlsx')
wb.close()  # zamknięcie pliku

# wczytanie pliku excel
workbook = load_workbook('sample.xlsx')
sheet = workbook.active  # aktywny arkusz
print(sheet)  # <Worksheet "Sheet">

# wypisanie zawartości komórki
print(sheet['A1'])  # <Cell 'Sheet'.A1>
print(sheet['A1'].value)  # 42

print(sheet['A2'].value) # 42

for row in sheet.iter_rows(min_row=1, max_row=5):
    for cell in row:
        print(cell.value)
# 42
# 42
# 42
# None
# None
# 42
# None
# None
# 42
# None
# None
# 1
# 2
# 3
# 4
# 5
# 6