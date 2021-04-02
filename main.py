# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import *

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Могу я узнать, как тебя зовут?')
name = input()
print('Привет,', name)

while True:
    print('Задай вопрос, ответом на который будет "да" или "нет"')
    question = input()
    print(choice(answers))
    print('Если хотите задать еще один вопрос нажмите "д"')
    string = input().lower()
    if string == 'д':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break