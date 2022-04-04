from urllib import request
from urllib.request import urlopen, urlretrieve

import requests as requests
from bs4 import BeautifulSoup

#  resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html')  # скачиваем файл
resp = requests.get('https://stepik.org/media/attachments/lesson/209723/4.html')
print(resp.status_code)
#  html = resp.read().decode('utf8')  # считываем содержимое
html = resp.content.decode('utf8')
soup = BeautifulSoup(html, 'html.parser')  # делаем суп
founded = soup.find_all('td')

for elem in founded:
    # print(elem.text)
    pass

#  print(soup.select('td')[:5].p)

#  Short way to find sum of elements on the page
print((sum(int(elem) for elem in soup.stripped_strings)))

#  Long way to find sum of elements on the page
cnt = 0
answer = 0

for td in soup.find_all('td'):
    cnt += 1
#    print('\'' + td.get_text('|', strip=True) + '\'')
    answer += int(td.get_text(strip=True))
    if cnt > 15:
        pass
print(f"Number of numbers found: {cnt}")
print(f"Answer is: {answer}")
