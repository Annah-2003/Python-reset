import random

def generate_fortune():
    fortunes = [
        "You will find happiness in unexpected places.",
        "A great adventure awaits you.",
        "Good things come to those who wait.",
        "A pleasant surprise is in store for you soon.",
        "You will meet someone special in the near future."
    ]
    return random.choice(fortunes)

def main():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    input("Press Enter to see your fortune...")
    fortune = generate_fortune()
    print(f"Your fortune: {fortune}")

if __name__ == "__main__":
    main()
