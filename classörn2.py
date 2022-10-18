class Personel:
    zamorani = 1.05
    def __init__(self,isim,soyisim,maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas


    def eposta(self):
        return f'{self.isim.lower()}.{self.soyisim.lower()}@firmam.com'

    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'

    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)


class Yazilimci(Personel):
    zam_orani = 1.1

    def __init__(self,isim,soyisim,maas,prog_dili):
        super().__init__(isim,soyisim,maas)
        print(f'Yeni personel yazılımcı kategorisine taşındı: {self.isim} {self.soyisim}')
        self.prog_dili = prog_dili

class Mudur(Personel):
    def __init__(self,isim,soyisim,maas,personeller=None):
        super().__init__(isim,soyisim,maas)
        if personeller is None:
            self.personeller = ['none']
        else:
            self.personeller = personeller

    def personel_ekle(self,per):
        if per not in self.personeller: #if bloğu eklemezsek bir daha kayıt olusturabilir
            self.personeller.append(per)

    def personel_cikar(self, per):
        if per in self.personeller: #if eklemezsek deger hatası verir
            self.personeller.remove(per)

    def personelleri_listele(self):
        for e, per in enumerate(self.personeller):
            e+=1
            print(e,per.tam_isim())



yaz_1 = Yazilimci('Sam','Winchester',10000,'python')
yaz_2 = Yazilimci('Sam','Winchester',15000,'java')

mdr_1 = Mudur('john','Wick',55000,[yaz_1, yaz_2])

print(mdr_1.tam_isim())
print('_______')
mdr_1.personelleri_listele()
print('________')
mdr_1.personel_ekle(yaz_2)
mdr_1.personel_cikar(yaz_1)
mdr_1.personelleri_listele()


class Personel:

    def __init__(self,isim,soyisim,maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title() #GLOBAL DEGİSTİRİLEBİLİR
        self.maas = maas
        self.__zamorani = 1.05 #PRIVATE DEGİSTİRİLEMEZ

    @property
    def eposta(self):
        return f'{self.isim.lower()}.{self.soyisim.lower()}@firmam.com'
    @property
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'

    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)

    @tam_isim.setter
    def tam_isim(self,ad):
        isim,soyisim= ad.split(' ')
        self.isim=isim
        self.soyisim=soyisim
    @tam_isim.deleter
    def tam_isim(self):
        print("DEĞİŞKENLER SİLİNDİ.")
        self.isim=None
        self.soyisim=None


per_1=Personel("zeynep","kıcıkoğlu",10000)
per_1.tam_isim='Hande Kaplan'
print(per_1.isim)
print(per_1.eposta)
print(per_1.tam_isim)
del per_1.tam_isim
print(per_1.isim)



