import random

answer_random = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова' ,'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет, я магический шар, и я знаю ответ на любой твой вопрос.')

name = ''
while len(name) == 0:
    name = input('Как я могу к тебе обращаться? ')

print(name + ',', 'я готов выслушать твой вопрос.')

while True:
    flag = ''                                       #Обнуляем флаг иначе не будет выхода из цикла
    
    answer = input()
    while len(answer) == 0:
        answer = input()
        
    print()
    print(random.choice(answer_random))
    print()
    print('У тебя есть ещё вопросы?')
    
    while len(flag) == 0:
        flag = input('y/n or д/н: ')
    
    if flag == 'y' or flag == 'д':
        print('Я готов выслушать твой вопрос. ')
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
