# -*-coding:Latin-1 -*

# INSTALL pip install terminaltables
# INSTALL pip install simplejson
# INSTALL pip install colorclass
# INSTALL WINDOWS python -m ...


# SLEEP
import time
# VARIABLE OS
import os
# API
import json
import urllib2
# COULEUR 
from colorclass import Color
# TABLEAU
from terminaltables import AsciiTable

####################################################################################

api_name = "https://api.coinmarketcap.com/v1/ticker/"
name_json = json.load(urllib2.urlopen(api_name))

# LISTE ID | SORTED() TRIE ALPHABET
ids = sorted([name['id'] for name in name_json]) 
 
for id in ids:
    print(id)

print "\n\n\n\n"

####################################################################################

# INPUT STRING
coin = raw_input("Name coin is : ")
nb_coins_string =  raw_input("How many coins : ")

# SI VIDE
if not nb_coins_string :

	os.system('cls' if os.name == 'nt' else 'clear')

	print "\n\n"
	print Color("{autored}Put your coins amount or put 0{/autored}")
	print "\n\n"

# CONVERSION STRING -> FLOAT
nb_coins = float(nb_coins_string)
####################################################################################
	

# JSON coin
api_coin = "https://api.coinmarketcap.com/v1/ticker/" + coin + "/?convert=EUR"
coin_json = json.load(urllib2.urlopen(api_coin))

# JSON BTC
api_btc  = "https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR";
btc_json = json.load(urllib2.urlopen(api_btc))

# COURS D'UN BITCOIN EN EURO
cours_btc = float(btc_json[0]["price_eur"])

# COURS MONNAIE : EURO, USD, BTC
coin_euro = round(float(coin_json[0]["price_eur"]),2)
coin_usd  = round(float(coin_json[0]["price_usd"]),2)
coin_btc  = float(coin_json[0]["price_btc"])

# POURCENTAGE 24H
btc_percent = str(btc_json[0]["percent_change_24h"])
coin_percent = str(coin_json[0]["percent_change_24h"])
# EXPLODE DE LA CHAINE POUR RECUPERER "-"
split_coins = coin_percent.split('.')
split_btc = btc_percent.split('.')			

# SOMME DE COINS EN BITCOIN
total_coin_btc = float(nb_coins * coin_btc)
# PRODUIT EN X, TOTAL DE COIN EN BTC * PRIX DU BTC EN EURO / 1
total_coin_eur = round(float(total_coin_btc * cours_btc),2)

array = [api_coin,coin_json,api_btc,btc_json,cours_btc,coin_euro,coin_usd,coin_btc,btc_percent,coin_percent,split_coins,split_btc,total_coin_btc,total_coin_eur]

def coins() :
	x = 0
	while x <= 13 :
		array[x]
		x = x + 1
	

		
if coin != "bitcoin" :

	question_btc_coin = raw_input("Do you still have bitcoins? (yes or no) : ")
	
	if question_btc_coin == "yes" :
	
		##########################################################################################################
		# SI IL RESTE DES BITCOINS, COMBIEN ?
		question_btc_coin = raw_input("How many bitcoins do you have left ? : ")
		
		# SI VIDE
		if not question_btc_coin :

			os.system('cls' if os.name == 'nt' else 'clear')

			print "\n\n"
			print Color("{autored}Put your coins amount or put 0{/autored}")
			print "\n\n"
			
		potentiel_buy = float(question_btc_coin)
		##########################################################################################################
		
		while True :

			coins()

			#------------------COURS BTC---------------------#
						
			if split_btc[0][0] == "-" :
			
				table_data = [
					['1 BTC --> Euro','BTC %'],
					[Color('{autored}'+ str(cours_btc) + '{/autored}'),
					 Color('{autored}'+ str(btc_percent) + '{/autored}')]
				]
				table = AsciiTable(table_data)
				print table.table
				
			else :
			
				table_data = [
					['1 BTC --> Euro','BTC %'],
					[Color('{autored}'+ str(cours_btc) + '{/autored}'),
					 Color('{autogreen}'+ str(btc_percent) + '{/autogreen}')]
				]
				table = AsciiTable(table_data)
				print table.table
				
			#------------------POTENTIEL---------------------#		
			 
			table_data = [
				[ 'Achat potentiel', 'Total potentiel'],
				[Color('{autored}'+ str(potentiel_buy / coin_btc) + '{/autored}'),
				Color('{autored}'+ str(potentiel_buy / coin_btc + nb_coins) + '{/autored}')]
			]
			table = AsciiTable(table_data)
			print table.table
			
			#-----------------SOMME TOTAL--------------------#			 
			
			if split_coins[0][0] == "-" :
		
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
			
	else  :
		
		while True :
		
			coins()
		
			#------------------COURS BTC---------------------#
				
			if split_btc[0][0] == "-" :
			
				table_data = [
					['1 BTC --> Euro','BTC %'],
					[Color('{autored}'+ str(cours_btc) + '{/autored}'),
					 Color('{autored}'+ str(btc_percent) + '{/autored}')]
				]
				table = AsciiTable(table_data)
				print table.table
				
			else :
			
				table_data = [
					['1 BTC --> Euro','BTC %'],
					[Color('{autored}'+ str(cours_btc) + '{/autored}'),
					 Color('{autogreen}'+ str(btc_percent) + '{/autogreen}')]
				]
				table = AsciiTable(table_data)
				print table.table

			#-----------------SOMME TOTAL--------------------#		 
			
			if split_coins[0][0] == "-" :
			
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
			

###################################################################"
	
	
elif coin == "bitcoin" :

	while True :

		coins()

		#------------------COURS BTC---------------------#
		 	 
		# SUPPRESSION % 
		table_data = [
			['1 BTC --> Euro'],
			[Color('{autored}'+ str(cours_btc) + '{/autored}')]
		]
		table = AsciiTable(table_data)
		print table.table
	
		#-----------------SOMME TOTAL--------------------#
			
		if split_coins[0][0] == "-" :
		
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
		
		
