import csv
from collections import defaultdict


def menu() -> object:
    """"Эта функция выводит меню."""
    print(
        'Меню: ',
        'Вывести иерархию команд. ',
        'Вывести сводный отчёт по департаментам. ',
        'Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. ', sep="\n"
    )

    option = ''
    options = {'1': '1', '2': '2', '3': '3'}

    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()

    if option == '1':
        return teams()
    elif option == '2':
        return report()
    elif option == '3':
        return save_csv()


def open_csv():
    with open('Corp_Summary.csv') as file:
        return csv.DictReader(file, delimiter=";")


def teams():
    """"Эта функция выводит команды по департаментам"""
    # with open('Corp_Summary.csv') as file:

    reader = open_csv()
        # csv.DictReader(file, delimiter=";")
    slovar_ = defaultdict(set)

    for row in reader:
        slovar_[row['Департамент']].add(row['Отдел'])

    for team in slovar_.keys():
        print(team, ":", ', '.join(list(slovar_[team])))


def report():
    """"Эта функция создает сводный отчет по департаментам. Выводит название департамента, численность,
    зарплатную вилку и среднюю зарплату."""
    with open('Corp_Summary.csv') as file:
        reader = csv.DictReader(file, delimiter=";")
        slovar_ = defaultdict(set)

        for row in reader:
            slovar_[row['Департамент']].add(int(row['Оклад']))

        for team in slovar_.keys():
            print(team, ": ", len(slovar_[team]), ', ', min(slovar_[team]), '-', max(slovar_[team]), ', ',
                  0 if len(slovar_[team]) == 0 else sum(slovar_[team]) / len(slovar_[team]), sep="")


def save_csv():
    """ Эта функция сохраняет тот же самый отчет в csv.
    Выполнять для этого другую функцию не надо."""
    with open('Corp_Summary.csv') as file:
        reader = csv.DictReader(file, delimiter=";")
        slovar_ = dict()

        for row in reader:
            if row['Департамент'] in slovar_.keys():
                slovar_[row['Департамент']].append(int(row['Оклад']))
            else:
                slovar_[row['Департамент']] = [int(row['Оклад'])]
        report_ = []
        for team in slovar_.keys():
            row_ = [team, len(slovar_[team]), min(slovar_[team]), max(slovar_[team]),
                    0 if len(slovar_[team]) == 0 else sum(slovar_[team]) / len(slovar_[team])]
            report_.append(row_)

        filename = 'report.csv'
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(report_)


if __name__ == '__main__':
    menu()
