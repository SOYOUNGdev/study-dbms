from member_module import *
import hashlib  # 암호화 시, 사용하는 모듈

if __name__ == '__main__':
    # %s 와 같은 서식문자를 적으면, 알아서 형변환이 되어서 args가 들어온다.
    insert_query = "insert into tbl_member(email, password, name) \
                    values (%s, %s, %s)"

    # 암호화
    password = '7890'
    encryption = hashlib.sha256()
    encryption.update(password.encode('utf-8'))
    insert_params = ['lss12345@naver.com', encryption.hexdigest(), '이순신']
    # save(insert_query, insert_params)

    # 회원 정보 전체 조회
    find_all_query = "select email, password, name from tbl_member"
    members = find_all(find_all_query)
    print(members)

    # 아이디로 회원 1명 조회
    # 이메일은 str -> 서식문자 = %s
    find_by_id_query = "select email, password, name from tbl_member where email = %s"
    params = ['hds1234']
    # member = find_by_id(find_by_id_query, params)
    # 1명임 -> member는 리스트 형태 아니고 dict 형태
    # print(member)

    # 회원 정보 수정, email에 gmail이 포함되어 있으면, 이름 뒤에 님을 붙인다.
    # %를 하나만 작성하면 서식문자로 인식한다. 2번 작성해야 '%'라는 문자로 인식한다.
    update_query = "update tbl_member \
                    set name = concat(name, '님') \
                    where email like concat('%%', %s, '%%')"
    # update_params = ['gmail']
    # update(update_query, update_params)

    # gmail 이메일을 가진 회원 삭제
    delete_query = "delete from tbl_member where email like concat('%%', %s, '%%')"
    delete_params = ['gmail']
    # delete(delete_query, delete_params)
