# Список денежных купюр
bills = [64, 32, 16, 8, 4, 2, 1]

# Функция для выплаты суммы n
def pay_amount(n):
    # Словарь для хранения количества купюр каждого достоинства
    bill_count = {bill: 0 for bill in bills}

    # Цикл по купюрам с самым большим достоинством до самой маленькой
    for bill in bills:
        # Считаем сколько купюр каждого достоинства нужно
        while n >= bill:
            bill_count[bill] += 1
            n -= bill

    # Возвращаем словарь с количеством купюр каждого достоинства
    return bill_count


# Тестируем функцию
n = input("Введите необходимую сумму: ")
bukv = n.isdigit()
if bukv == False:  # проверка на буквы
    while bukv == False:
        n = input("Введите число большее 1(цифрами): ")
        bukv = str.isnumeric(n)
n = int(n)
print(pay_amount(n))