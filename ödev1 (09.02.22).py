#Problem 1
#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

a=int(input("lütfen bir sayı giriniz:"))
b=int(input("lütfen bir sayı giriniz:"))
c=int(input("lütfen bir sayı giriniz:"))

sayılar=[a,b,c]
print("Sayıların çarpımı: {}".format(sayılar[0]*sayılar[1]*sayılar[2]))

#Problem 2
#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m)*Boy(m)
boy=float(input("Boyunuzu giriniz(m cinsinden):"))
kilo=int(input("Kilonuzu giriniz:"))

print("Beden kitle indeksiniz:",kilo/(boy*boy))



#Problem 3
#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünün toplam ne kadar ödemesini gerektiğini hesaplayın.

yakıt=float(input("Aracınız km başına ne kadar yakıyor:"))
yol=int(input("Kaç km yol yaptınız:"))
print("Ödemeniz gereken toplam tutar:",yakıt*yol)

#Problem 4
#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
ad=input("Adınız:")
soyad=input("Soyadınız:")
numara=input("Numaranız:")
bilgiler=[ad,soyad,numara]
print("Bilgileriniz:\nAd: {}\nSoyad: {}\nNumara: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))



#Problem 5
#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
a = input("a:")
b = input("b:")

print("Değiştirilmeden Önce Değerler\na: {} b: {}\n".format(a,b))

a,b = b,a

print("Değiştirildikten Sonraki Değerler\na: {} b: {}\n".format(a,b))



#Problem 6
#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2
a=int(input("Dik üçgenin birinci kenar uzunluğu:"))
b=int(input("Dik üçgenin ikinci kenar uzunluğu:"))

print("Dik üçgenin hipotenüs uzunluğu:",(a**2+b**2)**0.5)