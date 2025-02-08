import requests
from bs4 import BeautifulSoup
import pandas as pd
website=[]
Title=[]
price=[]
description=[]
urls={
    "Housing":"https://housing.com/rent/search-C4M2P1fge1l3jdv6wjkipT7psUn5c",
    "MagicBricks":"https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=2&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&Locality=New-Town&cityName=Kolkata&BudgetMin=10000&BudgetMax=30000"
}

headers = ({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36","Accept-Language":"en-US, en;q=0.5"
})
for site,url in urls.items():
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,"html.parser")

    if site=="Housing":
        title=soup.find_all("div",class_="T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title")
        rent=soup.find_all("div",class_="_csbfng _c8exct _g3qslr _fr1nms _1q73f6fq _4okugktf _1qkcc65e _j3gpidpf _4nrxyh40 T_a6707275")
        desc=soup.find_all("div",class_="T_29811730 _e2dlk8 T_b09e6dc4 _ks15vq _c81fwx _9s1txw _h3exct")

    if site=="MagicBricks":
        title=soup.find_all("h2",class_="mb-srp__card--title")
        rent=soup.find_all("div",class_="mb-srp__card__price--amount")
        desc=soup.find_all("div",class_="mb-srp__card--desc--text")

    for title, rent, desc in zip(title, rent, desc):

        Title.append(title.text.strip())
        price.append(rent.text.strip())
        description.append(desc.text.strip())
        website.append(site)


df=pd.DataFrame({"Website":website,
                 "Property_Title":Title,
                 "Rent":price,
                 "Description":description})
df.to_csv("Rent_Comparisons.csv")
print("Data saved successfully at Rent_Comparisons.csv")






