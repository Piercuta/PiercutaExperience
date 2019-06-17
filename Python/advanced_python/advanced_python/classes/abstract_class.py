
from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractAnimal(metaclass=ABCMeta):

    # abstract method
    @abstractmethod
    def make_noise(self):
        pass

    # an abstract read-only-property
    @abstractproperty
    def species(self):
        pass
  
    # abstract read/write property
    def getname(self):
        pass
    
    def setname(self, value):
        pass

    name = abstractproperty(getname, setname)
    
    # non-abstract method
    def is_alive(self):
        return True



"""
Exercise: Implement the Dog class so that the code below runs.
"""
class Dog(AbstractAnimal):
   
    def _init_(self):
        self._name =''
        self.alive = True
        self.species = 'berger allemand'

    def getname(self):
        return self._name

    def setname(self, value):
        self._name = value
    
    name = property(getname,setname)


    def make_noise(self):
        print("wof wof")

    def species(self):
        return self.species

rex = Dog()
print(rex.is_alive())
rex.make_noise()
print(rex.species())
rex.name = 'Rex'
print(rex.name)

