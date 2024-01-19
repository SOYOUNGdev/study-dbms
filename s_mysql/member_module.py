from s_mysql.connection_module import *

# cursor 객체가 있어야만 execute 할 수 있다.
# 데코레이터 함수가 실행되면서 cursor 객체를 전달 받는다.
@execute
def save(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)

# 전체 목록 조회는 params가 없다. (쿼리만 받아서 select -> 받아오기만 하면 된다.)
@execute
def find_all(cursor: Cursor, query: str) -> list:
    cursor.execute(query)
    return cursor.fetchall()

# id를 params로 받아오고 해당 정보 하나만 리턴
@execute
def find_by_id(cursor: Cursor, query: str, params: list) -> list:
    cursor.execute(query, params)
    return cursor.fetchone()

@execute
def update(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)

@execute
def delete(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)
