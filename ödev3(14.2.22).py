"""Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""

sayı=int(input("Bir sayı giriniz:"))
bölenleri=[]
for i in range(1,sayı):
    if sayı % i == 0:
        bölenleri.append(i)
    else:
        continue

print("Tam bölenleri:",bölenleri)
toplam=0
for x in bölenleri:
    print(x)
    print(type(x))
    toplam+=x

print("Tam bölenleri toplamı:",toplam)
if toplam == sayı:
    print("Bu bir mükemmel sayı.")
else:
    print("Mükemmel sayı değil.")


"""Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4"""

sayı2=input("\nBir sayı giriniz:")
hesap=0
liste=[]
for i in sayı2:
    liste.append(i)

for x in liste:
    x=int(x)
    hesap+=x**len(liste)

print("Hesap sonucu:",hesap)
sayı2=int(sayı2)
if hesap==sayı2:
    print("Bu bir Armstrong sayıdır.")
else:
    print("Bu bir Armstrong sayı değildir.")

"""Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin."""
for i in range(1,11):
    print("*************************************************")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))

"""Problem 4
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın."""
toplam=0
while True:
    a=input("Bir sayı giriniz(çıkmak için 'q' ya basın:)")
    if a =='q':
        print("By by...")
        break
    else:
        a=int(a)
        toplam+=a
        print("Toplam:",toplam)
        continue

"""Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın."""
for i in range(1,101):
    if i % 3== 0:
        print("3'e tam bölünen sayılar:",i)
        continue

"""Problem 6
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.
Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.
İpucu: Basit düşünmeye çalışın."""

list=[i for i in range(0,101,2)]
print(list)
listee = [x for x in range(1,101) if x % 2 == 0]
print(listee)
