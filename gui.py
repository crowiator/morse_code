# Importing required modules

import tkinter as tk
import tkinter.scrolledtext as st

# English to morse
ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Text is transformed to morse code
def text_to_morse_code(text):
    morse_code = []
    for word in text:
        if word == " ":
            new_word = " / "
        else:
            new_word = " " + ENGLISH_TO_MORSE[word.upper()] + " "
        morse_code.append(new_word)
    return morse_code


# Morse code is transformed to text
def morse_code_to_text(morse_code):
    text = []
    word = ""
    for char in morse_code:
        if char == "/":
            new_word = " "
            text.append(new_word)
        elif char == " " and word != "":
            new_word = list(ENGLISH_TO_MORSE.keys())[list( ENGLISH_TO_MORSE.values()).index(word)]
            text.append(new_word)
            word = ""
        elif char != " ":
           word += char
    word = ""
    return text


# Convert array to string
def list_to_string(list):
    str1 = ""
    for element in list:
        str1 += element

    return str1


def encrypt():
    output_text_area.delete('1.0', tk.END)
    sentence = input_text_area.get("1.0",'end-1c')
    morse_code = list_to_string(text_to_morse_code(sentence))
    output_text_area.insert(tk.END, morse_code)

def dencrypt():
    output_text_area.delete('1.0', tk.END)
    morse_code = input_text_area.get("1.0",'end-1c')
    sentence = list_to_string(morse_code_to_text(morse_code))
    output_text_area.insert(tk.END, sentence)
# Creating tkinter window
win = tk.Tk()
# Title for the app
win.title("Morse Code")

# Title Label
tk.Label(win,
         text="Morse Code",
         font=("Times New Roman", 25),
         foreground="white").grid(column=0,
                                  row=0, columnspan=3)

# Input Label
tk.Label(win,
         text="Enter text",
         font=("Times New Roman", 15),
         foreground="white").grid(column=0,
                                  row=1)


# Creating scrolled text area
# widget with Read only by
# disabling the state
input_text_area = st.ScrolledText(win,
                            height=5, width=52,
                            font=("Times New Roman",
                                  15))

input_text_area.grid(column=0, row=2,columnspan=3)

# Encrypt Button
tk.Button(win,text = 'Encrypt!', bd = '5',
                          command = encrypt).grid(column=0, row=3)

# Dencrypt Button
tk.Button(win,text = 'Decrypt', bd = '5',
                          command = dencrypt).grid(column=2, row=3)

# Output Label
tk.Label(win,
         text="Output",
         font=("Times New Roman", 15),
         foreground="white").grid(column=0,
                                  row=4)

output_text_area = st.ScrolledText(win,
                            height=5, width=52,
                            font=("Times New Roman",
                                  15))

output_text_area.grid(column=0, row=5, columnspan=3)
win.mainloop()