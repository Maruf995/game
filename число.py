import random
def main():
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        result = int(input(f"Угадай результат этих чисел ({num1} * {num2}) "))
        if result == num2 * num1:
            print("Молодец")
        elif result - 5 <= num2 * num1 <= result + 5:
            print("Было близко")
        else:
            print("Прости, Ты слишком тупой")
if __name__ == '__main__':
    main()

