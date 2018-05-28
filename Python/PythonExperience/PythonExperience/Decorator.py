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

