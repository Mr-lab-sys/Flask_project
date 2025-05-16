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
