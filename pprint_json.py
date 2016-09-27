import json
import os
from pprint import pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as f:
        return json.load(f)


def pretty_print_json(data):
    return pprint(data)


if __name__ == '__main__':
    #filepath = input('Type full path to json-file:\n')
    filepath = '../drinks.json'
    data = load_data(filepath)
    print(pretty_print_json(data))
