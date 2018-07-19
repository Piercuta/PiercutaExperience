# - *- coding: utf-8 -*-
import sys
import time
from ManageDico import *


if sys.argv[1] == "AddDefinition":

    monthlyDico = recup_dico()
    addDef = True
    while addDef: 
        var = input("Tapez un mot puis sa définition en les séparant de deux points : \n")
        confirmation = input("confirmez vous ce mot et sa définition ? y or n \n")
        while confirmation == 'n':
            var = input("Tapez un mot puis sa définition en les séparant de deux points \n")
            confirmation = input("confirmez vous ce mot et sa définition ? y or n \n")
        my_new_def = var.split(':')
        monthlyDico[my_new_def[0]] = my_new_def[1]
        reply = input("voulez vous ajouter une définition ? y or n \n")
        if reply == "n":
            addDef = False
    
    save_dico(monthlyDico)

if sys.argv[1] == "ShowMonthlyDefinition":
    monthlyDico = recup_dico()
    if len(monthlyDico) != 0:
        for key,value in monthlyDico.items():
            print (key + " : " + value + "\n\n")
            time.sleep(1)
    else:
        print("pas de définition ce mois-ci")

if sys.argv[1] == "ShowAllRegisteredDefinition":
    print ("option 3")

