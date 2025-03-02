import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


output_folder = r"D:\Documents_D\Python_Shadowfox\Web_Scraping"
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, "Rent_Comparisons.csv")


website, Title, price, description = [], [], [], []


urls = {
    "Housing": "https://housing.com/rent/search-C4M3P1fge1l3jdv6wjkipT7psUn5c",
    "MagicBricks": "https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=2&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&Locality=New-Town&cityName=Kolkata&BudgetMin=10000&BudgetMax=30000"
}


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5"
}


for site, url in urls.items():
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        continue

    soup = BeautifulSoup(response.content, "html.parser")

    title, rent, desc = [], [], []

    # Scrape based on website
    if site == "Housing":
        title = soup.find_all("h2", class_="title-style")
        rent = soup.find_all("div", class_="T_b18cbf2e _7l1ulh _r31e5h _g3gktf _csbfng _c8exct _bx1t02")
        desc = soup.find_all("div", class_="_c81fwx _cs1nn1 _vy1wug _g3gktf _1qkcs3je T_c03272d6")

    if site == "MagicBricks":
        title = soup.find_all("h2", class_="mb-srp__card--title")
        rent = soup.find_all("div", class_="mb-srp__card__price--amount")
        desc = soup.find_all("div", class_="mb-srp__card--desc--text")

    
    if title and rent and desc:
        for t, r, d in zip(title, rent, desc):
            Title.append(t.text.strip())
            price.append(r.text.strip())
            description.append(d.text.strip())
            website.append(site)


df = pd.DataFrame({
    "Website": website,
    "Property_Title": Title,
    "Rent": price,
    "Description": description
})

df.to_csv(output_file, index=False)
print(f"Data saved successfully at: {output_file}")
