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