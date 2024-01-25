"""
Morse Code Translator Function
摩斯密码

Objective:
Write a function named 'morse_translator' that translates a given string into Morse code.

Function Parameter:
text (string): The string to be translated into Morse code.

Instructions:
- Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
- The Morse code for each character should be separated by a space. 空格分开
- Each word in the string should be separated by a forward slash (/).
- The function should handle both uppercase and lowercase alphabetic characters. 大小写
- The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same. 对大小写字母一视同仁
- Non-alphabetic characters (like numbers or symbols) should not be translated. 非字母字符不翻译
- https://en.wikipedia.org/wiki/Morse_code

Example Test Cases:
1. morse_translator("HELLO WORLD") should return the Morse code for the given string.
2. morse_translator("Python") should return the Morse code for the given string.
3. morse_translator("Morse Code") should return the Morse code for the given string.
"""


def morse_translator(text):
    # Morse code mapping 摩斯密码映射
    morse_code_dict = {

        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Your code goes here
    # Remember to consider both upper and lower case letters, and spaces 要考虑大小写和空格
    # The function should return the translated Morse code string 返回翻译后的摩斯密码字符串


    morse = ''
    for char in text.upper(): # convert to upper case
        if char.isalpha(): #check if it is alphabet
            morse += morse_code_dict[char] + ' '
        elif char == ' ': #check if it is space
            morse += ' / '
        else:
            # if it is not alphabet or space, can not be translated
            return "Error: Can not translate non-alphabet, please input alphabet."

    return morse.strip() #remove the last space

# Morse code dictionary remains the same




# Test normal cases：

print(morse_translator("HELLO WORLD"))  
# Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

print(morse_translator("Python"))  
# Expected output: ".--. -.-- - .... --- -."

print(morse_translator("Morse Code"))
# Expected output: "-- --- .-. ... . / -.-. --- -.. ."


# Test cases for non-alphabet characters:
print(morse_translator("23"))  #number
print(morse_translator("Chesson is the best!")) #symbol
