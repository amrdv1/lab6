import random

def вгадай_число():
    число = random.randint(1, 100)
    спроби = 7

    print("Гра: Вгадай число!")
    print("Я загадав число від 1 до 100. У вас 7 спроб.")

    for i in range(1, спроби + 1):
        try:
            здогад = int(input(f"Спроба {i}: "))
        except ValueError:
            print("Вводьте лише число!")
            i -= 1
            continue

        if здогад == число:
            print(f"Вітаю! Ви вгадали число {число}!")
            return
        elif здогад < число:
            print("Більше.")
        else:
            print("Менше.")

    print(f"Ви не вгадали. Число було: {число}")

вгадай_число()