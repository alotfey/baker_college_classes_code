"""Lab 5 part 2"""

import json

# Write a Python program to convert JSON data to Python object.
# Sample JSON data
json_data = """
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
"""


# function to convert JSON data to Python object
def json_to_python(json_data):
    return json.loads(json_data)


# Convert JSON data to Python object
python_obj = json_to_python(json_data)
print(f"Python object: {python_obj}")
print(type(python_obj))

# Write a Python program to convert Python object to JSON data.

coverted_json = json.dumps(python_obj)
print(f"Converted JSON data: {coverted_json}")
print(type(coverted_json))

# Write a Python program to convert Python objects into JSON strings. Print all the values.
dataValues = {
    "name": "Ahmed",
    "age": 36,
    "state": "Michigan",
    "is_student": True,
    "courses": ["Big Data analyis", "Mathematics", "Physics"],
    "address": {
        "street": "123 main st",
        "city": "Canton",
    },
}


# convert Python object to JSON string
def python_to_json(data):
    return json.dumps(data, indent=4)


# Convert Python object to JSON string
json_string = python_to_json(dataValues)
print(f"JSON string: {json_string}")
print(type(json_string))

# Print each value in the original dictionary

for key, value in dataValues.items():
    print(f"{key}: {value}")
# Write a Python program to convert Python dictionary object (sort by key) to
# JSON data. Print the object members with indent level 4.
def python_dict_to_json(data):
    return json.dumps(data, indent=4, sort_keys=True)
# Convert Python dictionary to JSON data
json_data_sorted = python_dict_to_json(dataValues)
print(f"Sorted JSON data: {json_data_sorted}")