import re
import json
from settings import *
from models import Pizza


def main():
    HTML = open(FILE_NAME, 'r').read()
    pattern = RE_PATTERN
    matches = re.search(pattern, HTML)
    json_data = matches.group(1)
    data = json.loads(json_data)

    for item in data:
        if item['category_id'] == 1:
            name = item['name']
            variants = item['variations']

            for variant in variants:
                list_ingredients = []
                ingredients = variant['include_ingredients']
                for ingredient in ingredients:
                    list_ingredients.append(ingredient['name'])
                price = variant['price']
                size = variant['size']['value']
                testo_type = variant['dough']
                Pizza(name, price, size, list_ingredients, testo_type).add()


if __name__ == '__main__':
    main()
