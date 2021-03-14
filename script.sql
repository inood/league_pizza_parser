drop table if exists ingredients;
drop table if exists pizza;
drop table if exists dough;
drop table if exists pizza_ingredients;

PRAGMA encoding = 'UTF-8';

create table ingredients
(
    id   integer not null
        primary key autoincrement,
    name varchar
);

create table dough
(
    id   integer
        constraint dough_pk
           primary key autoincrement,
    name varchar
);

create table pizza
(
    id       integer          not null
        primary key autoincrement,
    name     varchar(255)     not null,
    price    integer not null,
    size     integer not null,
    dough_id integer          not null
        references dough,
    uuid varchar
);

create index pizza_dough_id_index
    on pizza (dough_id);

create table pizza_ingredients
(
    id             integer not null
         primary key autoincrement,
    pizza_id       int
        references pizza,
    ingredients_id int
        references ingredients
);

create index pizza_ingredients_ingredients_id_index
    on pizza_ingredients (ingredients_id);

create index pizza_ingredients_pizza_id_index
    on pizza_ingredients (pizza_id);

