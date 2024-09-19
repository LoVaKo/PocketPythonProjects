import random
from enum import Enum


class ConversionType(Enum):
    BINARY_TO_DECIMAL = 0
    BINARY_TO_HEX = 1
    DECIMAL_TO_BINARY = 2
    DECIMAL_TO_HEX = 3
    HEX_TO_BINARY = 4
    HEX_TO_DECIMAL = 5


class Notation(Enum):
    BINARY = 0
    DECIMAL = 1
    HEXADECIMAL = 2


CONVERSION_MAP = {
    ConversionType.BINARY_TO_DECIMAL: {
        'original_notation': Notation.BINARY,
        'new_notation': Notation.DECIMAL
    },
    ConversionType.BINARY_TO_HEX: {
        'original_notation': Notation.BINARY,
        'new_notation': Notation.HEXADECIMAL
    },
    ConversionType.DECIMAL_TO_BINARY: {
        'original_notation': Notation.DECIMAL,
        'new_notation': Notation.BINARY
    },
    ConversionType.DECIMAL_TO_HEX: {
        'original_notation': Notation.DECIMAL,
        'new_notation': Notation.HEXADECIMAL,
    },
    ConversionType.HEX_TO_BINARY: {
        'original_notation': Notation.HEXADECIMAL,
        'new_notation': Notation.BINARY,
    },
    ConversionType.HEX_TO_DECIMAL: {
        'original_notation': Notation.HEXADECIMAL,
        'new_notation': Notation.DECIMAL,
    },
}


def random_number(notation):
    if notation == Notation.BINARY:
        length = random.randint(3, 10)
        return '1' + ''.join(random.choice('01') for _ in range(length - 1))  # Start with 1 to prevent leading zeroes

    if notation == Notation.DECIMAL:
        return random.randint(0, 500)

    if notation == Notation.HEXADECIMAL:
        length = random.randint(2, 4)
        hex_digits = '0123456789ABCDEF'
        return ''.join(random.choice(hex_digits) for _ in range(length))


def convert(original_notation, new_notation, original_value):
    if original_notation == Notation.BINARY:
        decimal_value = int(original_value, 2)
    elif original_notation == Notation.DECIMAL:
        decimal_value = int(original_value)
    elif original_notation == Notation.HEXADECIMAL:
        decimal_value = int(original_value, 16)
    else:
        raise ValueError("Original notation not recognized")

    if new_notation == Notation.BINARY:
        return bin(decimal_value)[2:]  # Strip 0b prefix
    elif new_notation == Notation.DECIMAL:
        return str(decimal_value)
    elif new_notation == Notation.HEXADECIMAL:
        return hex(decimal_value)[2:].upper()  # Strip 0x prefix
    else:
        raise ValueError("New notation not recognized")


def check(correct_answer, user_answer):
    return correct_answer == str(user_answer)


def pick_conversion_type():
    choice = -1
    while choice < 0 or choice > 5:
        print("""
        -----Conversion Types-----   
        0. Binary to Decimal
        1. Binary to Hexadecimal
        2. Decimal to Binary
        3. Decimal to Hexadecimal
        4. Hexadecimal to Binary
        5. Hexadecimal to Decimal
        --------------------------
        """)

        try:
            choice = int(input("Please choose the conversion you'd like to practice [0-5] "))
            if choice < 0 or choice > 5:
                print("Invalid number. Please pick a number from 0 to 5.")
        except ValueError:
            print("Invalid input. Please provide a number.\n")

    return ConversionType(choice)


def check_answer(function, original_value, answer):
    return function(original_value, answer)


#  Main loop
keep_practicing = True

print("**** WELCOME TO CONVERSION PRACTICE ****")
while keep_practicing:
    conversion_type = pick_conversion_type()

    #  After picking conversion type, variables are automatically filled in with mapping
    mapping = CONVERSION_MAP[conversion_type]
    original_notation = mapping['original_notation']
    new_notation = mapping['new_notation']

    original_number = random_number(original_notation)
    correct_answer = convert(original_notation, new_notation, original_number)

    print(f"\nConverting from {original_notation.name} to {new_notation.name}: {original_number}")
    user_answer = input("Your answer: ")
    is_correct = check(correct_answer, user_answer)

    print("Your answer is: ", is_correct)

    if not is_correct:
        print("Correct answer:", correct_answer)

    yes_or_no = input("Do you want to continue practicing? [Y/n]").lower()
    if yes_or_no == 'n':
        print("Thanks for practicing!")
        keep_practicing = False
