#!/usr/bin/env python

import urllib2, urllib
import json
import time
import sys, os

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
	api = "https://vip.bitcoin.co.id/api/btc_idr/ticker"
	res = urllib2.urlopen(api)
	wibu = res.read()
	halah = json.loads(wibu)
	last = halah["ticker"]
	harga = int(last["last"])
	print " [+] Bitcoin to Indonesia Rupiah : Rp.{:,.2f}".format(harga) + "/BTC"
	time.sleep(1)

while True:
    try:
        main()
    except KeyboardInterrupt:
        print "\n" + " \033[1;31;40m[+] Exiting the program..." + "\n \033[1;33;40m[+] Happy Mining \033[0m"
        sys.exit(0)