import cgi
import db_untils

params = cgi.FieldStorage()

_id = params.getfirst('id',0)
name = params.getfirst('name','')
price = params.getfirst('price','0')


sql = 'update goods set name="{}", price={} where id={}'.format(name, price, _id)

db_untils.exec_sql(sql)