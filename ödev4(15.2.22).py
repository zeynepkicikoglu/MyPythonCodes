"""Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sağ 2yının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)."""
def mükemmel():

    for i in range(1,1001):
        toplam = 0
        for a in range(1, i):
            if i % a == 0:
                toplam += a
            else:
                continue
        if toplam == i:
            print("{} bir Mükemmel sayı.".format(i))


mükemmel()


def mukemmel(sayı):
    toplam = 0

    for i in range(1, sayı):

        if (sayı % i == 0):
            toplam += i

    return toplam == sayı


for i in range(1, 1001):
    if (mukemmel(i)):
        print("Mükemmel Sayı:", i)

"""Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın."""

def ebobbul(sayı1,sayı2):
    sayı1bölenleri=[]
    sayı2bölenleri=[]
    for s in range(1,sayı1+1):
        if sayı1%s==0:
            sayı1bölenleri.append(s)
        else:
            continue
    for d in range(1,sayı2+1):
        if sayı2%d ==0:
            sayı2bölenleri.append(d)
        else:
            continue

    ebobları=[]
    for f in sayı1bölenleri:
        for g in sayı2bölenleri:
            if f==g:
                print(f,g)
                ebobları.append(g)
            else:
                continue

    return ebobları[len(ebobları)-1]

sayı1=int(input("Bir sayı giriniz:"))
sayı2=int(input("Bir sayı giriniz:"))
print("ebob: ",ebobbul(sayı1,sayı2))


def ebob_bulma(sayı1, sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):

        if (not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:", ebob_bulma(sayı1, sayı2))

"""Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın."""


def ekok_bulma(sayı1, sayı2):
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1=(sayı1/i)
            sayı2 = (sayı2 / i)
            #sayı2 //= i


        elif (sayı1 % i == 0 and sayı2 % i != 0):
            ekok *= i

            #sayı1 //= i
            sayı1 = (sayı1 / i)


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i
            sayı2 = (sayı2 / i)

            #sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:", ekok_bulma(sayı1, sayı2))




"""Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
Örnek: 97 ---------> Doksan Yedi"""

birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10

    return onlar[ikinci] + " " + birler[birinci]


sayı = int(input("Sayı:"))

print(okunus(sayı))

"""Problem 5
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)"""


def pisagor_bulma():
    pisagor_listesi = list()
    for i in range(1, 101):
        for j in range(1, 101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                pisagor_listesi.append((i, j, int(c)))

    return pisagor_listesi


for i in pisagor_bulma():
    print(i)

