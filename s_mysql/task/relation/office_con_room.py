import hashlib
from crud_module import *

if __name__ == '__main__':
    # 회원가입
    save_query = "insert into tbl_client(email, password, name) values(%s, %s, %s)"

    password = '5678'
    encryption = hashlib.sha256()
    encryption.update(password.encode('utf-8'))
    password = encryption.hexdigest()

    save_params = ['user1@gmail.com', password, '회원1']
    save(save_query, save_params)

    # 회사 추가
    save_query = "insert into tbl_office(name, location) values(%s, %s)"
    save_params = '현대자동차', '삼성동'
    save(save_query, save_params)

    # 회의실 추가
    find_by_id_query = "select id from tbl_office where id = %s"
    find_by_id_params = 1,
    office = find_by_id(find_by_id_query, find_by_id_params)

    save_query = "insert into tbl_conference_room(office_id) values(%s)"
    save_params = (office.get('id'),)
    save(save_query, save_params)

    # 회사에 있는 회의실 정보 조회
    find_all_by_query = "select * from tbl_conference_room where office_id = %s"
    find_all_by_params = (office.get('id'),)
    conference_rooms = find_all_by(find_all_by_query, find_all_by_params)
    for conference_room in conference_rooms:
        print(f"{conference_room.get('office_id')}번 회사, {conference_room.get('id')}번 회의실")

    # 예약 시간 추가
    find_by_id_query = "select * from tbl_part_time where conference_room_id = %s"
    find_by_id_params = 1,
    conference_room = find_by_id(find_by_id_query, find_by_id_params)
    conference_room_id = conference_room.get('id')

    save_many_query = "insert into tbl_part_time(time, conference_room_id) values(%s, %s)"
    save_many_params = (
        ('9:00', conference_room_id),
        ('12:00', conference_room_id),
        ('15:00', conference_room_id),
    )
    save_many(save_many_query, save_many_params)

    # 예약 추가
    # 회의실 별 예약 시간 조회
    find_all_query = "select id, name, location from tbl_office"
    offices = find_all(find_all_query)

    for office in offices:
        find_all_by_query = "select id from tbl_conference_room where office_id = %s"
        find_all_by_params = office.get('get')
        conference_rooms = find_all_by(find_all_by_query, find_all_by_params)

        for conference_room in conference_rooms:
            find_all_by_query = "select id, time from tbl_part_time where conference_room_id = %s"
            find_all_by_params = conference_room.get('id'),
            part_times = find_all_by(find_all_by_query, find_all_by_params)
            for part_time in part_times:
                print(f"{part_time.get('conference_room_id')}번 회의실, {part_time.get('time')}")

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

