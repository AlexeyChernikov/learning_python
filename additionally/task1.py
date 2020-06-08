import collections as c
import os
import sys
import traceback


cur_collection = c.Counter("test message")

intro = """
1. Создать новую коллекцию
2. Подсчитать кол-во членов коллекции с помощью функции len()
3. Проверить принадлежность элемента к коллекции с помощью оператора in
4. Выполнить поиск подстроки
5. Выполнить обход коллекции с применением оператора цикла
6. Найти максимальный, минимальный элементы коллекции, а также сумму всех элементов
7. Найти кол-во определённого пользователем элемента коллекции
8. Выполнить конвертацию типа коллекции
9. Выполнить сортировку элементов коллекции
0. Завершить программу
"""

def task1():
    """ Создаёт новую коллекцию """
    global cur_collection
    new_collection = input("Введите новые элементы коллекции:\n")

    while True:
        print("1 - Разделить элем. через пробел\n2 - Не разделять")
        ans = input(">>> ")

        if ans == "1":
            cur_collection = c.Counter(new_collection.split(" "))
            break
        elif ans == "2":
            cur_collection = c.Counter(new_collection)
            break
        else:
            print("Неверная команда!\n")
        
    print("Новая коллекция создана!")

def task2():
    """ Печатает кол-во элем. в коллекции с помощью функции len() """
    print(f"Количество элементов в коллекции: {len(cur_collection)}")

def task3():
    """ Проверяет принадлежность элемента к коллекции с помощью оператора in """
    element = input("Введите элем., который хотите проверить: ")
    print("Элемент {0} коллекции".format("принадлежит" if element in cur_collection else "не принадлежит"))

def task4():
    """ Выполняет поиск подстроки в ключе """
    find_counter = 0
    substr = input("Введите подстроку: ")

    for key in cur_collection.keys():
        if substr in key:
            print(f"Найдено совпадение в ключе '{key}'")
            find_counter += 1
            
    if not find_counter:
        print("Совпадения не найдены!")
    
def task5():
    """ Выполняет обход коллекции с применением оператора цикла for """
    print("Элементы коллекции:")
    print("Ключ\tЗначение")
    for key, value in cur_collection.items():
        print(f"{key}\t{value}")

def task6():
    """ 
    Находит максимальный, минимальный элементы коллекции, а также сумму 
    всех элементов и выводит результаты на экран
    """
    print(f"Максимальный элемент: {max(cur_collection.values())}")
    print(f"Минимальный элемент: {min(cur_collection.values())}")
    print(f"Сумма элементов: {sum(cur_collection.values())}")

def task7():
    """ Находит кол-во определённого пользователем элемента коллекции """
    key = input("Введите желаемый элем.: ")
    print(f"Элемент '{key}' содержится в коллекции {cur_collection[key]} раз")

def task8():
    """ Выполняет конвертацию типа коллекции """
    # В демонстрационных целях конвертируется только в пределах функции
    print(f"Изначальная коллекция:\n{cur_collection}")
    print(f"Конвертация в обычный список:\n{list(cur_collection)}")
    print(f"Конвертация в обычный кортеж:\n{tuple(cur_collection)}")
    print(f"Конвертация в обычный словарь:\n{dict(cur_collection)}")

def task9():
    """ Выполняет сортировку элементов коллекции по ключу, по значению, по паре ключ-значение """
    print("Сортировка по ключу:")
    print("Отсортированная коллекция", sorted(cur_collection.keys()))
    print("Отсортированная коллекция в обратном порядке", sorted(cur_collection.keys(), reverse=True))

    print("Сортировка по значению:")
    print("Отсортированная коллекция", sorted(cur_collection.values()))
    print("Отсортированная коллекция в обратном порядке", sorted(cur_collection.values(), reverse=True))

    print("Сортировка по паре ключ-значение:")
    print("Отсортированная коллекция", sorted(cur_collection.items()))
    print("Отсортированная коллекция в обратном порядке", sorted(cur_collection.items(), reverse=True))

kill_program = lambda: sys.exit(0)

def main():
    os.system('cls')
    print(intro)

    while True:
        print(f"Текущая коллекция: {cur_collection}")
        try:
            tasks = {
                1: task1,
                2: task2,
                3: task3,
                4: task4,
                5: task5,
                6: task6,
                7: task7,
                8: task8,
                9: task9,
                0: kill_program
            }

            task_for_work = int(input("Введите номер задания: "))

            if task_for_work in tasks:
                tasks[task_for_work]()
            else:
                print("Задание не найдено!")

        except Exception:
            print("Ошибка при работе программы", traceback.format_exc())

        print()


if __name__ == "__main__":
    main()