from logger import input_contact, print_contacts, find_contact, change_contact, delete_contact


def interface():
    text = '' \
           "Главное меню:\n" \
           "1. Добавить контакт\n" \
           "2. Посмотреть все контакты\n" \
           "3. Найти контакт\n"\
           "4. Изменить контакт\n"\
           "5. Удалить контакт\n"\
           "\n"\
           "0. Выход\n"
    print(text)
    while True:
        comand = int(input('Введите команду: '))
        if comand == 1:
            input_contact()
        if comand == 2:
            print_contacts()
        if comand == 3:
            find_contact()
        if comand == 4:
            change_contact()
        if comand == 5:
            delete_contact()
        if comand == 0:
            return
        print('_' * 30)

if __name__ == '__main__':
    interface()