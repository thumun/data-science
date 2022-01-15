"""
CS260 Lab 2:
Author: Neha Thumu
Class: CS260
Date: 9/14/20
Description: The main file for this lab. Contains all the code for reading
the data from various files and plotting the information. Also creating best
fit lines/curves for the data. There are also residuals to compare the
predictions with the true values as well as an elbow graph. 
"""

# python libraries
import optparse
import matplotlib.pyplot as plt
import numpy as np
import sys

################################################################################
# MAIN
################################################################################

def main():

    '''
    Part: 1
    '''
    # read data from csv file and then organizing as x (years) and y (sea ice
    # extent) values
    years = []
    sea_ice_extent = []

    # copied the code from lab 1 for reading info from file
    sea_ice_file = open('data/sea_ice_1979-2012.csv','r')
    for line in sea_ice_file:
        tokens = line.split(",") # split data based on commas
        years.append(int(tokens[0]))
        sea_ice_extent.append(float(tokens[1]))
    print(years)
    print(sea_ice_extent)

    plt.ylim(0, 9)

    plt.scatter(years, sea_ice_extent, label="data of sea ice extent" +
    " 1979-2012", color="black")
    plt.xlabel("Years")
    plt.ylabel("Sea ice extent (millions of km^2)")
    plt.title("The Change in Sea Ice Extent over 1979-2012")
    plt.legend()

    # plt.show() #commenting out b/c of bug while saving

    plt.savefig("figures/part1.pdf", format='pdf')

    '''
    Part: 2
    '''
    # adding a linear line of best fit
    # rounded the numbers for the label
    linear = plt.plot(years, y_vals_linear_equ(years),
    label="ŷ = 190.5 - 0.0922x", color="red")
    plt.legend()

    plt.savefig("figures/part2_deg1.pdf", format='pdf')

    # removing linear line of best fit from graph
    linear[0].remove()

    # adding a quadratic line of best fit
    # rounded the numbers for the label
    quad = plt.plot(years, y_vals_quad_equ(years),
    label="ŷ = -15150.2 + 15.3x - 0.004x^2", color="green")
    plt.legend()

    plt.savefig("figures/part2_deg2.pdf", format='pdf')

    #plt.show()
    plt.clf()

    # calculating values of residuals for linear and quadratic models
    linear_predict = calculate_residuals(sea_ice_extent,
    y_vals_linear_equ(years))
    quad_predict = calculate_residuals(sea_ice_extent, y_vals_quad_equ(years))

    # graphing the residual linear model
    residual_linear = plt.scatter(years, linear_predict,
    label="ŷ = 190.5 - 0.0922x", color="blue")
    plt.xlabel("Years")
    plt.ylabel("Residuals")
    plt.title("Residuals for 1979-2012 data on Sea Ice")
    plt.legend()


    plt.savefig("figures/part2_residuals1.pdf", format='pdf')

    # removing the residual linear drom the chart
    residual_linear.remove()

    # graphing the quadratic residual model
    plt.scatter(years, quad_predict, label="ŷ = -15150.2 + 15.3x - "
    + "0.004x^2", color="orange")
    plt.legend()

    plt.savefig("figures/part2_residuals2.pdf", format='pdf')

    # clearing so can graph part 3 content
    plt.clf()
    #plt.show()

    '''
    Part: 3
    '''

    years_2013_2020 = []
    sea_ice_extent_2013_2020 = []

    sea_ice_2013_2020 = open('data/sea_ice_2013-2020.csv','r')
    for line in sea_ice_2013_2020:
        data_2013_2020 = line.split(",") # split data based on commas
        years_2013_2020.append(int(data_2013_2020[0]))
        sea_ice_extent_2013_2020.append(float(data_2013_2020[1]))
    print(years_2013_2020)
    print(sea_ice_extent_2013_2020)

    # plotting the old and new data
    plt.scatter(years, sea_ice_extent, label="1979-2012 data", color="black")
    plt.scatter(years_2013_2020, sea_ice_extent_2013_2020,
    label="2013-2020 data", color="blue")
    plt.xlabel("Years")
    plt.ylabel("Sea ice extent (millions of km^2)")
    plt.title("The Change in Sea Ice Extent over 1979-2020")
    plt.legend()

    total_years = all_years(years, years_2013_2020)

    # the linear line of best fit
    linear = plt.plot(total_years, y_vals_linear_equ(total_years),
    label="ŷ = 190.5 - 0.0922x", color="red")
    plt.legend()

    plt.savefig("figures/part3_pred1.pdf", format='pdf')

    # removing it from plot so can plot quadratic
    linear[0].remove()

    # plotting quadratic best fit curve
    quad = plt.plot(total_years, y_vals_quad_equ(total_years),
    label="ŷ = -15150.2 + 15.3x - 0.004x^2", color="green")
    plt.legend()

    plt.savefig("figures/part3_pred2.pdf", format='pdf')

    plt.clf()

    '''
    Part: 4
    '''

    all_coefficients = []

    deg_0_coef = [1.13010595]
    deg_1_coef = [2.4464070947147207, -2.816353589568698]
    deg_2_coef = [2.522610178119313, -3.27003073191282, 0.4743087284609393]
    deg_3_coef = [1.2231425230496584, 10.649616212253513, -34.083679747347574,
    23.590230897814727]
    deg_4_coef = [0.8075214798200756, 17.32934850900337, -62.32907523274797,
    66.75220156315058, -21.61184507602993]
    deg_5_coef = [1.1537400009153576, 9.784042834672174, -14.963934203443742,
    -54.05134690879839, 111.9406595086277, -53.20467363235635]
    deg_6_coef = [1.6031281515537332, -2.212955964351817, 87.09165569133722,
    -440.6384252637192, 832.5418657076268, -698.5859135919, 221.439066525518]
    deg_7_coef = [1.0048620515132924, 17.4112052205856, -133.45588391947206,
    713.2351017847259, -2320.831952624806, 3938.208550304347,
    -3249.3507974432723, 1036.2869129041017]
    deg_8_coef = [0.8889729225247591, 21.927863684690806, -196.3956341264095,
    1135.1023058754872, -3863.15628401735, 7177.078002707203,
    -7143.712758937181, 3524.932857125692, -654.5246542101304]
    deg_9_coef = [6.455577860121968, -214.55025432038786, 3518.6484115354933,
    -28016.264919570815, 126197.74461140906, -343436.25785927917,
    574211.0815161027, -575789.2765246094, 317309.99905972165,
    -73803.67907566673]
    deg_10_coef = [5.571266255808752, -173.07147738443035, 2771.613686468927,
    -21023.423222254118, 87668.04317051847, -210606.67961073387,
    280101.8712329003, -158297.13764038868, -49517.323077016044,
    107648.64893355407, -38599.19918692205]

    all_coefficients.append(deg_0_coef)
    all_coefficients.append(deg_1_coef)
    all_coefficients.append(deg_2_coef)
    all_coefficients.append(deg_3_coef)
    all_coefficients.append(deg_4_coef)
    all_coefficients.append(deg_5_coef)
    all_coefficients.append(deg_6_coef)
    all_coefficients.append(deg_7_coef)
    all_coefficients.append(deg_8_coef)
    all_coefficients.append(deg_9_coef)
    all_coefficients.append(deg_10_coef)

    x_values = []
    y_values = []
    data = []

    regression_train = open('data/regression_train.csv','r')
    for line in regression_train:
        data_regression = line.split(",") # split data based on commas
        data.append((float(data_regression[0]), float(data_regression[1])))

    # https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-
    # by-second-item/
    # followed code from above link to figure out how to iterate/get a value
    # from a tuple
    data.sort(key = lambda x:x[0])

    print(data)

    # sorting the x and y values from data into their own arrays
    for i in data:
        x_values.append(i[0])
        y_values.append(i[1])


    graph_models(x_values, y_values, all_coefficients)
    graph_elbow_plt(x_values, y_values, all_coefficients)

    pass


################################################################################
# HELPER FUNCTIONS
################################################################################

def y_vals_linear_equ(x_val):
    '''
    calculating the predicted y-values for the linear equation for best fit
    x_val: x-values from the data
    return: y_val (the predicted y-values)
    '''
    deg_1_coef = [190.5038227644984, -0.09224446142042844]
    y_val = []

    for i in x_val:
        y = deg_1_coef[0] + deg_1_coef[1]*i
        y_val.append(y)

    return y_val

def y_vals_quad_equ(x_val):
    '''
    calculating the predicted y-values for the quadratic equation for best fit
    x_val: x-values from the data
    return: y_val (the predicted y-values)
    '''
    deg_2_coef = [-15150.155305067638, 15.283380627913214,
    -0.0038525745647042583]
    y_val = []

    for i in x_val:
        y = deg_2_coef[0] + deg_2_coef[1]*i + deg_2_coef[2]*i**2
        y_val.append(y)

    return y_val


def calculate_residuals(data, predicted_y_val):
    '''
    calculating the residuals for part 2 (works for linear and quadratic)

    data: the y_values from the data
    predicted_y_val: the predicted y-values from the equation
    return: residuals (an array of residuals calculated for each set of true
    and predicted y values)
    '''
    residuals = []

    for i in range(len(data)):
        residual = data[i] - predicted_y_val[i]
        residuals.append(residual)

    return residuals

def y_vals_with_coefficients(x_vals, coefficients):
    '''
    calculating the y_values of the predictions (for the different degrees
    of polynomials)
    x_vals: the x values from the regression data
    coefficients: the different coefficients for a degree (not the list of all
    coefficients)
    return: y_vals (the predicted y-values for given degree)
    '''
    y_vals = []

    for i in x_vals:
        sum = 0
        for j in range(len(coefficients)):
            sum += coefficients[j]*pow(i, j)

        y_vals.append(sum)

    return y_vals

def graph_models(x_vals, y_vals, all_coefficients):
    '''
    Graphs the regression data (x and y values).
    Graphs the models for the different degrees of coefficients as predictions
    (lines/curves of best fit).
    x_vals: the values of x from the regression data
    y_vals: the values of y from the regression data
    all_coefficients: a list of all the degrees of coefficients
    '''
    for i in range(len(all_coefficients)):
        plt.scatter(x_vals, y_vals, label="true data", color="black")
        plt.plot(x_vals, y_vals_with_coefficients(x_vals,
        all_coefficients[i]), label="prediction", color="green")
        plt.xlabel("x values")
        plt.ylabel("y values")
        plt.title("Regression data for coefficient: {}".format(i))
        plt.legend()
        plt.savefig("figures/part4_deg{}.pdf".format(i), format='pdf')

        plt.clf()

def calculate_RSS(true_values, predicted_values):
    '''
    calculates the residual sum of squares by using the true and predicted
    values of y
    true_values: the values of y from the regression data
    predicted_values: the predicted values of y using equations
    return: RSS (the residual sum of squares)
    '''
    RSS = 0

    for i in range(len(true_values)):
        RSS += pow((true_values[i]-predicted_values[i]), 2)

    return RSS

def graph_elbow_plt(x_values, true_values, all_coefficients):
    '''
    creates the elbow plot using the x and y values from the data set
    x_values: the x_values from regression data
    true_values: the y_values (true vals) from the regression data
    '''
    all_RSS = []
    degree = []

    # using the number of elements in the list with degrees to find the
    # predicted values, the residual sum of squares, and the degree number
    for i in range(len(all_coefficients)):
        predicted_values = y_vals_with_coefficients(x_values,
        all_coefficients[i])
        all_RSS.append(calculate_RSS(true_values, predicted_values))
        degree.append(i)

    plt.scatter(degree, all_RSS, label="RSS", color="black")
    plt.xlabel("Degree of Polynomial")
    plt.ylabel("RSS")
    plt.title("Elbow Plot")
    plt.legend()
    plt.savefig("figures/part4_elbow.pdf", format='pdf')

    plt.clf()


def all_years(old, new):
    '''
    combines the years in order to create a plot where all the years from the
    two data sets are the x_values
    old: the years from 1979-2012
    new: the years from 2013-2020
    return: total (all the years in order)
    '''
    total = []

    for i in old:
        total.append(i)
        print(total)

    for j in new:
        total.append(j)
        print(total)

    return total

if __name__ == "__main__":
    main()
