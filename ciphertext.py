from tkinter import *
from tkinter import messagebox
def caesar(start_text, shift_amount, cipher_direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    result_label.config(text=f"Here's the {cipher_direction}d result: {end_text}")

window = Tk()
window.title("Caesar Cipher")
window.config(padx=500, pady=200)

logo = Label(text="Caesar Cipher", font=("Arial", 24, "bold"))
logo.grid(column=0, row=0, columnspan=2)

text_input = Entry(width=40)
text_input.grid(column=0, row=1, columnspan=2, pady=10)

shift_input = Entry(width=10)
shift_input.grid(column=0, row=2)

shift_label = Label(text="Shift Number")
shift_label.grid(column=1, row=2)

direction_label = Label(text="Select Direction")
direction_label.grid(column=0, row=3)

direction_var = StringVar()
direction_var.set("encode")

encode_radio = Radiobutton(text="Encode", value="encode", variable=direction_var)
encode_radio.grid(column=0, row=4)

decode_radio = Radiobutton(text="Decode", value="decode", variable=direction_var)
decode_radio.grid(column=1, row=4)

result_label = Label(text="")
result_label.grid(column=0, row=5, columnspan=2)

def cipher_button_click():
    text = text_input.get().lower()
    shift = int(shift_input.get()) % 26
    direction = direction_var.get()
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

cipher_button = Button(text="Encrypt/Decrypt", command=cipher_button_click)
cipher_button.grid(column=0, row=6, columnspan=2)

def reset():
    text_input.delete(0, END)
    shift_input.delete(0, END)
    direction_var.set("encode")
    result_label.config(text="")

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=0, row=7, columnspan=2)

window.mainloop()