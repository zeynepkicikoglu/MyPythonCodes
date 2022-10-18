
import json 
import requests
from bs4 import BeautifulSoup

url= "https://www.teknosa.com/iphone-ios-telefonlar-c-100001001"

html=requests.get(url).content
soup= BeautifulSoup(html, "html.parser")

listem= soup.find_all("div", {"class":"product-item"})
print(len(listem))

products=[]

 
for product in listem:
   
    isim= product.get("data-product-name")
    fiyat=product.get("data-product-price")
    url=product.get("data-product-url")


    products.append([isim,fiyat,url])

print(products)

with open("urunler.json", "w" ) as file:
    json.dump(products,file)
    






