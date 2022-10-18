"""Proje 1
Kodlama Egzersizimizde yazdığımız Kumanda Sınıfına ek olarak metodlar ve özellikler eklemeye çalışın."""
import time
import random
class Kumanda():
    def __init__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if (self.tv_durum=="Açık"):
            print("Televizyon zaten açık.")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum="Açık"
    def tv_kapat(self):
        if (self.tv_durum=="Kapalı"):
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapatılıyor...")
            self.tv_durum="Kapalı"
    def ses_ayarı(self):
        while True:
            cevap=input("Sesi azalt: '<\nSesi artır:'>'\nÇıkış: q\n:")
            if(cevap=='<'):
                if (self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses:",self.tv_ses)
            elif(cevap=='>'):
                if (self.tv_ses!=31):
                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses güncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi.")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]

        print("Şu anki kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durumu:{}\nTv ses:{}\nKanal durumu:{}\nŞu anki kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda=Kumanda()
print("""Televizyon Uygulaması
******************************
1-Tv Aç
2-Tv Kapat 
3-Ses Ayarları
4-Kanal Ekle
5-Kanal Sayısını Öğrenme
6-Rastgele Kanala Geçme
7-Televizyon Bilgileri

Çıkmak için 'q' ya basın.
******************************""")

while True:
    işlem=input("İşlem seçiniz:")
    if(işlem=='q'):
        print("Program sonlandırılıyor...")
        break
    elif(işlem=="1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayarı()
    elif (işlem == "4"):
        kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak giriniz:")
        kanal_listesi=kanal_isimleri.split(',')

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        print("Kanal sayısı:",len(kumanda))
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem...")




"""Proje 2
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.
Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın."""

class PC:
    def __init__(self,name,processor,screen,ram,inc,gb):
        self.name=name
        self.processor=processor
        self.screen=screen
        self.ram=ram
        self.inc=inc
        self.gb=gb
    def __len__(self):
        return self.gb
    def __str__(self):
        return f'{self.name} isimli Pcnin özellikleri: \n{self.processor} işlemci\n{self.screen}ekran\n{self.ram}ram\n{self.inc}inc\n{self.gb}gb'

pc_1 = PC("asus","windows","1920x1080","8GB","15","256")
print(pc_1)
print("len:",PC.__len__(pc_1))


"""Proje 3
Bu projede ise 4 tane sınıfı oluşturun.
Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.
Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.
At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin."""