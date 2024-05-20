import requests

def get_number_fact(number):
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Could not retrieve fact. Please try again later."

def main():
    number = int(input("Enter a number to get a fact about it: "))
    fact = get_number_fact(number)
    print(f"Fact about {number}: {fact}")

if __name__ == "__main__":
    main()
