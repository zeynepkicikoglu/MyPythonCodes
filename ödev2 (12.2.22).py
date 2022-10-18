"""Problem 1
#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)
 BKİ 18.5'un altındaysa -------> Zayıf
 BKİ 18.5 ile 25 arasındaysa ------> Normal
 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
 BKİ 30'un üstündeyse -------------> Obez"""

boy=float(input("Boyunuzu giriniz(m cinsinden):"))
kilo=int(input("Kilonuzu giriniz:"))
BKİ=kilo/(boy*boy)
print("Beden kitle indeksiniz: {}".format(BKİ))
if BKİ<18.5:
    print("Zayıf")
elif BKİ>=18.5 and BKİ<25:
    print("Normal")
elif BKİ>=25 and BKİ<30:
    print("Fazla kilolu")
elif BKİ>=30:
    print("Obez")
else:
    print("Hata")


#Problem 2
#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

a=int(input("Bir sayı giriniz:"))
b=int(input("Bir sayı giriniz:"))
c=int(input("Bir sayı giriniz:"))

if a>b and a>c:
    print("Girdiğiniz en büyük sayı {}'dır.".format(a))
elif b>a and b>c:
    print("Girdiğiniz en büyük sayı {}'dır.".format(b))
elif c>a and c>b:
    print("Girdiğiniz en büyük sayı {}'dır.".format(c))
else:
    print("Hata")

"""Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına göre harf notunu hesaplayın.
    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.
    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF"""
vize1=int(input("Vize 1 notunuzu girin:"))
vize2=int(input("Vize 2 notunuzu girin:"))
final=int(input("Final notunuzu girin:"))
ort=((vize1*0.3)+(vize2*0.3)+(final*0.4))
if ort>=90:
    print("AA")
elif ort<90 and ort>=85:
    print("BA")
elif ort<85 and ort>=80:
    print("BB")
elif ort<80 and ort>=75:
    print("CB")
elif ort<75 and ort>=70:
    print("CC")
elif ort<70 and ort>=65:
    print("DC")
elif ort<65 and ort>=60:
    print("DD")
elif ort<60 and ort>=55:
    print("FD")
elif ort<55:
    print("FF")
else:
    print("Hata")


"""Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o
Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz. """
#Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

işlem1=input("tipi üçgen mi dörtgen mi:")
if işlem1=="üçgen":
    a=int(input("üçgenin 1. kenar uzunluğu:"))
    b=int(input("üçgenin 2. kenar uzunluğu:"))
    c=int(input("üçgenin 3. kenar uzunluğu:"))
    if a!=b and a!=c and b!=c:
        print("Bu bir çeşitkenar üçgen.")
    elif a == b and a == c and b == c:
        print("Bu bir eşkenar üçgen.")
    elif (a == b and a != c) or (a==c and a!=b) or (b==c and b!=c):
        print("Bu bir ikizkenar üçgen.")
    else:
        print("Bu değişik bir üçgen.")

elif işlem1=="dörtgen":
    a=int(input("dörtgenin 1. kenar uzunluğu:"))
    b=int(input("dörtgenin 2. kenar uzunluğu:"))
    c=int(input("dörtgenin 3. kenar uzunluğu:"))
    d=int(input("dörtgenin 4. kenar uzunluğu:"))
    if a==b and a==c and a==d and b==c and b==d and c==d:
        print("Bu bir kare.")
    elif (a == b and a != c and c == d) or (a == c and b == d and a != d) or (a==d and b==c and a!=b):
        print("Bu bir dikdörtgen.")
    else:
        print("Bu sıradan bir dikdörtgen.")

else:
    print("Yanlış giriş")