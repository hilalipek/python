

def hesapla(k1,k2):
    alan=(k1*k2)/2
    cevre=pow (pow(k1,2) + pow (k2,2), 1/2 )+ k1+k2
    return"ücgenin alani:{} \n ücgenin cevresi:{}".format(alan,cevre)


kenar1 = int(input("birinci kenarın uzunlugunu girin"))
kenar2 = int(input("ikinci kenarın uzunlugunu girin"))




print(hesapla(kenar1,kenar2))