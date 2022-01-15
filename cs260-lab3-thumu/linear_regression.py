"""
Author      : Neha Thumu
Class       : CS260
Date        : 9/22/21
Description : This is the main driver program for gradient descent. Calculating
analytical and stochastic weights for the data.
"""

# python libraries import here
import optparse
import matplotlib.pyplot as plt
import numpy as np

################################################################################
# MAIN
################################################################################

def main() :
    opts = parse_args()
    filename = opts.data_filename

    # reading the data from the file & adding it into a numpy array
    data = np.loadtxt(filename, delimiter=',')

    # organizing the data into X and y value num arrays
    X = data[:, 0:-1]
    y = data[:, -1:]

    X_with_ones = add_ones_column(X)

    # this is for part 2 (checking the weights from sea ice and regression
    # train data with lab2)
    w = fit(X_with_ones, y)
    # printing the weights
    # print(w)

    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)

    # X is normalized
    X_normalized = (X-X_mean)/X_std

    y_mean = y.mean(axis=0)
    y_std = y.std(axis=0)

    # y is normalized
    y_normalized = (y-y_mean)/y_std

    ones_added_X_normalized = add_ones_column(X_normalized)

    analytic_w = fit(ones_added_X_normalized, y_normalized)
    analytic_cost = cost(ones_added_X_normalized, y_normalized, analytic_w)

    alpha = 0.01
    eps = 1e-6 # changed the value of epsilon in order to converge
    tmax = 10000

    SGD_weights, cost_iterations, alpha = fit_SGD(ones_added_X_normalized,
    y_normalized, alpha, eps, tmax)

    SGD_cost = cost_iterations[-1]

    print("analytic cost: ", analytic_cost)
    print("analytic weight: \n", analytic_w)
    print("Values for SGD: ")
    print("alpha: ", alpha)
    print("epsilon: ", eps)
    print("tmax: ", tmax)
    print("SGD cost: ", SGD_cost)
    print("SGD weights: \n", SGD_weights)
    print("Number of iterations for SGD descent to converge: ",
    len(cost_iterations))

    number_of_iterations = np.arange(len(cost_iterations))

    # plot for the iterations vs cost
    plt.scatter(number_of_iterations, cost_iterations, color="blue")
    plt.xlabel("Number  of Iterations")
    plt.ylabel("Costs")
    plt.title("The Change in Cost per Iteration")

    plt.savefig("figures/cost_J.pdf", format='pdf')

    pass

################################################################################
# HELPER FUNCTIONS
################################################################################

def parse_args():
    '''
    parsing the command line arguments
    return: opts (arguments)
    '''
    parser = optparse.OptionParser(description='run linear regression method')

    parser.add_option('-d', '--data_filename', type='string', help='path to' +\
        ' CSV file of data')

    (opts, args) = parser.parse_args()

    mandatories = ['data_filename']
    for m in mandatories:
        if not opts.__dict__[m]:
            print('mandatory option ' + m + ' is missing\n')
            parser.print_help()
            sys.exit()

    return opts

def fit(X, y) :
    """
    Closed-form solution.
    calculates the weights by using the equation: (XtX)^-1Xty
    return: w[:,0] (the optimal weights)
    """
    Xt = np.transpose(X)
    w = np.matmul(np.matmul(np.linalg.inv(np.matmul(Xt, X)),Xt),y)

    return w

def fit_SGD(X, y, alpha=0.01, eps=1e-10, tmax=10000):
    """
    SGD solution

    X: matrix of features
    y: matrix of response variable
    alpha: step size
    eps: comparison value (with cost)
    tmax: max number of iterations (force quit number)

    return weights
    """

    # to store the values of cost for each iteration
    all_costs = []

    w = np.zeros((len(X[0]),1))

    counter = 0
    cost_previous = cost(X, y, w)

    cost_current = 0

    num_rows, num_cols = X.shape

    while tmax > 0:
        for i in range(num_rows):
            x_i = X[i:i+1,0:]
            y_i = y[i:i+1, 0:]

            h = np.dot(x_i, w)

            # the gradient
            grad = alpha * (h - y_i)*x_i

            # transpose in order to make sure subtraction has right dimensions
            w = w - np.transpose(grad)

            cost_current = cost(X, y, w)
            all_costs.append(cost_current)

            if abs(cost_current - cost_previous) < eps:
                return (w, all_costs, alpha)

            cost_previous = cost_current
            tmax-=1

        # lowering step size
        alpha = alpha/10

    return (w, all_costs, alpha)

    pass

def predict(X, w) :
    """
    Predict output [predicted y] for X using weight vector w.
    X: matrix of features
    w: weights
    return: np.matmul(X, w) (the predicted y values which is the matrix
            multiplication of X and w)
    """
    return np.matmul(X, w)

def cost(X, y, w) :
    """
    Calculate the loss/cost function.
    X: matrix of features
    y: matrix of response variable
    w: weights

    return: cost
    """

    predicted_y = predict(X, w)
    residual = np.subtract(predicted_y, y)

    first_column = residual[:,0]

    cost = np.dot(first_column, first_column)/2

    return cost

def add_ones_column(X):
    '''
    adds a 1's column to the beginning of the matrix to make calculations
    easier
    X: matrix of features
    return: the data matrix with the added 1's column
    '''
    ones = np.ones((len(X),1))
    return np.concatenate((ones, X), axis=1)

def append_polynomial(X, d):
    # gave this a try
    # idea: recursively call function d times until columns up to x^d  are
    # added

    if d < 1:
        return X
    else:
        X_d = np.matmul(X, np.transpose(X))
        X.append(X_d)
        return append_polynomial(X, d-1)



if __name__ == "__main__" :
    main()
