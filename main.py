import requests
import random
import string
import time
import os
import colorama
from colorama import Fore
import sys

print(r"""   _  ___ __              _____                      __          
  / |/ (_) /________     / ___/__ ___  ___ _______ _/ /____  ____
 /    / / __/ __/ _ \   / (_ / -_) _ \/ -_) __/ _ `/ __/ _ \/ __/
/_/|_/_/\__/_/  \___/   \___/\__/_//_/\__/_/  \_,_/\__/\___/_/   
                                                                 """)
print(Fore.WHITE + "\t \t \t \t \t \t \t \t Developer: https://github.com/daarkfight00 ✔ \n ")
print(Fore.GREEN + "Questo software e' stato realizzato solo per scopo illustrativo, percio' non sono responsabile delle azioni che chiunque possa compiere con questo programma...")
print(Fore.CYAN  +"\nThis software is for illustrative purposes only, so I am not responsible for the actions that anyone can perform with this program...")
messaggio = Fore.RED +"\n \n \t \t \t \t \t Please Don't Use It For illegal Activity  [X]\n \n"
for char in messaggio:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
input(Fore.WHITE  +"Premere un tasto per continuare")
os.system("cls")

time.sleep(2)
print("Generating Nitro Links")
time.sleep(0.3)

num = int(input('How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered the high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid ✅ | {nitro} ")
            break
        else:
            print(f" Invalid ❌ | {nitro} ")

input("\nYou have generated, Now press enter to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you got no luck, generate 20 million codes for luck or else.")