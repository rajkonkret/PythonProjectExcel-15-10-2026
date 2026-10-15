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