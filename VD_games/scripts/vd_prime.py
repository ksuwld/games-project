import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_game():
    n = random.randint(2, 100)
    print(f"Is {n} a prime number? (yes/no)")
    user = input().strip().lower()
    correct_answer = "yes" if is_prime(n) else "no"
    if user == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The answer was {correct_answer}.")

if __name__ == "__main__":
    prime_game()

