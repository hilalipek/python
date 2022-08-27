ortalama = float(input('Ders Ortalamanızı Girin : '))

if (ortalama >= 85):
    print("Not: 5, Dersten Geçtiniz.")
elif (70 < ortalama < 85):
    print("Not: 4, Dersten Geçtiniz.")
elif (50 < ortalama < 70):
    print("Not: 3, Dersten Geçtiniz.")
else:
    print("Dersten Kaldınız.")
