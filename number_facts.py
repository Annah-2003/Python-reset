import tkinter as tk
import requests

def get_number_fact():
    global fact_label  # Make fact_label global
    number = int(number_entry.get())
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    if response.status_code == 200:
        fact = response.text
    else:
        fact = "Could not retrieve fact. Please try again later."
    fact_label.config(text=fact)

def main():
    global number_entry, fact_label
    root = tk.Tk()
    root.title("Number Facts")

    number_label = tk.Label(root, text="Enter a number:")
    number_label.pack()

    number_entry = tk.Entry(root)
    number_entry.pack()

    get_fact_button = tk.Button(root, text="Get Fact", command=get_number_fact)
    get_fact_button.pack()

    fact_label = tk.Label(root, text="")
    fact_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
