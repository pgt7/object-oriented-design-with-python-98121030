# define a Person class
class Person:

    # define a constructor
    def __init__(self, name):
        self.name = name


# instanciation
name = input("Enter a name = ")
person = Person(name)

print(person.__dict__)

# add age parameter to Person instance
age = input("Enter an age = ")
person.__dict__['age'] = age

print(person.__dict__)