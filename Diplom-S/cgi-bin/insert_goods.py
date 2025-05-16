import cgi
import db_untils

params = cgi.FieldStorage()

name = params.getfirst('name','')
price = params.getfirst('price','0')

sql = 'insert into goods(name, price) values ("{}",{});'.format(name, price)

db_untils.exec_sql(sql)
