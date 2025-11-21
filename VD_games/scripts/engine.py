def greet(game_name):
    print(f"Welcome to the VD Games! Playing {game_name}.")

def run_rounds(round_fn, rounds=3):
    for _ in range(rounds):
        if not round_fn():
            print("Wrong answer. Game over.")
            return
    print("Congratulations!")

