print('Фомин Влаимир Александрович, Синергия, группа 106')

programms = [
    'Задание 1',
    'Задание 2',
]

def main():

    # Перечисляем существущие прогрраммы
    for pKey, programm in enumerate(programms):
        print(f'#{pKey} - {programm}')

    programm = int(input('Выберите программу: '))

    if programm == 0:
        print(f'Тут мы узнаем, принадлежит ли число интервалу от 100 до 999.')
        number = int(input('Введите число: '))

        if number >= 100 and number <= 999:
            print('Всё Ок! Число в диапазоне от 100 до 999 :)')
        else:
            print('Упс, число не ходит в диапазон, попроуйте снова.')

    elif programm == 1:
        print(f'Тут мы узнаем скидку на покупку. \n3% - от 500 р. и 5% - от 1000 р.')
        number = int(input('Введите стоимость: '))

        percent = number / 100

        if number >= 1000:
            discount = number - ( percent * 5 )
            print(f'Поздравляем, вам придоставляется скидка в 5% - {discount}')
        elif number >= 500 and number < 1000:
            discount = number - ( percent * 3 )
            print(f'Поздравляем, вам придоставляется скидка в 3% - {discount}')

    elif programm == 2:
        print(f'Тут мы узнаем скидку на покупку. \n3% - от 500 р. и 5% - от 1000 р.')
        number = int(input('Введите стоимость: '))

    # Хотите продожить?
    question = [
        f'Вы только что смотрели программу #{programm}',
        'Желаете продожить? [1 - Продожить, 0 - Выйти] ',
    ]

    answer = int(input('\n'.join(question)))

    if answer:
       main() 

main()
