import random

def start_game():
    print("Welcome to the Guessing Game!")
    print("I've chosen a number between 1 and 100. Try to guess it!")

def generate_number():
    return random.randint(1, 100)

def check_guess(number, guess, attempts):
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        return True
    return False

def main():
    start_game()
    number_to_guess = generate_number()
    max_attempts = 3  
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        print(f"Attempts remaining: {max_attempts - attempts + 1}")
        guess = int(input("Enter your guess: "))
        if check_guess(number_to_guess, guess, attempts):
            break
        else:
            if attempts < max_attempts:
                print("Try again!")
            else:
                print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    main()
