import random
import time
from datetime import datetime


def save_statistics(attempts, duration, success):
    """Сохраняет статистику игры в файл."""
    with open("game_stats.txt", "a", encoding="utf-8") as file:
        file.write(
            f"{datetime.now()} | Попыток: {attempts} | Время: {duration:.2f} сек | Результат: {'Победа' if success else 'Поражение'}\n")


def guess_number():
    """Основная логика игры."""
    number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            guess = int(input("Введи число: "))
            attempts += 1
            if guess < number:
                print("Слишком маленькое!")
            elif guess > number:
                print("Слишком большое!")
            else:
                print(f"Поздравляю! Ты угадал число {number} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, вводи только целые числа.")

    end_time = time.time()
    duration = end_time - start_time
    save_statistics(attempts, duration, success=True)


if __name__ == "__main__":
    guess_number()
