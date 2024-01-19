# https://ocr.space/OCRAPI
# K87921123288957
# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true
import requests

def img_to_txt(img_url):
    url = f'https://api.ocr.space/parse/imageurl?apikey=K87921123288957&url={img_url}&language=kor&isOverlayRequired=true'
    response = requests.get(url)
    response.raise_for_status()

    result = response.json()
    # print(type(result))
    return result['ParsedResults'][0]['ParsedText']