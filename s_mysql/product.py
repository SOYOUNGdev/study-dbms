from s_mysql.product_module import *
import pandas as pd

if __name__ == '__main__':
    # 상품 추가
    # insert_query = "insert into tbl_product(name, price, created_date)\
    #                 values(%s, %s, %s)"
    # datetime -> 시 분 초까지 작성
    # date -> 일 까지 작성
    insert_params = ['마우스', 85000, '2024-01-17T17:21:00']
    # save(insert_query, insert_params)

    # 전체 상품 조회
    find_all_query = "select name, price, created_date from tbl_product"
    # products = find_all(find_all_query)
    #
    # for product in products:
    #     print(f'상품명: {product["name"]}')

    # result = find_all(find_all_query)
    # df = pd.DataFrame(result)
    # df.head()
    # print(df)

    # 상품 정보 중 가격이 3000원 이상인 상품은 10% 할인해준다.
    update_query = "update tbl_product \
                    set price = price * (1 - (%s * 0.01)) \
                    where price >= %s"
    update_params = [10, 3000]
    # update(update_query, update_params)


    # 여러 정보를 한 번에 추가
    insert_query = "insert into tbl_product(name, price, created_date) values (%s, %s, %s)"
    insert_params = (
        ('키보드', 120000, None),
        ('노트북', 950000, None),
        ('칫솔', 3500, None),
        ('치약', 7500, None),
        ('라이터', 1000, None)
    )
    save_many(insert_query, insert_params)

    # 평균 가격보다 높은 상품은 모두 삭제한다.
    delete_query = "delete from tbl_product \
                    where price > (select avg.avg_price from (select round(avg(price)) as avg_price from tbl_product) avg)"
    # find_avg_price_query = "select round(avg(price)) as avg_price from tbl_product"
    # avg_results = find_all(find_avg_price_query)
    # avg_price = avg_results[0]['avg_price'] # avg_results : list 타입
    # # print(type(avg_results[0])) # dict 타입
    # delete_params = [avg_price]

    delete(delete_query, None)
