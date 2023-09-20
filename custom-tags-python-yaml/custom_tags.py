import yaml

# Defining the custom constructor function
# Calling the construct_mapping method to create Python dictionary that matches the YAML node
def constructor(loader, node):
    fields = loader.construct_mapping(node)
    return Person(**fields)

# Constructor YAML and specifying the custom tag for it
yaml.add_constructor('!Person', constructor)


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Loading this object and printing the details about the person
# 'unsafe_load' function to load YAML with custom tags
with open("custom_tags.yaml", "r") as stream:
    try:
        dict_person = yaml.unsafe_load(stream) # Storing in dict_person
        print(dict_person) # Print to show the type
        person = dict_person["person"] # Grabbing the person stored in dict_person variable by using the key "person"
        print(person.name, person.age) # Specified in YAML
    except yaml.YAMLError as e:
        print(e)
    