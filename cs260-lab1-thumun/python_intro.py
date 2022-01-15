'''
Author      : Neha Thumu
Class       : CS260
Date        : 9/6/21

Description: This is the python intro file. This intro covers different kinds
of methods. One with a comparison, one with sorting/shuffling, a recursive
method, and a binary search method.

'''

# TODO add imports here
import random

################################################################################
# MAIN
################################################################################

def main():
    '''
    For each function below, please write tests in main to confirm that it works
    correctly. Although the focus of this assignment is not on testing (so you
    don't necessarily need to check *every* case), it is good practice to
    consider both the standard and corner cases when writing your tests.
    '''

    # movie ticket cost
    # movie_ticket_cost()

    # shuffle_in_place(["hi", "bye", "test"]) # multiple items
    # shuffle_in_place([]) # empty list
    # shuffle_in_place(["hi"]) # one item

    # shuffle_out_of_place(["hi", "bye", "test"]) # multiple items
    # shuffle_out_of_place(["hi"]) # one item
    # shuffle_out_of_place([]) # empty list

    # print(fib(4))
    # print(fib(0)) #test base case
    # print(fib(1)) #test base case

    # print(binary_search_r(1,[1])) #one element in list
    # print(binary_search_r(1,[0]))
    # print(binary_search_r(1,[])) #empty list
    # print(binary_search_r(3,[1,2,4,5,6]))
    # print(binary_search_r(3,[1,2,3,5,6])) #not in the list

    # print(binary_search_nr(1,[1])) #one element in list
    # print(binary_search_nr(1,[0]))
    # print(binary_search_nr(1,[])) #empty list
    # print(binary_search_nr(3,[1,2,3,4,5,6])) #not in the list
    # print(binary_search_nr(3,[1,2,4,5,6])) #not in the list


    pass

################################################################################
# FUNCTIONS
################################################################################

# split into two functions in order to make testing easier
def movie_ticket_cost():
    '''
    Asks user for age and prints the cost of ticket based on their age.
    return: ticket cost based on age (int)

    '''
    # converts string age to int for comparison
    age = int(input("What is your age? "))
    return get_movie_ticket_cost(age)


# logic for movie ticket cst depending on age
def get_movie_ticket_cost(age):
    '''
    compares the user inputted age with age parameters for the ticket costs in
    order to figure out the cost
    '''
    if 0 <= age <= 12:
        print("Ticket costs: $8")
    elif 13 <= age <= 64:
        print("Ticket costs: $12")
    elif age >= 65:
        print("Ticket costs: $8")
    else:  # for negative numbers
        print("Invalid age")

    pass


def shuffle_in_place(lst):
    '''
    moving the elements of the list in a random fashion. Shuffles the list by
    modifying the original list.
    '''

    for i in range(0, len(lst)):
        new_position = random.randrange(len(lst))
        placeholder = lst[new_position]

        lst[new_position] = lst[i]
        lst[i] = placeholder

    print(lst)

    pass

def shuffle_out_of_place(lst):
    '''
    moving the elements of the list in a random fashion. keeps the original
    list in tact and outputs the shuffled list as a new list.
    '''

    output_lst = lst[:]

    for i in range(0, len(output_lst)):
        new_position = random.randrange(len(output_lst))
        placeholder = output_lst[new_position]

        output_lst[new_position] = output_lst[i]
        output_lst[i] = placeholder

    print("original list:")
    print(lst)
    print("shuffled list:")
    print(output_lst)

    pass

def fib(n):
    '''
    generates the nth fibonacci number
    n: non-negative number
    return: nth fibonacci number (int)
    '''
    num = int(n)

    if (num == 1 or num == 0):
        return 1
    else:
        return fib(num - 2) + fib(num - 1)

    pass

def binary_search_r(query, lst): # recursive version
    '''
    finds a given element by using recursive implementation of binary search
    algorithm

    query: an element to be found, lst: list of elements

    return: index of element found or -1 if not found
    '''
    print(lst)

    if (len(lst) == 0):
        return -1

    compare = round(len(lst)/2)

    if (query != lst[compare] and len(lst) == 1):
        return -1

    if (query == lst[compare]):
        return compare

    elif (query > lst[compare]):
        return binary_search_r(query, lst[compare:len(lst)])

    else:
        return binary_search_r(query, lst[0:compare])


    pass


def binary_search_nr(query, lst): # non-recursive version
    '''
    finds a given element by using non-recursive implementation of binary search
    algorithm

    query: an element to be found, lst: list of elements

    return: index of element found or -1 if not found
    '''

    if (len(lst) == 0):
        return -1

    while (len(lst) != 1):
        compare = round(len(lst)/2)

        if (query == lst[compare]):
            return compare

        elif (query > lst[compare]):
            lst = lst[compare:len(lst)]

        else:
            lst = lst[0:compare]

    if (query == lst[0]):
        return 0
    else:
        return -1


    pass

if __name__ == "__main__":
    main()
