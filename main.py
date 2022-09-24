morse = [
    {'A': '.-'},
    {'B': '-...'},
    {'C': '-.-.'},
    {'D': '-..'},
    {'E': '.'},
    {'F': '..-.'},
    {'G': '--.'},
    {'H': '....'},
    {'I': '..'},
    {'J': '.---'},
    {'K': '-.-'},
    {'L': '.-..'},
    {'M': '--'},
    {'N': '-.'},
    {'O': '---'},
    {'P': '.--.'},
    {'Q': '--.-'},
    {'R': '.-.'},
    {'S': '...'},
    {'T': '-'},
    {'U': '..-'},
    {'V': '...-'},
    {'W': '.--'},
    {'X': '-..-'},
    {'Y': '-.--'},
    {'Z': '--..'},
    {'1': '.----'},
    {'2': '..---'},
    {'3': '...--'},
    {'4': '....-'},
    {'5': '.....'},
    {'6': '-....'},
    {'7': '--...'},
    {'8': '---..'},
    {'9': '----.'},
    {'0': '-----'},
    {' ': '/'}
]

string = input('Type the word you would like to convert to morse code: ')

def morse_converter(str):
    string_to_convert = [*str.upper()]
    morse_string = []
    for char in string_to_convert:
        for index in range(len(morse)):
            for key, value in morse[index].items():
                if char == key:
                    morse_string.append(value)
        morse_string.append(' ')

    morse_string = ''.join(morse_string)
    return morse_string


converted_str = morse_converter(string)
print(converted_str)

