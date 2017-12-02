import json
from time import sleep

import requests
from bs4 import BeautifulSoup

def get_MTA_home():
    r = requests.get('https://mta.info')
    if r.status_code != 200:
        return None

    return r.text

html = get_MTA_home()
if html is not None:
    # soup = BeautifulSoup(html, 'html.parser')
    r = requests.get('http://www.mta.info/service_status_json/25204112')
    data = json.loads(r.json())
    subway = data['subway']
    lines = subway['line']
    my_list = []
    for line in lines:
        if line['name'] != 'SIR':
            my_list.append({
                line['name']: line['status']
            })
    my_line = 'R'
    print(my_list)
    for trainline in my_list:
        key = list(trainline.keys())
        if my_line in key[0]:
            print('found it', my_line)
            if trainline[key[0]] != 'GOOD STATUS':
                print('ALERT, train is delayed')
                IFTTT = 'https://maker.ifttt.com/trigger/train_delayed/with/key/cMlapZuzhROcnd8BA9EDac'
                r = requests.post(IFTTT, json={
                    'value1': trainline[key[0]],
                    'value2': key[0],
                })
                print(r.status_code, r.text)


'''
 block = soup.find("div", {"id": "block-block-521"})
anchors = block.find_all("a")
clean_links = []
for link in anchors:
    clean_links.append((link.text, link.get('href')))
print(clean_links)
'''
