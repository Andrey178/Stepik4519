import openpyxl as openpyxl
import wget
import xlrd


def task(name):
    # Download xlsx file from source
    # filename = wget.download('https://stepik.org/media/attachments/lesson/245266/tab.xlsx', 'tab.xlsx')
    filename = 'tab.xlsx'
    print(filename)

    # Open xlsx file with xlrd library and count
    wb = xlrd.open_workbook(filename)
    sheet_names = wb.sheet_names()
    print(sheet_names)
    sh = wb.sheet_by_name(sheet_names[0])
    nmin = sh.row_values(6)[2]
    for rownum in range(7, 27):
        temp = sh.row_values(rownum)
        nmin = min(nmin, temp[2])
    print(nmin)

    # Open xlsx file with openpyxl library and count
    wb = openpyxl.load_workbook(filename)
    sheet_names = wb.sheetnames
    print(sheet_names)
    sh = wb[sheet_names[0]]
    nmin = sh.cell(row=7, column=3).value
    print(f"{str(nmin)} => {str(sh.cell(row=7, column=3).coordinate)}")
    for rownum in sh['C7':'C27']:
        temp = rownum[0].value
        nmin = min(nmin, temp)
    print(nmin)


if __name__ == '__main__':
    task('main')
