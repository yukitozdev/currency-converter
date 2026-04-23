import tkinter as tk
from tkinter import messagebox
from converters import brl_to_usd, brl_to_eur, usd_to_brl, eur_to_brl

def converter_currency():
    try:
        amount = float(entry_amount.get())
        option = selected_option.get()

        if option == "BRL to USD":
            result = brl_to_usd(amount)
            symbol = "$"
        
        elif option == "BRL to EUR":
            result = brl_to_eur(amount)
            symbol = '€'

        elif option == "USD to BRL":
            result = usd_to_brl(amount)
            symbol = "R$"
        
        elif option == "EUR to BRL":
            result = eur_to_brl(amount)
            symbol = "R$"
        
        result_label.config(text=f"Result: {symbol}{result:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Currency converter")
root.geometry("350x250")
root.resizable(False,False)

title_label = tk.Label(root, text="Currency Converter", font=("Arial", 16))
title_label.pack(pady=5)

selected_option = tk.StringVar()
selected_option.set ("BRL to USD")

option = [
    "BRL to USD",
    "BRL to EUR",
    "USD to BRL",
    "EUR to BRL"
]

dropdown = tk.OptionMenu(root, selected_option, *option)
dropdown.pack(pady=5)

entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=converter_currency)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()