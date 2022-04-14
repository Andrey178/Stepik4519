from main2_1 import get_xls_file
import xmltodict

filename, file_url = 'map1.osm', 'https://stepik.org/media/attachments/lesson/245571/map1.osm'


def task(name):
    get_xls_file(filename, file_url)
    fin = open('map1.osm', 'r', encoding='utf8')
    xml = fin.read()
    fin.close()

    parsedxml = xmltodict.parse(xml)
    print(parsedxml['osm']['node'][100]['@id'])


if __name__ == '__main__':
    task('main')
