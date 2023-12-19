import os
import json
import logging
import argparse
from datetime import datetime


logging.basicConfig(filename='log_sys.log.', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('<идентификация пользователя>')



def baza():
    logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Старт программы")
    global s
    if os.path.isfile("next_users.json"):
        with open('next_users.json', 'r', encoding='UTF-8') as f:
            array = json.load(f)
            s = set()
            for level, val in array.items():
                for indev, name in val.items():
                    s.add(indev)
    else:
        array = {}
        s = set()
    while True:
        name = input('Введите имя: ')
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Пользователь ввел имя {name}")
        if name == 'exit':
            logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Завершение программы")
            break
        indef = (input("Введите личный идентификатор: "))
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')}"
                    f"Пользователь {name} ввел личный идентификатор {indef} ")
        if indef in s:
            print('такой айди есть, введите другой')
            logger.warning(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')}"
                           f"такой ID есть, введите другой")
            continue
        else:
            s.add(indef)
        level = (input("Введите уровень доступа (от 1 до 7): "))
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')}"
                    f"Пользователь {name} ввел уровень доступа {level} ")
        if int(level) > 7 or int(level) < 1:
            print("Введите корректный уровень доступа")
            logger.warning(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')}"
                           f"Некорректный уровень доступа")
            continue
        if level in array:
            array[level][indef] = name
        else:
            array[level] = {indef: name}
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Завершение программы")
        break

    print(array)
    with open('next_users.json', 'w', encoding='UTF-8') as f:
        json.dump(array, f, ensure_ascii=False, indent=2)


baza()


if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='log in to the system')
        parser.add_argument('name', metavar='name', type=str, nargs=1,
                            help='username')
        parser.add_argument('indef', metavar='indef', type=int, nargs=1,
                            help='user ID')
        parser.add_argument('level', metavar='level', type=int, nargs=1,
                            help='user access level')
        args = parser.parse_args()
        print(baza(args.name, args.indef, args.level))

