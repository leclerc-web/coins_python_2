# -*-coding:Latin-1 -*

# INSTALL pip install terminaltables
# INSTALL pip install simplejson
# INSTALL pip install colorclass
# INSTALL WINDOWS python -m ...


# FONCTION SLEEP
import time
# IMPORT VARIABLE OS CLEAR
import os
# API
import json
import urllib2
# COULEUR TABLEAU
from colorclass import Color


####################################################################################
api_name = "https://api.coinmarketcap.com/v1/ticker/"
name_json = json.load(urllib2.urlopen(api_name))

# CREATION LISTE ID | SORTED() POUR TRIE ALPHABET
ids = sorted([name['id'] for name in name_json]) 
 
for id in ids:
    print(id)

print "\n\n\n\n"

####################################################################################


# INPUT STRING
coin = raw_input("Name coin is : ")
nb_coins_string =  raw_input("How many coins : ")
question_btc_coin = raw_input("Have you got Bitcoin ? (yes or no) : ")


# SI VIDE
if not nb_coins_string :

 os.system('cls' if os.name == 'nt' else 'clear')

 print "\n\n"
 print Color("{autored}Put your coins amount or put 0{/autored}")
 print "\n\n"

 
# CONVERSION STRING  INPUT EN FLOAT
nb_coins = float(nb_coins_string)


if question_btc_coin == "yes" :
	
	# SI IL RESTE DES BITCOINS, COMBIEN EN A T ON ?
	question_btc_coin = raw_input("How many Bitcoin ? : ")
	potentiel_buy = float(question_btc_coin)
	
	x = 1
	while x >= 0 :

		# JSON coin
		api_coin = "https://api.coinmarketcap.com/v1/ticker/" + coin + "/?convert=EUR"
		coin_json = json.load(urllib2.urlopen(api_coin))

		# JSON BTC
		api_btc  = "https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR";
		btc_json = json.load(urllib2.urlopen(api_btc))
		

		# VALEUR D'UN BITCOIN E EURO
		cours_btc = float(btc_json[0]["price_eur"])


		# VALEUR DE LA MONNAIE EN EURO, USD, BTC
		coin_euro = round(float(coin_json[0]["price_eur"]),2)
		coin_usd  = round(float(coin_json[0]["price_usd"]),2)
		coin_btc  = float(coin_json[0]["price_btc"])

		# POURCENTAGE
		coin_percent = str(coin_json[0]["percent_change_24h"])
		# EXPLODE DE LA CHAINE POUR RECUPERER "-"
		split = coin_percent.split('.')
		
		
		# SOMME DE COINS EN BITCOIN
		total_coin_btc = float(nb_coins * coin_btc)
		# PRODUIT EN X, TOTAL DE COIN EN BTC * PRIX DU BTC EN EURO / 1
		total_coin_eur = round(float(total_coin_btc * cours_btc),2)




		#------------------COURS BTC---------------------#

		from terminaltables import AsciiTable
		table_data = [
			['1 BTC --> Euro'],
			[Color('{autored}'+ str(cours_btc) + '{/autored}')]
		]
		table = AsciiTable(table_data)
		print table.table

		#------------------POTENTIEL---------------------#
		
		from terminaltables import AsciiTable
		table_data = [
			[ 'Achat potentiel', 'Total potentiel'],
			[Color('{autored}'+ str(potentiel_buy / coin_btc) + '{/autored}'),
			Color('{autored}'+ str(potentiel_buy / coin_btc + nb_coins) + '{/autored}')]
		]
		table = AsciiTable(table_data)
		print table.table
		
		#-----------------SOMME TOTAL--------------------#
		
		# SI "-" EXISTE, POURENTAGE AFFICHE EN ROUGE
		if split[0][0] == "-" :
			from terminaltables import AsciiTable
			table_data = [
				['TOTAL ' + coin +'','TOTAL BTC', 'TOTAL euros', coin +' %'],
				[Color('{autored}' + str(nb_coins) + '{/autored}'),
				 Color('{autored}' + "{:.8f}".format(total_coin_btc) + '{/autored}'),
				 Color('{autored}' + str(total_coin_eur) + '{/autored}'),
				 Color('{autored}' + str(coin_percent) + '{/autored}')]				   
			]
			table = AsciiTable(table_data)
			print table.table
		else : 
			from terminaltables import AsciiTable
			table_data = [
				['TOTAL ' + coin +'','TOTAL BTC', 'TOTAL euros', coin +' %'],
				[Color('{autored}' + str(nb_coins) + '{/autored}'),
				 Color('{autored}' + "{:.8f}".format(total_coin_btc) + '{/autored}'),
				 Color('{autored}' + str(total_coin_eur) + '{/autored}'),
				 Color('{autogreen}' + str(coin_percent) + '{/autogreen}')]				   
			]
			table = AsciiTable(table_data)
			print table.table

		#------------------COURS COINS---------------------#

		from terminaltables import AsciiTable
		table_data = [
			['Cours '+ coin +' --> $', 'Cours ' + coin + ' --> EURO', 'Cours ' + coin +' --> SATOSHIS'],
			[Color('{autored}' + str(coin_usd) + '{/autored}'), 
			 Color('{autored}' + str(coin_euro) + '{/autored}'),
			 Color('{autored}' + "{:.8f}".format(coin_btc) + '{/autored}')]
		]
		table = AsciiTable(table_data)
		print table.table

		# ACTUALISATION API 
		time.sleep(5)
		# CMD CLEAR
		os.system('cls' if os.name == 'nt' else 'clear')
		
else :

	x = 1
	while x >= 0 :

		# JSON coin
		api_coin = "https://api.coinmarketcap.com/v1/ticker/" + coin + "/?convert=EUR"
		coin_json = json.load(urllib2.urlopen(api_coin))

		# JSON BTC
		api_btc  = "https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR";
		btc_json = json.load(urllib2.urlopen(api_btc))
		

		# VALEUR D'UN BITCOIN E EURO
		cours_btc = float(btc_json[0]["price_eur"])


		# VALEUR DE LA MONNAIE EN EURO, USD, BTC
		coin_euro = round(float(coin_json[0]["price_eur"]),2)
		coin_usd  = round(float(coin_json[0]["price_usd"]),2)
		coin_btc  = float(coin_json[0]["price_btc"])

		# POURCENTAGE
		coin_percent = str(coin_json[0]["percent_change_24h"])
		# EXPLODE DE LA CHAINE POUR RECUPERER "-"
		split = coin_percent.split('.')
		
		
		# SOMME DE COINS EN BITCOIN
		total_coin_btc = float(nb_coins * coin_btc)
		# PRODUIT EN X, TOTAL DE COIN EN BTC * PRIX DU BTC EN EURO / 1
		total_coin_eur = round(float(total_coin_btc * cours_btc),2)




		#------------------COURS BTC---------------------#

		from terminaltables import AsciiTable
		table_data = [
			['1 BTC --> Euro'],
			[Color('{autored}'+ str(cours_btc) + '{/autored}')]
		]
		table = AsciiTable(table_data)
		print table.table


		#-----------------SOMME TOTAL--------------------#
		
		# SI "-" EXISTE, POURENTAGE AFFICHE EN ROUGE
		if split[0][0] == "-" :
			from terminaltables import AsciiTable
			table_data = [
				['TOTAL ' + coin +'','TOTAL BTC', 'TOTAL euros', coin +' %'],
				[Color('{autored}' + str(nb_coins) + '{/autored}'),
				 Color('{autored}' + "{:.8f}".format(total_coin_btc) + '{/autored}'),
				 Color('{autored}' + str(total_coin_eur) + '{/autored}'),
				 Color('{autored}' + str(coin_percent) + '{/autored}')]				   
			]
			table = AsciiTable(table_data)
			print table.table
		else : 
			from terminaltables import AsciiTable
			table_data = [
				['TOTAL ' + coin +'','TOTAL BTC', 'TOTAL euros', coin +' %'],
				[Color('{autored}' + str(nb_coins) + '{/autored}'),
				 Color('{autored}' + "{:.8f}".format(total_coin_btc) + '{/autored}'),
				 Color('{autored}' + str(total_coin_eur) + '{/autored}'),
				 Color('{autogreen}' + str(coin_percent) + '{/autogreen}')]				   
			]
			table = AsciiTable(table_data)
			print table.table

		#------------------COURS COINS---------------------#

		from terminaltables import AsciiTable
		table_data = [
			['Cours '+ coin +' --> $', 'Cours ' + coin + ' --> EURO', 'Cours ' + coin +' --> SATOSHIS'],
			[Color('{autored}' + str(coin_usd) + '{/autored}'), 
			 Color('{autored}' + str(coin_euro) + '{/autored}'),
			 Color('{autored}' + "{:.8f}".format(coin_btc) + '{/autored}')]
		]
		table = AsciiTable(table_data)
		print table.table

		# ACTUALISATION API 
		time.sleep(5)
		# CMD CLEAR
		os.system('cls' if os.name == 'nt' else 'clear')