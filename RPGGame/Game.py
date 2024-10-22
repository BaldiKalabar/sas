# рпг игра
import random, time,pygame
from tkinter import *
pygame.init()
#Музыка
smagagz=pygame.mixer.Sound("StartFonMus.ogg")
smagagz2=pygame.mixer.Sound("Fonmagaz2.ogg")
smaze=pygame.mixer.Sound("pec.ogg")
shagi=pygame.mixer.Sound("shagi.ogg")
sfonfight=pygame.mixer.Sound("Fonpvp.ogg")
sfonfight2=pygame.mixer.Sound("Fonpvp2.ogg")
sfonfight3=pygame.mixer.Sound("Fonpvp3.ogg")
sbosspvp=pygame.mixer.Sound("BossPvP.ogg")
sstartfonmusk=pygame.mixer.Sound("WTF.ogg")
sstartfonmusk.play(1,0,0)
name = input("Введите Имя")
time.sleep(1)
slosnot = int(input("Выберете уровень сложности  \n 1 - Простой 😆(Рекомендуеться) \n 2 - Средний ☺️ \n 3 - Сложный 🤬 \n 4 - БЕЗУМНЫЙ 😈 "))
while slosnot!= 1 and slosnot != 2 and slosnot != 3 and slosnot != 4:
    slosnot = int(input("Выберете уровень сложности  \n 1 - Простой 😆(Рекомендуеться) \n 2 - Средний ☺️ \n 3 - Сложный 🤬 \n 4 - БЕЗУМНЫЙ 😈 "))
time.sleep(1)
skin_pers = int(input("Выберете себе скин персонажа \n 1 - 😐 \n 2 - 👹 \n 3 - 😀 \n 4 - 😎 \n 5 - 🤗 \n 6 - 🤡 \n 7 - 😼"))
while skin_pers != 1 and skin_pers != 2 and skin_pers != 3 and skin_pers != 4 and skin_pers != 5 and skin_pers != 6 and skin_pers != 7:
    skin_pers = int(input("Выберете себе скин персонажа \n 1 - 😐 \n 2 - 👹 \n 3 - 😀 \n 4 - 😎 \n 5 - 🤗 \n 6 - 🤡 \n 7 - 😼"))
if skin_pers == 1:
    skin_pers = '😐'
if skin_pers == 2:
    skin_pers = '👹'
if skin_pers == 3:
    skin_pers = '😀'
if skin_pers == 4:
    skin_pers = '😎'
if skin_pers == 5:
    skin_pers = '🤗'
if skin_pers == 6:
    skin_pers = '🤡'
if skin_pers == 7:
    skin_pers = '😼'
smerti = 0
HERO = {
    "name": name
}
CHRS = {
    "Сила": 10,
    "Выносливость": random.randint(15, 45),
    "Усталость": random.randint(3, 7)
}
inventory = {
    "Броня": 15,
    "Зелье здоровья": random.randint(1, 5),
    "меч": 0,
    "щит": 0,
    'Money': 0,
    'ключ':0
}
NAME='Противник'
ENEMY = {
    "NAME": NAME,
    "Health": 100,
    "Hand": 100,
    "Зелья": 1
}
# Загрузка
max = random.randint(10, 100)
symb_load = '\\|/-\\|/-'
length_load = len(symb_load)
count = 0
heiqght = 10
p = 0
d = ""
loop = 1
# Карта
esda = 0
win = 0
pobeda = 0
Endwin = 0
fight = 0
mapgame = 1
rg = 0
run = 0
obxpole = 0
HERO = {
    "name": name,
    "Базовый урон": 15,
    '3': 100 + CHRS["Выносливость"] * 1,
    "И": inventory,
}
TOVARKOL = {
    'меч': 1,
    'щит': 1,
    'зелье здоровья': 50,
    'ключ': 1
}

TOVAR = {
    'меч': 150,
    'щит': 150,
    'зелье здоровья': 20,
    'ключ': 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
}
twopred = ''
pred = ''
magaz = 1
firstgomagaz=0
sstartfonmusk.stop()
while loop == 1:
    if magaz == 1:
        if firstgomagaz == 1:
            smagagz2.play(loops=1, maxtime=0, fade_ms=0)
            for i in range(2):

                print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                print("Вы заходите в Магазин.")
                time.sleep(1)
                print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                print("Вы заходите в Магазин..")
                time.sleep(1)
                print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                print("Вы заходите в Магазин...")
        if firstgomagaz == 0:
            smagagz.play(loops=1, maxtime=0, fade_ms=0)
            for i in range(8):
                print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                print("Вы заходите в Магазин.")
                time.sleep(1)
                print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                print("Вы заходите в Магазин..")
                time.sleep(1)
                print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                print("Вы заходите в Магазин...")
                time.sleep(0.5)
            firstgomagaz += 1


        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')

        print("Добро Пожаловать в Магазин Теней")
        pred = ''
        while pred != "выход":


            magazbye = 0
            mapmagaz = [
                ['🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱'],
                ['🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱'],
                ['🧱', '🧱', '🧱', '🔳', '🔳', '🔳', '🧱', '🧱', '🧱', '🧱'],
                ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
            mapmagaz1 = [['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱'],
                         ['🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🔳', '🔳', '🔳', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
            mapmagaz2 = [['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱'],
                         ['🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🔳', '🔳', '🔳', '🧱', '🧱', '🧱', '🧱'],
                         ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
            mapmagaz3false = [['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                              ['🧱', '❌', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                              ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '❌', '🧱', '🧱', '🧱'],
                              ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '❌', '🧱'],
                              ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                              ['🧱', '🧱', '🧱', '🔳', '🧱', '❌', '🧱', '🧱', '🧱', '🧱'],
                              ['🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱'],
                              ['🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🔳', '🧱', '❌', '🧱'],
                              ['🧱', '🧱', '🧱', '🔳', '🔳', '🔳', '🧱', '🧱', '🧱', '🧱'],
                              ['🧱', '❌', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
            mapmagaz3true = [['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                             ['🧱', '✅', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                             ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '✅', '🧱', '🧱', '🧱'],
                             ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '✅', '🧱'],
                             ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                             ['🧱', '🧱', '🧱', '🔳', '🧱', '✅', '🧱', '🧱', '🧱', '🧱'],
                             ['🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱'],
                             ['🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🔳', '🧱', '✅', '🧱'],
                             ['🧱', '🧱', '🧱', '🔳', '🔳', '🔳', '🧱', '🧱', '🧱', '🧱'],
                             ['🧱', '✅', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]

            mapmagazbye = [['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱'],
                           ['🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🔳', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
            mapmagazbye = [['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱'],
                           ['🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🔳', '🔳', '🔳', '🧱', '🧱', '🧱', '🧱'],
                           ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
            mapmagazrazgovorst = [['🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱'],
                                  ['🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱'],
                                  ['🧱', '🧱', '🧱', '🔳', '🔳', '🔳', '🧱', '🧱', '🧱', '🧱'],
                                  ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
            mapmagazrazgovorst2 = [['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                                   ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                                   ['🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                                   ['🔳', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱'],
                                   ['🧱', '🔳', '🧱', '🧱', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱'],
                                   ['🧱', '🧱', '🔳', '🧱', '🧱', '🧱', '🔳', '🧱', '🧱', '🧱'],
                                   ['🧱', '🧱', '🧱', '🔳', '🔳', '🔳', '🧱', '🧱', '🧱', '🧱'],
                                   ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
            for i in mapmagaz:
                for j in i:
                    print(j, end=' ')
                print('')
            print("У вас", inventory['Money'], "монет")
            pred = input(
                'Что хотите купить? (Чтобы выйти, напиши "выход")\n Для разговора нажми р-r. \nЧтобы посмотреть товар в магазине, нажми м-v.').lower()
            print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
            if pred != 'выход' and pred != 'h' and pred != 'р' and pred != 'м' and pred != 'v':
                print("у меня нет данного предмета")
            else:
                while pred == 'h' or pred == 'р':
                    print('Я [УДАЛЕНО] О чём ты хочешь поговорить?')
                    for i in mapmagazrazgovorst:
                        for j in i:
                            print(j, end=' ')
                        print('')
                    twopred = int(input(
                        "1-Кто ты вообще такой? \n2-Зачем ты открыл этот магазин? \n3-Как тебя зовут? \n4-О лабиринте \n5-О ключе-выходе\n6-Выйти"))
                    print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    while twopred != 1 and twopred != 2 and twopred != 3 and twopred != 4 and twopred != 5 and twopred != 6:
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                        print('Я [УДАЛЕНО] о чем ты хочеш поговорить?')
                        for i in mapmagazrazgovorst2:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        twopred = int(input(
                            "1-Кто ты вообще такой? \n2-Зачем ты открыл этот магазин? \n3-Как тебя зовут? \n4-О лабиринте  \n5-О ключе-выходе\n6-Выйти"))
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    if twopred == 1:
                        print("Я сгусток тьмы. От меня ничего не осталось. И я ничего не помню. И я не Виноват.")
                        for i in mapmagazrazgovorst2:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        time.sleep(4)
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    if twopred == 2:
                        print('Чтобы... вспомнить, кто я, собирая монеты, я что-то не вспоминаю')
                        for i in mapmagazrazgovorst2:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        time.sleep(4)
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    if twopred == 3:
                        print('О да меня зовут [УДАЛЕНО] и я могу помоч стать сильнее чем [ЗАБЛОКИРОВАНО]')
                        for i in mapmagazrazgovorst2:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        time.sleep(4)
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    if twopred == 4:
                        print(
                            'Лабиринт - это как место чистилища, ты должен пройти нужное количество кругов, чтобы выйти.')
                        for i in mapmagazrazgovorst2:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        time.sleep(4)
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    if twopred == 5:
                        print(
                            'А ты о той безделушке которую я недавно нашел, ну она мне не нужна так как я не в силе драться поэтому могу её тебе продать за твою жизнь или 250 монет')
                        TOVAR['ключ'] = 250

                        for i in mapmagazrazgovorst2:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        time.sleep(4)
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    if twopred == 6:
                        pred = 'ничего'
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                while pred == 'м' or pred == 'v':
                    for i in mapmagazrazgovorst:
                        for j in i:
                            print(j, end=' ')
                        print('')
                    print("У вас", inventory['Money'], "монет")
                    print("Что бы вернуться назад напиши (назад)")
                    print('Меч за твою жизнь или', TOVAR['меч'], 'монет')
                    print('Щит за', TOVAR['щит'], 'монет')
                    print('Зелье здоровья за', TOVAR['зелье здоровья'], 'монет')
                    print('Ключ за', TOVAR['ключ'], 'монет')
                    twopred = input('Так что хочеш купить?').lower()
                    while twopred != 'назад' and twopred != 'меч' and twopred != 'щит' and twopred != 'зелье здоровья' and twopred != 'ключ':
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                        for i in mapmagazrazgovorst:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        print("У вас", inventory['Money'], "монет")
                        print("Что бы вернуться назад напиши (назад)")
                        print('Меч за твою жизнь или', TOVAR['меч'], 'монет')
                        print('Щит за', TOVAR['щит'], 'монет')
                        print('Зелье здоровья за', TOVAR['зелье здоровья'], 'монет')

                        print('Ключ за', TOVAR['ключ'], 'монет')
                        twopred = input('Так что хочеш купить?').lower()
                    if twopred == 'назад':
                        pred = ''
                    if twopred == 'меч':
                        pred = 'меч'
                    if twopred == 'щит':
                        pred = 'щит'
                    if twopred == 'зелье здоровья':
                        pred = 'зелье здоровья'
                    if twopred == 'ключ':
                        pred = 'ключ'
                if pred == 'выход':
                    for i in mapmagazbye:
                        for j in i:
                            print(j, end=' ')
                        print('')
                    print("Увидимся снова, или нет_)")
                    time.sleep(2)
                    print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    print('Ну а мы продолжаем игру)')
                    time.sleep(2)
                    mapgame = 1
                    magaz = 0
                    Endwin = 0
                if pred == 'щит' or pred == 'зелье здоровья' or pred == 'меч' or pred == 'ключ':
                    if TOVARKOL[pred] != 0:
                        for i in mapmagaz2:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        time.sleep(2)
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                        if inventory['Money'] > TOVAR[pred]:
                            for i in mapmagaz3true:
                                for j in i:
                                    print(j, end=' ')
                                print('')
                            inventory['Money'] -= TOVAR[pred]
                            TOVARKOL[pred] = TOVARKOL[pred] - 1

                            if slosnot == 1:
                                if pred == 'меч':
                                    inventory['меч'] = 20
                                if pred == 'щит':
                                    inventory['щит'] = 30
                            if slosnot == 2:
                                if pred == 'меч':
                                    inventory['меч'] = 55
                                if pred == 'щит':
                                    inventory['щит'] = 55
                            if slosnot == 3:
                                if pred == 'меч':
                                    inventory['меч'] = 30
                                if pred == 'щит':
                                    inventory['щит'] = 52
                            if slosnot == 4:
                                if pred == 'меч':
                                    inventory['меч'] = 20
                                if pred == 'щит':
                                    inventory['щит'] = 20
                            if pred == 'ключ':
                                inventory['ключ'] = 1
                        else:
                            for i in mapmagaz3false:
                                for j in i:
                                    print(j, end=' ')
                                print('')
                        time.sleep(1)
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                        for i in mapmagaz2:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        time.sleep(2)
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                        for i in mapmagaz1:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        time.sleep(2)
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                        for i in mapmagaz1:
                            for j in i:
                                print(j, end=' ')
                            print('')
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    else:
                        print('У меня больше нет данного товара')

            print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
    rp = random.randint(1, 4)
    if rp == 1:
        pole = [['💎', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                ['💎', '🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🧱', skin_pers, '🧱'],
                ['💎', '🧱', '🟫', '🧱', '🟫', '🟫', '🧱', '🟫', '🧱', '🟫', '🧱'],
                ['💎', '🧱', '🟫', '🟫', '🟫', '🧱', '🧱', '🟫', '🧱', '🟫', '🧱'],
                ['💎', '🧱', '🟫', '🧱', '🟫', '🟫', '🧱', '🟫', '🟫', '🟫', '🧱'],
                ['💎', '🧱', '🟫', '🟫', '🧱', '🟫', '🟫', '🧱', '🟫', '🟫', '🧱'],
                ['💎', '🧱', '🟫', '🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🧱', '🧱'],
                ['💎', '🧱', '🧱', '🧱', '🟫', '🟫', '🧱', '🟫', '🟫', '🟫', '🧱'],
                ['💎', '🧱', '🟫', '🟫', '🟫', '🧱', '🟫', '🟫', '🟫', '🟫', '🧱'],
                ['💎', '🟫', '🟫', '🧱', '🧱', '🧱', '🟫', '🧱', '🧱', '🧱', '🧱'],
                ['💎', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
    if rp == 2:
        pole2 = [['💎', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                 ['💎', '🟫', '🟫', '🟫', '🟫', '🟫', '🧱', '🟫', '🟫', '🟫', '🧱'],
                 ['💎', '🧱', '🧱', '🧱', '🧱', '🟫', '🟫', '🟫', '🧱', '🟫', '🧱'],
                 ['💎', '🧱', '🟫', '🟫', '🟫', '🧱', '🟫', '🧱', '🟫', '🟫', '🧱'],
                 ['💎', '🧱', '🟫', '🧱', '🧱', '🧱', '🧱', '🧱', '🟫', '🟫', '🧱'],
                 ['💎', '🧱', '🟫', '🟫', '🟫', skin_pers, '🧱', '🟫', '🧱', '🟫', '🧱'],
                 ['💎', '🧱', '🟫', '🧱', '🧱', '🟫', '🧱', '🟫', '🧱', '🟫', '🧱'],
                 ['💎', '🧱', '🟫', '🟫', '🟫', '🟫', '🧱', '🟫', '🟫', '🟫', '🧱'],
                 ['💎', '🧱', '🟫', '🧱', '🧱', '🧱', '🧱', '🟫', '🧱', '🟫', '🧱'],
                 ['💎', '🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🧱', '🟫', '🧱'],
                 ['💎', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
    if rp == 3:
        pole3 = [['🧱', '💎', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '💎', '🧱'],
                 ['🧱', '🟫', '🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🧱'],
                 ['🧱', '🟫', '🧱', '🟫', '🟫', '🟫', '🧱', '🧱', '🧱', '🧱', '🧱'],
                 ['🧱', '🟫', '🧱', '🧱', '🟫', '🟫', '🧱', '🧱', '🟫', '🟫', '🧱'],
                 ['🧱', '🟫', '🧱', '🧱', '🧱', '🟫', '🧱', '🟫', '🧱', '🟫', '🧱'],
                 ['🧱', '🟫', '🧱', '🟫', '🟫', skin_pers, '🟫', '🟫', '🧱', '🟫', '🧱'],
                 ['🧱', '🟫', '🟫', '🟫', '🧱', '🟫', '🧱', '🟫', '🟫', '🟫', '🧱'],
                 ['🧱', '🟫', '🧱', '🟫', '🟫', '🟫', '🟫', '🧱', '🟫', '🧱', '🧱'],
                 ['🧱', '🧱', '🟫', '🧱', '🟫', '🧱', '🧱', '🧱', '🧱', '🟫', '🧱'],
                 ['🧱', '🟫', '🟫', '🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🧱'],
                 ['🧱', '💎', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '💎', '🧱']]
    if rp == 4:
        pole4 = [['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
                 ['🧱', '🟫', '🧱', '🧱', '🧱', '🧱', '🧱', '🟫', '🧱', '🟫', '🧱'],
                 ['🧱', skin_pers, '🟫', '🟫', '🧱', '🧱', '🧱', '🧱', '🧱', '🟫', '🧱'],
                 ['🧱', '🟫', '🧱', '🟫', '🟫', '🧱', '🟫', '🧱', '🧱', '🟫', '🧱'],
                 ['🧱', '🧱', '🟫', '🟫', '🧱', '🧱', '🟫', '🟫', '🟫', '💎', '🧱'],
                 ['🧱', '🧱', '🧱', '🟫', '🟫', '🧱', '🟫', '🧱', '🟫', '🟫', '🧱'],
                 ['🧱', '🟫', '🟫', '🟫', '🟫', '🧱', '🟫', '🟫', '🧱', '🟫', '🧱'],
                 ['🧱', '🟫', '🧱', '🟫', '🧱', '🟫', '🧱', '🧱', '🟫', '🟫', '🧱'],
                 ['🧱', '🟫', '🧱', '🧱', '🟫', '🧱', '🧱', '🧱', '🟫', '🟫', '🧱'],
                 ['🧱', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🧱', '🧱'],
                 ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱', '🧱']]
    if rp == 1:
        cordi1 = 1
        cordi2 = 9
        obxpole = pole
    if rp == 2:
        cordi1 = 5
        cordi2 = 5
        obxpole = pole2
    if rp == 3:
        cordi1 = 5
        cordi2 = 5
        obxpole = pole3
    if rp == 4:
        cordi1 = 2
        cordi2 = 1
        obxpole = pole4
    while Endwin == 0 and smerti == 0:
        smagagz.stop()
        smagagz2.stop()

        if slosnot == 1:
            ProtScet = random.randint(5, 8)
        if slosnot == 2:
            ProtScet = random.randint(4, 6)
        if slosnot == 3:
            ProtScet = random.randint(3, 5)
        if slosnot == 4:
            ProtScet = random.randint(2, 4)
        while mapgame == 1:
            # Игра на карте
            if mapgame == 1:
                smaze.play(1,0,0)
                run = 0
                print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                for i in obxpole:
                    for j in i:
                        print(j, end=' ')
                    print('')
                esda = input('Куда идём s=вниз w=вверх d=право a=лево')
                while esda != "a" and esda != "s" and esda != "d" and esda != "w" and esda != "ф" and esda != "ы" and esda != "в" and esda != "ц":
                    esda = input('Куда идём s=вниз w=вверх d=право a=лево')
                if esda == "s" or esda == 'ы':
                    shagi.play()
                    rg += 1
                    if rp == 1:
                        pole[cordi1][cordi2] = '🟫'
                        cordi1 = cordi1 + 1
                        if pole[cordi1][cordi2] == '🧱':
                            pole[cordi1][cordi2] = '🧱'
                            cordi1 = 1
                            cordi2 = 9
                            pole[cordi1][cordi2] = skin_pers
                        if pole[cordi1][cordi2] == '💎':

                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole[cordi1][cordi2] = skin_pers
                    if rp == 2:
                        pole2[cordi1][cordi2] = '🟫'
                        cordi1 = cordi1 + 1
                        if pole2[cordi1][cordi2] == '🧱':
                            pole2[cordi1][cordi2] = '🧱'
                            cordi1 = 5
                            cordi2 = 5
                            pole2[cordi1][cordi2] = skin_pers
                        if pole2[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole2[cordi1][cordi2] = skin_pers
                    if rp == 3:
                        pole3[cordi1][cordi2] = '🟫'
                        cordi1 = cordi1 + 1
                        if pole3[cordi1][cordi2] == '🧱':
                            pole3[cordi1][cordi2] = '🧱'
                            cordi1 = 5
                            cordi2 = 5
                            pole3[cordi1][cordi2] = skin_pers
                        if pole3[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole3[cordi1][cordi2] = skin_pers
                    if rp == 4:
                        pole4[cordi1][cordi2] = '🟫'
                        cordi1 = cordi1 + 1
                        if pole4[cordi1][cordi2] == '🧱':
                            pole4[cordi1][cordi2] = '🧱'
                            cordi1 = 2
                            cordi2 = 1
                            pole4[cordi1][cordi2] = skin_pers
                        if pole4[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole4[cordi1][cordi2] = skin_pers
                if esda == "w" or esda == 'ц':
                    shagi.play()
                    rg += 1
                    if rp == 1:
                        pole[cordi1][cordi2] = '🟫'
                        cordi1 = cordi1 - 1
                        if pole[cordi1][cordi2] == '🧱':
                            pole[cordi1][cordi2] = '🧱'
                            cordi1 = 1
                            cordi2 = 9
                            pole[cordi1][cordi2] = skin_pers
                        if pole[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole[cordi1][cordi2] = skin_pers
                    if rp == 2:
                        pole2[cordi1][cordi2] = '🟫'
                        cordi1 = cordi1 - 1
                        if pole2[cordi1][cordi2] == '🧱':
                            pole2[cordi1][cordi2] = '🧱'
                            cordi1 = 5
                            cordi2 = 5
                            pole2[cordi1][cordi2] = skin_pers
                        if pole2[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole2[cordi1][cordi2] = skin_pers
                    if rp == 3:
                        pole3[cordi1][cordi2] = '🟫'
                        cordi1 = cordi1 - 1
                        if pole3[cordi1][cordi2] == '🧱':
                            pole3[cordi1][cordi2] = '🧱'
                            cordi1 = 1
                            cordi2 = 9
                            pole3[cordi1][cordi2] = skin_pers
                        if pole3[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole3[cordi1][cordi2] = skin_pers
                    if rp == 4:
                        pole4[cordi1][cordi2] = '🟫'
                        cordi1 = cordi1 - 1
                        if pole4[cordi1][cordi2] == '🧱':
                            pole4[cordi1][cordi2] = '🧱'
                            cordi1 = 2
                            cordi2 = 1
                            pole4[cordi1][cordi2] = skin_pers
                        if pole4[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole4[cordi1][cordi2] = skin_pers
                if esda == "d" or esda == 'в':
                    shagi.play()
                    rg += 1
                    if rp == 1:
                        pole[cordi1][cordi2] = '🟫'
                        cordi2 = cordi2 + 1
                        if pole[cordi1][cordi2] == '🧱':
                            pole[cordi1][cordi2] = '🧱'
                            cordi1 = 1
                            cordi2 = 9
                            pole[cordi1][cordi2] = skin_pers
                        if pole[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole[cordi1][cordi2] = skin_pers
                    if rp == 2:
                        pole2[cordi1][cordi2] = '🟫'
                        cordi2 = cordi2 + 1
                        if pole2[cordi1][cordi2] == '🧱':
                            pole2[cordi1][cordi2] = '🧱'
                            cordi1 = 5
                            cordi2 = 5
                            pole2[cordi1][cordi2] = skin_pers
                        if pole2[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole2[cordi1][cordi2] = skin_pers
                    if rp == 3:
                        pole3[cordi1][cordi2] = '🟫'
                        cordi2 = cordi2 + 1
                        if pole3[cordi1][cordi2] == '🧱':
                            pole3[cordi1][cordi2] = '🧱'
                            cordi1 = 5
                            cordi2 = 5
                            pole3[cordi1][cordi2] = skin_pers
                        if pole3[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole3[cordi1][cordi2] = skin_pers
                    if rp == 4:
                        pole4[cordi1][cordi2] = '🟫'
                        cordi2 = cordi2 + 1
                        if pole4[cordi1][cordi2] == '🧱':
                            pole4[cordi1][cordi2] = '🧱'
                            cordi1 = 2
                            cordi2 = 1
                            pole4[cordi1][cordi2] = skin_pers
                        if pole4[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole4[cordi1][cordi2] = skin_pers
                if esda == "a" or esda == 'ф':
                    shagi.play()
                    rg += 1
                    if rp == 1:
                        pole[cordi1][cordi2] = '🟫'
                        cordi2 = cordi2 - 1
                        if pole[cordi1][cordi2] == '🧱':
                            pole[cordi1][cordi2] = '🧱'
                            cordi1 = 1
                            cordi2 = 9
                            pole[cordi1][cordi2] = skin_pers
                        if pole[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole[cordi1][cordi2] = skin_pers
                    if rp == 2:
                        pole2[cordi1][cordi2] = '🟫'
                        cordi2 = cordi2 - 1
                        if pole2[cordi1][cordi2] == '🧱':
                            pole2[cordi1][cordi2] = '🧱'
                            cordi1 = 5
                            cordi2 = 5
                            pole2[cordi1][cordi2] = skin_pers
                        if pole2[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole2[cordi1][cordi2] = skin_pers
                    if rp == 3:
                        pole3[cordi1][cordi2] = '🟫'
                        cordi2 = cordi2 - 1
                        if pole3[cordi1][cordi2] == '🧱':
                            pole3[cordi1][cordi2] = '🧱'
                            cordi1 = 5
                            cordi2 = 5
                            pole3[cordi1][cordi2] = skin_pers
                        if pole3[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole3[cordi1][cordi2] = skin_pers
                    if rp == 4:
                        pole4[cordi1][cordi2] = '🟫'
                        cordi2 = cordi2 - 1
                        if pole4[cordi1][cordi2] == '🧱':
                            pole4[cordi1][cordi2] = '🧱'
                            cordi1 = 2
                            cordi2 = 1
                            pole4[cordi1][cordi2] = skin_pers
                        if pole4[cordi1][cordi2] == '💎':
                            print("ERROR")
                            time.sleep(5)
                            Endwin = 1
                            mapgame = 0
                            magaz = 1
                        pole4[cordi1][cordi2] = skin_pers
                if rg == ProtScet:
                    mapgame = 0
                    fight = 1
        while fight == 1:
            smaze.stop()

            HPBoost = 0
            FightBooost = 0
            slboost = 0
            if inventory['ключ'] == 1:
                sfonfight.stop()
                NAME = 'Босс'
                HPBoost = 100
                FightBooost = 30
                slboost = random.randint(3,5)
                sbosspvp.play(1,0,0)
            else:
                musicl = random.randint(1, 3)
                if musicl == 1:
                    sfonfight.play(1, 0, 0)
                if musicl == 2:
                    sfonfight2.play(1, 0, 0)
                if musicl == 3:
                    sfonfight3.play(1, 0, 0)
            # Игра на битве
            if slosnot == 1:
                ENEMY['Health'] = random.randint(400, 450) + HPBoost
                ENEMY['Hand'] = random.randint(50, 70) + FightBooost
                ENEMY['Зелья'] = random.randint(1,4) + slboost
                CHRS['Сила'] = random.randint(100, 150)
                CHRS['Усталость'] = random.randint(10, 20)
                CHRS['Выносливость'] = random.randint(125, 150)
            if slosnot == 2:
                ENEMY['Health'] = random.randint(200, 220)+ HPBoost
                ENEMY['Hand'] = random.randint(80, 100)+ FightBooost
                ENEMY['Зелья'] = random.randint(1, 4) + slboost
                CHRS['Сила'] = random.randint(70, 100)
                CHRS['Усталость'] = random.randint(7, 10)
                CHRS['Выносливость'] = random.randint(125, 130)
            if slosnot == 3:
                ENEMY['Health'] = random.randint(190, 220)+ HPBoost
                ENEMY['Hand'] = random.randint(100, 130)+ FightBooost
                ENEMY['Зелья'] = random.randint(1, 4) + slboost
                CHRS['Сила'] = random.randint(60, 90)
                CHRS['Усталость'] = random.randint(5, 8)
                CHRS['Выносливость'] = random.randint(90, 100)
            if slosnot == 4:
                ENEMY['Health'] = random.randint(250, 300)+ HPBoost
                ENEMY['Hand'] = random.randint(130, 180)+ FightBooost
                ENEMY['Зелья'] = random.randint(1, 4) + slboost
                CHRS['Сила'] = random.randint(50, 90)
                CHRS['Усталость'] = random.randint(5, 8)
                CHRS['Выносливость'] = random.randint(50, 80)
            # Рандомная Стата в сложности
            if CHRS['Сила'] > 10 and CHRS['Сила'] < 25:
                if slosnot == 1:
                    inventory['Зелья здоровья'] = random.randint(6, 10)
                if slosnot == 2:
                    inventory['Зелья здоровья'] = random.randint(6, 8)
                if slosnot == 3:
                    inventory['Зелья здоровья'] = random.randint(4, 7)
                if slosnot == 4:
                    inventory['Зелья здоровья'] = random.randint(3, 5)
            if CHRS['Сила'] > 35 and CHRS['Сила'] < 245:
                if slosnot == 1:
                    inventory['Зелья здоровья'] = random.randint(8, 10)
                if slosnot == 2:
                    inventory['Зелья здоровья'] = random.randint(6, 8)
                if slosnot == 3:
                    inventory['Зелья здоровья'] = random.randint(4, 7)
                if slosnot == 4:
                    inventory['Зелья здоровья'] = random.randint(3, 5)
            for iter in range(max):
                temp = int(round(iter * 100 / 1000) // 2)
                if count >= length_load - 1:
                    count = 0
                else:
                    count += 1
                    time.sleep(0.1)
                print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
            max = random.randint(10, 50)
            symb_load = '\\|/-\\|/-'
            length_load = len(symb_load)
            count = 0
            heiqght = 10
            for iter in range(max):
                temp = int(round(iter * 100 / 1000) // 2)
                if count >= length_load - 1:
                    count = 0
                else:
                    count += 1
                    time.sleep(0.1)
                print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
            HERO["3"] = 100 * CHRS["Выносливость"] * 0.1 - 100
            print("Начальная Стата ", HERO['name'])
            print("Выносливость", CHRS["Выносливость"])
            print("Сила", CHRS["Сила"])
            print("зельки", inventory["Зелье здоровья"])
            health_icon = '❤'
            Hero_health_bar = int(HERO['3'] // 10) * health_icon
            Enemy_bar_health_icon = '❤'
            Enemy_bar_health_bar = ENEMY['Health'] * Enemy_bar_health_icon
            print(
                f'-----> Здоровье {name} \n{name} - {Hero_health_bar}  \n------> Здоровье {NAME} \n{NAME} - {Enemy_bar_health_bar}')
            while HERO["3"] > 0 and ENEMY['Health'] > 0:
                print("Количество атак", CHRS["Усталость"])
                if NAME == 'Босс':
                    d = input(
                        "-----> ⚔️Нажмите для атаки (a-ф)\n-----> 🧪Для использования зельки (s-ы) \n-----> 🔥Что бы восстановить силы (d-в) \n-----> 🏃‍➡️Что бы сбежать ERROR ")
                    print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    while d != "a" and d != "s" and d != "d" and d != "f" and d != "ф" and d != "ы" and d != "в" and d != "а":
                        d = input(
                            "-----> ⚔️Нажмите для атаки (a-ф)\n-----> 🧪Для использования зельки (s-ы) \n-----> 🔥Что бы восстановить силы (d-в) \n-----> 🏃‍➡️Что бы сбежать ERROR ")
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                else:
                    d = input(
                        "-----> ⚔️Нажмите для атаки (a-ф)\n-----> 🧪Для использования зельки (s-ы) \n-----> 🔥Что бы восстановить силы (d-в) \n-----> 🏃‍➡️Что бы сбежать PRESS (F-а) ")
                    print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                    while d != "a" and d != "s" and d != "d" and d != "f" and d != "ф" and d != "ы" and d != "в" and d != "а":
                        d = input(
                            "-----> ⚔️Нажмите для атаки (a-ф)\n-----> 🧪Для использования зельки (s-ы) \n-----> 🔥Что бы восстановить силы (d-в) \n-----> 🏃‍➡️Что бы сбежать PRESS (F-а) ")
                        print(heiqght * '\n', f'{symb_load[count]} - Загрузка', heiqght * '\n')
                if d == 'a' or d == 'ф':
                    if CHRS['Усталость'] != 0:
                        CHRS['Усталость'] -= 1
                        crit = random.randint(0, 20)
                        print('⚔️Критический урон составил ', crit)
                        ENEMY["Health"] = ENEMY["Health"] - HERO["Базовый урон"] - crit - inventory['меч']
                        Enemy_bar_health_bar = ENEMY['Health'] * Enemy_bar_health_icon
                        print(f'----->⚔️{NAME} получил урон \n{NAME} - {Enemy_bar_health_bar}')
                        if random.randint(1, 10) in [1, 2, 3, 4, 5]:
                            critprotiv = random.randint(0, 20)
                            print(f"----->⚔️{name} получил урон")
                            HERO["3"] = HERO["3"] - ENEMY["Hand"] + inventory["Броня"] - critprotiv + inventory['щит']
                            Hero_health_bar = int(HERO['3'] // 10) * health_icon
                            print(f'-----> Здоровье {name} \n{name}-{Hero_health_bar}')
                        else:
                            print(f"-----> {name} защитился🛡️🛡️🛡️")
                    else:
                        print("Вы устали, вам стоит отдохнуть")
                if d == 'f' or d == 'а':
                    if NAME == 'Босс':
                        print('ERROR')
                    else:
                        if CHRS['Усталость'] > 0:
                            if random.randint(1, 15) in [1]:
                                print("Вы сбежали")
                                run = 1
                                ENEMY["Health"] = -1000000
                            else:
                                CHRS['Усталость'] -= 1
                                HERO["3"] = HERO["3"] - ENEMY["Hand"] + inventory["Броня"] - random.randint(30, 50) + \
                                            inventory['щит'] + 10
                                print(f"⚔️{NAME} не отпускает вас")
                                Hero_health_bar = int(HERO['3'] // 10) * health_icon
                                print(f'-----> Здоровье {name} \n{name}-{Hero_health_bar}')
                        else:
                            print("Вы устали, вам стоит отдохнуть")
                if d == 's' or d == 'ы':
                    if inventory["Зелье здоровья"] > 0:
                        inventory['Зелье здоровья'] -= 1
                        HERO["3"] += 100
                        print(f"-----> {name} вылечелся 🧪")
                        Hero_health_bar = int(HERO['3'] // 10) * health_icon
                        print(f'-----> Здоровье {name} \n{name}-{Hero_health_bar}')
                        if random.randint(1, 6) in [1, 2]:
                            HERO["3"] = HERO["3"] - ENEMY["Hand"] + inventory["Броня"] + inventory['щит'] + 10
                            print(f"⚔️{NAME} воспользоволся моментом и нанес урон")
                            Hero_health_bar = int(HERO['3'] // 10) * health_icon
                            print(f'-----> Здоровье {name} \n{name}-{Hero_health_bar}')
                    else:
                        print("-----> Зельки больше нет")
                        if random.randint(1, 6) in [1, 2, 3, 6]:
                            HERO["3"] = HERO["3"] - ENEMY["Hand"] + inventory["Броня"] + 40
                            print("⚔️{NAME} воспользоволся моментом и нанес урон")
                            Hero_health_bar = int(HERO['3'] // 10) * health_icon
                            print(f'-----> Здоровье {name} \n{name}-{Hero_health_bar}')
                if d == 'd' or d == 'в':
                    if random.randint(1, 10) in [1, 2, 3, 4, 5, 6,]:
                        p = random.randint(1, 13)
                        if p in [1]:
                            print(HERO['name'], "агресивно смотрит на ", ENEMY['NAME'])
                        if p in [2]:
                            print(HERO['name'], "ничего не делает как и ",ENEMY['NAME'])
                        if p in [3]:
                            print(HERO['name'], "думает о великом и забывает про битву, как и ",ENEMY['NAME'])
                        if p in [4]:
                            print(HERO['name'], "спрятался, техническое отступление")
                        if p in [5]:
                            print("Никто не попал")
                        if p in [6]:
                            print("Вы изучаете друг друга для того что бы нанести более сильный удар")
                        if p in [7]:
                            print(f"Вы пытаетесь украть зелья {NAME} но у вас это не получается")
                        if p in [8]:
                            print("Вы устали но продолжаете бороться")
                        if p in [9]:
                            print("Вы прячитесь что бы отдохнуть от этой битвы , теперь вы можете нанести удар")
                        if p in [10]:
                            print(
                                f"Вы отвлекаете {NAME} максимально долго что бы востоновить силы для следущего удара")
                        if p in [11]:
                            print("Вы выпустили пауков, откуда они у вас? Неважно вы можете атаковать ")
                        if p in [12]:
                            print(HERO["name"], "Не сдавайся, в тебя и так никто не верит")
                        if p in [13]:
                            print(HERO["name"], "Наполняется решимостью довести битву до конца")
                        CHRS['Усталость'] += 1
                        if random.randint(1, 20) in [1, 6]:
                            print("Вам повезло и вы нашли ещё зельек")
                            inventory["Зелье здоровья"] += random.randint(1, 2)
                    else:
                        HERO["3"] = HERO["3"] - ENEMY["Hand"] + inventory["Броня"] + 10 + inventory['щит'] - FightBooost
                        print(f"⚔️{NAME} воспользоволся моментом и нанес урон")
                        Hero_health_bar = int(HERO['3'] // 10) * health_icon
                        print(f'-----> Здоровье {name} \n{name}-{Hero_health_bar}')
                if ENEMY["Health"] < 80 and run != 1:
                    if ENEMY["Зелья"] > 0:
                        ENEMY["Health"] += random.randint(1, 60)
                        Enemy_bar_health_bar = ENEMY['Health'] * Enemy_bar_health_icon
                        ENEMY["Зелья"] -= 1
                        print(f'----->🧪 {NAME} вылечелся и теперь у него  \n{NAME} - {Enemy_bar_health_bar}')
                        if random.randint(1, 6) in [1, 2, 3]:
                            print(f"⚔️{name} воспользоволся моментом и нанес урон")
                            ENEMY["Health"] = ENEMY["Health"] - HERO["Базовый урон"] - inventory['меч']
                            Enemy_bar_health_bar = ENEMY['Health'] * Enemy_bar_health_icon
                            print(f'-----> Здоровье {NAME} \n{NAME} - {Enemy_bar_health_bar}')
                    else:
                        pass
            if HERO["3"] < 0 and ENEMY["Health"] < 0:
                print("КАК ВЫ ОБА УМЕРЛИ ? Чтож считайте что это ничья")
            if HERO["3"] < 0:
                defaut=input("")
                smerti = 1
                Endwin = 2
                fight = 0
                s = random.randint(1, 5)
                if s == 1:
                    print(f"Ты помер, {name} попробуй ещё раз")
                if s == 2:
                    print(f"В тебя и так не кто не верил, {name} попробуй ещё раз")
                if s == 3:
                    print(f"Не сдавайся!, {name} попробуй ещё раз, в этот раз тебе больше повезет")
                if s == 4:
                    print(f"Ты... {name} попробуй ещё раз")
                if s == 5:
                    print('ХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХХАХАХАХАХАХХАХАХАХХАХАХАХАХХАХАХАХАХАХАХ')
                time.sleep(4)
                print('Переходим на главный экран')
                time.sleep(4)
            if ENEMY["Health"] < 0:
                if run == 1:
                    if slosnot == 1:
                        ProtScet = random.randint(5, 8)
                    if slosnot == 2:
                        ProtScet = random.randint(4, 6)
                    if slosnot == 3:
                        ProtScet = random.randint(3, 5)
                    if slosnot == 4:
                        ProtScet = random.randint(2, 4)
                    fight = 0
                    mapgame = 1
                    sfonfight.stop()
                    sfonfight2.stop()
                    sfonfight3.stop()
                    time.sleep(4)
                    print("Возрашаемся на карту...")
                    time.sleep(3)
                    rg = 0
                else:
                    if run == 0:
                        rm = 0
                        if slosnot == 1:

                            rm = random.randint(30, 35)
                            inventory["Money"] += rm
                        if slosnot == 2:
                            rm = random.randint(20, 25)
                            inventory["Money"] += rm
                        if slosnot == 3:
                            rm = random.randint(15, 20)
                            inventory["Money"] += rm
                        if slosnot == 4:
                            rm = random.randint(10, 18)
                            inventory["Money"] += rm
                    wn= random.randint(1,5)
                    if wn == 1:
                        print(f"{NAME} умер, ПОБЕДА🎉🎉🎉")
                    if wn == 2:
                        print('В тебя все верели но надо продолжать🎉🎉🎉')
                    if wn == 3:
                        print('Противник был повержен в пух и прах🎉🎉🎉')
                    if wn == 4:
                        print('Никогда несдавайся и у тея всё получиться, а пока что ПОБЕДА🎉🎉🎉')
                    if wn == 5:
                        print('ПОБЕДА🎉🎉🎉')
                    if NAME !='Босс':

                        print('Вы получили', rm, 'монет')
                        if slosnot == 1:
                            ProtScet = random.randint(5, 8)
                        if slosnot == 2:
                            ProtScet = random.randint(4, 6)
                        if slosnot == 3:
                            ProtScet = random.randint(3, 5)
                        if slosnot == 4:
                            ProtScet = random.randint(2, 4)
                        fight = 0
                        mapgame = 1
                        time.sleep(4)
                        print("Возрашаемся на карту...")
                        time.sleep(3)
                        rg = 0
                        sfonfight.stop()
                        sfonfight2.stop()
                        sfonfight3.stop()
                    else:
                        sbosspvp.stop()
                        print('Вы получили, свободу')
                        time.sleep(5)
                        win = 1
                        fight = 0
                        Endwin = 1
    if smerti == 1:
        sfonfight.stop()
        sfonfight2.stop()
        sfonfight3.stop()
        sbosspvp.stop()
        loop = input("Ты умер... Ты это знаеш? Так вот, хочешь заного начать? \n (ДА) --- (НЕТ)").lower()
        win = 0
        while loop != "ДА" and loop != 'Да' and loop != 'да' and loop != 'нет' and loop != 'НЕТ' and loop != 'Нет':
            loop = input("Ты умер... Ты это знаеш? Так вот, хочешь заного начать? \n (ДА) --- (НЕТ)").lower()
            win = 0
    if win == 1:
        sbosspvp.stop()
        loop = input("Ты победил, но готов ты начать ещё  раз? \n (ДА) --- (НЕТ)").lower()
        while loop != "ДА" and loop != 'Да' and loop != 'да' and loop != 'нет' and loop != 'НЕТ' and loop != 'Нет':
            loop = input("Ты победил, но готов ты начать ещё  раз? \n (ДА) --- (НЕТ)").lower()
    if loop == 'да':
        loop = 1
        Endwin = 0
        mapgame = 0
        smerti = 0
        win = 0
        rg = 0
        magaz = 1
        NAME = 'Противник'
        inventory['ключ'] = 0
        TOVARKOL['ключ'] = 1
    if loop == 'нет':
        loop = 0
        mapgame = 0
        smerti = 0
        win = 0
        Endwin = 0