import math
# iki kenarı girilen dik üçgenin uzun kenar hesabı
a = int(input("a kenarinin uzunlugunu giriniz:"))
b = int(input("b kenarinin uzunlugunu giriniz:"))
hipotenus = math.pow(a,2) +  math.pow(b,2)
print(math.sqrt(hipotenus))
