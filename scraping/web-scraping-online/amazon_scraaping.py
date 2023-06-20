import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/s?k=python+books'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

session = requests.Session()
session.headers.update(headers)

response = session.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('div', {'data-component-type': 's-search-result'})

for result in results[:10]:
    product_name = result.find('h2').text.strip()
    product_price = result.find('span', {'class': 'a-price-whole'}).text.strip()
    product_rating = result.find('span', {'class': 'a-icon-alt'}).text.strip().split()[0]
    print(product_name)
    print(product_price)
    print(product_rating)
