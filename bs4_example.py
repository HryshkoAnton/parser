from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://pythondigest.ru/'

r = requests.get(BASE_URL)

soap = BeautifulSoup(r.text, "html.parser")

print(soap.title)

msgs = soap.select("a.issue-item-title")


parsed_msgs = []

for msg in msgs:
    txt = msg.get_text()
    parsed_msgs.append(txt)

print(len(msgs))
print(parsed_msgs)


