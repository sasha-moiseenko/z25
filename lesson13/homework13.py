"""
Описать для каждой таблицы из домашки(lesson12) класс,
который позволяет взаимодействовать с конткретной таблицей
Пример:
class User:
    ...
    def get_users(user_id=None, username=None):
        ...
    def create_users(*users_list):
        ...
class Test:
    ...
и тд
"""

import psycopg2


class GetDBData:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        connection = psycopg2.connect(f'postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}')
        return connection


class Users(GetDBData):
    def __init__(self, dbname, user, password, host, port):
        super().__init__(dbname, user, password, host, port)
        self.db = GetDBData.connect(self)
        self.cursor = self.db.cursor()

    def get_user(self, _id=None, username=None):
        if _id:
            self.cursor.execute(f'SELECT * FROM app_users WHERE id = {_id};')
            result = self.cursor.fetchall()
        if username:
            self.cursor.execute(f'SELECT * FROM app_users WHERE username = {username};')
            result = self.cursor.fetchall()

    def insert_users(self, *users_list):
        for user in users_list:
            self.cursor.execute(f'''INSERT INTO app_users (username) VALUES ('{user}');''')
            self.db.commit()


if __name__ == '__main__':
    # db_ = GetDBData('postgres', 'postgres', '1234', 'localhost', '5432')
    # db_.connect()
    us = Users('postgres', 'postgres', '1234', 'localhost', '5432')
    print(us.insert_users('sasha', 'artsiom'))

