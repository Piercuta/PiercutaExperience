# - *- coding: utf-8 -*-
import sys
import datetime
import time
from ManageDico import *


if sys.argv[1] == "AddDefinition":
        
    my_monthly_dico = recup_dico(my_monthly_dico_filename)
    if(my_monthly_dico.datetime.month != datetime.datetime.now().month):
        my_monthly_dico = Dictionnary()
    my_full_dico = recup_dico(my_full_dico_filename)

    add_def = True
    while add_def:
        confirmation = 'n'
        while confirmation == 'n':
            definition, confirmation = def_and_confirmation()
            my_new_def = definition.split(':')
            my_monthly_dico.dictionnary[my_new_def[0]] = my_new_def[1]
            reply = input("voulez vous ajouter une définition ? y or n \n")
            if reply == "n":
                add_def = False   

    save_dico(my_monthly_dico_filename, my_monthly_dico)
    my_full_dico.add_dictionnary(my_monthly_dico.dictionnary)
    save_dico(my_full_dico_filename, my_full_dico)

if sys.argv[1] == "ShowMonthlyDefinition":
    my_monthly_dico = recup_dico(my_monthly_dico_filename)
    if len(my_monthly_dico.dictionnary) != 0:
        for key,value in my_monthly_dico.dictionnary.items():
            print (key + " : " + value + "\n\n")
            time.sleep(1)
    else:
        print("pas de définition ce mois-ci")

if sys.argv[1] == "ShowAllRegisteredDefinition":
    my_full_dico = recup_dico(my_full_dico_filename)
    if len(my_full_dico.dictionnary) != 0:
        for key,value in my_full_dico.dictionnary.items():
            print (key + " : " + value + "\n\n")
            time.sleep(1)
    else:
        print("pas de définition dans le diciotnnaire")

