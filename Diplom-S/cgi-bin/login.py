import cgi
import cgitb
import sqlite3
from werkzeug.security import check_password_hash

# Включаем отладочную информацию
cgitb.enable()

# Устанавливаем правильную кодировку
print("Content-type: text/html; charset=utf-8\n")

# Получаем данные из формы
form = cgi.FieldStorage()
username = form.getfirst('username', '')
password = form.getfirst('password', '')

# Проверка, что поля заполнены
if username and password:
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        # Запрашиваем пароль для данного пользователя
        cur.execute('SELECT password FROM users WHERE username = ?', (username,))
        row = cur.fetchone()

        # Проверяем, совпадает ли пароль
        if row and check_password_hash(row[0], password):
            message = f"Добро пожаловать, {username}!"
        else:
            message = "Неверное имя пользователя или пароль."

        # Закрываем соединение с базой данных
        conn.close()

    except sqlite3.Error as e:
        message = f"Ошибка при подключении к базе данных: {e}"

else:
    message = "Не все поля заполнены."

# Выводим результат в HTML
print(f'''
<html>
<head><meta charset="utf-8"><title>Результат</title></head>
<body>
<p>{message}</p>
<a href="/index.html">Назад</a>
</body>
</html>
''')