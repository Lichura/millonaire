
import json
import requests
import time
from urllib.request import urlopen



def get_prices():
	print("llamando a la url")
	print("los datos son:")
	print("el BCH vale:")


def get_url(url,currency):
	url_readed = requests.get(url)
	newDictionary = url_readed.json()
	print("obteniendo datos de la url " + url)
	print(newDictionary)
	valor = newDictionary[currency]
	print("valor obtenido para esta transaccion: " + str(valor) + currency )
	return valor

def define_currencies(input_currency, output_currency):
	new_url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"
	new_url = new_url.format(input_currency, output_currency)
	return new_url

def comprar_o_vender(valor):
	global flag_compra
	global plata
	if flag_compra == False:
		print("vender")
		plata = plata / valor
		flag_compra = True
		print("Tienes EUR:" + str(plata))
	else:
		print("comprar")
		plata = plata * valor
		flag_compra = False
		print("Tienes BCH: " + str(plata))

print("Version 1.0 millonaire")
valor_inicial = 100
flag_compra = True
plata = valor_inicial

print("Tu valor inicial en euros es:" + str(valor_inicial))
for i in range(0,100):
	url = define_currencies('EUR','BCH')
	valor = get_url(url, 'BCH')
	comprar_o_vender(valor)
	print("================================")
	time.sleep(60)
