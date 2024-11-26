import requests
import json
import getpass
import os
import argparse

parser = argparse.ArgumentParser(prog="devsecbuster", description="used to find sometimes hidden directories.")
parser.add_argument("-t", "--target", required=True, type=str, help="The target ip adress")
parser.add_argument("-w", "--wordlist", required=True, type=str, help="The wordlist used")
parser.add_argument("-p", "--protocol", help="Use if the website is http", action="store_true")
args = parser.parse_args()

print(args.target)

bool = True
header = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML>"
}
positivelistdenied = []
positivelistacces = []
if bool == True:
    if args.protocol:
        protocol = "http"
    else:
        protocol = "https"
    url = args.target
    wordlist =  args.wordlist
    try:    
        r = open(f"{wordlist}")
    except:
        print("File not found or invalid.")
        bool = False
    buffer = r.read()
    buffer = buffer.split("\n")
    for i in buffer:
        urm = f"{protocol}://{url}/{i}"
        c = requests.get(urm, headers=header)
        print(f"{urm}\t\t{c.status_code}")
        if c.status_code == 403:
            positivelistdenied.append(f"{urm}\t\t{c.status_code}")
        elif c.status_code == 200:
            positivelistacces.append(f"{urm}\t\t{c.status_code}")
    print("Usable:")
    print("\tunaccesible:")
    for i in positivelistdenied:
        print(f"\t\t{i}")
    print("\taccesable:")
    for i in positivelistacces:
        print(f"\t\t{i}")
    bool = False