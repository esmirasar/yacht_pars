import requests
from bs4 import BeautifulSoup


def parsing(url):
    response = requests.get(url)

    parsing_product = BeautifulSoup(response.text, 'html.parser')

    products = parsing_product.find_all('div', class_='section_item')
    list_category = []
    for section_item in products:
        category_name = section_item.find('a', class_='thumb').img['title']
        subcategory = section_item.find_all('li', class_='sect')
        for i in subcategory:
            list_category.append(i.a.text)

    return list_category


url = 'https://yacht-parts.ru/catalog/'
print(parsing(url))
# TODO распарсить все категории
