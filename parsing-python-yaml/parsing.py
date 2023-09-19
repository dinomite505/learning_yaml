import yaml

with open("parsing.yaml", "r") as stream:
    try:
        print(yaml.safe_load(stream)) # Using safe_load to allow external documents to enter our Python application (to reduce risks)
    except yaml.YAMLError as e:
        print(e)

# 'safe_load' function doesn't support all the features (like custom data types), so you can use 'unsafe_load' function for that matter.
# Use the 'safeLoadAll' function to read a multi-document YAML file all at once.


# Running the script with 'python parsing.py' outputs:
# {'groceries': ['eggs', 'strawberries', 'milk', 'potatoes']}
#It has made a dictionary out of our YAML sequence