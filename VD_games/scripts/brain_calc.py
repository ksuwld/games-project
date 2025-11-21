import random
import operator

def get_expression():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    op = random.choice(list(operations.keys()))
    expr = f"{num1} {op} {num2}"
    answer = operations[op](num1, num2)
    return expr, answer

def main():
    print("VD-calc")
    print("Welcome to the VD games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    rounds = 3
    for _ in range(rounds):
        expr, answer = get_expression()
        print(f"What is the result of the expression?\nQuestion: {expr}")
        user_input = input("Your answer: ")
        try:
            user_answer = int(user_input)
        except ValueError:
            print(f"'{user_input}' is not a number ;(. Let's try again, {name}!")
            continue
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

