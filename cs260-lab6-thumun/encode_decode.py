"""
testing the encode and decode methods from Shannon.py on actual data (covid
vaccine data) and sample files.
Author: Neha Thumu
Date: 10/28/21
"""

################################################################################
# IMPORTS
################################################################################

from Shannon import Shannon

################################################################################
# MAIN
################################################################################

def main():

    vaccines = read_file("data/vaccine_tweets_codes_source.csv", "ISO-8859-1")
    print(vaccines)

    # initialzing a character dictionary (for the characters in vaccines file)
    characters_dict = {}
    for character in vaccines:
        characters_dict[character] = 0

    # counting the number of characters
    for character in vaccines:
        characters_dict[character] += 1

    # print(characters_dict[" "])
    # print(len(vaccines))

    # intiializing and creating the dictionary of character probabibilities
    character_prob_dict = dict.fromkeys(characters_dict)
    for key in character_prob_dict:
        character_prob_dict[key] = characters_dict[key]/len(vaccines)

    # print(character_prob_dict)

    shannon = Shannon(character_prob_dict)
    tweets = read_file("data/vaccine_tweets_to_encode.csv", "ISO-8859-1")

    #print(shannon.shannon_encoding)

    tweets_encoded = shannon.encode(tweets)
    write_file("output/vaccine_tweets_encoded.txt", tweets_encoded,
    "ISO-8859-1")

    # tweets_decoded = shannon.decode(tweets_encoded)
    # print(tweets_decoded)

    secret_msg = read_file("data/secrete_message_to_decode.txt", "ISO-8859-1")
    secret_message_decoded = shannon.decode(secret_msg)

    write_file("output/secret_message_decoded.txt", secret_message_decoded,
    "ISO-8859-1")

    # print(secret_message_decoded)


    pass

################################################################################
# HELPER FUNCTIONS
################################################################################

def read_file(filename, encode="utf-8"):
    """
    This function reads in the contents of the file at the filename (string).
    The contents are returned as a string.
    """
    to_ret = ""
    file = open(filename, 'r', encoding=encode, newline="")
    for line in file:
        to_ret = to_ret + line
    file.close()
    return to_ret

def write_file(filename, output, encode="utf-8"):
    """
    This function writes output (string) to the file at the filename (string).
    """
    file = open(filename, 'w', newline="")
    file.write(output)
    file.close()

if __name__ == "__main__":
    main()
