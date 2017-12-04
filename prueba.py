
import json
import requests
import time
from urllib.request import urlopen



def get_precio_actual(url,currency):
	url_readed = requests.get(url)
	newDictionary = url_readed.json()
	print("obteniendo datos de la url " + url)
	valor = newDictionary[currency]
	print("El precio actual es: " + str(valor) + " " + currency )
	return valor

def define_currencies(input_currency, output_currency):
	print("generando URL para obtener datos")
	new_url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"
	new_url = new_url.format(input_currency, output_currency)
	return new_url

def logica_de_compra_venta(porcentaje, precio_actual, precio_a_comparar):
	print("precio a comparar: " + str(precio_a_comparar))
	if precio_a_comparar != 0:
		porcentaje_a_comparar = (precio_actual / precio_a_comparar)
		if porcentaje_a_comparar < 0:
			porcentaje_a_comparar = porcentaje_a_comparar * (-1)
		porcentaje_a_comparar = porcentaje_a_comparar - 1
		print("porcentaje: " + str(porcentaje_a_comparar))
		if porcentaje_a_comparar >= porcentaje:
			return True
	else:
		return True

def comprar_o_vender():
	global flag_comprar_bitcoin
	global plata
	global precio_de_venta
	global precio_de_compra
	if flag_comprar_bitcoin == False:
		print("vender")
		url = define_currencies('USD','IOTA')
		precio_actual = get_precio_actual(url, 'IOTA')
		if logica_de_compra_venta(PORCENTAJE, precio_actual, precio_de_venta):
			plata = plata / precio_actual
			print("Tienes EUR:" + str(plata))
			flag_comprar_bitcoin = True
			precio_de_compra = precio_actual
		else:
			print("No es conveniente realizar la transaccion")
	else:
		print("comprar")
		url = define_currencies('USD','IOTA')
		precio_actual = get_precio_actual(url, 'IOTA')
		if logica_de_compra_venta(PORCENTAJE, precio_actual, precio_de_compra):
			plata = plata * precio_actual
			print("Tienes IOTAs: " + str(plata))
			flag_comprar_bitcoin = False
			precio_de_venta = precio_actual
		else:
			print("No es conveniente realizar la transaccion")

#constantes
PORCENTAJE = 0.005
#variables
valor_inicial = 100
flag_comprar_bitcoin = True
plata = valor_inicial
precio_de_compra = 0
precio_de_venta = 0
precio_actual = 0

print("Version 1.0 millonaire")
print("Tu valor inicial en euros es:" + str(valor_inicial))


for i in range(0,100):
	comprar_o_vender()
	print("================================")
	time.sleep(60)

print("Tu valor final es: " + str(precio_de_venta)) 
print("Tu valor final es: " + str(precio_de_compra)) 