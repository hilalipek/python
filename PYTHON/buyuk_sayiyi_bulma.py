a=int(input("birinci sayiyi giriniz"))
b=int(input("ikinci sayiyi giriniz"))
c=int(input("ucuncu sayiyi giiriniz"))

if (a >= b) and (a >= c):
   buyuk = a
elif (b >= a) and (b >= c):
   buyuk = b
else:
   buyuk = c
 
print(a,",",b,"ve",c,"içinde büyük olan sayı",buyuk)