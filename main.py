import requests
from bs4 import BeautifulSoup

href = []
list_category = []


# Парсинг каталога и категорий товаров
def parsing_catalog():
    response = requests.get('https://yacht-parts.ru/catalog/')

    parsing_product = BeautifulSoup(response.text, 'lxml')

    products = parsing_product.find_all('div', class_='catalog_section_list')

    for section_item in products:
        category_name = section_item.find('a', class_='thumb').img['title']

        subcategory = section_item.find_all('li', class_='sect')

        list_category.extend([i.a.text for i in subcategory])
        href.extend([i.a['href'] for i in subcategory])

    return href


# Парсинг ссылок на отдельные категории
def parsing_href():
    list_name = []
    url_name = 'https://yacht-parts.ru/'
    for i in href:
        list_name.append(i)
        url_name += i
    response = requests.get(url_name)
    parsing_product = BeautifulSoup(response.text, 'html.parser').find_all('div', class_='item-title')
    list_name.extend([j.find('span').text for j in parsing_product])

    return list_name


parsing_catalog()
print(*parsing_href(), sep='\n')
