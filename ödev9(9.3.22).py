"""Problem 1
Elinizde uzunca bir string olsun.
            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık."""


x="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

liste=list()
frekansbulma=dict()
for i in x.lower():
    liste.append(i)

for i in liste:
    if (i in frekansbulma):
        frekansbulma[i] += 1
    else:
        frekansbulma[i] = 1

for harf,sayı in frekansbulma.items():
    print("{} cümlesinde; {} harfi {} kez geçmektedir.".format(x,harf,sayı))
    print("*******************************************")


s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans = dict()

for karakter in s:
    if (karakter in frekans):
        frekans[karakter] += 1
    else:
        frekans[karakter] = 1
for i, j in frekans.items():
    print(i, ":", j)


"""Problem 2
"şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.
                    Memlekete sis çökmüş bir gece
                    Usulca yanağıma sen düşüyorsun
                    Sabah saat dokuzu beş geçe
                    Terk edip bizleri gidiyorsun
                    Ayrılık bu kadar yakmamıştı içimizi
                    Farkında mısın bilmiyorum
                    Aldın beraberinde cumhuriyetimizi
                    Korkunç bir veda, sararmıştı her yer
                    Ellerini uzat tutmak istiyoruz
                    Masmavi gözleri kaybetmiş çocuk
                    Aldı bir sabah ruhumuzu
                    Lakin nasıl bölmesin yokluğun uykumuzu
Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu 
string'i ekrana yazdırın."""

with open("şiir.txt","r",encoding="utf-8") as file:
    şiir=file.read()
    şiir_satırları=list()
    şiirinbaşı=list()
    şiir=şiir.split("\n")
    for i in şiir:
        şiir_satırları.append(i)
    for i in şiir_satırları:
        şiirinbaşı.append(i[0])

    a="".join(şiirinbaşı)
    print(a)

    bas_harfler = ""

with open("şiir.txt", "r", encoding="utf-8") as file:
    for satır in file:
        bas_harfler += satır[0]
print(bas_harfler)


"""Problem 3
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir 
satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.
                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com
                           //
                           //
                           //
İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz."""

with open("mailler.txt","r",encoding="utf-8") as file:
    dosyaiçeriği=file.read()
    list()
    list = dosyaiçeriği.split(" ")

    for i in list:
        if i.endswith("@gmail.com") or i.endswith("@yahoo.com") or i.endswith("@xyz.com"):
            print("Mail:",i)
        else:
            continue


with open("mailler2.txt", "r", encoding="utf-8") as file:
    for satır in file:
        satır = satır[:-1]
        if (satır.endswith(".com") and satır.find("@") != -1 and satır.find("@") != 2 and satır.find(".") != 2):
            print(satır)
        else:
            continue

"""Problem 4
Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri 
isimlere göre sıralı bir şekilde yazdırmaya çalışın.
isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]"""

isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = zip(isim,soyisim)
a=1
for i,j in liste:
    print(a,":",i,j)
    a+=1




