"""Proje 1
Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız programı geliştirerek kalanları
 "kalanlar.txt" dosyasında ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın."""


with open("dosya1.txt","r",encoding= "utf-8") as file:
    for satır in file:
        satır = satır[:-1]
        liste = satır.split(",")
        isim = liste[0]
        not1 = int(liste[1])
        not2 = int(liste[2])
        not3 = int(liste[3])
        son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)
        gecenler=list()
        kalanlar=list()

        if (son_not >= 90) or (son_not >= 85) or (son_not >= 80) or (son_not >= 75) or (son_not >= 70) or (son_not >= 65) or (son_not >= 60) or (son_not >= 55):
            gecenler.append(isim + son_not)
        else:
            kalanlar.append(isim + son_not)

        with open("kalanlar.txt", "w", encoding="utf-8") as file2:
            for i in kalanlar:
                file2.write(i)

        with open("gecenler.txt", "w", encoding="utf-8") as file3:
            for i in gecenler:
                file3.write(i)




"""Proje 2
"futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları
rastgele yerleştirin. Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 
3 farklı dosyaya yazın."futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.
                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
                           //
                           //
                           //
                           //
                           //"""
with open("futbolcular.txt", "r", encoding="utf-8") as file:
    gs = list()
    bjk = list()
    fb = list()

    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")
        if (satır_elemanları[1] == "Fenerbahçe"):
            fb.append(satır + "\n")
        elif (satır_elemanları[1] == "Galatasaray"):
            gs.append(satır + "\n")

        else:
            bjk.append(satır + "\n")
    with open("gs.txt", "w", encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)

    with open("fb.txt", "w", encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)
    with open("bjk.txt", "w", encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)