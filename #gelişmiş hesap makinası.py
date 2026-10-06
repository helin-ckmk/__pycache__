#gelişmiş hesap makinası
import math

while True:
    sayi1 = float(input("Birinci sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))

    print("Toplama:", sayi1 + sayi2)
    print("Çıkarma:", sayi1 - sayi2)
    print("Çarpım:", sayi1 * sayi2)

    if sayi2 != 0:
        print("Bölme:", sayi1 / sayi2)
    else:
        print("Bölme: Tanımsız (0'a bölünemez)")

    print("Ortalama:", (sayi1 + sayi2) / 2)

    print("1. sayının karesi:", sayi1 ** 2)
    print("2. sayının karesi:", sayi2 ** 2)

    if sayi1 >= 0:
        print("1. sayının karekökü:", math.sqrt(sayi1))
    else:
        print("1. sayının karekökü: Tanımsız")

    if sayi2 >= 0:
        print("2. sayının karekökü:", math.sqrt(sayi2))
    else:
        print("2. sayının karekökü: Tanımsız")