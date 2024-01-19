import hashlib
from random import randint
from crud_module import *
from s_mysql.task.mysql_with_api.papago.papago import *
from s_mysql.task.mysql_with_api.sms.send_sms import random_auth
from mail_module import send_email
from s_mysql.task.mysql_with_api.ocr.ocr import *


# 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
# 아이디(이메일) 중복 검사
if __name__ == '__main__':

    menu = "1. 회원가입\n" \
           "2. 로그인\n" \
           "3. 번역기능 사용\n" \
           "4. 이미지 업로드\n" \
           "5. 나가기\n" \

    input_menu_message = '메뉴 선택: '
    input_phone_message = '인증번호 받을 핸드폰:'
    auth_check_message = '인증번호 6자리 입력: '
    email_input_message = '이메일 입력: '
    password_input_message = '비밀번호 입력: '
    name_input_message = '사용자 이름: '
    new_password_message = '새 비밀번호 입력: '
    text_input_message = '문장 입력(한국어): '

    while True:
        print(menu)
        auth_number = "".join([str(randint(0, 9)) for i in range(6)])

        choice = input(input_menu_message)

        if choice == '1':
            phone_number = input(input_phone_message)
            # 랜덤 인증번호 6자리 생성

            random_auth(phone_number, auth_number)

            # result = '1234'
            input_auth = input(auth_check_message)
            if input_auth == auth_number:
                while True:
                    input_email = input(email_input_message)

                    find_by_id_check_query = "select email from tbl_member where email = %s"
                    params = [input_email]

                    if find_by_id(find_by_id_check_query, params):
                        print('이미 사용중인 이메일 입니다.')
                    else:
                        input_name = input(name_input_message)
                        input_password = input(password_input_message)

                        encryption = hashlib.sha256()
                        encryption.update(input_password.encode('utf-8'))

                        insert_query = "insert into tbl_member(email, password, name) values (%s, %s, %s)"

                        insert_params = [input_email, encryption.hexdigest(), input_name]
                        save(insert_query, insert_params)
                        print('회원 가입 성공')
                        break

        elif choice == '2':
            # 로그인 후 마이페이지로 이동
            # 회원 비밀번호 변경(EMAIL API) - 랜덤한 코드 10자리 발송 후 검사
            while True:
                input_email = input(email_input_message)
                find_by_id_check_query = "select name, email, password from tbl_member where email = %s"
                params = [input_email]
                user = find_by_id(find_by_id_check_query, params)
                if user:
                    input_password = input(password_input_message)
                    encryption = hashlib.sha256()
                    encryption.update(input_password.encode('utf-8'))

                    if user['password'] == encryption.hexdigest():
                        print(f'{user.get("name")}님 마이페이지')
                        for key in user:
                            if key == 'password':
                                continue
                            print(user.get(key))

                        message = "비밀번호 변경 [Y/n]: "
                        check = input(message)

                        if check == 'Y':
                            code = "".join(map(str, [chr(i + 65) for i in range(0, 26)] + [i for i in range(0, 10)]))
                            certification_number = ""

                            for i in range(10):
                                certification_number += code[randint(0, len(code))]

                            send_email(user['email'], certification_number)
                            message = f"{user['email']}로 인증코드를 전송했습니다.\n10자리 인증번호: "
                            email_auth = input(message)
                            if email_auth == certification_number:
                                # 새로운 비밀번호 입력
                                new_password = input(new_password_message)
                                encryption = hashlib.sha256()
                                encryption.update(input_password.encode('utf-8'))

                                update_query = "update tbl_member set password = %s where email = %s"
                                params = [encryption.hexdigest(), user['email']]
                                update(update_query, params)
                                print('비밀번호 변경 완료')
                                break
                            else:
                                print('인증번호 오류')
                        else:
                            break
                    else:
                        print('비밀번호 오류')
                    break
                else:
                    print('해당 이메일을 가진 사용자가 없습니다.')
                break

        # 사용자가 입력한 한국어를 영어로 번역
        # 한국어와 번역된 문장을 DBMS에 저장
        # 번역 내역 전체 조회
        elif choice == '3':
            input_text = input(text_input_message)
            output_text = translate(input_text)
            insert_query = "insert into tbl_translate(text) values(%s)"
            params = [output_text]
            save(insert_query, params)

            find_all_query = "select text from tbl_translate"
            contents = find_all(find_all_query)
            for content in contents:
                print(f'내용: {content["text"]}')


        elif choice == '4':
            # 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
            # 이미지 경로: https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/
            img_name = input('이미지 이름: ')
            img_url = input('이미지 주소: ')
            result = img_to_txt(img_url)
            # print(type(result)) # string
            insert_query = "insert into tbl_image(file_name, file_content, file_path) values(%s, %s, %s)"
            insert_params = [img_name, result, '/upload/'+ img_url]
            save(insert_query, insert_params)

            # 전체 경로와 추출한 텍스트 전체 조회
            find_all_query = "select file_content, file_path from tbl_image"
            images = find_all(find_all_query)
            for image in images:
                print(f'내용: {image["file_content"]} \n경로: {image["file_path"]}')

        else:
            break


