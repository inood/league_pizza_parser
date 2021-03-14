# Парсер пицц с сайта "PapaJohns"

Создание БД:

```sh
 $ python create_db.py
```

Файл настроек: _settings.py_

Запуск парсера
```sh
 $ python parser.py
```

### Схема БД

![схема](https://github.com/inood/league_pizza_parser/blob/master/images/schema.png?raw=true)

Таблица: Пицца

![пицца](https://github.com/inood/league_pizza_parser/blob/master/images/pizza_table.png?raw=true)

Таблица: Ингредиенты

![ингредиенты](https://github.com/inood/league_pizza_parser/blob/master/images/ingredients_table.png?raw=true)

Таблица: Вид теста

![вид теста](https://github.com/inood/league_pizza_parser/blob/master/images/dough_table.png?raw=true)

Таблица связи пицца-ингредиенты

![связь](https://github.com/inood/league_pizza_parser/blob/master/images/pizza-ingredients_table.png?raw=true)
