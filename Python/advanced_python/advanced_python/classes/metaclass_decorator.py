"""
Metaclasses: Crazy stuff you can do with classes.

Instructions: 
1) Run the code
2) Admire what is happening
3) Don't try this at work, unless you have excluded all alternatives
   and you really know what you are doing 
   and you have talked to at least one sane person.
"""

class monkeymeta(type):

    def __new__(mcs, name, bases, dict):
        cls = type.__new__(mcs, name, bases, dict)

        def wrapper(*args):
            instance = cls('monkeys')
            instance.monkeys = args[0]
            return instance

        return wrapper


class CrazyMonkeys(metaclass=monkeymeta):
    """
    Class with monkeys appearing out of nowhere
    """
    def __init__(self, name):
        self.name = name

# class Foo():
#     pass

# x = Foo()
# print(type(x))
# print(type(Foo))
# Man = type('Man', (), {})

# pierre = Man()
# print (pierre)
# print (type(pierre))

# def display_age(obj):
#     print('age = ', obj.age)

# Child = type('Child', (Man,), {'age':100, 'display_age':display_age})
# print(Child)
# print(Child.display_age(Child))
# class Foo():
#     pass

# def new(cls):
#     x=object.__new__(cls)
#     x.pierre = 'yes'
#     return x
# Foo.__new__ = new
# f = Foo()
# print(f.pierre)

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

class Foo(metaclass=MyMeta):
    pass
obj1 = Foo()
print (obj1.attr)