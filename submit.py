import requests
import json
import datetime
from access_token import find_access_token

submit_url = 'http://dailyhealth-api.sustech.edu.cn/api/form/save'

content_path = './content.json'
header_path = './header.json'


def submit(token=''):
    today = datetime.datetime.today()
    date_string = "%d-%02d-%02d" % (today.year, today.month, today.day)

    with open(content_path, encoding='utf-8') as f:
        content = json.load(f)

    with open(header_path, encoding='utf-8') as f:
        header = json.load(f)
    
    content['formDate'] = date_string
    header['accessToken'] = token
    

    response = requests.post(submit_url, data=json.dumps(content), headers=header)
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    token = find_access_token()
    print(token)
    submit(token)
    