# Criando os produtos
from core.models import Category, Product
import csv
import io
import urllib.request
from pprint import pprint



def csv_online_to_list(url: str) -> list:
    '''
    Lê um CSV a partir de uma url.
    '''
    url_open = urllib.request.urlopen(url)
    reader = csv.DictReader(io.StringIO(
        url_open.read().decode('utf-8')), delimiter=',')
    csv_data = [line for line in reader]
    return csv_data

products = csv_online_to_list('https://raw.githubusercontent.com/rg3915/django-chartjs/master/fix/products.csv')
pprint(products)
aux = []
for product in products:
    data = {
        'title': product['title'],
        'price': product['price']
    }
    category_title = product.get('category')
    category = Category.objects.filter(title=category_title).first()
    obj = Product(**data)
    if category:
        obj = Product(category=category, **data)
    aux.append(obj)

Product.objects.bulk_create(aux)