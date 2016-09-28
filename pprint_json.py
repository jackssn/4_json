import json
import os
from pprint import pprint

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


def pretty_print_json(data):
    pprint(data)    # pprint не умеет выводить данные в формате json
                    # почему? у меня работает


if __name__ == '__main__':
    filepath = input('Type full path to json-file:\n')
    data = load_data(filepath)
    if data:
        pretty_print_json(data)
    else:
        print('File not found.')
