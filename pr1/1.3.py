# -- coding: utf-8 --
age = int(input('Введите ваш возраст: '))
name = str(input('Введите своё имя: '))
if age<=0 and age>=75:
    print('ошибка')
    exit()
if name == 'Иван':
    print('ошибка')
    exit()
if age >= 16:
    print('Поздравляем вы поступили в ВГУИТ')
else:
    print('Сначала нужно окончить школу')
    print('Вам осталось учиться', 16-age, 'года')

