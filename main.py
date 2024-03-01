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

url_imagenes = []

for i , imagen in enumerate(src_todos):
    if imagen['src'].endswith('png'):
        print(imagen['src'])
        r = requests.get(f"https://scrapepark.org/{imagen['src']}")

        with open(f'imagen_{i}.png' , 'wb') as f:
            f.write(r.content)

print('-' * 30)

URL_BASE = 'https:/scrapepark.org/courses/spanish'
URL_TABLA = soup.find_all('iframe')[0]['src']

request_tabla = requests.get(f'{URL_BASE}/{URL_TABLA}')

html_tabla = request_tabla.text
soup_tabla = BeautifulSoup(html_tabla, "html.parser")
soup_tabla.find('table')

productos_faltantes = soup_tabla.find_all(['th' , 'td'] , attrs={'style':'color: red;'})
productos_faltantes = [talle.text for table in productos_faltantes]

print(productos_faltantes)

print('-' * 30)