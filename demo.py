import requests
from bs4 import BeautifulSoup

url_country = "https://www.aljazeera.com/news/2020/01/countries-confirmed-cases-coronavirus-200125070959786.html"

re = requests.get(url_country)
page1 = re.content

soup = BeautifulSoup(page1, 'html.parser')
country_name = soup.find_all('h3')

for country in country_name[0:-4]:
    print(country.text)