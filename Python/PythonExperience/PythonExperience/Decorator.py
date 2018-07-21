# répondre un nom qui rime avec le prénom
import os

class Jardin:
    """Objet Jardin"""
    def __init__(self, surface = 0):
        self.surface = surface
        self.legumes = list()
        self.fruits = list()

    def MonDeco(fonction):
       def MyFonction(self):
           print ("Bonjour ma couille")
           fonction(self)
           print ("Au Revoir ma couille")
       return MyFonction

    @MonDeco
    def afficherLegumes(self):
        for var in self.legumes:
            print(var)

   

MonJardin = Jardin(15)
MonJardin.legumes.append("citrouille")
MonJardin.legumes.append("tomate")
MonJardin.afficherLegumes()

import fnmatch
import time

#rootPath = '/'
rootPath = "C:\\"
pattern = '*.pdf'
 
now = time.time()
print (os.getcwd())
print (rootPath)
for root, dirs, files in os.walk(rootPath):
    print (root , dirs, files)
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
after = time.time()
print (after - now)