import sqlite3
import db_untils

print('Content-type: text/html\n')

connection = sqlite3.connect('data.db')
#connection = sqlite3.connect('cgi-bin/data.db')

cursor = connection.cursor()

db_untils.select_goods(cursor)

connection.close()