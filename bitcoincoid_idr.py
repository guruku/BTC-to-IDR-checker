#!/usr/bin/env python

import urllib2, urllib
import json
import os
from sys import stdout, exit
from time import sleep

os.system("clear")

print (''' \033[1;32;40m=============================================================================================\033[0m
\033[1;32;40m =\033[1;31;40m  /$$$$$$$  /$$$$$$$$ /$$$$$$          /$$                     /$$$$$$ /$$$$$$$  /$$$$$$$  \033[1;32;40m=
\033[1;32;40m =\033[1;31;40m | $$__  $$|__  $$__//$$__  $$        | $$                    |_  $$_/| $$__  $$| $$__  $$ \033[1;32;40m=
\033[1;32;40m =\033[1;31;40m | $$  \ $$   | $$  | $$  \__/       /$$$$$$    /$$$$$$         | $$  | $$  \ $$| $$  \ $$ \033[1;32;40m=
\033[1;32;40m =\033[1;31;40m | $$$$$$$    | $$  | $$            |_  $$_/   /$$__  $$        | $$  | $$  | $$| $$$$$$$/ \033[1;32;40m=
\033[1;32;40m =\033[1;37;40m | $$__  $$   | $$  | $$              | $$    | $$  \ $$        | $$  | $$  | $$| $$__  $$ \033[1;32;40m=
\033[1;32;40m =\033[1;37;40m | $$  \ $$   | $$  | $$    $$        | $$ /$$| $$  | $$        | $$  | $$  | $$| $$  \ $$ \033[1;32;40m=
\033[1;32;40m =\033[1;37;40m | $$$$$$$/   | $$  |  $$$$$$/        |  $$$$/|  $$$$$$/       /$$$$$$| $$$$$$$/| $$  | $$ \033[1;32;40m=
\033[1;32;40m =\033[1;37;40m |_______/    |__/   \______/          \___/   \______/       |______/|_______/ |__/  |__/ \033[1;32;40m=\033[0m''')
print " \033[1;32;40m=============================================================================================\033[0m"
print " \033[1;37;40m[+] Tools to check the exchange rate virtual money currency to Indonesia Rupiah           [+]\033[0m"
print " \033[1;37;40m[+] Code by : Bayu Fedra A                                                                [+]\033[0m"
print " \033[1;37;40m[+] Github  : https://github.com/B3yeZ/  || FB : Bayu Fedra  ||  Intagram: @bayufedraa    [+]\033[0m"
print " \033[1;37;40m[+] API VIA Btcoin.co.id                                                                  [+]\033[0m"
print " \033[1;32;40m=============================================================================================\033[0m"

def main():
	api = [	"https://vip.bitcoin.co.id/api/btc_idr/ticker",
			"https://vip.bitcoin.co.id/api/bch_idr/ticker",
			"https://vip.bitcoin.co.id/api/btg_idr/ticker",
			"https://vip.bitcoin.co.id/api/eth_idr/ticker",
			"https://vip.bitcoin.co.id/api/etc_idr/ticker",
			"https://vip.bitcoin.co.id/api/ltc_idr/ticker",
			"https://vip.bitcoin.co.id/api/nxt_idr/ticker",
			"https://vip.bitcoin.co.id/api/waves_idr/ticker",
			"https://vip.bitcoin.co.id/api/str_idr/ticker",
			"https://vip.bitcoin.co.id/api/xrp_idr/ticker",
			"https://vip.bitcoin.co.id/api/xzc_idr/ticker",]

	for i in api:		
		res = urllib2.urlopen(i)
		wibu = res.read()
		halah = json.loads(wibu)
		last = halah["ticker"]
		harga = int(last["last"])
		
		if "btc_idr" in i:
			print " [+] Bitcoin to Indonesia Rupiah          : Rp.{:,.2f}".format(harga) + " /BTC"
		elif "bch_idr" in i:
			print " [+] Bitcoin Cash to Indonesia Rupiah     : Rp.{:,.2f}".format(harga) + "  /BCH"
		elif "btg_idr" in i:
			print " [+] Bitcoin Gold to Indonesia Rupiah     : Rp.{:,.2f}".format(harga) + "   /BTG"
		elif "eth_idr" in i:
			print " [+] Ethereum to Indonesia Rupiah         : Rp.{:,.0f}".format(harga) + "     /ETH"
		elif "etc_idr" in i:                                                                   
			print " [+] Ethereum Classic to Indonesia Rupiah : Rp.{:,.0f}".format(harga) + "        /ETC"
		elif "ltc_idr" in i:                                                                   
			print " [+] Litecoin to Indonesia Rupiah         : Rp.{:,.0f}".format(harga) + "      /LTC"
		elif "nxt_idr" in i:                                                                   
			print " [+] NXT to Indonesia Rupiah              : Rp.{:,.0f}".format(harga) + "         /NXT"
		elif "waves_idr" in i:                                                                 
			print " [+] Waves to Indonesia Rupiah            : Rp.{:,.0f}".format(harga) + "        /Waves"
		elif "str_idr" in i:
			print " [+] Stellar Lumens to Indonesia Rupiah   : Rp.{:,.0f}".format(harga) + "          /XLM"
		elif "xrp_idr" in i:                                                                   
			print " [+] Ripple to Indonesia Rupiah           : Rp.{:,.0f}".format(harga) + "         /XRP"
		elif "xzc_idr" in i:                                                                   
			print " [+] Zcoin to Indonesia Rupiah            : Rp.{:,.0f}".format(harga) + "      /XZC"
			print "\033[F"*12
		else:
			print " "

while True:
    try:
        main()
    except KeyboardInterrupt:
        print "\n\n\n\n\n\n\n\n\n\n" + " \033[1;31;40m[+] Exiting the program..." + "\n \033[1;33;40m[+] Happy Mining \033[0m"
        exit(0)