csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(csv):
    """Чтение данных"""
    return [x.split(';') for x in csv.split('\n')]


def _sort(data):
    print('Словарь до сортировки', data)
    return sorted(data, key=lambda x: int(x[1]))


def _filter(data):
    return [x for x in data if int(x[1]) > 10]


def main():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


if __name__ == '__main__':
    print(main())
