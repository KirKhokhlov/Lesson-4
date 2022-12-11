#!/usr/python3

import random

# Задание 1

border = "=" * 117
print(f"\n{border}\n\nЗадание 1\n")
sps = []
while len(sps) < 10:
    sps.append(random.randint(0, 10))
print("Массив: ", sps)
for i in range(0, len(sps)):
    for j in range(0, len(sps) - 1):
        if sps[j] > sps[j + 1]:
            sps[j], sps[j + 1] = sps[j + 1], sps[j]
print("Массив отсортирован по возрастанию:", sps)
print(f"\n{border}\n")

# Задание 2

print("Задание 2\n")
colors = dict()
colors["red"] = (255, 0, 0)
colors["green"] = (0, 255, 0)
colors["blue"] = (0, 0, 255)
for i in colors.keys():
    print(f"Цвет: {i} | RGB: {colors[i]}")
print(f"\n{border}\n")

# Задание 3

print("Задание 3\n")
firs_set = set()
second_set = set()
for i in range(0, 10):
    firs_set.add(random.randint(0, 10))
    second_set.add(random.randint(0, 10))
sets = [firs_set.intersection(second_set), firs_set.difference(second_set), second_set.difference(firs_set),
        firs_set.symmetric_difference(second_set)]
for i in range(len(sets)):
    if len(sets[i]) == 0:
        sets[i] = "таких элементов нет"
print("Первое множество:", firs_set)
print("Второе множество:", second_set, "\n")
print("Элементы, которые - ")
print("-входят одновременно в оба множества:", sets[0])
print("-входят только в первое, но не входят во второе:",  sets[1])
print("-входят только во второе, но не входят в первое:",  sets[2])
print("-входят в первое или во второе, но не в оба из них одновременно:",  sets[3])
print(f"\n{border}\n")

# Задание 4

print("Задание 4\n")
backpack_weight = 0
max_weight = 20
backpack = dict()
while True:
    print("1 - Положить пердмет\n2 - Удалить предмет\n3 - Посмотреть рюкзак\n4 - Закрыть рюкзак\n")
    choice = input("Введите выбранное действие: ")
    while choice not in {"1", "2", "3", "4"}:
        choice = input("Ошибка формата. Введите свой выбор снова: ")
    choice = int(choice)
    if choice == 1:
        name = input("Введите название предмета: ")
        weight = input("Введите вес предмета: ")
        while not weight.isdigit():
            weight = input("Ошибка формата. Введите вес снова: ")
        weight = int(weight)
        if weight + backpack_weight > max_weight:
            print("\nПредмет не уместить в рюкзак.")
            print(f"Вес рюкзака = {backpack_weight}/{max_weight}\n")
        else:
            backpack_weight += weight
            if name in backpack:
                backpack[name] += weight
            else:
                backpack[name] = weight
            print("\nВаш рюкзак (название предмета - вес предмета):")
            for i in backpack.keys():
                print(f"{i} - {backpack[i]}")
            print(f"Вес рюкзака = {backpack_weight}/{max_weight}\n")
    if choice == 2:
        if len(backpack.keys()) == 0:
            print("\nРюкзак пуст. Удалять нечего.\n")
        else:
            print("\nЧто вы хотите удалить?")
            print("Ваш рюкзак (название предмета - вес предмета):")
            for i in backpack.keys():
                print(f"{i} - {backpack[i]}")
            print(f"Вес рюкзака = {backpack_weight}/{max_weight}\n")
            name = input(": ")
            while name not in backpack.keys():
                name = input("Ошибка формата. Введите название предмета повторно: ")
            backpack_weight -= backpack.get(name)
            backpack.pop(name)
            print(f"\nПредмет {name} удалён.")
            if len(backpack.keys()) == 0:
                print("Рюкзак пуст.\n")
            else:
                print("Ваш рюкзак (название предмета - вес предмета):")
                for i in backpack.keys():
                    print(f"{i} - {backpack[i]}")
                print(f"Вес рюкзака = {backpack_weight}/{max_weight}\n")
    if choice == 3:
        if len(backpack.keys()) == 0:
            print("\nРюкзак пуст.\n")
        else:
            print("\nВаш рюкзак (название предмета - вес предмета):")
            for i in backpack.keys():
                print(f"{i} - {backpack[i]}")
            print(f"Вес рюкзака = {backpack_weight}/{max_weight}\n")
    if choice == 4:
        print("\nЗакрываю рюкзак...")
        break
print(f"\n{border}\n")
