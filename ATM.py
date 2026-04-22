import random


def show_menu():
    print("\n=== БАНК ===")
    print("1. Показать баланс")
    print("2. Пополнить счёт")
    print("3. Снять деньги")
    print("4. Выйти")


def check_pin(correct_pin):
    attempts = 3
    while attempts > 0:
        pin = input("Введите PIN-код: ")
        if pin == correct_pin:
            print("Доступ разрешён")
            return True
        else:
            attempts -= 1
            print(f"Неверный PIN. Осталось попыток: {attempts}")

    print("Доступ заблокирован. Пожалуйста, попробуйте позже.")
    return False


def show_balance(balance):
    print(f"\nВаш баланс: {balance:.2f} сом")


def deposit(balance):
    try:
        amount = float(input("Введите сумму пополнения: "))

        if amount <= 0:
            print("Сумма должна быть больше 0")
            return balance

        # 🎲 СЛУЧАЙНЫЙ БОНУС
        bonus = random.randint(0, 20)
        print(f"Бонус от банка: {bonus} сом")

        balance += amount + bonus
        print("Счёт успешно пополнен")

        return balance

    except ValueError:
        print("Ошибка: введите число")
        return balance


def withdraw(balance):
    try:
        amount = float(input("Введите сумму снятия: "))

        if amount <= 0:
            print("Сумма должна быть больше 0")
        elif amount > balance:
            print("Недостаточно денег")
        else:
            balance -= amount
            print("Деньги успешно сняты")

        return balance

    except ValueError:
        print("Ошибка: введите число")
        return balance


def main():
    balance = 0
    correct_pin = "jarkynai2009"

    if not check_pin(correct_pin):
        return

    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print("До свидания!")
            break

        else:
            print("Неверный выбор, попробуйте снова")


main()
