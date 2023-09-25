import random
computer_number = random.randint(1, 100)
attempts = 0

while True:
    player_input = input("Guess the number (1-100): ")
    attempts += 1

    if not player_input.isdigit():
        print("Invalid input.Try again...")
        continue

    player_num = int(player_input)
    if player_num > computer_number:
        print("Too High!")
    elif player_num < computer_number:
        print("Too Low!")
    else:
        print(f"Congratulations!!! You Guessed The Number {computer_number} , After {attempts} Attempts.")
        break
#END