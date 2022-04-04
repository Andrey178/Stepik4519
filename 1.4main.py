from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html')  # скачиваем файл
html = resp.read().decode('utf8')  # считываем содержимое
soup = BeautifulSoup(html, 'html.parser')  # делаем суп

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
