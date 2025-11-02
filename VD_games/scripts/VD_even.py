import random
import prompt


def is_even(number):
    return number % 2 == 0


def run_game():
    print("Welcome to the VD-games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_in_row = 0
    max_correct_answers = 3

    while correct_answers_in_row < max_correct_answers:
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ").lower()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_in_row += 1
        else:
            # Исправлена логика вывода правильного ответа
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return  # Выход из функции run_game при неверном ответе

    # Эти print'ы будут достигнуты только если цикл while завершится
    # успешно (т.е., пользователь дал 3 правильных ответа подряд)
    print("Correct!") # Этот print кажется избыточным, но оставлен по структуре
    print(f"Congratulations, {user_name}!")


def main():
    run_game()


if __name__ == "__main__":
    main()
