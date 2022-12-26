import random
import phonenumbers
import string
from phonenumbers import geocoder, carrier,timezone
from pystyle import Center
import fade
import os
from colorama import Fore

banner = """

                                                                    ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
                                                                    ▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                                                                    ▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███      ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
                                                                    ▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                                                                    ▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
                                                                    ▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                                                                    ░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                                                                    ░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░      ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
                                                                            ░  ░  ░    ░ ░           ░    ░  ░   ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                                                                                                ░                       ░                               
"""

def main():
    os.system('clear || cls')
    os.system("title Phone Checker By LDZ#9999")
    pressenter = input("Press enter to continue\n idée de LDZ#9999 et Whaxor#1234")
    os.system('clear || cls')
    faded_text = fade.blackwhite(banner)
    print(faded_text)
    while True:
        phone = ('').join(random.choices(string.digits, k=9))
        num=f'+33{phone}'
        number = phonenumbers.parse(num)
        valid = phonenumbers.is_valid_number(number)
        pays = geocoder.description_for_number(number,'fr')
        opera = carrier.name_for_number(number,'fr')
        if valid == True and opera != "":
            print(f"                                                              {Fore.LIGHTGREEN_EX}>{Fore.LIGHTWHITE_EX} Numero{Fore.LIGHTCYAN_EX} :{Fore.LIGHTMAGENTA_EX} {num}{Fore.LIGHTWHITE_EX} |{Fore.LIGHTBLACK_EX} Country{Fore.LIGHTCYAN_EX} :{Fore.LIGHTMAGENTA_EX} {pays}{Fore.LIGHTWHITE_EX} |{Fore.LIGHTBLACK_EX} Operator{Fore.LIGHTCYAN_EX} :{Fore.LIGHTMAGENTA_EX} {opera}")
            with open("phoneonly.txt", "a") as save:
                save.write(f"{num} \n")
            with open("phone_and_informations.txt", "a") as save:
                save.write(f"{num} | Country : {pays} | Operator : {opera}\n")
main()
