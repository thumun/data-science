'''
Author      : Neha Thumu
Class       : CS260
Date        : 9/07/21
Description : This is the Student file for the Introduction to Python
portion of Lab 1. This file consists of a review of how to make a constructor,
get methods, and how to create/manipulate objects of a class (through methods).
There is also a review on the dictionary data structure- how to create it,
access/add key-value pairs, and deleting key-value pairs.

'''

import numpy as np

class Student:

    """ ========== TODO : START ========== """

    """TODO: Create a constructor."""

    # initialization of the instance variables
    full_name = ""
    graduation_year = 0
    college_name = ""
    course_list = []

    def __init__(self, full_name, graduation_year, college_name):
        self.full_name = full_name
        self.graduation_year = graduation_year
        self.college_name = college_name
        self.course_list = []

    """TODO: Write getters. Although not necessary in python, it is good
    practice to have getter and setter methods (as needed) for the sake of
    encapsulazation."""

    def get_full_name(self):
        '''
        return the full_name instance variable of the object
        self: the object
        return: full_name (string)
        '''
        return self.full_name

    def get_graduation_year(self):
        '''
        return the graduation_year instance variable of the object
        self: the object
        return: graduation_year (int)
        '''
        return self.graduation_year

    def get_college_name(self):
        '''
        return the college_name instance variable of the object
        self: the object
        return: college_name (string)
        '''
        return self.college_name

    """TODO: Write the add course method"""

    def add_course(self, course_name):
        '''
        adds the course to the course_list if not already in the course_list
        self: the object, course_name: the name of the course in question
        '''
        if (course_name in self.course_list):
            print("Student is already taking %s" %(course_name))
        else:
            self.course_list.append(course_name)
            print("%s has been added" %(course_name))

    """TODO: Write the drop course method"""

    def drop_course(self, course_name):
        '''
        deletes the course from the course_list unless not in the course_list
        self: the object, course_name: the name of the course in question
        '''
        if (course_name in self.course_list):
            self.course_list.remove(course_name)
            print("%s had been removed" %(course_name))
        else:
            print("%s is not being taken by the student" %(course_name))

    """TODO: Write the __str__ method"""

    # ADD COMMENT
    def __str__(self):
        '''
        returns info about the instance variables of the object
        self: the object
        return: stated above (string)
        '''
        return ("This student's name is %s. They go to %s and will graduate %i.\
        They are taking the following courses: %s."
        %(self.full_name, self.college_name, self.graduation_year,
        self.course_list))


    """ ========== TODO : END ========== """

def main():

    """ ========== TODO : START ========== """
    """TODO: Create an instance of Student and test all the methods"""
    '''
    print("Student Class Testing\n")
    # TODO create instance
    neha = Student("Neha Thumu", 2024, "Haverford")

    print("Testing the getters:")
    # TODO test getters
    print(neha.get_full_name())
    print(neha.get_graduation_year())
    print(neha.get_college_name())

    print("\nTesting add_course and drop_course:")
    # TODO test add/drop

    neha.add_course("Intro to drawing")
    # testing if adding the same course twice works
    neha.add_course("Intro to drawing")

    neha.drop_course("Intro to drawing")

    # testing if dropping a course that not taking works
    neha.drop_course("Intro to linguistics")

    print("\nTest __str__:")
    # TODO test __str__
    print(neha)
    '''

    student_lst = [["Fiona Xu", 2022, "Haverford College"],
                    ["Ivy Zhang", 2024, "Bryn Mawr College"],
                    ["Alton Wiggers", 2025, "Swarthmore College"],
                    ["Luis Contreras-Orendain", 2022, "Haverford College"],
                    ["Lizzie Spano", 2023, "Bryn Mawr College"]]

    print("Student Dictionary Exercises\n")
    # TODO create dictionary called students
    students = {}

    # iterating through list and adding to the dictionary by making them into
    # objects of the Student class
    for i in range(len(student_lst)):
        id = i
        students[id] = Student(student_lst[i][0], student_lst[i][1],
         student_lst[i][2])

    print("Dictionary contents:")
    print_dict(students)

    print("\n Trying to add a student with same key:")
    students[0] = Student("Neha Thumu", 2024, "Haverford College")

    print("\n Dictionary contents afterwards:")
    print_dict(students)

    print("\n Trying to add a student with new key and a repeated value/Student:")
    students[6] = Student("Alton Wiggers", 2025, "Swarthmore College")

    print("\n Dictionary contents afterwards:")
    print_dict(students)

    specific_id = 1
    print("\n Getting Student at key %i:" % (specific_id))
    print(students[specific_id])

    print("\n Removing Student at key %i:" % (specific_id))
    del students[specific_id]


    print("Dictionary contents afterwards:")
    print_dict(students)



    """ ========== TODO : END ========== """


def print_dict(dictionary):
    """Function that prints out the keys and values in a dictionary"""
    for key, val in dictionary.items():
        print(key, val)


if __name__ == "__main__":
    main()
