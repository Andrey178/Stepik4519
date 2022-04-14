from main2_3_2 import load_openpyxl_file

filename, index, file_path = '.xlsx', 1000, 'data/'


def count_payments(file_path, xls_filename, index):  # Sort data in table and print it
    vedomost = []
    for i in range(1, index + 1):
        file = (file_path+str(i)+filename)
        # print(file)
        table = load_openpyxl_file(file)
        sh = table.active
        vedomost.append([sh['B2'].value, sh['D2'].value])
    print(len(vedomost))
    vedomost.sort(key=lambda elem: elem[0])
    for i in range(0, len(vedomost)):
        print(f"{vedomost[i][0]} {vedomost[i][1]}")


def task(name):
    # get_xls_file(filename, file_url)
    count_payments(file_path, filename, index)


if __name__ == '__main__':
    task('main')
