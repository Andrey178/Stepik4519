from main2_3_2 import get_xls_file, load_openpyxl_file

filename, pagename, file_url = 'trekking3.xlsx', ['Справочник', 'Раскладка'],\
                               'https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx'


def count_product_day_data(xls_filename, pagename):  # Sort data in table and print it
    table = load_openpyxl_file(xls_filename)
    # print(table.sheetnames)
    sh0 = table[pagename[0] if pagename[0] in table.sheetnames else table.sheetnames[0]]
    sh1 = table[pagename[1] if pagename[1] in table.sheetnames else table.sheetnames[1]]
    # day_menu, menu = [], list(sh0.iter_rows(min_row=2, max_col=5, values_only=True))
    day_menu, menu = [], dict((elem[0], elem[1:]) for elem in sh0.iter_rows(min_row=2, max_col=5, values_only=True))
    for row in sh1.iter_rows(min_row=2, max_col=3, values_only=True):  # Take line from day menu
        menu_data = list(row)
        menu_data.extend(menu[menu_data[1]])
        day_menu.append(menu_data)

    day_menu_calories = [0]*7
    for elem in day_menu:
        if day_menu_calories[0] != elem[0]:
            if day_menu_calories[0] != 0:
                print(*(int(elem) for elem in day_menu_calories[2:]))
            day_menu_calories = elem[:3] + [0]*4
        for index in range(3, len(elem)):
            product_item = elem[index] or 0
            day_menu_calories[index] += product_item*(elem[2]/100)
    # print(*list(map(lambda elem1: int(elem1), day_menu_calories[2:])))
    print(*(int(elem) for elem in day_menu_calories[2:]))


def task(name):
    get_xls_file(filename, file_url)
    count_product_day_data(filename, pagename)


if __name__ == '__main__':
    task('main')
