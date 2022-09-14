def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка-маляр 🦆 устала таскать этот дурацкий зонтик  '
        'Оставить ли ей его у друга? ️'
    )
    option2 = ''
    options2 = {'да': True, 'нет': False}
    while option2 not in options2:
        print('Выберите: {}/{}'.format(*options2))
        option2 = input()


def step2_no_umbrella():
    print(
        'Утка-маляр 🦆 все-таки попала под дождь, но рядом есть магазин с плащами  '
        'Купить ли ей плащ? ️'
    )
    option3 = ''
    options3 = {'да': True, 'нет': False}
    while option3 not in options3:
        print('Выберите: {}/{}'.format(*options3))
        option3 = input()


if __name__ == '__main__':
    step1()
