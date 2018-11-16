import requests
from pathlib import Path


BASE_URL = "https://pythondigest.ru/"
BASE_SAVE_PATH = Path('./output')


r = requests.get(BASE_URL)

print(r.status_code)
html_file_path = BASE_SAVE_PATH / 'python_digest.html'

with open(str(html_file_path.absolute()), 'wb') as f:
    f.write(r.content)

