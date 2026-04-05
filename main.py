from logic import calculate

def main():
    print("Введите два числа и выберите операцию.")

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: нужно вводить только числа.")
        return

    operation = input("Выберите операцию (+, -, *, /): ")
    result = calculate(num1, num2, operation)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
