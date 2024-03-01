from bs4 import BeautifulSoup
import requests


#Obtener el HTML
URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

#2. "Parsear" ese html
soup = BeautifulSoup(html_obtenido,"html.parser")

primer_h2 = soup.find('h2')
print('-' * 30)
print(primer_h2)

#solo texto
print('-' * 30)
print(primer_h2.text)

print('-' * 30)
h2_todos = soup.find_all('h2')
print(h2_todos)

print('-' * 30)
h2_uno_solo = soup.find_all('h2' , limit=1)
print(h2_uno_solo)
print('-' * 30)

for seccion in h2_todos:
    print(seccion.text)
print('-' * 30)

for seccion in h2_todos:
    print(seccion.get_text(strip = True))
print('-' * 30)

divs = soup.find_all('div' , class_ = "heading-container heading-center")

for div in divs:
    print(div)
    print(" ")

print('-' * 30)

src_todos = soup.find_all(src=True)
for elemento in src_todos:
    if elemento['src'].endswith(".jpg"):
        print(elemento)
        
print('-' * 30)

# url_imagenes = []

# for i , imagen in enumerate(src_todos):
#     if imagen['src'].endswith('png'):
#         print(imagen['src'])
#         r = requests.get(f"https://scrapepark.org/{imagen['src']}")

#         with open(f'imagen_{i}.png' , 'wb') as f:
#             f.write(r.content)

print('-' * 30)

URL_BASE = 'https://scrapepark.org/courses/spanish'
URL_TABLA = soup.find_all('iframe')[0]['src']

request_tabla = requests.get(f'{URL_BASE}/{URL_TABLA}')

html_tabla = request_tabla.text
soup_tabla = BeautifulSoup(html_tabla, "html.parser")
soup_tabla.find('table')

productos_faltantes = soup_tabla.find_all(['th', 'td'], attrs={'style':'color: red;'})
productos_faltantes = [talle.text for talle in productos_faltantes]

print(productos_faltantes)

print('-' * 30)

divs = soup.find_all('div', class_='detail-box')
productos = []
precios = []

for div in divs:
  if (div.h6 is not None) and ('Patineta' in div.h5.text):
    producto = div.h5.get_text(strip=True)
    precio = div.h6.get_text(strip=True).replace('$', '')
    # Se puede agregar filtros
    print(f'producto: {producto:<16} | precio: {precio}')
    productos.append(producto)
    precios.append(precio)

print('-' * 30)

URL_BASE = "https://scrapepark.org/courses/spanish/contact"

for i in range(1 , 3):
   URL_FINAL = f"{URL_BASE}{i}"
   print(URL_FINAL)
   r = requests.get(URL_FINAL)
   soup = BeautifulSoup(r.text, "html.parser")
   print(soup.h5.getText)

print('-' * 30)
import re

URL_BASE = 'https://scrapepark.org/courses/spanish'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, "html.parser")

telefonos = soup.find_all(string = re.compile("\d+-\d+-\d+"))
telefonos


print('-' * 30)
copyrights = soup.find_all(string=re.compile("©"))
copyrights[0]

primer_copyright = copyrights[0]
primer_copyright.parent

# # Otro ejemplo con elementos al mismo nivel
menu = soup.find(string=re.compile("MENÚ"))
# menu.parent
menu.parent.find_next_siblings()

print('-' * 30)

strings_a_buscar = ["MENÚ", "©", "carpincho", "Patineta"]

for string in strings_a_buscar:
  try:
    resultado = soup.find(string=re.compile(string))
    print(resultado.text)
  except AttributeError:
    print(f"El string '{string}' no fue encontrado")

print('-' * 30)

productos.insert(0, "productos")
precios.insert(0, "precios")
# datos = dict(zip(productos, precios))
datos = dict(zip(productos, precios))
datos.items()
import csv

with open('datos.csv','w') as f:
    w = csv.writer(f)
    w.writerows(datos.items())
    
print('-' * 30)