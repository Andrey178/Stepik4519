import requests
import xmltodict

from main2_1 import get_xls_file

filename, file_url = 'map4.osm', 'https://stepik.org/media/attachments/lesson/245681/map2.osm'


def task(name):
    get_xls_file(filename, file_url)
    fin = open(filename, 'r', encoding='utf8')
    # xml = requests.get(file_url).text.encode(encoding='utf8')
    xml = fin.read()
    fin.close()

    parsedxml = xmltodict.parse(xml)
    types_o, values_o, fuel_stations = set(), set(), 0
    for node in parsedxml['osm']['node']:  # search objects with tag 'tag'
        if 'tag' in node and isinstance(node['tag'], list):
            for elem in node['tag']:
                if elem['@k'] == 'amenity' and elem['@v'] == 'fuel':
                    types_o.add(elem['@k']), values_o.add(elem['@v']),
                    fuel_stations += 1
                    print(f"{fuel_stations} {node['@id']} {elem['@v']} ", end='')
                    for param in node['tag']:
                        if param['@k'] in ['brand', 'operator', 'name']:
                            print(f"{param['@k']}: \'{param['@v']}\' ", end='')
                    print('')
        elif 'tag' in node:
            if node['tag']['@v'] == 'fuel':
                fuel_stations += 1
                print(f"{fuel_stations} {node['@id']} {node['tag']['@k']} {node['tag']['@v']} ")
                # print(node['tag']['@k'], node['tag']['@v'])
                # print(node)
            else:
                types_o.add(node['tag']['@k']), values_o.add(node['tag']['@v'])
    print(f"Fuel stations : {fuel_stations}")

    for way in parsedxml['osm']['way']:  # search objects with tag 'цфн'
        if 'tag' in way and isinstance(way['tag'], list):
            for elem in way['tag']:
                if elem['@k'] == 'amenity' and elem['@v'] == 'fuel':
                    fuel_stations += 1
                    # print(list(elem2['@ref'] for elem2 in way['nd']))
                    print(f"{fuel_stations} {way['@id']} {elem['@v']}", end=' ')
                    for param in way['tag']:
                        if param['@k'] in ['brand', 'operator', 'name']:
                            print(f"{param['@k']}: \'{param['@v']}\' ", end='')
                    print()
        elif 'tag' in way:
            if way['tag']['@v'] == 'fuel':
                fuel_stations += 1
                print(f"{fuel_stations} {way['@id']} {way['tag']['@v']} ")
    print(f"Fuel stations : {fuel_stations}")
    # print(sorted(list(types_o)))
    # print(sorted(list(values_o)))


if __name__ == '__main__':
    task('main')
