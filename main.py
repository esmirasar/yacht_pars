import requests
from bs4 import BeautifulSoup

list_category = []
href = []


def parsing_catalog():
    response = requests.get('https://yacht-parts.ru/catalog/')

    parsing_product = BeautifulSoup(response.text, 'html.parser')

    products = parsing_product.find_all('div', class_='catalog_section_list')

    for section_item in products:
        category_name = section_item.find('a', class_='thumb').img['title']

        subcategory = section_item.find_all('li', class_='sect')

        for i in subcategory:
            list_category.append(i.a.text)
            href.append(i.a['href'])

    return href


def parsing_card():
    list_name = []
    for i in href:
        list_name.append(i)
        url_name = 'https://yacht-parts.ru/' + i
        response = requests.get(url_name)
        parsing_product = BeautifulSoup(response.text, 'html.parser')
        parsing_name_product = parsing_product.find_all('div', class_='item-title')
        for j in parsing_name_product:
            list_name.append(j.find('span').text)

    return list_name


parsing_catalog()
print(parsing_card())
