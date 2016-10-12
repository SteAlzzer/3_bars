# 3_bars

# Чё умеет?
Скрипт выводит
- самый маленький бар;
- самый большой бар;
- самый ближайший бар (по gps-координатам).

Для этого подсасывается БД баров в формате json.
Файл можно взять здесь: http://data.mos.ru/opendata/7710881420-bary

# Как это делает? (божественно)
Юзадж: python bars.py (-s|-b|-c longitude latitude)
### -s (--smallest) для поиска самого маленького бара
### -b (--biggest) для поиска самого большого бара
### -c (--closest longtitude latitude) для поиска самого ближайшего бара относительно долготы и широты


# Примерчики:
`python bars.py -p Бары.json -s`
`python bars.py -p Бары.json -b`
`python bars.py -p Бары.json -s -b`
`python bars.py -p Бары.json -c 55.889165 37.707438`
`python bars.py -p Бары.json -c 55.889165 37.707438 -s -b`