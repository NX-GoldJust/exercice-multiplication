from colorama import * 
from colorama import init as colorama_init
from random import randint, choice
colorama_init(autoreset=True)
import os
b = Back.WHITE
print(b+Fore.RED+"Programme réalisé Par GoldJust")
t = input(b+Fore.BLUE+"Mettez les tables de multiplications que vous voulez révisé séparé les par un / comme ceci: 1/2 etc"+Back.RESET+"\n\n")
import time
tab = t.split("/")
[int(a) for a in tab]
while True:
    os.system("cls")
    


    pr = int(randint(1, 10))
    d = int(choice(tab))

    result = pr*d
    
    sarep = input(f"Combien fait {str(pr)}x{str(d)} ?\n")
    if int(sarep) == int(result):
        print("Bravo c'est la bonne réponse")
    else:
        print(f"Non, pas {str(sarep)} mais plutot {str(result)}")
    time.sleep(3)
    
