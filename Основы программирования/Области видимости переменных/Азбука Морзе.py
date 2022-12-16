MorseCode = {'A': '.-', 'B': '-...',
             'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-',
             'L': '.-..', 'M': '--', 'N': '-.',
             'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',
             'X': '-..-', 'Y': '-.--', 'Z': '--..',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.',
             '0': '-----', ', ': '--..--', '.': '.-.-.-',
             '?': '..--..', '/': '-..-.', '-': '-....-',
             '(': '-.--.', ')': '-.--.-'}

NewMorseCode = {}
for key, value in MorseCode.items():
    NewMorseCode[value] = key


def encode_to_morse(text):
    text = text.upper().split()
    for letter in text:
        print(" ".join([MorseCode[i] for i in letter]), end='', sep=' ')


def decode_from_morse(code):
    code = code.split()
    for character in code:
        print("".join(NewMorseCode[character]), end='', sep=' ')


def main():
    while True:
        question = int(input("1 - морзе => латиница\n2 - латиница => морзе"))
        if question == 1:
            decode_from_morse(input())

        elif question == 2:
            encode_to_morse(input())
