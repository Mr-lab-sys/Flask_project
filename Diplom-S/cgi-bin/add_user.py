import cgi
import cgitb
import sqlite3
from werkzeug.security import generate_password_hash

# Включаем отладочную информацию
cgitb.enable()

# Заголовок с указанием кодировки UTF-8
print("Content-type: text/html; charset=utf-8\n")

# Получаем данные из формы
form = cgi.FieldStorage()
username = form.getfirst('username', '')
password = form.getfirst('password', '')

# Проверяем, если поля формы заполнены
if username and password:
    hashed_password = generate_password_hash(password)
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        message = f"Пользователь {username} успешно зарегистрирован."
    except sqlite3.IntegrityError:
        message = f"Пользователь {username} уже существует."
    finally:
        conn.close()
else:
    message = "Не все поля заполнены."

# Отправляем HTML-ответ с сообщением
print(f'''
<html>
<head><meta charset="utf-8"><title>Результат</title></head>
<body>
<p>{message}</p>
<a href="/index.html">Назад</a>
</body>
</html>
''')