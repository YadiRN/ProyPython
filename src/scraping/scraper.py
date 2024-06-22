import requests # Importar el modulo requests para hacer las solicitudes HTTP
from bs4 import BeautifulSoup  # Importa este modulo para analizar los documentos HTML
import pandas as pd # Se importa para manejar los datos en los DataFrames

def fetch_page(url):
    """Se obtiene el contenido de una pagina"""
    response=requests.get(url) # REalizamos una solicitud GET a la URL proporcionada.
    if response.status_code == 200: # Comparamos el status code con el 200 que signigica que fue una peticion exitosa
        return response.content #Para devolver el contenido de la pagina, cuando la solicitud es exitosa
    else:
        raise Exception(f"Failed to fetch pago:{url}") # Lanzamos una excepcion cuando la solicitud falle
    

def parse_product(product):
    """Analizamos los detalles de un producto"""
    title= product.find("a", class_="title").text.strip()
    description = product.find("p", class_="description").text.strip() # Econtramos y se obtiene la descripcion del producto
    price = product.find("h4",class_="price").text.strip() # Se ecuentra y obtiene el precio del producto
    return{
        "title": title, # Traemos un diccionario con el titulo, la descripcion y el precio del producto
        "description": description,
        "price": price,
    }
def scrape(url):
    """Funcion principal del scraping"""
    page_content = fetch_page(url) # Para obtener el codigo base de la pagina
    soup = BeautifulSoup(page_content, "html.parser") # Analizamos el contenido de la pagina con BeautifulSoup
    print(soup)
    products = soup.find_all("div",class_="thumbnail") # Devolvemos todos los elementos div con la clase "thumbnail" que representa productos
    products_data=[] # Inicializa una lista para almacenar los datos de los productos
    
    for product in products: 
        product_info = parse_product(product) # Analizamos cada producto encontrado 
        products_data.append (product_info) # Para agregar los datos del producto a la lista
        
    return pd.DataFrame(products_data)
        
#Definimos el URL base para el Scraping
base_url="https://webscraper.io/test-sites/e-commerce/allinone" # Encontramos y obtenemos el titulo del producto

# Llamamos a la función scrape para obtener los datos del producto

df= scrape(base_url)

# Imprimimos el DF resultante

print(df)


df.to_csv('data/raw/products.csv', index=False) # Guardamos los datos en un archivo CSV sin incluir el índice
