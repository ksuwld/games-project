import random

def progression_round():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    progression = [start + i * step for i in range(length)]
    missing_index = random.randint(0, length - 1)
    answer = progression[missing_index]
    progression_with_missing = progression.copy()
    progression_with_missing[missing_index] = ".."
    print("Question:", ' '.join(str(x) for x in progression_with_missing))
    user = input("What number is missing? ")
    if user.strip() == str(answer):
        print("Correct!")
        return True
    else:
        print(f"Wrong! The answer was {answer}.")
        return False


