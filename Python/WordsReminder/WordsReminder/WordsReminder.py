# - *- coding: utf-8 -*-
import sys
import datetime
import time
from ManageDico import *
import argparse
import subprocess

parser = argparse.ArgumentParser(description='This my first program with argument')
parser.add_argument('-ad','--addDefinition', action='store_true',help='add a definition')
parser.add_argument('-smd','--showMonthlyDefinition', action='store_true' ,help='show monthly definition')
parser.add_argument('-sad','--showAllDefinition', action='store_true', help='show all definition')
parser.add_argument('-gd','--generateDictionnary', nargs = 1, help='generate the txt dictionnar file')
args = parser.parse_args()

def main(args):

    #pull git command
    try:
        print (subprocess.check_output(['git','pull']))
    except:
        print("problem while pulling repo")

    if args.addDefinition:      
        my_monthly_dico = recup_dico(my_monthly_dico_filename)
        if(my_monthly_dico.datetime.month != datetime.datetime.now().month):
            my_monthly_dico = Dictionnary()
        my_full_dico = recup_dico(my_full_dico_filename)

        add_def = True
        while add_def:
            confirmation = False
            while not confirmation:
                definition, confirmation = def_and_confirmation()
            my_new_def = definition.split(':')
            my_monthly_dico.dictionnary[my_new_def[0]] = my_new_def[1]
            reply = input_checking("Voulez vous ajouter une définition ? y or n \n", r"^(y|n)$")
            if reply == "n":
                add_def = False   

        save_dico(my_monthly_dico_filename, my_monthly_dico)
        my_full_dico.add_dictionnary(my_monthly_dico.dictionnary)
        save_dico(my_full_dico_filename, my_full_dico)
       
        #commit and push changes
        try:
            print(subprocess.check_output(['git', 'commit', '-m', 'commit def', 'monthly_dictionnary']))
            print(subprocess.check_output(['git', 'commit', '-m', 'commit def', 'full_dictionnary']))
            print(subprocess.check_output(['git', 'push']))
        except:
            print ("problem while committing changes")

    if args.showMonthlyDefinition:
        my_monthly_dico = recup_dico(my_monthly_dico_filename)
        if len(my_monthly_dico.dictionnary) != 0:
            for key,value in sorted(my_monthly_dico.dictionnary.items(), key= lambda x: x[0].lower()):
                print ('{:<14}  {:<14}\n'.format( key, value))
                time.sleep(2)
        else:
            print("pas de définition ce mois-ci")

    if args.showAllDefinition:
        my_full_dico = recup_dico(my_full_dico_filename)
        if len(my_full_dico.dictionnary) != 0:
            for key,value in sorted(my_full_dico.dictionnary.items(),  key= lambda x: x[0].lower()):
                print ('{:<14}  {:<14}\n'.format( key, value))
                time.sleep(1)
        else:
            print("pas de définition dans le diciotnnaire")

    if args.generateDictionnary:
        dico_name = args.generateDictionnary[0]
        my_dico = recup_dico(dico_name)  
        with open(dico_name + '.txt', 'w') as file:
            for key,value in sorted(my_dico.dictionnary.items(), key= lambda x: x[0].lower()):
                file.write ('{:<14}  {:<14}\n'.format( key, value))
    pass

if __name__ == "__main__":
    main(args)

