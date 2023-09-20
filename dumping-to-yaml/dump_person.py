import yaml


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('Dino', 29) # Creating a new person
dump_person = yaml.dump(person) # Sending in my person to YAMl
print(dump_person)

# It outputs special type (Python object) that says that it is a person in the main module
# !!python/object:__main__.Person
# age: 29
# name: Dino

# It is a custom type, not a default YAML type