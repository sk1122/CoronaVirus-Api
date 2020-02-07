# Importing Important Libraries
from flask import Flask, render_template, url_for, jsonify
import requests
from bs4 import BeautifulSoup

# Constant Variables
URL = "https://www.worldometers.info/coronavirus/"
COUNTRY_URL = "https://www.aljazeera.com/news/2020/01/countries-confirmed-cases-coronavirus-200125070959786.html"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


# Initializing Variables from libraries
app = Flask(__name__)
r = requests.get(URL, headers)
re = requests.get(COUNTRY_URL, headers)

# html of requested page
html = r.content
page = re.content

# BeautifulSoup WebScraping
soup = BeautifulSoup(html, 'html.parser')
soup_country = BeautifulSoup(page, 'html.parser')
p = soup.find_all('span')
country_name = soup_country.find_all('h3')

# Death Number
death_toll = p[6].text
print(death_toll)

# Cases
cases = p[4].text
print(cases)

# Critical Cases
critical_cases = p[5].text
print(critical_cases)

# Recovered Cases
recovered_cases = p[7].text
print(recovered_cases)

# Country Names
country_names = []
for country in country_name[0:-4]:
    country_names.append(country.text)
print(country_names)

# Flask Web App - Home Route
@app.route('/')
def home():
    return render_template("index.html")

# Flask Web App - Api Route
@app.route('/api/', methods=['GET'])
def api():
    try:
        return jsonify(country=country_names, cases=cases, recovered=recovered_cases, critical_cases=critical_cases, death=death_toll)
    except ConnectionError:
        return "Internet Not Found!"

if __name__ == "__main__":
    app.run(debug=True)
