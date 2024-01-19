import pymysql
from pymysql.cursors import Cursor
conn = pymysql.connect(host='13.124.179.245', user='mysql', passwd='1234', db='test', charset='utf8', autocommit=False)
cursor = conn.cursor(pymysql.cursors.DictCursor)
sql = "insert into tbl_member(email, password, name) values ('soyoungim.sy@gmail.com', '0123', '임소영')"
# cursor.execute(sql)
# console과 connection은 서로 다른 session이지만,
# commit으로 확정을 했기 때문에
# console에서 select 문으로 테이블을 확인해보면 데이터가 잘 들어가있다.
conn.commit()

sql = "select email, password, name from tbl_member"
cursor.execute(sql)

# select 쿼리를 사용하면 어떤 데이터를 가져올 때 fetch--()사용해야함
# fetchall() : 모든 결과 데이터를 가져올 때 사용
# fetchone() : 결과 중 첫번째 데이터를 가져올 때 사용
# fetchmany(n) : 결과 중 n개의 데이터를 가져올 때 사용
print(cursor.fetchall())
conn.commit()

cursor.close()
conn.close()