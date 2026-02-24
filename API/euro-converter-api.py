# Este código es un programa de conversión de moneda que utiliza una API para obtener las tasas de cambio actuales.

import requests

mi_url = "https://api.frankfurter.app/latest?from=EUR" # Definimos la URL de la API que queremos consultar
respuesta = requests.get(mi_url) # Usamos 'mi_url' que definimos arriba

datos = respuesta.json()["rates"]


# Menu para poder elegir 3 opciones de conversion de euro a otras monedas. 
# El usuario ingresa la cantidad de euros que desea convertir y el programa muestra el resultado de la conversión.

print("Bienvenido ingresa una de las siguientes opciones para convertir de Euro a las siguentes monedas : \n 1. Dólares (USD) \n 2. Libras Esterlinas (GBP) \n 3. Yen Japonés (JPY)  ")
opcion= input("Ingrese la opción deseada: ").strip()

match opcion:
    case "1":
        moneda = "USD"
    case "2":
        moneda = "GBP"
    case "3":
        moneda = "JPY"
    case _:
        moneda = None 
        
if moneda != None:
    cantidad = float(input(f"Ingresa la cantidad de Euros para convertir a {moneda}: ")) #Segun la opcion que elija el usuario, se le pedira ingresar la cantidad de euros a convertir a la moneda seleccionada.
    
    resultado = cantidad * datos[moneda]
    
    print(f"Resultado: {cantidad} EUR = {resultado:.2f} {moneda}")# Finalmente, se muestra el resultado de la conversión al usuario.
else:
    print("Opción no válida. Por favor, elige una opción del 1 al 3.")

