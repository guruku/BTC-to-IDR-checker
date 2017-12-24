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
print " \033[1;37;40m[+] Code by : Bayu Fedra                                                                  [+]\033[0m"
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
			"https://vip.bitcoin.co.id/api/xlm_btc/ticker",
			"https://vip.bitcoin.co.id/api/xrp_idr/ticker",
			"https://vip.bitcoin.co.id/api/xzc_idr/ticker",] #XLM to IDR API is Invalid
	#BTC
	api_btc = "https://vip.bitcoin.co.id/api/btc_idr/ticker"
	res_btc = urllib2.urlopen(api_btc)
	wibu_btc = res_btc.read()
	halah_btc = json.loads(wibu_btc)
	last_btc = halah_btc["ticker"]
	harga_btc = int(last_btc["last"])

	#BCH
	api_bch = "https://vip.bitcoin.co.id/api/bch_idr/ticker"
	res_bch = urllib2.urlopen(api_bch)
	wibu_bch = res_bch.read()
	halah_bch = json.loads(wibu_bch)
	last_bch = halah_bch["ticker"]
	harga_bch = int(last_bch["last"])

	#BTG
	api_btg = "https://vip.bitcoin.co.id/api/btg_idr/ticker"
	res_btg = urllib2.urlopen(api_btg)
	wibu_btg = res_btg.read()
	halah_btg = json.loads(wibu_btg)
	last_btg = halah_btg["ticker"]
	harga_btg = int(last_btg["last"])
	
	#ETH
	api_eth = "https://vip.bitcoin.co.id/api/eth_idr/ticker"
	res_eth = urllib2.urlopen(api_eth)
	wibu_eth = res_eth.read()
	halah_eth = json.loads(wibu_eth)
	last_eth = halah_eth["ticker"]
	harga_eth = int(last_eth["last"])
	
	#ETC
	api_etc = "https://vip.bitcoin.co.id/api/etc_idr/ticker"
	res_etc = urllib2.urlopen(api_etc)
	wibu_etc = res_etc.read()
	halah_etc = json.loads(wibu_etc)
	last_etc = halah_etc["ticker"]
	harga_etc = int(last_etc["last"])
	
	#LTC
	api_ltc = "https://vip.bitcoin.co.id/api/ltc_idr/ticker"
	res_ltc = urllib2.urlopen(api_ltc)
	wibu_ltc = res_ltc.read()
	halah_ltc = json.loads(wibu_ltc)
	last_ltc = halah_ltc["ticker"]
	harga_ltc = int(last_ltc["last"])
	
	#NXT
	api_nxt = "https://vip.bitcoin.co.id/api/nxt_idr/ticker"
	res_nxt = urllib2.urlopen(api_nxt)
	wibu_nxt = res_nxt.read()
	halah_nxt = json.loads(wibu_nxt)
	last_nxt = halah_nxt["ticker"]
	harga_nxt = int(last_nxt["last"])
	
	#Waves
	api_waves = "https://vip.bitcoin.co.id/api/waves_idr/ticker"
	res_waves = urllib2.urlopen(api_waves)
	wibu_waves = res_waves.read()
	halah_waves = json.loads(wibu_waves)
	last_waves = halah_waves["ticker"]
	harga_waves = int(last_waves["last"])
	
	#XLM -> API Intterupt
	
	#XRP
	api_xrp = "https://vip.bitcoin.co.id/api/xrp_idr/ticker"
	res_xrp = urllib2.urlopen(api_xrp)
	wibu_xrp = res_xrp.read()
	halah_xrp = json.loads(wibu_xrp)
	last_xrp = halah_xrp["ticker"]
	harga_xrp = int(last_xrp["last"])

	#XZC
	api_xzc = "https://vip.bitcoin.co.id/api/xzc_idr/ticker"
	res_xzc = urllib2.urlopen(api_xzc)
	wibu_xzc = res_xzc.read()
	halah_xzc = json.loads(wibu_xzc)
	last_xzc = halah_xzc["ticker"]
	harga_xzc = int(last_xzc["last"])
	
	print " [+] Bitcoin to Indonesia Rupiah          : Rp.{:,.0f}".format(harga_btc) + " /BTC"
	print " [+] Bitcoin Cash to Indonesia Rupiah     : Rp.{:,.0f}".format(harga_bch) + "  /BCH"
	print " [+] Bitcoin Gold to Indonesia Rupiah     : Rp.{:,.0f}".format(harga_btg) + "   /BTG"
	print " [+] Ethereum to Indonesia Rupiah         : Rp.{:,.0f}".format(harga_eth) + "  /ETH"
	print " [+] Ethereum Classic to Indonesia Rupiah : Rp.{:,.0f}".format(harga_etc) + "     /ETC"
	print " [+] Litecoin to Indonesia Rupiah         : Rp.{:,.0f}".format(harga_ltc) + "   /LTC"
	print " [+] NXT to Indonesia Rupiah              : Rp.{:,.0f}".format(harga_nxt) + "      /NXT"
	print " [+] Waves to Indonesia Rupiah            : Rp.{:,.0f}".format(harga_waves) + "     /Waves"
	print " [+] Ripple to Indonesia Rupiah           : Rp.{:,.0f}".format(harga_xrp) + "      /XRP"
	print " [+] Zcoin to Indonesia Rupiah            : Rp.{:,.0f}".format(harga_xzc) + "   /XZC"
	print "\033[F"*11

while True:
    try:
        main()
    except KeyboardInterrupt:
        print "\n\n\n\n\n\n\n\n\n\n" + " \033[1;31;40m[+] Exiting the program..." + "\n \033[1;33;40m[+] Happy Mining \033[0m"
        exit(0)