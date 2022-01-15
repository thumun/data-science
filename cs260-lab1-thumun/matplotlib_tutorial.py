'''
TODO: add header here
'''

import matplotlib.pyplot as plt
import numpy as np

################################################################################
# MAIN
################################################################################

def main():
    # TODO your code here

    # read data from csv file and then organizing as x (years) and y (users)
    # values
    years = []
    users = []
    fb_file = open('data/facebook_users.csv','r')
    for line in fb_file:
        tokens = line.split(",") # split data based on commas
        years.append(int(tokens[0]))
        users.append(int(tokens[1]))
    print(years)
    print(users)

    # numpy method
    # user_data = np.loadtxt('data/facebook_users.csv', delimiter=',')
    # print(user_data)

    plt.scatter(years, users, color="black")
    plt.xlabel("Years")
    plt.ylabel("Number of Users")
    plt.title("The Number of Monthly Active Facebook Users worldwide in the 4th"
    + " Quarter")

    # plt.show()

    def values_of_linear_equation(x_values):
        '''
        calculates y values for given x based on linear equation
        x_values: the x values
        return: y_values (list of numbers)
        '''
        y_values = []

        for i in x_values:
            y = -432342.27 + 215.39 * i
            y_values.append(y)

        return y_values


    x_val_for_linear_equ = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,
    2019,2020,]
    plt.plot(x_val_for_linear_equ,
    values_of_linear_equation(x_val_for_linear_equ), color="blue")

    #plt.show() commented b/c bug when saving

    plt.savefig("figures/facebook_users.pdf", format='pdf')
    plt.clf()

    quad_coefs = [0, 4, -1]       # y = 4x - x^2
    cubic_coefs = [2, 0, -2, 1]   # y = 2 - 2x^2 + x^3
    x_val = np.linspace(0, 5, 20) # start at 0, end at 5, with 10 points total


    def find_quad_values(x_val):
        '''
        calculates y values for given x based on quadratic equation
        x_values: the x values
        return: y_values (list of numbers)
        '''
        y_val = []

        for i in x_val:
            y = 4*i - i**2
            y_val.append(y)

        return y_val

    def find_cubic_values(x_val):
        '''
        calculates y values for given x based on cubic equation
        x_values: the x values
        return: y_values (list of numbers)
        '''
        y_val = []

        for i in x_val:
            y = 2 - 2*(i**2) + i**3
            y_val.append(y)

        return y_val

    plt.plot(x_val, find_quad_values(x_val), label="y = 4x - x^2",
     color="red")
    plt.plot(x_val, find_cubic_values(x_val), label="y = 2 - 2x^2 + x^3",
     color="green")

    plt.xlabel("Inputs")
    plt.ylabel("Outputs")
    plt.title("Cubic values vs Quad values")
    plt.legend()

    #plt.show() #commenting out b/c of a bug when saving

    plt.savefig("figures/quad_cubic.pdf", format='pdf')


pass

if __name__ == "__main__" :
    main()
