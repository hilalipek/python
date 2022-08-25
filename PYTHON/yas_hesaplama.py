# Doğum yılını giren kullanıcının yaşını veren program
from datetime import datetime


dogum = int(input("dogum yılınızı giriniz:"))
an = datetime.now()
yıl = an.year


yas = yıl - dogum

print("Yaşınız :" ,yas)

