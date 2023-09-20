import yaml

# Creating a list containing 9 dictionaries (mappings)
persons = [{'name': 'Dino','age': 29}, 
           {'name': 'Claire', 'age': 27},
           {'name': 'Anna', 'age': 36},
           {'name': 'Gunther', 'age': 56},
           {'name': 'Sascha', 'age': 33},
           {'name': 'Lucas', 'age': 31},
           {'name': 'Ronald', 'age': 42},
           {'name': 'Beatrice', 'age': 22},
           {'name': 'Maxi', 'age': 26}]

# Sorts 'persons' alphabetically by name
persons_sorted_by_name = sorted(persons, key=lambda x: x['name'])

# Sort persons by age
persons_sorted_by_age = sorted(persons, key=lambda x: x['age'])

# Adding in my list of persons sorted by name
print("Sorted by Name")
print(yaml.dump(persons_sorted_by_name))

# Adding to my list of persons sorted by age
print("Sorted by Age:")
print(yaml.dump(persons_sorted_by_age))


# It has created YAML and turned our Python list into two separate YAML sequences 
# containing nine (9) mappings each and sorting them them alphabetically and by age 

