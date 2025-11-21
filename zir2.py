f = int(input("Введіть висоту ялинки: "))

for i in range(1, f + 1):
    print(" " * (f - i) + "*" * (2 * i - 1))