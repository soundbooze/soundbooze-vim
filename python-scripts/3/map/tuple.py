from collections import namedtuple

def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name="Danny", age=31)

# Use as namedtuple
p = profile()
print(p, type(p))
print(p.name)
print(p.age)

# Use as plain tuple
p = profile()
print(p[0])
print(p[1])

# Unpack it immediatly
name, age = profile()
print(name)
print(age)
