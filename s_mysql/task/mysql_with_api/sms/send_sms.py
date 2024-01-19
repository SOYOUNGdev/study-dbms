import json
from s_mysql.task.mysql_with_api.sms import message

def random_auth(phone_number, number):
    data = {
        'messages': [
            {
                'to': phone_number,
                'from': '01023290798',
                'text': number
            },
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

