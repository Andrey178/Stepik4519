# This is a sample Python script.
from urllib.request import urlopen
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def task(name):
    # Use a breakpoint in the code line below to debug your script.
    html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
    # print(html)
    counted_c = html.count('C++')
    counted_python = html.count('Python')
    print('C++' if counted_c > counted_python else 'Python')
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    task('main')
