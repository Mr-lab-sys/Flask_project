import json
import sqlite3
import cgi
import html

params = cgi.FieldStorage()

goods = params.getfirst('goods','[1,2,3]')
goods = json.loads(goods)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

exp = str(-int(goods[0]))

for i in range(1, len(goods)):
    exp += ',' + str(-int(goods[i]))

cursor.execute('select * from goods where id in ({});'.format(exp))
x = cursor.fetchall()

connection.close()

html_table = '<table border="1px" width="300px">'
for i in x:
    html_table += '<tr>'
    for j in i:
        html_table += '<td>' + html.escape(str(j)) + '</td>'
    html_table += '</tr>'
html_table += '</table>'
print('Content-Type: text/html; charset=utf-8\n')

print(f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Корзина</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script>
        function pay() {{
            alert('Ваша оплата прошла успешно');
        }}
    </script>
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h1 class="mb-4">Корзина</h1>
        <h4>Ваш выбор:</h4>
        <div class="table-responsive mb-4">
            {html_table}
        </div>
        <button class="btn btn-success" onclick="pay()">Оплатить</button>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''')
