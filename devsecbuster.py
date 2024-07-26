mport requests
import json
import getpass
from dependencies import banner
import os

bool = True
header = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML>
}
positivelistdenied = []
positivelistacces = []

if bool == True:
    protocol = input("what protocol does the url use? ")
    url = input("What url do you want to test? ")
    wordlist =  input("Wordlist to use? ")
    r = open(f"{wordlist}")
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
if input("Try again? ") in ["y", "yes"]:
    bool = True

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
if input("Try again? ") in ["y", "yes"]:
    bool = True

