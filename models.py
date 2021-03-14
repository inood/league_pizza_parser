import json

import requests

from settings import POST_URL
from db_manager import sql


class PizzaEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Pizza):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Pizza:

    def __init__(self, name, price, size, ingredients, dough):
        self.name = name
        self.price = price
        self.size = size
        self.ingredients = ingredients
        self.dough = dough

    def add_dough(self):
        dough_row = sql.get(
            "select id, name from dough where name = ?", [self.dough]
        )
        if len(dough_row) == 0:
            dough_id = sql.insert("insert into dough (name) values (?)",
                            [self.dough])
            return dough_id
        else:
            return dough_row[0][0]

    def add_pizza(self):
        pizza_id = sql.insert(
            "insert into pizza (name, price, size, dough_id) values (?,?,?,?)",
            (self.name, self.price, self.size, self.add_dough())
        )
        return pizza_id

    def get_or_create_ingredient(self, ingredient):
        ingredient_row = sql.get(
            "select id, name from ingredients where name = ?", [ingredient]
        )
        if len(ingredient_row) == 0:
            ingredient_id = sql.insert("insert into ingredients (name) values (?)",
                             [ingredient]
                             )
            return ingredient_id
        else:
            return ingredient_row[0][0]

    def get_uuid(self, id_pizza):
        url = POST_URL
        json_data = json.dumps(self, cls=PizzaEncoder, ensure_ascii=False)
        headers = {
            'Content-Type': 'text/plain'
        }
        response = requests.request("POST", url, headers=headers,
                                    data=json_data.encode('utf-8'))
        uuid_data = json.loads(response.text)
        uuid = uuid_data['response_uuid']
        # print(f'{self.name} - {uuid}')
        sql.exec(
            "update pizza set uuid = ? where id = ?", (uuid, id_pizza)
        )

    def add(self):
        id_pizza = self.add_pizza()
        for ingredient in self.ingredients:
            id_ingredient = self.get_or_create_ingredient(ingredient)
            sql.insert(
                "insert into pizza_ingredients (pizza_id, ingredients_id) values (?,?)",
                (id_pizza, id_ingredient)
            )
        self.get_uuid(id_pizza)
