
import random
import time


sayı=random.randrange(1,20)

tahminhakkı=7

while True:
    tahmin=int(input("Tahmininizi giriniz:"))

    if tahmin<sayı:
        print("Değerlendiriliyor...")
        time.sleep(1)
        print("Daha büyük sayı girin.")
        tahminhakkı-=1
    elif tahmin>sayı:
        print("Değerlendiriliyor...")
        time.sleep(1)
        print("Daha küçük sayı girin.")
        tahminhakkı-=1
    else:
        print("Değerlendiriliyor...")
        time.sleep(1)
        print("{}. tahmin sonrası bildiniz,Tebrikler. Sayı:".format(8-tahminhakkı),sayı)
        break
    if tahminhakkı==0:
        print("Değerlendiriliyor...")
        time.sleep(1)
        print("Tahmin hakkınız kalmadı.")
        break










