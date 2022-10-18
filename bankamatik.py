tc='1234567890'
şifre='123'
ad='zeynep'
soyad='kıcıkoğlu'
para= 1000000
işlemler={ 1 : "para çekme" , 2 : "para yatırma"}

idnumber= input('tc: ')
password= input('şifre: ')



if(idnumber == tc):
    if(password == şifre):
        print(f'hoş geldin {ad} {soyad} şuanki mevcut paranız: {para}')
        print(işlemler)
    
    else:
        print('hatalı şifre')
else:
    print('hatalı tc')    

işlemno=int(input('işlem seçin: '))

if (işlemno == 1):
    miktar=int(input('Ne kadar para çekmek istiyorsunuz? '))
    if (miktar<= para):
        sonuç= para - miktar
        print(f"kalan paranız {sonuç}")
    else:
        print("maalesef o kadar paranız yok")
else:
    yatırım=int(input('Ne kadar para yatırmak istiyorsunuz? '))
    sonuç=para+yatırım
    print(f"mevcut paranız {sonuç}")


print(f"iyi günler {ad} {soyad} yine bekleriz")
     

    




