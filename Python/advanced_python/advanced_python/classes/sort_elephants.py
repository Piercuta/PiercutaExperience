"""
Sort elephants by trunk sizes.
"""
from pprint import pprint


class Elephant:

    def __init__(self, name, trunk_size):
        self.name = name
        self.trunk_size = trunk_size

    def __str__(self):
        return "This is Elephant {} with a trunk of size {})".format(self.name, self.trunk_size)

    def __repr__(self):
        return "{:10s} (trunk: {})".format(self.name, self.trunk_size)

    def __gt__(self, other):
        return self.trunk_size < other.trunk_size


elephants = [
    Elephant('mama', 5), 
    Elephant('baby', 1),
    Elephant('grandma', 6), 
    Elephant('daughter', 4),
    Elephant('papa', 7), 
    Elephant('son', 2), 
    Elephant('uncle', 5)
]

# use __str__ to display elephant information
print(elephants[0])

print(elephants)
# use __rpr__ to display
pprint(elephants)


print("\nAnd now the biggest elephants go first:")

# use __gt__ to sort
elephants.sort()

pprint(elephants)

# print(elephants[0])
