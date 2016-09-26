import json


def load_data(filepath):
    with open(path, encoding='utf-8') as json_bar_file:
        line = json_bar_file.read().encode('utf-8', 'ignore')

    bars = json.loads(line.decode('utf-8', 'ignore').replace('\r', '').replace('\n', ''))
    return bars


def get_biggest_bar(data):
    max = 0
    m = -1
    for i, b in enumerate(data):
        if max < b['Cells']['SeatsCount']:
            max = b['Cells']['SeatsCount']
            m = i
    return data[m]



def get_smallest_bar(data):
    min = 10000000
    m = -1
    for i, b in enumerate(data):
        if min > b['Cells']['SeatsCount']:
            min = b['Cells']['SeatsCount']
            m = i
    return data[m]


def get_closest_bar(data, longitude, latitude):
    min = 10000000
    m = -1
    for i, b in enumerate(data):
        dx = abs(longitude - b['Cells']['geoData']['coordinates'][1])
        dy = abs(latitude - b['Cells']['geoData']['coordinates'][0])
        # radius = power((power(dx, 2) + power(dy, 2)), 0.5)
        radius = ((dx ** 2)+(dy ** 2)) ** 0.5
        if min > radius:
            min = radius
            m = i
    return data[m]


if __name__ == '__main__':
    path = './Бары.json'
    bars = load_data(path)
    biggest = get_biggest_bar(bars)
    smallest = get_smallest_bar(bars)
    closest = get_closest_bar(bars, 55.889165, 37.707438)

