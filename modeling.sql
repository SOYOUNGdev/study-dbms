/*
   회원          주문              상품
   ----------------------------------------
   번호PK      번호PK          번호PK
   ----------------------------------------
   아이디U, NN   날짜NN          이름NN
   비밀번호NN   회원번호FK, NN   가격D=0
   이름NN      상품번호FK, NN   재고D=0
   주소NN
   이메일
   생일
*/
create table tbl_user(
    id bigint primary key,
    user_id varchar(255) not null unique,
    password varchar(255) not null,
    name varchar(255) not null,
    address varchar(255) not null,
    email varchar(255),
    birth date
);

create table tbl_product(
    id bigint primary key,
    name varchar(255) not null,
    price int default 0,
    stock int default 0
);

create table tbl_order(
    id bigint primary key,
    order_date datetime default current_timestamp,
    user_id bigint not null,
    product_id bigint not null,
    constraint fk_order_user foreign key(user_id)
    references tbl_user(id),
    constraint fk_order_product foreign key(product_id)
    references tbl_product(id)
);

drop table tbl_order;
drop table tbl_user;
drop table tbl_product;

show tables;

/*
    1. 요구사항 분석
        꽃 테이블과 화분 테이블 2개가 필요하고,
        꽃을 구매할 때 화분도 같이 구매합니다.
        꽃은 이름과 색상, 가격이 있고,
        화분은 제품번호, 색상, 모양이 있습니다.
        화분은 모든 꽃을 담을 수 없고 정해진 꽃을 담아야 합니다.

    2. 개념 모델링
    3. 논리 모델링
    4. 물리 모델링
    5. 구현
*/

create table tbl_flower(
    id bigint primary key,
    name varchar(255) not null,
    color varchar(255) not null,
    price int default 0
);

create table tbl_pot(
    id bigint primary key,
    color varchar(255) not null,
    shape varchar(255) not null,
    flower_id bigint not null,
    constraint fk_pot_flower foreign key(flower_id)
    references tbl_flower(id)
);

drop table tbl_pot;
drop table tbl_flower;

show tables;


/*
    복합키(조합키): 하나의 PK에 여러 컬럼을 설정한다.
*/
create table tbl_flower(
    name varchar(255) not null,
    color varchar(255) not null,
    price int default 0,
    primary key(name, color)
);

create table tbl_pot(
    id bigint primary key,
    color varchar(255) not null,
    shape varchar(255) not null,
    flower_name varchar(255) not null,
    flower_color varchar(255) not null,
    constraint fk_pot_flower foreign key(flower_name, flower_color)
    references tbl_flower(name, color)
);

drop table tbl_pot;
drop table tbl_flower;

show tables;

/*
    1. 요구사항 분석
        안녕하세요, 동물병원을 곧 개원합니다.
        동물은 보호자랑 항상 같이 옵니다. 가끔 보호소에서 오는 동물도 있습니다.
        보호자가 여러 마리의 동물을 데리고 올 수 있습니다.
        보호자는 이름, 나이, 전화번호, 주소가 필요하고
        동물은 병명, 이름, 나이, 몸무게가 필요합니다.

    2. 개념 모델링
    3. 논리 모델링
    4. 물리 모델링
    5. 구현
*/

create table owner(
    id bigint primary key,
    name varchar(255) not null,
    age int default 0,
    phone varchar(255) not null,
    address varchar(255) not null
);

alter table owner rename tbl_owner;

create table pet(
    id bigint primary key,
    name varchar(255) default '사랑',
    ill_name varchar(255) not null,
    age int default 0,
    weight decimal(3, 2) default 0.0,
    owner_id bigint,
    constraint fk_pet_owner foreign key(owner_id)
                references tbl_owner(id)
);

alter table pet rename tbl_pet;

drop table tbl_pet;
drop table tbl_owner;

show tables;

/*
    1. 요구사항 분석
        안녕하세요 중고차 딜러입니다.
        이번에 자동차와 차주를 관리하고자 방문했습니다.
        자동차는 여러 명의 차주로 히스토리에 남아야 하고,
        차주는 여러 대의 자동차를 소유할 수 있습니다.
        그래서 우리는 항상 등록증(Registration)을 작성합니다.
        자동차는 브랜드, 모델명, 가격, 출시날짜가 필요하고
        차주는 이름, 전화번호, 주소가 필요합니다.

    2. 개념 모델링
    3. 논리 모델링
    4. 물리 모델링
    5. 구현
*/
create table tbl_car(
    id bigint primary key,
    brand varchar(255) not null,
    model varchar(255) not null,
    price bigint default 0,
    release_date date default (current_date)
);

create table tbl_car_owner(
    id bigint primary key,
    name varchar(255) not null,
    phone varchar(255) not null,
    address varchar(255) not null
);

create table tbl_car_registration(
    id bigint primary key,
    car_id bigint not null,
    car_owner_id bigint not null,
    constraint fk_car_registration_car foreign key(car_id)
                                 references tbl_car(id),
    constraint fk_car_registration_car_owner foreign key(car_owner_id)
                                 references tbl_car_owner(id)
);

drop table tbl_car_registration;
drop table tbl_car;
drop table tbl_car_owner;

show tables;

/*
    요구 사항
    커뮤니티 게시판을 만들고 싶어요.
    게시판에는 게시글 제목과 게시글 내용, 작성한 시간, 작성자가 있고,
    게시글에는 댓글이 있어서 댓글 내용들이 나와야 해요.
    작성자는 회원(tbl_user)정보를 그대로 사용해요.
    댓글에도 작성자가 필요해요.
*/
create table tbl_user(
    id bigint primary key,
    user_id varchar(255) not null unique,
    password varchar(255) not null,
    name varchar(255) not null,
    address varchar(255) not null,
    email varchar(255),
    birth date
);

create table tbl_post(
    id bigint primary key,
    title varchar(255) not null,
    content varchar(255) not null,
    create_date datetime default current_timestamp,
    user_id bigint not null,
    constraint fk_post_user foreign key(user_id)
                     references tbl_user(id)
);

create table tbl_reply(
    id bigint primary key,
    content varchar(255) not null,
    user_id bigint not null,
    post_id bigint not null,
    constraint fk_reply_user foreign key(user_id)
                     references tbl_user(id),
    constraint fk_reply_post foreign key(post_id)
                     references tbl_post(id)
);

drop table tbl_reply;
drop table tbl_post;
drop table tbl_user;

show tables;

/*
    요구사항

    마이페이지에서 회원 프로필을 구현하고 싶습니다.
    회원당 프로필을 여러 개 설정할 수 있고,
    대표 이미지로 선택된 프로필만 화면에 보여주고 싶습니다.
*/
create table tbl_user(
    id bigint primary key,
    user_id varchar(255) not null unique,
    password varchar(255) not null,
    name varchar(255) not null,
    address varchar(255) not null,
    email varchar(255),
    birth date
);

create table tbl_file(
    id bigint primary key,
    file_path varchar(255) default '/upload/',
    file_name varchar(255),
    is_main varchar(255) default 'ELSE',
    user_id bigint,
    constraint fk_file_user foreign key(user_id)
                     references tbl_user(id)
);

drop table tbl_file;
drop table tbl_user;

use test;
show tables;



/*  문제1
    1. 요구사항

    학사 관리 시스템에 학생과 교수, 과목을 관리합니다.
    학생은 학번, 이름, 전공 학년이 필요하고
    교수는 교수 번호, 이름, 전공, 직위가 필요합니다.
    과목은 고유한 과목 번호와 과목명, 학점이 필요합니다.
    학생은 여러 과목을 수강할 수 있으며,
    교수는 여러 과목을 강의할 수 있습니다.
    학생이 수강한 과목은 성적(점수)이 모두 기록됩니다.

    3. 논리적 설계
        학생      교수      과목          학사 시스템
        학번PK    번호PK    번호PK        학생 학번FK
        이름NN    이름NN    학생 학번FK    교수 번호FK
        전공NN    전공NN    교수 번호FK    과목 번호FK
        학년D=1   직위NN    학점D=0       성적
                           과목명NN

*/

create table tbl_student(
    id bigint primary key,
    name varchar(255) not null,
    major varchar(255) not null,
    grade int default 1
);

create table tbl_professor(
    id bigint primary key,
    name varchar(255) not null,
    major varchar(255) not null,
    job_position varchar(255) not null
);

create table tbl_subject(
    id bigint primary key,
    name varchar(255) not null unique,
    credit int default 0,
    student_id bigint,
    professor_id bigint,
    constraint fk_subject_student foreign key(student_id)
                        references tbl_student(id),
    constraint fk_subject_professor foreign key(professor_id)
                        references tbl_professor(id)
);

create table tbl_school_system(
    score decimal(2, 1) default 0,
    student_id bigint,
    professor_id bigint,
    subject_id bigint,
    constraint fk_school_system_student foreign key(student_id)
                   references tbl_student(id),
    constraint fk_school_system_professor foreign key(professor_id)
                   references tbl_professor(id),
    constraint fk_school_system_subject foreign key(subject_id)
                   references tbl_subject(id)
);


/*alter table school_system rename tbl_school_system;*/
show tables;

/*  문제2
    1. 요구사항

    대카테고리, 소카테고리가 필요해요.
    2.
    3. 논리적 설계
        대카테고리          소카테고리
        카테고리 번호PK     상품 번호PK
        카테고리 이름NN     상품 이름NN
                           상품 가격D=0
                           상품의 종류(카테고리 번호)FK
*/
create table tbl_big_category(
    id bigint primary key,
    name varchar(255) not null
);

create table tbl_small_category(
    id bigint primary key,
    name varchar(255) not null,
    price int default 0,
    category_id bigint,
    constraint fk_small_category_big_category foreign key(category_id)
                           references tbl_big_category(id)
);

show tables;

/*  문제3
    1. 요구 사항

    회의실 예약 서비스를 제작하고 싶습니다.
    회원별로 등급이 존재하고 사무실마다 회의실이 여러 개 있습니다.
    회의실 이용 가능 시간은 파트 타임으로서 여러 시간대가 존재합니다.

    2.
    3. 논리적  설계
        회원          사무실         회의실         시간대         예약
        번호PK        번호PK        번호PK          번호PK         번호PK
        아이디NN,U     이름NN        이름NN        시작시간NN      날짜NN
        비밀번호NN     주소NN         주소NN        종료시간NN     회원번호FK
        이름NN        전화번호NN      사무실번호FK                 시간번호FK
        주소NN                                                   회의실번호FK
        이메일
        생일
*/
create table tbl_user(
    id bigint primary key,
    user_id varchar(255) not null unique,
    password varchar(255) not null,
    name varchar(255) not null,
    address varchar(255) not null,
    email varchar(255),
    birth date
);
create table tbl_office(
    id bigint primary key,
    name varchar(255) not null,
    address varchar(255) not null,
    phone varchar(255) not null
);
create table tbl_meeting_room(
    id bigint primary key,
    address varchar(255) not null,
    office_id bigint,
    constraint fk_meeting_room_office foreign key(office_id)
                             references tbl_office(id)
);
create table tbl_time(
    id bigint primary key,
    start_time time not null,
    end_time time not null
);
create table tbl_reservation(
    id bigint primary key,
    reservation_time timestamp not null,
    user_id bigint,
    meeting_room_id bigint,
    time_id bigint,
    constraint fk_reservation_user foreign key(user_id)
                            references tbl_user(id),
    constraint fk_reservation_meeting_room foreign key(meeting_room_id)
                            references tbl_meeting_room(id),
    constraint fk_reservation_time foreign key(time_id)
                            references tbl_time(id)
);

show tables;

/*  문제4
    요구사항

    유치원을 하려고 하는데, 아이들이 체험학습 프로그램을 신청해야 합니다.
    아이들 정보는 이름, 나이, 성별이 필요하고 학부모는 이름, 나이, 주소, 전화번호, 성별이 필요해요
    체험학습은 체험학습 제목, 체험학습 내용, 이벤트 이미지 여러 장이 필요합니다.
    아이들은 여러 번 체험학습에 등록할 수 있어요.

    논리적 설계
        아이          학부모         체험학습        이미지
        번호PK        번호PK        번호PK          번호PK
        이름NN        이름NN        제목NN          경로
        나이D=5       나이D=35      내용NN          이름
        성별D='남'    주소NN        아이 번호FK     체험학습번호FK
        학부모번호FK   전화번호NN
                      성별D='남'


*/
create table tbl_parent(
    id bigint primary key,
    name varchar(255) not null,
    age int default 35,
    address varchar(255) not null,
    phone varchar(255) not null,
    gender varchar(255) default '남자'
);
create table tbl_child(
    id bigint primary key,
    name varchar(255) not null,
    age int default 5,
    gender varchar(255) default '남자',
    parent_id bigint,
    constraint fk_child_parent foreign key(parent_id)
                      references tbl_parent(id)
);
create table tbl_outside_study(
    id bigint primary key,
    title varchar(255) not null,
    content varchar(255) not null,
    child_id bigint,
    constraint fk_outside_study_child foreign key(child_id)
                              references tbl_child(id)
);

create table tbl_image(
    id bigint primary key,
    image_path varchar(255) default '/upload/',
    image_name varchar(255),
    outside_study_id bigint,
    constraint fk_image_outside_study foreign key (outside_study_id)
                      references tbl_outside_study(id)
);

show tables;


/*  문제5
    요구사항

   안녕하세요, 광고 회사를 운영하려고 준비중인 사업가입니다.
    광고주는 기업이고 기업 정보는 이름, 주소, 대표번호, 기업종류(스타트업, 중소기업, 중견기업, 대기업)입니다.
    광고는 제목, 내용이 있고 기업은 여러 광고를 신청할 수 있습니다.
    기업이 광고를 선택할 때에는 카테고리로 선택하며, 대카테고리, 중카테고리, 소카테고리가 있습니다.

    논리적 설계
        기업          광고          카테고리
        번호PK        번호PK        번호PK
        이름NN        제목NN        대
        주소NN        내용NN        중
        대표번호NN    기업번호FK     소
        종류D=중소                  광고번호FK
*/
create table tbl_company(
    id bigint primary key,
    name varchar(255) not null,
    address varchar(255) not null,
    phone varchar(20) not null,
    type varchar(255) not null
);
create table tbl_advertisement(
    id bigint primary key,
    title varchar(255) not null,
    content varchar(255) not null,
    company_id bigint,
    constraint fk_advertisement_company foreign key(company_id)
                              references tbl_company(id)
);
create table tbl_category(
    id bigint primary key,
    big_category varchar(255) not null,
    middle_category varchar(255) not null,
    small_category varchar(255) not null,
    advertisement_id bigint,
    constraint fk_category_advertisement foreign key(advertisement_id)
                         references tbl_advertisement(id)
);

show tables;



/*  문제6
    요구사항

    음료수 판매 업체입니다. 음료수마다 당첨번호가 있습니다.
    음료수의 당첨번호는 1개이고 당첨자의 정보를 알아야 상품을 배송할 수 있습니다.
    당첨 번호마다 당첨 상품이 있고, 당첨 상품이 배송 중인지 배송 완료인지 구분해야 합니다.

    논리적 설계
        음료수         당첨자         배송             상품
        번호PK        번호PK        번호PK             번호PK
        당첨번호NN     이름NN        배송상태 D=NO      이름NN
        당첨자번호FK   전화번호NN    음료번호FK          음료번호FK
                      주소NN       당첨자번호FK

*/
create table tbl_winner(
    id bigint primary key,
    name varchar(255) not null,
    phone varchar(20) not null,
    address varchar(20) not null
);

create table tbl_drink(
    id bigint primary key,
    lucky_number bigint unique,
    winner_id bigint,
    constraint fk_drink_winner foreign key(winner_id)
                            references tbl_winner(id)
);

create table tbl_winner_goods(
    id bigint primary key,
    name varchar(255) not null,
    winner_id bigint,
    constraint fk_winner_goods_winner foreign key(winner_id)
                             references tbl_winner(id)
);

create table tbl_delivery(
    id bigint primary key,
    is_complete varchar(255) default 'NO',
    winner_goods_id bigint,
    winner_id bigint,
    constraint fk_delivery_winner_goods foreign key(winner_goods_id)
                         references tbl_drink(id),
    constraint fk_delivery_winner foreign key(winner_id)
                         references tbl_winner(id)
);


show tables;


/*  문제7
    요구사항

    이커머스 창업 준비중입니다. 기업과 사용자 간 거래를 위해 기업의 정보와 사용자 정보가 필요합니다.
    기업의 정보는 기업 이름, 주소, 대표번호가 있고
    사용자 정보는 이름, 주소, 전화번호가 있습니다. 결제 시 사용자 정보와 기업의 정보, 결제한 카드의 정보 모두 필요하며,
    상품의 정보도 필요합니다. 상품의 정보는 이름, 가격, 재고입니다.
    사용자는 등록한 카드의 정보를 저장할 수 있으며, 카드의 정보는 카드번호, 카드사, 회원 정보가 필요합니다.

    논리적 설계
        기업          구매자         카드          상품          결제
        번호pk        번호PK        번호PK         번호PK       번호PK
        이름NN        이름NN        카드번호NN,U    이름NN       사용자번호FK
        주소NN        주소NN        카드사NN       가격D=0       기업번호FK
        대표번호NN    전화번호NN     회원번호FK     재고D=0       카드번호FK
                                                 사용자번호FK   상품번호FK

*/

create table tbl_companies(
    id bigint primary key,
    name varchar(255) not null,
    address varchar(255) not null,
    phone varchar(20) not null
);

create table tbl_purchaser(
    id bigint primary key,
    name varchar(255) not null,
    address varchar(255) not null,
    phone varchar(20) not null
);

create table tbl_card(
    id bigint primary key,
    number varchar(30) not null,
    card_brand varchar(255) not null,
    purchaser_id bigint,
    constraint fk_card_purchaser foreign key(purchaser_id)
                     references tbl_purchaser(id)
);
create table tbl_goods(
    id bigint primary key,
    name varchar(255) not null,
    price int default 0,
    stock int default 0,
    purchaser_id bigint,
    constraint fk_goods_purchaser foreign key(purchaser_id)
                      references tbl_purchaser(id)
);
create table tbl_order(
    id bigint primary key,
    purchaser_id bigint,
    companies_id bigint,
    card_id bigint,
    goods_id bigint,
    constraint fk_order_purchaser foreign key(purchaser_id)
                     references tbl_purchaser(id),
    constraint fk_order_companies foreign key(companies_id)
                     references tbl_companies(id),
    constraint fk_order_goods foreign key(goods_id)
                     references tbl_goods(id)
);

show tables;




