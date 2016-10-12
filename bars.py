import json
import os
from optparse import OptionParser

def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(path, encoding='utf-8') as json_bar_file:
        line = json_bar_file.read()

    bars = json.loads(line)
    return bars


def get_biggest_bar(data):
    max_value = 0
    max_value_index = -1
    for i, current_bar in enumerate(data):
        if max_value < current_bar['Cells']['SeatsCount']:
            max_value = current_bar['Cells']['SeatsCount']
            max_value_index = i
    print('*****', data[max_value_index]['Cells']['global_id'])
    print('*****', data[max_value_index]['Cells']['Name'])
    return data[max_value_index]



def get_smallest_bar(data):
    min_value = 10000000
    min_value_index = -1
    for i, current_bar in enumerate(data):
        if min_value > current_bar['Cells']['SeatsCount']:
            min_value = current_bar['Cells']['SeatsCount']
            min_value_index = i
    return data[min_value_index]


def get_closest_bar(data, longitude, latitude):
    min_radius = 10000000
    min_radius_index = -1
    for i, current_bar in enumerate(data):
        dx = abs(longitude - current_bar['Cells']['geoData']['coordinates'][1])
        dy = abs(latitude - current_bar['Cells']['geoData']['coordinates'][0])
        radius = ((dx ** 2)+(dy ** 2)) ** 0.5
        if min_radius > radius:
            min_radius = radius
            min_radius_index = i
    return data[min_radius_index]


if __name__ == '__main__':

    usage = 'Usage: %prog -p path_to_bars_json (-s|-b|-c longitude latitude)'
    parser = OptionParser(usage=usage)

    parser.add_option('-p', '--path', action='store', type='string', help='Путь до файла с барами в json')
    parser.add_option('-s', '--smallest', action='store_true', help='Найти самый маленький бар')
    parser.add_option('-b', '--biggest', action='store_true', help='Найти самый большой бар')
    parser.add_option('-c', '--closest', action='store_true', help='Найти самый ближайший бар (необходимо указать Долготу Широту)')
    
    options,arguments=parser.parse_args()
    options = options.__dict__

    if options['path']:
        path = options['path']
    else:
        print(u'Необходимо указать путь до файла с барами в json')
        exit(-1)

    bars_db = load_data(path)

    if options['smallest']:
        bar = get_smallest_bar(bars_db)
        print(u'Самый маленький бар: {}'.format(bar['Cells']['Name']))
        print(u'Адрес: {}'.format(bar['Cells']['Address']))
        print(u'Размер: {} мест'.format(bar['Cells']['SeatsCount']))

    if options['biggest']:
        bar = get_biggest_bar(bars_db)
        # print('Самый большой бар: {}'.format(bar['Cells']['Name']))
        # print('Адрес: {}'.format(bar['Cells']['Address']))
        # print('Размер: {} мест'.format(bar['Cells']['SeatsCount']))

    if options['closest']:
        print(arguments)
        exit(1)
        bar = get_biggest_bar(bars_db)
        print('Самый большой бар: {}'.format(bar['Cells']['Name']))
        print('Адрес: {}'.format(bar['Cells']['Address']))
        print('Размер: {} мест'.format(bar['Cells']['SeatsCount']))

    # closest = get_closest_bar(bars, 55.889165, 37.707438)

