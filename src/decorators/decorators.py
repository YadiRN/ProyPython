import time # Importamos el modulo time para medir el tiempo de ejcución
import logging # Importamos el modulo loggin para registrar mensajes.

# Configuramos el logger

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

"""
Configuramos el registro de mensajes (LOGGING) de manera que muestre mensajes de nivel INFO y superior.
Definimos el formato de los mensajes de registro, incluyendo la marca de tiempo (asctime), el nivel de mensaje (levelname) y el mensaje (message)
"""

def timeit(func):
    """Decorador para medir el tiempo de ejecución de una función"""
    def wrapper(*args, **kwargs):
        start_time = time.time() # Registramos el tiempo de inicio
        result = func(*args, **kwargs) # Se ejecuta la función decoradora
        end_time = time.time() # Registramos el tiempo de finalización
        elapsed_time = end_time - start_time # Calculamos el tiempo transcurrido
        logging.info(f"{func.__name__} ejecutada en {elapsed_time:4f} seconds") # Registramos el tiempo de ejecucion
        return result # Retornanamos el resultado de la funcion
    return wrapper # Devolvemos el decorador.

def logit(func):
    """Decorador para registrar la ejecucion de una funcion"""
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}") # Registramos el inicio de la ejecucion
        result = func(*args, **kwargs) # Ejecutamos la funcion decoradora
        logging.info(f"Completado {func.__name__}") # Registramos que la ejecucion de la funcion finaliza
        return result # Devolvemos el resultado de la funcion.
    return wrapper
        