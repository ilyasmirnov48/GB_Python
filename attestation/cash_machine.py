import logging
import argparse
from datetime import datetime


logging.basicConfig(filename='cash.log.', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('<банкомат>')


def luxury(balance):
    if balance > 5_000_000:
        balance *= 0.9
    return balance


def add_money(balance):
    logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Запрос на внесение средств")
    balance = luxury(balance)
    successful_operation = False
    value = int(input('Введите сумму, которую необходимо внести: '))
    if value % 50 == 0:
        balance += value
        successful_operation = True
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Внесено = {value}")
    else:
        print('Операция не выполнена!\nВведите сумму кратную 50')
        logger.warning(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')}"
                       f"Операция отменена, введена сумма не кратная 50")
    return balance, successful_operation


def percent(value):
    commission = value * 0.015
    if commission < 30:
        commission = 30
    elif commission > 600:
        commission = 600
    return commission


def get_money(balance):
    logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Запрос на снятие средств")
    balance = luxury(balance)
    successful_operation = False
    value = int(input('Введите сумму, которую необходимо снять: '))
    write_offs = value + percent(value)
    if value % 50 == 0:
        if balance >= write_offs:
            balance -= write_offs
            successful_operation = True
            logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Снятие = {value}")
        else:
            print('Недостаточно средств!')
            logger.warning(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} На счете не достаточно средств")
    else:
        print('Операция не выполнена!\nВведите сумму кратную 50')
        logger.warning(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')}"
                       f"Операция отменена, введена сумма не кратная 50")
    return balance, successful_operation


count = 0
balance = 0
while True:
    logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Начало работы с банкоматом")
    print('1 - Пополнить счет;\n2 - Снять наличные;\n3 - Выйти.\n')
    command = int(input('Введите команду: '))
    if command == 1:
        balance, successful_operation = add_money(balance)
        if successful_operation:
            count += 1
    elif command == 2:
        balance, successful_operation = get_money(balance)
        if successful_operation:
            count += 1
    elif command == 3:
        logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Завершение работы с банкоматом")
        break
    else:
        print('Некорректная команда!!! Команда, должна содержать значения: 1 или 2 или 3')
        logger.warning(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Некорректная команда!!!")
    if count == 3:
        balance *= 1.03
        count = 0
    print('Ваш баланс: ', balance)
    logger.info(f"{datetime.now().strftime('%d %B %Y %H:%M:%S')} Информация о счёте: баланс = {balance}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Расчет коммисии')
    parser.add_argument('commission', metavar='value', type=int, nargs=1,
                        help='calculates the accrued interest')
    args = parser.parse_args()
    print(percent(*args.value))