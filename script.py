"""
Booky is a return book system using translations of letters into id numbers.
This is to validate that the book being returned is the same as the one that was checked out, and to prevent fraud.
"""

# Translations for letters into id numbers
book_id = {
    'A': 243,
    'B': 192,
    'C': 892,
    'D': 407,
    'E': 518,
    'F': 368,
    'G': 217,
    'H': 349,
    'I': 501,
    'J': 920,
    'K': 188,
    'L': 218,
    'M': 427,
    'N': 888,
    'O': 791,
    'P': 101,
    'Q': 111,
    'R': 210,
    'S': 614,
    'T': 493,
    'U': 338,
    'V': 632,
    'W': 238,
    'X': 992,
    'Y': 763,
    'Z': 225
}

# Book scanner funciton
def scan_book(book_name):
    # Remove spaces
    book_name = book_name.replace(" ", "")
    
    # Loop through the letters
    translated_code = []
    for letter in book_name:
        translated_code.append(str(book_id.get(letter, 0)))
    return " ".join(translated_code)

# Prompt user for book name in capital letters
book_name = input("Please enter your book's name in ALL caps: ")
print(scan_book(book_name))