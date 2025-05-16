# ===== FILE: start.py =====
# Импорт библиотек для запуска Web-сервера
from http.server import HTTPServer, CGIHTTPRequestHandler

# Адрес сервера и номер порта, который он будет "слушать"
server_address = ('localhost', 80)

# Создаем объект Web-сервер
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

# Старт Web-сервера
print('start')
print('https://localhost')
httpd.serve_forever()
print('stop')

# ===== FILE: cgi-bin/basket.py =====
import json
import sqlite3
import cgi

params = cgi.FieldStorage()

goods = params.getfirst('goods','[1,2,3]')
goods = json.loads(goods)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

exp = str(-int(goods[0]))

for i in range(1, len(goods)):
    exp += ',' + str(-int(goods[i])) #'-7,-11,-5'

cursor.execute('select * from goods where id in ({});'.format(exp))
x = cursor.fetchall() #[[1,'товар',7686856, Null]]

connection.close()

html = '<table border="1px" width="300px">'

for i in x:
    html += '<tr>'
    for j in i:
        html += '<td>' + str(j) + '</td>'
    html += '</tr>'
html += '</table>'

print('Content-type: text/html\n')

print('''
<!DOCTYPE html>
<html>
<head>
    <title>Корзина</title>
    <script>
    function pay(){
        alert('Ваша оплата прошла успешно');
        }
    </script>
</head>
<body>
<h1>Корзина</h1>
<h2>Ваш выбор:</h2>''' +
html +
'''
<br>
<button onclick='pay()'>Оплатить</button>   
</body>
</html>
''')

# ===== FILE: cgi-bin/create_db.py =====
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

sql = '''
create table if not exists goods(
id integer primary key autoincrement,
name text,
price integer,
comment text
)'''

cursor.execute(sql)

cursor.execute('insert into goods(name, price) values("Самолет", 1000)')
cursor.execute('insert into goods(name, price) values("Пароход", 2000)')
cursor.execute('insert into goods(name, price) values("Снегоход", 3)')

connection.commit()

cursor.execute('select * from goods')
x = cursor.fetchall()
print(x)
connection.close()

# ===== FILE: cgi-bin/db_untils.py =====
import sqlite3
import json


def select_goods(cursor):
    cursor.execute('select * from goods')
    x = cursor.fetchall()  # [[1, 'sony', 554, NULL],[],[]]
    html = '<table border="1px" width="300px" align="center">'
    for i in x:
        html += '<tr>'
        for j in i:
            html += '<td>' + str(j) + '</td>'
        html += '<td><input type="checkbox" id="' + str(-i[0])+ '" onchange="check_box_click(this)"></td>'
        html += '</tr>'
    html += '</table>'

    y = json.dumps(html)
    print(y)


def exec_sql(sql):
    print('Content-type: text/html\n')

    connection = sqlite3.connect('data.db')
    # connection = sqlite3.connect('cgi-bin/data.db')

    cursor = connection.cursor()

    cursor.execute(sql)

    connection.commit()
    select_goods(cursor)

    connection.close()


# ===== FILE: cgi-bin/delete_goods.py =====
import cgi

params = cgi.FieldStorage()

_id = params.getfirst('id',0)

sql = 'delete from goods where id={}'.format(_id)

exec_sql(sql)

# ===== FILE: cgi-bin/getgoods.py =====
import sqlite3

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')
#connection = sqlite3.connect('cgi-bin/data.db')

cursor = connection.cursor()

select_goods(cursor)

connection.close()

# ===== FILE: cgi-bin/getstat_sql.py =====
import sqlite3
import json
import cgi

params = cgi.FieldStorage()

fun_name = params.getfirst('fun_name','')
result_id = params.getfirst('result_id', '-1')

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('select {}(price) from goods;'.format(fun_name))

x = cursor.fetchall() #[(785956,)]

connection.close()

y = json.dumps([x[0][0], result_id])
print(y)

# ===== FILE: cgi-bin/insert_goods.py =====
import cgi

params = cgi.FieldStorage()

name = params.getfirst('name','')
price = params.getfirst('price','0')

sql = 'insert into goods(name, price) values ("{}",{});'.format(name, price)

exec_sql(sql)


# ===== FILE: cgi-bin/update_goods.py =====
import cgi

params = cgi.FieldStorage()

_id = params.getfirst('id',0)
name = params.getfirst('name','')
price = params.getfirst('price','0')


sql = 'update goods set name="{}", price={} where id={}'.format(name, price, _id)

exec_sql(sql)
