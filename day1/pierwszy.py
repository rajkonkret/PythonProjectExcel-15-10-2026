import sys

print('Hello World')  # wypisz/wydrukuj
print("Radek")
# Hello World
# Radek

# ctrl / - wstawaia komentarz
# print('Radek")
#   File "C:\Users\Szkolenie\PycharmProjects\PythonProject\day1\pierwszy.py", line 6
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 6)
#
# Process finished with exit code 1

print("Dalsza część programu")

# typ tekstowy - str
print(45)
print(type(45))
# <class 'int'> - liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

print("37" + "78")  # 3778, konkatenacja
print(37 + 78)  # 115

# ctrl alt l - formatowanie kodu
# print("34" + 70)
# TypeError: can only concatenate str (not "int") to str

print("35" * 168)
print(35 * 168)  # 5880

# rzutowanie
print(int("35") + int(168))
# 203

print(25 * "-")
# <class 'float'> zmiennoprzecinkowe
print(4.56)
print(type(4.56))

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
# min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15,
# mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# błąd zaokrąglenia
print(0.1 + 0.9)
print(0.1 + 0.2)
# 1.0
# 0.30000000000000004

# decimal - pozwala ominąć problem zaokrąglenia

# zmienna - pudełko na dane
# snake_case

# typowanie dynamiczne
name = "Radek"
print(type(name))  # <class 'str'>
print(name)

name = 90
print(name)  # 90
print(type(name))  # <class 'int'>

# rzutowanie
a = "1"
b = 0
# print(a + b) # TypeError: can only concatenate str (not "int") to str
print(str("1") + str(0))
print(float("1") + int(b))
# 10
# 1.0

print(25 * "-")

# teksty są niemutowalne
tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

tekst.upper()
print(tekst)
print(tekst.upper())  # WITAJ ŚWIECIE
nowy_tekst = tekst.upper()
print(nowy_tekst)

zmienna1 = "GROSS"
zmienna2 = "groß"

print(zmienna1 == zmienna2)  # False
print(zmienna1.lower() == zmienna2.lower())  # False
print(zmienna1.casefold() == zmienna2.casefold())  # True

# typ logiczny
# True, False
print(1 != 0)  # True

name = "Radek"
# Imię pacjenta:... Dane:
print("Imię pacjenta:" + name + "Dane")
print("Imię pacjenta:", name, "Dane")

# f-string
print(f"Imię pacjenta: {name} Dane:")
# print("Imię pacjenta:" + name + "Dane")

a = 4.5678
print(f"Liczba: {a}")  # Liczba: 4.5678
print(f"Liczba: {a:.2f}")  # Liczba: 4.57
print(a)  # 4.5678

# %f - float
print("Liczba %f" % a)  # Liczba 4.567800
print("Liczba %.2f" % a)  # Liczba 4.57

# ctrl d - powielenie linijki
# print("Liczba %f" % "Radek") # TypeError: must be real number, not str

print("""
Tekst
    wielolinijkowy
    """)
# "Tekst
#     wielolinijkowy
#     "

"""
Komentarz
    wielolinijkowy - dokumnetacja - docstring"""
print(print.__doc__)

print(100 / 3)  # 33.333333333333336 float
print(100 // 3)  # częśc całkowita dzielenia
print(100 % 3)  # modulo - reszta z dzielnia
print(10 % 3)

zysk = 98078965431234
print(f"Nasza duża liczba {zysk:,}")  # Nasza duża liczba 98,078,965,431,234
print(f"Nasza duża liczba {zysk:_}")  # Nasza duża liczba 98_078_965_431_234
print(f"Nasza duża liczba {zysk:_}".replace("_", " "))  # Nasza duża liczba 98 078 965 431 234
print(f"Nasza duża liczba {zysk:_}".replace("_", "."))  # Nasza duża liczba 98.078.965.431.234

liczba = 10_000_000_000_000
print(type(liczba))  # <class 'int'>
print(liczba)  # 10000000000000

# kolekcje
# lista - zachowuje kolejność, pozwale przechowywac różne typy na raz
lista = [1, 2, 3, 4, 5, 6, "Radek"]
print(lista)  # [1, 2, 3, 4, 5, 6, 'Radek']
print(type(lista))  # <class 'list'>

lista = []  # pusta lista
lista.append("Radek")
lista.append("Radek")
lista.append("Tomek")
lista.append("Dawid")
lista.append("Artur")

print(lista)
# ['Radek', 'Radek', 'Tomek', 'Dawid', 'Artur']

# remove - usunięcie z listy, pierwszy z lewej
lista.remove("Radek")
print(lista)  # ['Radek', 'Tomek', 'Dawid', 'Artur']

lista_copy = lista.copy()  # kopia elementów listy
lista_k = lista  # skopiowany adres (referencje)
print(lista_k)
print(lista)
# ['Radek', 'Tomek', 'Dawid', 'Artur']
# ['Radek', 'Tomek', 'Dawid', 'Artur']

lista.clear()
print(lista_k)  # []
print(lista)  # []
print(lista_copy)  # ['Radek', 'Tomek', 'Dawid', 'Artur']

# krotka - kolekcja niemutowalna
# pomaga lepiej wykorzystac pamieć
krotka = tuple(lista_copy)
print(krotka)
print(type(krotka))
# ('Radek', 'Tomek', 'Dawid', 'Artur')
# <class 'tuple'>

tupla1 = "Radek", "Tomek"
print(type(tupla1))  # <class 'tuple'>

tupla2 = ("Radek",)
print(type(tupla2))  # <class 'tuple'>

# tupla1[0] = "190"  # TypeError: 'tuple' object does not support item assignment

# zbiór - przechowuje unikalne wartosci
# nie zachowuje kolejnosci
# nie ma indeksu
lista = [2, 5, 6, 8, 6, 7, 2, 8, 5, 9]

zbior = set(lista)
print(zbior)  # {2, 5, 6, 7, 8, 9}
print(type(zbior))  # <class 'set'>

pusty_zbior = set()  # tylko i wyłącznie tak
print(pusty_zbior)  # set()

pusty_zbior.add(15)
pusty_zbior.add(15)
pusty_zbior.add(45)
pusty_zbior.add(15)
pusty_zbior.add(34)
print(pusty_zbior)  # {34, 45, 15}

#  słownik - {klucz : wartosc}
# None
# odpowiednik jsona
slownik = {"name": "Radek", "age": 56}
print(slownik)  # {'name': 'Radek', 'age': 56}
print(type(slownik))  # <class 'dict'>

print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_items([('name', 'Radek'), ('age', 56)])

print(slownik['name'])  # Radek
# print(slownik['imie'])  # KeyError: 'imie'
print(slownik.get('imie'))  # None
print(slownik.get("age"))  # 56

pusty_slownik = {}
print(type(pusty_slownik))  # <class 'dict'>
print(pusty_slownik)  # {}

# # input()  # wczytaj
# tekst = input("Podaj imię:")
# print(tekst)
# Podaj imię:Radek
# Radek

# napisac apliakcję kalkulator
# a = int(input("Podaj pierwszą liczbę:"))
# b = input("Podaj drugą liczbę:")
# print(a + float(b))
# Podaj pierwszą liczbę:3
# Podaj drugą liczbę:4
# 7.0

print(eval("5 + 6"))  # 11

print(pusty_slownik)
pusty_slownik['name'] = "Radek"
print(pusty_slownik)  # {'name': 'Radek'}

pusty_slownik.update({"age": 67})
print(pusty_slownik)

print(pusty_slownik.items())

# [('name', 'Radek'), ('age', 67)]
p_s = {}
print(p_s)  # {}
p_s.update([('name', 'Radek'), ('age', 67)])
print(p_s)
# {'name': 'Radek', 'age': 67}

name = "Radek"
if name == "Radek":
    print("Radek")
elif name == "Tomek":
    print("Tomek")
else:
    print("Inny")
# Radek

name = "Radek"
if name:
    print("Ok")

print(bool(name))  # True

# od pythona 3.10
# match case

odp = "java"
match odp:
    case "python":
        print("python")
    case "jave":
        print("java")
    case _:
        print("inny")
# inny

for i in range(5):  # od 0 do 4
    print(i)

for i in lista_copy:
    print(i)

# Radek
# Tomek
# Dawid
# Artur

licznik = 0
while licznik < 10:
    licznik += 1
    print(licznik)

# print(5 / 0)
try:
    # print(5 / 0)
    wynik = 90 / 89
except ZeroDivisionError:
    print("Nie dziel przez zero")
except Exception as e:
    print("Bład:", e)
else:  # gdy nie ma błedu
    print(wynik)
finally:
    print("Zawsze")
# Nie dziel przez zero
