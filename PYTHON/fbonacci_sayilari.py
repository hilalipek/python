# FİBONACCİ SAYILARİ
#0 1 1 2 3 5 8 13 21 34 55

def fibo (sinir):
    sayi1=0
    sayi2=1
    print(sayi1,sayi2,end=",")
    for i in range(sinir-2):
        toplam=sayi1+sayi2
        print(toplam,end=(","))
        sayi1=sayi2
        sayi2=toplam
fibo(10)


