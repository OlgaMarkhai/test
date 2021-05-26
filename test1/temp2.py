import numpy as np

number = str(np.random.randint(1, 101))  # загаданное число
print("Загадано число от 1 до 100")
predict = int(input("введите число"))  # предполагаемое число

def binary_search(number, predict):

    count = 0  # счетчик попыток
    lower_bound = 0
    upper_bound = len(number)
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        count += 1  # плюсуем попытку

        if number[middle] == predict:
            return middle

        elif number[middle] > predict:
            upper_bound = middle - 1
        elif number[middle] < predict:
            lower_bound = middle + 1
    print(f"Вы угадали число {number} за {count} попыток.")
binary_search(number, predict)
