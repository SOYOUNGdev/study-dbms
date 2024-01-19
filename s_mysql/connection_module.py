import pymysql
from pymysql.cursors import Cursor

def connect():
    conn = pymysql.connect(host='3.39.224.78', user='mysql', passwd='1234', db='test', charset='utf8', autocommit=False)
    # cursor : 내가 작성한 쿼리가 직접 실행될 수 있게 해주는 객체
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

def execute(crud):
    result = None

    def manage(*args):
        nonlocal result
        # connect 함수를 쓸 떄마다 새로운 세션이 열린다.
        # connect 함수의 리턴값이 튜플 형태로 들어오기 때문에 바로 받을 수 있다.
        conn, cursor = connect()
        try:
            # 원래 함수의 매개변수에 cursor 객체와 args를 전달한다.
            # args는 입력받은 쿼리와 입력 받은 param
            result = crud(cursor, *args)
            conn.commit()
        except Exception as e:
            print(e.__str__())
            conn.rollback()

        # 오류 발생 여부와 상관없이 무조건 닫아야함.
        finally:
            # 역순으로 닫는다.(conn 오픈 -> cursor 오픈 -> cursor 클로즈 -> conn 클로즈
            cursor.close()
            conn.close()

        return result

    return manage

