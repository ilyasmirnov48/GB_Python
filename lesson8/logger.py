import os

def input_contact():
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w')
        f.close()
    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите фамилию, имя и телефон: ').strip().split()
        f.write(';'.join(user) + '\n')


def print_contacts():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
        for contact in contacts:
            print(*contact.strip().split(';'))


def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Фамилия \n2. Имя\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    data = input('Введите данные: ')
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[command_index-1]:
            print(' '.join(full_contact))


def change_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
        search = input('Введите фамилию, имя или номер телефона контакта,\nкоторый надо изменить: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        for i in range(len(full_contact)):
            if search == full_contact[i]:
                print(' '.join(full_contact))
                name = (';'.join(full_contact) + '\n')
                print('Какой параметр необходимо изменить?:\n1. Фамилия \n2. Имя\n3. Телефон')
                command_index = int(input('Команда: '))
                if command_index == 1:
                    full_contact[command_index-1] = input('Введите новую фамилию: ')
                elif command_index == 2:
                    full_contact[command_index-1] = input('Введите новое имя: ')
                elif command_index == 3:
                    full_contact[command_index-1] = input('Введите новый номер: ')
                else:
                    print('Других параметров нету.')
                print(' '.join(full_contact))
                for i in range(len(contacts)):
                    if name == contacts[i]:
                        contacts[i] = (';'.join(full_contact) + '\n')

            with open('data.txt', "w", encoding="UTF-8") as f:
                f.write("".join(contacts))


def delete_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
        delete = input('Введите фамилию, имя или номер телефона контакта,\nкоторый необходимо удалить: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        for i in range(len(full_contact)):
            if delete == full_contact[i]:
                name = (';'.join(full_contact) + '\n')
                print('Это контакт который надо удалить:', ' '.join(full_contact), '?\n1. да\n2. нет')
                command = int(input('Команда: '))
                if command == 1:
                    for i in range(len(contacts)):
                        if name == contacts[i]:
                            contacts.remove(contacts[i])
                            break
                elif command == 2:
                    return delete_contact()
                else:
                    print('Недопустимая команда!')

            with open('data.txt', "w", encoding="UTF-8") as f:
                f.write("".join(contacts))
