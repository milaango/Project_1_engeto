"""
main.py: první projekt do Engeto Online Python Akademie

author: Milan Angelis
email: milanangelis@seznam.cz
"""


TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


def count_numeric_strings(list_of_words: list) -> tuple:
    """
    Function that analyzes a list of words and returns a tuple
        with the count of numeric strings and their numerical sum.

    :param list_of_words: parameter "list_of_words" containing words (str)
    :type list_of_words: list
    :return: a pair of values where the first element is the count of numeric strings,
        and the second element is their numerical sum.
    :rtype: tuple

    :Example:
    >>> result = count_numeric_strings(["2", "ring", "82"])
    >>> result
    (2, 84)
    """

    numeric_strings = [string for string in list_of_words if string.isdigit()]
    sum_of_strings = len(numeric_strings)
    sum_of_numbers = 0
    for item in numeric_strings:
        sum_of_numbers += int(item)
    results = (sum_of_strings, sum_of_numbers)
    return results


def count_alphabetical_strings(list_of_words: list) -> tuple:
    """
    Function that analyzes a list of words and returns a tuple
        with the counts of titlecase, uppercase, and lowercase words.
    
    :param list_of_words: parameter "list_of_words" containing words (str)
    :type list_of_words: list
    :return: a tuple where the first, second and third element represents 
        the counts of titlecase, uppercase and lowercase words (in that order)
    :rtype: tuple

    :Example:
    >>> result = count_alphabetical_strings(["Honey", "ring", "sit", "MONKEY"])
    >>> result
    (1, 1, 2)
    """

    titles = 0
    uppercase_words = 0
    lowercase_words = 0
    for word in list_of_words:
        if word.istitle():
            titles += 1
        elif word.islower():
            lowercase_words += 1
        elif word.isupper():
            uppercase_words += 1
    word_counts = (titles, uppercase_words, lowercase_words)
    return word_counts


def count_frequencies(list_of_words: list) -> tuple:
    """
    Function that counts the frequencies of words with the same length,
        with the maximum length of words = 15.

    :param list_of_words: a list containing words (str)
    :type list_of_words: list
    :return: A tuple where the j-th element contains 
        the number of words with length j + 1
    :rtype: tuple

    :Example:
    >>> frequencies = count_frequencies(["NY", "ok", "ME", "365", "London"])
    >>> frequencies
    (0, 3, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    """
    
    counts = list()
    for number in range(15):
        calculator = 0
        for word in list_of_words:
            if len(word) == number + 1:
                calculator += 1
        counts.append(calculator)
    return tuple(counts)


# a dictionary containing usernames and passwords:
registered_users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}

# user's input (name and password):
user_name_input = str(input("username: "))
password_input = str(input("password: "))


if registered_users.get(user_name_input) == password_input:
    # if the username and password are in the dictionary 
    # of registered users, pass:
    sum_of_texts = len(TEXTS)
    print("-"*40)
    print(f"Welcome to the app, {user_name_input}")
    print(f"We have {sum_of_texts} texts to be analyzed.")
    print("-"*40)

    # choose one of the texts:
    choice = input(f"Enter a number btw. 1 and {sum_of_texts} to select: ")

    # if user's choice is not digit:
    if not choice.isdigit():
        print("You have not entered a number, terminating the program..")

    # if user's choice is out of range:
    elif int(choice) not in range(1, sum_of_texts + 1):
        print(
        "You have not chosen the right number, terminating the program.."
        )

    else:
        # creating a list of words without specific symbols (.,- etc.):
        words = (
            TEXTS[int(choice) - 1]
            .replace(".", "")
            .replace("    ", "")
            .replace(",", "")
            .replace("\n", " ")
            .replace("-"," ")
            .split(" ")
        )

        # analyzing the text using functions:

        sum_of_words = len(words)
        numeric_strings_sum, sum_of_numbers = count_numeric_strings(words)
        titlecase_words_sum, uppercase_words_sum, lowercase_words_sum = (
            count_alphabetical_strings(words)
        )

        print(f"There are {sum_of_words} words in the selected text.")
        print(f"There are {titlecase_words_sum} titlecase words.")
        print(f"There are {uppercase_words_sum} uppercase words.")
        print(f"There are {lowercase_words_sum} lowercase words.")
        print(f"There are {numeric_strings_sum} numeric strings.")
        print(f"The sum of all the numbers {sum_of_numbers}.")

        # printing a frequency chart for words of the same length:
        
        print("-" * 40)
        print(f"LEN|  OCCURENCES  |NR.")
        print("-" * 40)
        word_counts = count_frequencies(words)

        for number in range(len(word_counts)):
            if word_counts[number] != 0: # only if frequencies > 0
                stars = "*" * word_counts[number]
                gaps = " " * (20 - len(stars))
                
                if number < 9:
                    print(
                        " " 
                        + str(number + 1) 
                        + "|" 
                        + stars 
                        + gaps 
                        + "|" 
                        + str(len(stars))
                    )
                else:
                    print(
                        str(number + 1) 
                        + "|" 
                        + stars 
                        + gaps 
                        + "|" 
                        + str(len(stars))
                    )

else:
    print("unregistered user, terminating the program..")