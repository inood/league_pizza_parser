import sqlite3

from settings import DATABASE_FILE, SQL_SCRIPT_FILE


class SqlClass:

    def __init__(self):
        try:
            self.conn = sqlite3.connect(DATABASE_FILE)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print('Произошла ошибка:', e.args[0])

    def get(self, query, bind=''):
        try:
            getAll = self.cursor.execute(query, bind)
            self.conn.commit()
            return getAll.fetchall()
        except sqlite3.Error as e:
            print('Произошла ошибка:', e.args[0])

    def insert(self, query, bind=''):
        try:
            insert = self.cursor.execute(query, bind)
            self.conn.commit()
            return insert.lastrowid
        except sqlite3.Error as e:
            print('Произошла ошибка:', e.args[0])

    def exec(self, query, bind=''):
        try:
            affectRow = self.cursor.execute(query, bind)
            self.conn.commit()
            return affectRow.rowcount
        except sqlite3.Error as e:
            print('Произошла ошибка:', e.args[0])

    def exec_script(self, script):
        try:
            affectRow = self.cursor.executescript(script)
            self.conn.commit()
            return affectRow.rowcount
        except sqlite3.Error as e:
            print('Произошла ошибка:', e.args[0])


sql = SqlClass()


def create_db():
    '''
    Создание пустой базы данных из файла скрипта
    '''
    try:
        with open(SQL_SCRIPT_FILE, 'r') as sqlite_file:
            sql_script = sqlite_file.read()

        sql.exec_script(sql_script)
        print('Скрипт SQLite успешно выполнен')

    except sqlite3.Error as error:
        print(f'Ошибка создания БД: {error}')
