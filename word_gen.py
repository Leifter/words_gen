"""Скрипт для генерации случайного списка слов из файла words.lst"""

import random
import colorama
import os
colorama.init()


# Переопределение input для совместимости с Python 2
try:
    input = raw_input
except NameError:
    pass

def clearShell():
    #os.system(['clear', 'cls'][os.name == os.sys.platform])
    os.system('cls')


# Считываем строки из файла
with open("words.lst") as words:
    words_data = words.readlines()

words_clean = []
# Формируем список слов.
for word in words_data:
    word = word.split("\t")
    try:
        words_clean.append(word[1].replace('\n', ''))  # Убираем номера слов, оставляем только слово
    except IndexError:
        pass

print(words_clean)
# Вводим количество слов для проверки
num_words = int(input("Введите количество слов для запоминания: "))
# Генерируем индексы случайных слов
rand_indexes = []
while len(rand_indexes) < num_words:
    i = random.randint(0, len(words_clean))
    if i not in rand_indexes:
        rand_indexes.append(i)

# Выводим слова поочереди, очищая экран
n = 1
for i in rand_indexes:
    print("{:2}. {}".format(n, words_clean[i]), end='')
    input("")
    clearShell()    # Очищаем экран консоли
    n += 1

print("Слова закончились. Запишите результаты на бумажке. \n"
      "Дальше нажмите Enter 2 раза для вывода списка слов на экран и проверки результатов")
input()
input()

print("Вот список сгенерированных слов:")
n = 1
for i in rand_indexes:
    print("{:2}. {}".format(n, words_clean[i]))
    n += 1

