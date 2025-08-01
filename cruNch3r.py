#!/usr/bin/python3
import signal
import argparse
import textwrap
import threading
import requests as rq
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from alive_progress import alive_bar
from urllib3.exceptions import InsecureRequestWarning

# Execption 
rq.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Get arguments
parser = argparse.ArgumentParser(
    prog='cruNch3r.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent(r'''\
-------------------------------------------------------------
------------ | Mass scan for check live host | --------------
-------------------------------------------------------------
                     __     _     _____
  ___ _ __ _   _  /\ \ \___| |__ |___ / _ __
 / __| '__| | | |/  \/ / __| '_ \  |_ \| '__|
| (__| |  | |_| / /\  / (__| | | |___) | |
 \___|_|   \__,_\_\ \/ \___|_| |_|____/|_|
                                        V 0.1
          ---------------------|by h4rith.com
-------------------------------------------------------------'''),
    usage='python3 %(prog)s -uL [URLList]',
    epilog='---------------- Script from h4rithd.com ----------------')

parser._action_groups.pop()
required = parser.add_argument_group('[!] Required arguments')
required.add_argument('-u','--urllist', metavar='', required=True, help='Target URLs file')
required.add_argument('-to','--timeout', metavar='', type=int, help='Set timeout (Default is 3)')
args = parser.parse_args()

#Style
class style():
    HEADER = '\033[95m'
    BLINK = '\33[5m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BOLD  = '\033[1m'
    RESET = '\033[0m'
    RED = '\033[31m'

# Get URL list
with open(args.urllist) as f:
  url_list = [x.rstrip() for x in f]

# Set Timeout
if args.timeout is not None:
    t_out = args.timeout
else:
    t_out = 3

# Table Settings
table = PrettyTable()
table.title = "-----------| cruNch3r v0.1 :: by h4rithd.com |-----------"
table.field_names = ['URL', 'Status', 'Title']
table.align['URL'] = 'l'
table.align['Title'] = 'l'
table.sortby = 'Status'

def quit(signal, frame):
    print (style.RED+"----------| Programe stoped due to press CTRL + C "+style.RESET)
    print("Bye!")
    raise SystemExit

def run():
   with alive_bar(len(url_list),bar='blocks') as bar:
      for url in (url_list):
         try:
            req = rq.get(url,timeout=t_out,verify=False)
            soup = BeautifulSoup(req.text, 'html.parser')
            if (soup.title is not None):
               table.add_row([url,req.status_code,soup.title.text])
            else:
               table.add_row([url,req.status_code,'Title Not Found'])
            bar()
         except rq.exceptions.ConnectionError as errc:
            print (style.RED+"-----------------------------------------------------------------"+style.RESET)
            print (style.RED+"[!] Error Connecting: Check your internet connection!!"+style.RESET)
            print (style.RED+"-----------------------------------------------------------------"+style.RESET)
         except rq.exceptions.Timeout as errt:
            print (style.RED+"-----------------------------------------------------------------"+style.RESET)
            print (style.YELLOW+"[!] Timeout Error: Max timeout = 3; use -to flag to increase"+style.RESET)
            print (style.RED+"-----------------------------------------------------------------"+style.RESET)
         except rq.exceptions.RequestException as err:
            print (style.RED+"-----------------------------------------------------------------"+style.RESET)
            print (style.RED+"[!] OOps: Something Else",err+style.RESET)
            print (style.RED+"-----------------------------------------------------------------"+style.RESET)
            raise SystemExit
   print("\n\n-----------| cruNch3r v0.1 :: by h4rithd.com |-----------")
   print(table)
   print("\n\n")
   raise SystemExit

# Main
if __name__ == '__main__':
   signal.signal(signal.SIGINT, quit)
   run_thread = threading.Thread(target=run)
   run_thread.start()
