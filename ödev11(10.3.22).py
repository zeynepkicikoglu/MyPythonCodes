"""Programlama Ödevi - Iteratorlar ve Generatorlar

Program 1
"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. Bu sınıfın init
fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının
karesi yazdırılsın. StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.
Örnek olarak;
kareler = Kareler(5)
iteration = iter(kareler)
next(iteration)
1
next(iteration)
4
next(iteration)
9
next(iteration)
16
next(iteration)
25
next(iteration)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-24-94812372e992> in <module>()
----> 1 next(iteration)
<ipython-input-1-105b1e41e5e3> in __next__(self)
     20
     21             self.sayı = 1
---> 22             raise StopIteration
     23
     24
StopIteration:"""

class Kareler():
    def __init__(self,maksimum=0):
        self.maksimum=maksimum
        self.sayılar=1
    def __iter__(self):
        return self
    def __next__(self):
        if (self.sayılar<=self.maksimum):
            sonuc = self.sayılar ** 2
            self.sayılar += 1
            return sonuc
        else:
            raise StopIteration

myfunc=Kareler(5)
iterator=iter(myfunc)
for i in iterator:
    print(i)


"""Program 2
1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın."""
print("****************************************************")

def asal_mı(sayı):
    i = 2
    while i < sayı:
        if (sayı % i == 0):
            return False
        i += 1
    return True

def asal_generator():
    i = 2
    while True:
        if (asal_mı(i)):
            yield i
        i += 1

for sayı in asal_generator():
    if (sayı > 1000):
        break
    print(sayı)












