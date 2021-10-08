import random
import colorama
import os
colorama.init()

def clearShell():
    #os.system(['clear', 'cls'][os.name == os.sys.platform])
    os.system('cls')

with open("words.lst") as words:
    words_data = words.read()

words_clean = []
words_data = words_data.split("\n")
for word in words_data:
    word = word.split("\t")
    try:
        words_clean.append(word[1])
    except IndexError:
        pass


for word in words_data:
    word = word.split("\t")
    try:
        words_clean.append(word[1])
    except IndexError:
        pass

num_words = int(input("Введите количество слов для запоминания:"))

rand_indexes = []
while len(rand_indexes) < num_words:
    i = random.randint(0, len(words_clean))
    if i not in rand_indexes:
        rand_indexes.append(i)

n = 1
for i in rand_indexes:
    try:
        print("{:2}. {}".format(n, words_clean[i]), end='')
        input("")
        clearShell()
        n += 1
    except:
        print("Exception {}".format(1))

print("Слова закончились. Запишите результаты на бумажке, нажмите 2 раза Enter. И после проверьте результаты")
input()
input()

print("Вот их список")
n = 1
for i in rand_indexes:
    try:
        print("{:2}. {}".format(n, words_clean[i]))
        n += 1
    except:
        print("Exception {}".format(1))


# print(i)

# print(words_clean)