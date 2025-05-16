import db_untils
import cgi

params = cgi.FieldStorage()

_id = params.getfirst('id',0)

sql = 'delete from goods where id={}'.format(_id)

db_untils.exec_sql(sql)