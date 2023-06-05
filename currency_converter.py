import tkinter as tk
from tkinter import messagebox
import requests

def currency_converter(amount, from_currency, to_currency):
    api_key = ''  # replace with your API key
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            exchange_rate = data['rates'].get(to_currency)
            if exchange_rate is not None:
                converted_amount = amount * exchange_rate
                return converted_amount
            else:
                messagebox.showerror('Invalid Currency', f"Invalid 'to' currency: {to_currency}")
        except ValueError:
            messagebox.showerror('Error', 'Invalid response received from the API.')
        except KeyError:
            messagebox.showerror('Invalid Currency', 'Invalid currency. Please check your input.')
    else:
        messagebox.showerror('Error', 'Unable to retrieve exchange rates. Please try again later.')

def convert_button_clicked():
    amount = float(entry_amount.get())
    from_currency = entry_from_currency.get().upper()
    to_currency = entry_to_currency.get().upper()

    converted_amount = currency_converter(amount, from_currency, to_currency)
    if converted_amount:
        messagebox.showinfo('Conversion Result', f'{amount} {from_currency} is equal to {converted_amount} {to_currency}')

# creates the main window
window = tk.Tk()
window.title('Currency Converter')

# creates the input fields and labels
label_amount = tk.Label(window, text='Amount:')
label_amount.grid(row=0, column=0, padx=10, pady=10)
entry_amount = tk.Entry(window)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

label_from_currency = tk.Label(window, text='From Currency:')
label_from_currency.grid(row=1, column=0, padx=10, pady=10)
entry_from_currency = tk.Entry(window)
entry_from_currency.grid(row=1, column=1, padx=10, pady=10)

label_to_currency = tk.Label(window, text='To Currency:')
label_to_currency.grid(row=2, column=0, padx=10, pady=10)
entry_to_currency = tk.Entry(window)
entry_to_currency.grid(row=2, column=1, padx=10, pady=10)

# creates the convert button
convert_button = tk.Button(window, text='Convert', command=convert_button_clicked)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# starts the main GUI event loop
window.mainloop()


