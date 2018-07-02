class Garden:
    """Object modeling a garden"""
    def __init__(self, surface, soilType, location):
        self.surface = surface
        self.vegetables = list(tuple())
        self.fruits = list(tuple())

    def DisplayGardenContent(self):
        for var in self.vegetables:
            print ("there are " +  str(var[0]) + " of " +  var[1].name)

from enum import Enum
class VegType(Enum):
    Feuille = 2
    Racine = 1
    Fruit = 4
    Fleur = 3

class VegFamilly(Enum):
    Alliacees = 1
    Apiacees = 2
    Asteracees = 3
    Brassicacees = 4
    Chenopodiacees = 5
    Curcubitacees = 6
    Solanacees = 7
    Valerianacees = 8
    Fabacees = 9
    Lamiacees = 10
    Poacees = 11
    Polygonacees = 12

class Vegetable:
    """object representing a vegetable"""
    def __init__(self, name, vegType, vegFamilly):
        self.name = name
        self.vegType = vegType
        self.vegFamilly = vegFamilly

    def DisplayVegInformation(self):
        print ("My Vegetable is a : " + self.name + "\nThe VegType is a " + self.vegType.name+ "\nThe VegFamilly is from " + self.vegFamilly.name)

MonJardin = Garden(100, "clay", "brittany")

Tomate = Vegetable("Tomate", VegType.Fruit, VegFamilly.Solanacees)
Aubergine = Vegetable("Aubergine", VegType.Fruit, VegFamilly.Solanacees)
Courgette = Vegetable("Courgette", VegType.Fruit, VegFamilly.Curcubitacees)
Tomate.DisplayVegInformation()

MonJardin.vegetables.append((5, Courgette))
MonJardin.vegetables.append((10 ,Tomate))
MonJardin.DisplayGardenContent()


