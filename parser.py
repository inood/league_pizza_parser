import re
import json
from settings import *
from models import Pizza


def main():
    success_count = 0
    HTML = open(FILE_NAME, 'r').read()
    matches = re.search(RE_PATTERN, HTML).group(1)
    data = json.loads(matches)
    object_count = len(data)
    print(f'Найдено: {object_count} наименований пицц')

    for item in data:
        if item['category_id'] == 1:
            name = item['name']
            variants = item['variations']
            variants_count = len(variants)
            print(f'Обрабатывается {name} и {variants_count} вариантов ее исполнения\n')

            for variant in variants:
                list_ingredients = []
                ingredients = variant['include_ingredients']

                for ingredient in ingredients:
                    list_ingredients.append(ingredient['name'])

                price = variant['price']
                size = variant['size']['value']
                testo_type = variant['dough']

                try:
                    Pizza(name, price, size, list_ingredients, testo_type).add()
                    success_count += 1
                except:
                    print('ошибка обработки объекта')

    print(f'Обработка завершена\nОбработано: {success_count} записей')


if __name__ == '__main__':
    main()
