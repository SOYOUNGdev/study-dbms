from crud_module import *
from field_trip import FieldTrip
from post import Post
from owner import Owner
import hashlib

from s_mysql.task.mysql_with_api.crud_module import find_all_by

if __name__ == '__main__':
    # 학부모 정보 추가
    # save_many_query = "insert into tbl_parent(name, age, gender, address, phone) \
    #                    values(%s, %s, %s, %s, %s)"
    # save_many_params = (
    #     ('한동석', 20, '남자', '경기도 남양주', '01012341234'),
    #     ('홍길동', 30, '여자', '서울시 강남구', '01033333333'),
    #     ('이순신', 40, '선택안함', '경기도 남양주', '01055555555')
    # )
    # save_many(save_many_query, save_many_params)

    # 아이 추가
    # find_by_id_query = "select id, name, age, gender, address, phone from tbl_parent where id = %s"
    # find_by_id_params = 1,
    # find_by_id_params = 3,
    # find_by_id_params = 2,
    # parent = find_by_id(find_by_id_query, find_by_id_params)
    # parent_id = parent.get("id")

    # save_many_query = "insert into tbl_child(name, age, gender, parent_id) \
    #               values(%s, %s, %s, %s)"
    # save_many_params = (
    #     ('둘리', 4, '남자', parent_id),
    #     ('또치', 9, '여자', parent_id),
    # )
    # save_many_params = (
    #     ('도너', 4, '남자', parent_id),
    # )
    # save_many_params = (
    #     ('마이콜', 11, '선택안함', parent_id),
    # )
    # save_many(save_many_query, save_many_params)

    # 체험학습 추가
    # save_many_query = "insert into tbl_field_trip (title, content, count) \
    #                    values(%s, %s, %s)"
    # save_many_params = (
    #     ('테스트 제목1', '테스트 내용1', 10),
    #     ('테스트 제목2', '테스트 내용2', 50),
    #     ('테스트 제목3', '테스트 내용3', 40),
    #     ('테스트 제목4', '테스트 내용4', 100)
    # )
    # save_many(save_many_query, save_many_params)

    # 첨부파일 추가
    # save_query = "insert into tbl_file(file_path, file_name) \
    #               values(%s, %s)"
    # save_params = ('2024/01/18', 'img002.png')
    # save(save_query, save_params)

    # find_all_query = "select id from tbl_file order by id desc"
    # file_id = find_all(find_all_query)[0].get("id")
    #
    # find_all_query = "select id from tbl_field_trip order by id desc"
    # field_trip_id = find_all(find_all_query)[0].get("id")
    #
    # save_query = "insert into tbl_field_trip_file(id, field_trip_id) \
    #               values (%s, %s)"
    # save_params = file_id, field_trip_id

    # save(save_query, save_params)

    # 체험학습 상세보기
    # find_by_id_query = "select id, title, content, count \
    #                     from tbl_field_trip \
    #                     where id = %s"
    # find_by_id_params = 4,
    # field_trip = find_by_id(find_by_id_query, find_by_id_params)
    #
    # find_all_by_query = "select f.id, f.file_path, f.file_name \
    #                     from tbl_file f join tbl_field_trip_file ft \
    #                     on ft.field_trip_id = %s and f.id = ft.id"
    #
    # files = find_all_by(find_all_by_query, find_by_id_params)
    #
    # field_trip = FieldTrip(field_trip.get("id"), field_trip.get("title"), field_trip.get("content"), field_trip.get("count"), *files)
    # print(field_trip.__dict__)
    # print(field_trip.get_full_path())

    # 회원가입
    ## save_query = "insert into tbl_user(user_id, password, name, address) \
    ##               values(%s, hex(aes_encrypt(%s, 'hello mysql')), %s, %s)"
    # save_query = "insert into tbl_user(user_id, password, name, address) \
    #               values(%s, %s, %s, %s)"
    # password = hashlib.sha256()
    # password.update('5555'.encode('utf-8'))
    # password = password.hexdigest()
    #
    # save_params = 'hgd9999', password, '홍길동', '서울시 강남구'
    # save(save_query, save_params)

    # 게시글 작성
    # find_by_id_query = "select id from tbl_user where id = %s"
    # find_by_params = 1,
    # user = find_by_id(find_by_id_query,find_by_params)
    #
    # save_query = "insert into tbl_post (title, content, user_id) \
    #               values (%s, %s, %s)"
    # save_params = '테스트 제목1', '테스트 내용1', user.get("id")
    # save(save_query,save_params)

    # 게시글 목록
    # find_all_query = "select p.id, title, content, create_date, u.name \
    #                   from tbl_user u join tbl_post p\
    #                   on u.id = p.user_id\
    #                   order by id desc"
    # posts = find_all(find_all_query)
    # for post in posts:
    #     print(post)

    # 게시글 상세보기
    # find_by_id_query = "select id from tbl_post where id = %s"
    # find_by_id_params = 1,
    # post = find_by_id(find_by_id_query, find_by_id_params)
    # post_id = post.get("id")
    #
    # find_by_id_query = "select p.id, title, content, create_date, u.name \
    #                     from tbl_user u join tbl_post p \
    #                     on u.id = p.user_id\
    #                     where p.id = %s"
    # find_by_id_params = post_id,
    # post = find_by_id(find_by_id_query, find_by_id_params)

    # 댓글 목록
    # find_all_by_query = "select r.id, name, content\
    #                from tbl_user u join tbl_reply r \
    #                on r.post_id = %s and u.id = r.user_id"
    #
    # find_all_by_params = post.get("id"),
    # replies = find_all_by(find_all_by_query, find_all_by_params)
    #
    # post = Post(post.get("id"), post.get("title"), post.get("content"), post.get("create_date"), post.get("name"), replies)
    # print(post.__dict__)

    # 댓글 작성
    # find_by_id_query = "select id from tbl_user where id = %s"
    # find_by_id_params = 2,
    # user = find_by_id(find_by_id_query, find_by_id_params)
    # user_id = user.get("id")
    #
    # find_by_id_query = "select id from tbl_post where id = %s"
    # find_by_id_params = 1,
    # post = find_by_id(find_by_id_query, find_by_id_params)
    # post_id = post.get("id")
    #
    # save_many_query = "insert into tbl_reply (content, user_id, post_id) \
    #                    values (%s, %s, %s)"
    # save_many_params = (
    #     ('댓글 테스트1', user_id, post_id),
    #     ('댓글 테스트2', user_id, post_id),
    # )
    # save_many(save_many_query, save_many_params)

    # # 보호자 추가
    # save_many_query = "insert into tbl_owner(name, age, phone, address) \
    #                    values (%s, %s, %s, %s)"
    # save_many_params = (
    #     ('서경덕', '20', '01012345678', '경기도 수원시'),
    #     ('홍길동', '30', '01056781234', '경기도 용인시'),
    #     ('이순신', '40', '01011111111', '서울시 강남구'),
    # )
    # # save_many(save_many_query, save_many_params)
    #
    # # 반려동물 추가
    # find_by_id_query = "select id from tbl_owner where id = %s"
    # find_by_id_params = 3,
    # owner = find_by_id(find_by_id_query, find_by_id_params)
    # owner_id = owner.get("id")
    #
    # save_many_query = "insert into tbl_pet(name, ill_name, age, weight, owner_id) \
    #                    values (%s, %s, %s, %s, %s)"
    # save_many_params = (
    #     # ('둘리', '감기', '10', 4.5, owner_id),
    #     # ('초코', '독감', '11', 3.20, owner_id),
    #     # ('또치', '골절', '12', 9, '2'),
    #     # ('도우너', '기생충 감염', '8', '8.23', None),
    #     ('뭉치', '감기', '14', '9.86', '3'),
    #     # ('설이', '감기', '15', '7.44', None),
    # )
    #
    # # save_many(save_many_query, save_many_params)
    #
    # # 전체 목록
    # find_all_query = "select id, name, age, phone, address from tbl_owner"
    # owners = find_all(find_all_query)
    # owners_with_pets = []
    # for owner in owners:
    #     find_all_by_query = "select id, name, ill_name, age, weight, owner_id from tbl_pet where owner_id = %s"
    #     find_all_by_params = owner.get("id"),
    #     pets = find_all_by(find_all_by_query, find_all_by_params)
    #     owners_with_pets.append(Owner(owner.get("id"), owner.get("name"), owner.get("age"), owner.get("phone"), owner.get("address"), pets))
    #
    # for owner in owners_with_pets:
    #     print(owner.__dict__)



    # 숙제
    # 회원가입
    # save_query = "insert into tbl_client(email, password, name) values(%s, %s, %s)"
    #
    # password = '5678'
    # encryption = hashlib.sha256()
    # encryption.update(password.encode('utf-8'))
    # password = encryption.hexdigest()
    #
    # save_params = ['user1@gmail.com', password, '회원1']
    # save(save_query, save_params)

    # 회사 추가
    # save_query = "insert into tbl_office(name, location) values(%s, %s)"
    # save_params = '현대자동차', '삼성동'
    # save(save_query, save_params)

    # 회의실 추가
    # # 1번 회사에 있는 회의실 정보 조회
    # find_all_by_query = "select * from tbl_conference_room where office_id = %s"
    # find_all_by_params = 1,
    # conference_rooms = find_all_by(find_all_by_query, find_all_by_params)
    # for conference_room in conference_rooms:
    #     print(f"{conference_room.get('office_id')}번 회사, {conference_room.get('id')}번 회의실")

    # save_query = "insert into tbl_conference_room(office_id) values(%s)"
    # save_params = 2
    # save(save_query, save_params)

    # 회의실마다 이용가능 시간 추가
    # # 회의실 별 예약 시간 조회
    # find_all_by_query = "select * from tbl_part_time where conference_room_id = %s"
    # find_all_by_params = 1,
    # part_times = find_all_by(find_all_by_query, find_all_by_params)
    # for part_time in part_times:
    #     print(f"{part_time.get('conference_room_id')}번 회의실, {part_time.get('time')}")
    # save_many_query = "insert into tbl_part_time(time, conference_room_id) values(%s, %s)"
    # save_many_params = (
    #     ('9:00', 1),
    #     ('12:00', 1),
    #     ('15:00', 1),
    #     ('9:00', 2),
    #     ('12:00', 2),
    #     ('15:00', 2),
    #     ('9:00', 3),
    #     ('12:00', 3),
    #     ('15:00', 3),
    #     ('9:00', 4),
    #     ('12:00', 4),
    #     ('15:00', 4),
    #     ('9:00', 5),
    #     ('12:00', 5),
    #     ('15:00', 5),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # 예약 추가
    save_many_query = "insert into tbl_reservation(time, client_email, conference_room_id) values(%s, %s, %s)"
    save_many_params = (
        ('9:00', 'isy1234@naver.com', 1),
        ('15:00', 'isy1234@naver.com', 4),
        ('12:00', 'user1@gmail.com', 1),
    )
    # save_many(save_many_query, save_many_params)

    # 회의실 전체 내용 조회(예약이 이미 완료된 회의실 시간은 보여지지 않는다).
    find_all_query = "select * from tbl_reservation"
    reservations = find_all(find_all_query)
    for reservation in reservations:
        print(f"{reservation.get('conference_room_id')}번 회의실, {reservation.get('time')}시 예약완료")

    find_all_query = "select cr.id, pt.time \
                      from tbl_conference_room cr join tbl_part_time pt \
                      on cr.id = pt.conference_room_id \
                      left join tbl_reservation r on \
                      cr.id = r.conference_room_id and pt.time = r.time \
                      where r.id is null"

    available_times = find_all(find_all_query)
    for available_time in available_times:
        print(f"{available_time.get('id')}번 회의실, {available_time.get('time')}")
