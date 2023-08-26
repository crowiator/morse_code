# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  #  print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}






def text_to_morse_code(text):
    morse_code = []
    for word in text:
        if word == " ":
            new_word = " / "
        else:
            new_word = " " + ENGLISH_TO_MORSE[word.upper()] + " "
        morse_code.append(new_word)
    return morse_code

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
    new_word = list(ENGLISH_TO_MORSE.keys())[list(ENGLISH_TO_MORSE.values()).index(word)]
    text.append(new_word)
    word = ""
    return text
def list_to_string(list):
    str1 = ""
    for element in list:
        str1 += element

    return str1
def main():
    choose = input("Enter operation: \n 1. Text to Morse Code \n 2. Morse Code to Text ");
    if choose == 1:
        sentence = input(" Enter your text")
        morse_code = list_to_string(text_to_morse_code(sentence))
        print(morse_code)
    else:
        morse_code = input(" Enter your morse_code")
        sentence = list_to_string(morse_code_to_text(morse_code))
        print(sentence)

if __name__ == '__main__':
    main()