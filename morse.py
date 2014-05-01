#!/usr/bin/python
import sys
import json


def main():
    mappings = get_letter_to_code_mappings()
    if sys.argv[-1] == '-a':
        return get_whole_morse_codes_string(mappings)

    letter = get_wanted_letter()
    return mappings.get(letter)


def get_whole_morse_codes_string(mappings):
    """Get a string that represents all the mappings in the morse alphabet."""
    def tuple_to_string(letter_code_pair):
        """Convert a tuple to a mapping string."""
        letter, code = letter_code_pair
        return '{letter}: {code}'.format(letter=letter, code=code)

    items = mappings.items()
    sorted_items = sorted(mappings.items())
    return '\n'.join(map(tuple_to_string, sorted_items))


def get_letter_to_code_mappings():
    """Get Morse code mappings dictionary."""
    return {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
        'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l':
        '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
        'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
        'x': '-..-', 'y': '-.--', 'z': '--..', '=': '-...-', '?': '..--..',
        '/': '-..-.', ',': '--..--', '.': '.-.-.-', ':': '---...', '\'':
        '.----.', '-': '-....-', '(': '-.--.-', ')': '-.--.-', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '@': '.--.-.',
    }

def get_wanted_letter():
    return sys.argv[-1]


if __name__ == '__main__':
    print main()
