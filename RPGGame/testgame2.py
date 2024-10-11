import random

# Определение символов
WALL = "'🧱',"
FLOOR = "'🟫',"
EXIT = "'💎',"
PLAYER = "'😐',"

# Размеры карты
WIDTH = 11
HEIGHT = 11

# Создание пустой карты
map_data = [[FLOOR for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Генерация стен
for i in range(HEIGHT):
    for j in range(WIDTH):
        if i == 0 or i == HEIGHT - 1 or j == 0 or j == WIDTH - 1:
            map_data[i][j] = WALL

# Генерация случайных стен внутри карты
for _ in range(random.randint(40, 50)):
    i = random.randint(1, HEIGHT - 2)
    j = random.randint(1, WIDTH - 2)
    map_data[i][j] = WALL

# Генерация выхода
while True:
    i = random.randint(1, HEIGHT - 2)
    j = random.randint(1, WIDTH - 2)
    if map_data[i][j] == FLOOR:
        map_data[i][j] = EXIT
        break

# Генерация персонажа
while True:
    i = random.randint(1, HEIGHT - 2)
    j = random.randint(1, WIDTH - 2)
    if map_data[i][j] == FLOOR:
        map_data[i][j] = PLAYER
        break

# Вывод карты
for row in map_data:
    print(' '.join(row))
