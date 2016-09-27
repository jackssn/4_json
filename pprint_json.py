import json
import os
from pprint import pprint

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    filepath = input('Type full path to json-file:\n')
    data = load_data(filepath)
    pretty_print_json(data)
