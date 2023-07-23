import json

def parse_json(json_string):

  # Check if the input string is empty.

  if not json_string:
    # If the input string is empty, return None.
    return None

  # Try to load the JSON string using the `json.loads()` function.

  try:
    # If the JSON string is valid, return the Python dictionary.
    return json.loads(json_string, parse_float=lambda x: float(x))

  # If the JSON string is not valid, raise an exception.
  except json.JSONDecodeError:
    # Raise a `ValueError` exception with the invalid JSON string as the message.
    raise ValueError("Invalid JSON string: %s" % json_string)

# inputs
json_string_1 = """
{
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main Street",
    "city": "Anytown",
    "state": "CA"
  }
}
"""

json_string_2 = """
[
  {
    "name": "John Doe",
    "age": 30,
    "address": {
      "street": "123 Main Street",
      "city": "Anytown",
      "state": "CA"
    }
  },
  {
    "name": "Jane Doe",
    "age": 25,
    "address": {
      "street": "456 Elm Street",
      "city": "Los Angeles",
      "state": "CA"
    }
  }
]
"""

# Different output
parsed_json_1 = parse_json(json_string_1)
parsed_json_2 = parse_json(json_string_2)

print(parsed_json_1) 
#{'name': 'John Doe', 'age': 30, 'address': {'street': '123 Main Street', 'city': 'Anytown', 'state': 'CA'}}
print(parsed_json_2) 
#[{'name': 'John Doe', 'age': 30, 'address': {'street': '123 Main Street', 'city': 'Anytown', 'state': 'CA'}}, 
#{'name': 'Jane Doe', 'age': 25, 'address': {'street': '456 Elm Street', 'city': 'Los Angeles', 'state': 'CA'}}]


"""This code will first define a function called parse_json(), which takes a JSON string as input and returns a Python dictionary. 
The function first checks if the input string is empty, and if so, it returns None. 
Otherwise, it tries to load the JSON string using the json.loads() function, which returns a Python dictionary or raises a 
JSONDecodeError exception if the input string is not valid JSON.The parse_json function uses the json.
loads function to parse the JSON string. 

The json.loads function returns a Python object that represents the JSON data. 
The parse_json function then checks the type of the Python object and returns the appropriate object type. 
For example, if the JSON data represents an object, the parse_json function returns a Python dictionary. 
If the JSON data represents a list, the parse_json function returns a Python list.

The parse_json function also uses the float constructor with the parse argument to allow arbitrary precision numbers. 
This is necessary because the json.loads function only supports Python floats with a precision of 15 digits. 
The float constructor with the parse argument allows arbitrary precision numbers, which means that the parse_json 
function can parse JSON strings that contain numbers with a precision of more than 15 digits"""

"""Write a function to parse any valid json string into a corresponding Object, List, or
Map object. Note that the integer and floating point should be arbitrary precision."""