fakto = 1
sayi = int(input("faktoriyeli alınacak sayıyı giriniz"))
if sayi <= 0:
    print("negtif sayı girmeyinn")
else:
    for i in range(1, sayi+1):
        fakto = fakto * i
    print("sonuc:", fakto)
