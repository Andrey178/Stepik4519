from main2_1 import get_xls_file
import xmltodict

filename, file_url = 'map2.osm', 'https://stepik.org/media/attachments/lesson/245678/map1.osm'


def task(name):
    get_xls_file(filename, file_url)
    fin = open('map1.osm', 'r', encoding='utf8')
    xml = fin.read()
    fin.close()

    parsedxml = xmltodict.parse(xml)
    # print(*parsedxml['osm']['node'][1], sep='\n')
    node_w_tag, node_wo_tag = 0, 0
    for node in parsedxml['osm']['node']:
        if 'tag' in list(node):
            node_w_tag += 1
        else:
            node_wo_tag += 1
    print(f"Nodes with tag: {node_w_tag} and nodes without tag: {node_wo_tag}")


if __name__ == '__main__':
    task('main')
