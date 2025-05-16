import sqlite3
from werkzeug.security import generate_password_hash

# Подключаемся к базе данных
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Создаем таблицу goods, если ее нет
sql_goods = '''
create table if not exists goods(
id integer primary key autoincrement,
name text,
price integer,
comment text
)'''

cursor.execute(sql_goods)

# Вставляем данные в таблицу goods
cursor.execute('insert into goods(name, price) values("Самолет", 1000)')
cursor.execute('insert into goods(name, price) values("Пароход", 2000)')
cursor.execute('insert into goods(name, price) values("Снегоход", 3)')

# Создаем таблицу users, если ее нет
sql_users = '''
create table if not exists users(
id integer primary key autoincrement,
username text not null unique,
password text not null
)'''

cursor.execute(sql_users)

# Пример добавления пользователя
username = "test_user"
password = "password123"
hashed_password = generate_password_hash(password)

# Вставляем данные в таблицу users
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

# Фиксируем изменения в базе данных
connection.commit()

# Выполняем запрос, чтобы убедиться, что все данные вставлены правильно
cursor.execute('select * from goods')
goods = cursor.fetchall()
print("Товары:", goods)

cursor.execute('select * from users')
users = cursor.fetchall()
print("Пользователи:", users)

# Закрываем соединение с базой данных
connection.close()