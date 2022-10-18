"""ALIŞTIRMAlAR
while True:
    try:
        a=int(input("a:"))
        b=int(input("b:"))
        print(float(a/b))
    except Exception as ex:
        print("yanlış bilgi:",ex)
    else:
        break
    finally:
        print("try except sonlandı.")

x=10
if x>5:
    raise Exception("x 5 den büyük değer alamaz")


def check_password(psw):
    import re
    if len(psw)<8:
        raise Exception("parola en az 7 karakter içermelidir.")
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf içermelidir.")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[_@€]",psw):
        raise Exception("parola alpha numeric karakter içermelidir.")
    elif re.search("\s",psw):
        raise Exception("parola boşluk içermemelidir.")


while True:
    try:
        password=input("şifrenizi girin:")
        check_password(password)
    except Exception as ex:
        print(ex)
    else:
        print("geçerli parola girin")
        break
    finally:
        print("validation tamamlandı.")"""


"""1:liste elemanları içindeki sayısal değerleri bulunuz."""
liste=["1","2","5a","10b","abc","10","50"]
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

"""2:Kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğundan 
emin olunuz aksi halde hata mesajı yazın."""

while True:
    sayı=input("sayı:")
    if sayı=="q":
        print("by by")
        break
    try:
        result = float(sayı)
        print("girdiğiniz sayı:",result)
    except ValueError:
        print("gecersiz sayı")
        continue

"""Girilen parola için türkçe karakter uyarısı verin:"""

def CheckPassword(parola):
    turkce_karakter="şçğüöıİ"

    for i in parola:
        if i in turkce_karakter:
            raise TypeError("Parola türkçe karakter içeremez.")
        else:
            pass
    print("gecerli parola")

parola = input("parola:")

try:
    CheckPassword(parola)
except TypeError as err:
    print(err)

"""4:Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin"""
def Faktoriyel(x):
    x=int(x)
    if x < 0:
        raise ValueError("negatif değer")
    result=1
    for i in range(1,x+1):
        result*=i
    return result

for x in [3,10,20,-3,'10a']:
    try:
        y=Faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)




"""Problem 1
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.
liste = ["345","sadas","324a","14","kemal"]
Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın."""
liste2 = ["345","sadas","324a","14","kemal"]
for i in liste2:
    try:
        i=int(i)
    except Exception as ex:
        print(ex)
    else:
        print(i)



"""Problem 2
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return 
ile bu değeri dönsün. Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. Daha sonra,
içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift 
sayıları bastırın."""

def Ciftsayimi(sayi):
    if (sayi % 2 == 0):
        return f'{sayi} is a even number'
    else:
        raise ValueError("tek sayı")

sayi = int(input("sayı girin:"))
Ciftsayimi(sayi)

liste3=[34,42,41,76,765,77]

for h in liste3:
    if h%2==0:
        print(h)
    else:
        continue

