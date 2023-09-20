# loading and debugging YAML file
import yaml

# Importing pyyaml library
with open("debugging.yaml", "r") as stream:
    try:
        file = yaml.safe_load(stream) # parses content of yaml file and load into Python dictionary
        choices = file["config"]["choices"] # extracts value associated with "choices"
        code = file["config"]["options"][2] # extracts the third element [2] from "options"
        print(choices) # print(code) to se how octal value value impacts your input
    except yaml.YAMLError as e:
        print(e)
