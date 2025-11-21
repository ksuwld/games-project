import random
import math

def get_gcd_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    answer = math.gcd(num1, num2)
    return question, answer

def main():
    print("VD-gcd")
    print("Welcome to the VD games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    rounds = 3
    for _ in range(rounds):
        question, answer = get_gcd_question()
        print(f"Question: {question}")
        user_input = input("Your answer: ")
        try:
            user_answer = int(user_input)
        except ValueError:
            print(f"'{user_input}' is not a number ;(. Let's try again, {name}!")
            break
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()

