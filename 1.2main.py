# This is a sample Python script.
from urllib.request import urlopen
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def task(name):
    # Use a breakpoint in the code line below to debug your script.
    html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
    html_code = str(html)

# Create list of between code word entries
    max_index = html_code.count("<code>")
    code_length = len("<code>")
    last_index = 0
    set_codes = []
    for i in range(max_index):
        index1 = html_code.find('<code>', last_index)
        index2 = html_code.find('</code>', index1)
        set_codes.append(html_code[index1+code_length: index2])
        last_index = index2

# Count frequency of the entries
    dic_codes = {}
    for elem in set_codes:
        dic_codes[elem] = dic_codes.get(elem, 0) + 1

# Count max frequency
    sorted_max = []
    for elem in dic_codes.items():
        if elem[1] == max(dic_codes.values()):
            sorted_max.append(elem[0])

# Print most frequent phrase in alphabet order
    sorted_max.sort()
    print(*sorted_max)


if __name__ == '__main__':
    task('main')
