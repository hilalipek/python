import math

birinciSayi = int(input("Birinci Sayıyı Giriniz : "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))

ebob=math.gcd(birinciSayi,ikinciSayi)
ekok=(birinciSayi*ikinciSayi)/ebob 
        
print ("EBOB:", ebob)
print ("EKOK:", ekok)