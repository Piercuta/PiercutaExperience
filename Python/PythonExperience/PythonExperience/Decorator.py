# répondre un nom qui rime avec le prénom
import os

class Jardin:
    """Objet Jardin"""
    def __init__(self, surface = 0):
        self.surface = surface
        self.legumes = list()
        self.fruits = list()
        self._rendement = 0
    
    def _get_rendement(self):
        print("on accède à la valeur")
        return self._rendement

    def _set_rendement(self, new_value):
        print("on change la valeur")
        self._rendement = new_value

    # property
    rendement = property(_get_rendement,_set_rendement)

    def MonDeco(fonction):
       def MyFonction(self):
           print ("Bonjour ma couille")
           fonction(self)
           print ("Au Revoir ma couille")
       return MyFonction
    # decorator
    @MonDeco
    def afficherLegumes(self):
        for var in self.legumes:
            print(var)

    # special method
    def __repr__(self):
        return "légumes : {}, fruits : {}".format(self.legumes,self.fruits)
   
    def __str__(self):
        return "fruits : {}, légumes : {}".format(self.fruits,self.legumes)

    def __getattr__(self, name):
        print ("pas d'attribut nommé : " + name)

    def __setattr__(self, name, value):
        print("attribut modifié")
        object.__setattr__(self, name, value)

    def __len__(self):
        return 3000

    def __add__(self, value):
        self.surface += value

    def __eq__(self, Jardin):
        return self.surface == Jardin.surface



MonJardin = Jardin(15)
MonJardinBis = Jardin(5)
MonJardinBis + 10
print(MonJardinBis.surface)
print (MonJardin == MonJardinBis)
print (len(MonJardin))
MonJardin.legumes.append("citrouille")
MonJardin.legumes.append("tomate")
MonJardin.fruits.append("pomme")
MonJardin.surface = 5
print(MonJardin.fruits)
print(MonJardin.caca)
print(repr(MonJardin))
MonJardin.afficherLegumes()
print(MonJardin._rendement)
print(MonJardin.rendement)
MonJardin.rendement = 12
print(MonJardin.rendement)
MonJardin._rendement = 122
print(MonJardin._rendement)



#import fnmatch
#import time

##rootPath = '/'
#rootPath = "C:\\"
#pattern = '*.pdf'
 
#now = time.time()
#print (os.getcwd())
#print (rootPath)
#for root, dirs, files in os.walk(rootPath):
#    print (root , dirs, files)
#    for filename in fnmatch.filter(files, pattern):
#        print(os.path.join(root, filename))
#after = time.time()
#print (after - now)