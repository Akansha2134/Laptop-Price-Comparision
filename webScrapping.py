import requests
from bs4 import BeautifulSoup
import pandas as pd

def Web_scrapping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup

hb = "C:\Desktop\scrap\Mobile- Buy Products Online at Best Price in India - All Categories _ Flipkart.com(1).html"
czone = "C:\Desktop\scrap\Mobile- Buy Products Online at Best Price in India - All Categories _ Flipkart.com(1).html"

product1 = Web_scrapping(hb)
product2 = Web_scrapping(czone)

# Product prices
product1_price = product1.find("span", class_ = "price-sales")
product2_price = product2.find("span", class_ = "price-sales")

# for cleaning purposes
product1_price = product1_price.text.strip()
product2_price = product2_price.text.strip()

# products name
product1_name = product1.title.text.strip()
product2_name = product2.title.text.strip()

# Website's name
website1 = 'HB Computers'
website2 = "Computer Zone"

# creating data frame
data = {
    "Product Name": [product1_name, product2_name],
    "Price" : [product1_price, product2_price],
    "Website_name" : [website1, website2]
}

df = pd.DataFrame(data)

# Converting into csv file
df.to_csv("Laptop_price.csv", index=False)



