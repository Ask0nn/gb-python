from db_context import *
import os


menu: str = '\t1. Просмотр справочника\n' \
            '\t2. Добавить\n' \
            '\t3. Изменить\n' \
            '\t4. Удалить\n' \
            '\t0. Выход\n'


def show_all():
    contacts = Contacts.select()
    print('{:<8} {:<15} {:<10}'.format('#', 'Имя', 'Номер'))
    for contact in contacts:
        print('{:<8} {:<15} {:<10}'.format(contact.id, contact.name, contact.phones))


def add():
    print()
    line = input('Введите значения через пробел (несколько номеров через запятую)\n'
                 '{Имя телефон1,телефон2}')\
        .split(' ')
    Contacts.create(name=line[0], phones=line[1])
    print("Новый контакт добавлен")


def edit():
    show_all()
    _id = int(input('Введите # контакта который хотите изменить'))
    line = input('Введите значения через пробел (несколько номеров через запятую)\n'
                 '{Имя телефон1,телефон2}') \
        .split(' ')
    Contacts.update(name=line[0], phones=line[1]).where(Contacts.id == _id).execute()
    print("Контакт изменен")


def delete():
    show_all()
    _id = int(input('Введите # контакта который хотите удалить'))
    Contacts.delete().where(Contacts.id == _id).execute()
    print("Контакт удален")


init()
while(True):
    os.system('cls')
    print(menu)
    num = int(input('Выберите пункт меню (введите число):'))
    if num == 1:
        show_all()
    elif num == 2:
        add()
    elif num == 3:
        edit()
    elif num == 4:
        delete()
    elif num == 0:
        break
    input()

