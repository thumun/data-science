"""

Class for creating the Shannon encoding algorithm and applying it to data sets.

Author: Neha Thumu
Date: 10/28/20
"""

import math

################################################################################
# CLASSES
################################################################################

class Shannon:

    def __init__(self, char_probs):
        """
        constructor for the class
        setting up the character probabilities and the shannon encoding for a
        set
        """
        self.char_probs = char_probs
        self.shannon_encoding = probToBinary(self.char_probs)
        pass

    def encode(self, str_input):
        """
        creating the code version of the input (transforming the input to bits
        based on the shannon encoding)
        """
        output = ""
        for letter in str_input:
            output += self.shannon_encoding[letter]

        return output
        pass

    def decode(self, str_input):
        """
        deciphering the input (from bits to the character/letter version using
        the keys from the shannon encoding)
        """

        output = ""
        bit = ""

        for digit in str_input:
            bit += digit

            for key in self.shannon_encoding:
                if bit == self.shannon_encoding[key]:
                    output += key
                    bit = ""

        return output

        pass

################################################################################
# MAIN
################################################################################

def main():

    char_probs = {"A": 0.25, "B": 0.125, "C": 0.5, "D": 0.125}
    shannon = Shannon(char_probs)
    #probToBinary(char_probs)

    orig = "ABAACDDBACCDAAABDBBABCDDCBA"
    encoded = shannon.encode(orig)
    decoded = shannon.decode(encoded)
    assert decoded == orig


    # TODO
    pass

################################################################################
# HELPER FUNCTIONS
################################################################################

def probToBinary(dic):
    """
    finding the shannon encoding for the given dictionary
    dic: the dictionary of characters
    return: the shannon_encoding for the given dictionary
    """

    sorted_prob = sorted(dic.values()) # can I use this
    sorted_prob.reverse() # can I use this?

    # sorting the key-value pairs based on the probability
    # highest probability to lowest
    sorted_prob_dict = {}
    for i in sorted_prob:
        for key in dic:
            if dic[key] == i:
                sorted_prob_dict[key] = dic[key]

    # creating the cummulative prob dict
    # creating bits dict - # of bits for each probability
    cummulative_prob_dict = {}
    bits_dict = {}
    cummulative = 0
    for i in sorted_prob_dict:
        prob = sorted_prob_dict[i]
        bits_dict[i] = math.ceil((-1*(math.log(prob)/math.log(2))))
        cummulative_prob_dict[i] = cummulative

        cummulative = cummulative + prob


    # finding the shannon encoding values for each key by converting
    # cummulative_prob_dict values into binary and making them the correct
    # number of bits
    shannon_encoding = {}
    for key in cummulative_prob_dict:
        binary_rep = convBinary(cummulative_prob_dict[key], bits_dict[key])
        shannon_encoding[key] = binary_rep[0:bits_dict[key]]


    # print(sorted_prob_dict)
    # print(cummulative_prob_dict)
    # print(bits_dict)
    # print(shannon_encoding)

    return shannon_encoding

    pass

def convBinary(num, bit_length):
    """
    converting the numbers into a binary string
    num: the numbers to be converted
    bit_length: number of bits supposed to be in binary string
    return: (recursively) calculating the value
    """
    if num == 0:
        return "0"*bit_length
    else:
        multi = num*2
        if multi >= 1:
            return "1" + convBinary(multi-1,  bit_length)
        else:
            return "0" + convBinary(multi,  bit_length)




if __name__ == "__main__":
    main()
