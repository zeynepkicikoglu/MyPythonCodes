kullanıcılar={}
number=input("kullanıcı no: ")
name=input("kullanıcı adı: ")
surname=input("kullanıcı soyadı: ")
tckimlik=input("tc kimlik: ")
password=input("şifre: ")

kullanıcılar[number]={
'ad': name,
'soyad': surname,
'tckimlik' : tckimlik,
'şifre': password

}
print(kullanıcılar)