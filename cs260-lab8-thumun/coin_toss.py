"""
Running the CLT and Randomized Trial methods on a coin toss scenario to find
if a given sample is unfair. 
Author: Neha Thumu
Date: 11/11/21
"""

import math
from scipy.integrate import quad
from scipy.stats import norm
import random
import matplotlib.pyplot as plt


def main():
    n = 80
    numheads = 54
    tails = 0
    heads = 1

    # probabilities of the fair coin
    probabilities = {0 : 1/2, 1: 1/2}
    sample_mean = numheads/n

    z_score = get_z_score(n, sample_mean, probabilities)
    p_val = get_p_val(z_score)

    print(f"CLT p-value: {p_val}")

    # print(one_trial(80))
    trials = run_trials(n)
    ec = extreme_count(trials, sample_mean)

    print(f"Random trials p-value: {ec/len(trials)}")

    # plotting as a histogram
    plt.hist(trials, density=True)
    plt.xlabel("Fractions of Heads")
    plt.ylabel("Fractional Count")
    plt.title("Histogram of Coin Toss")
    plt.savefig("figures/coin_toss.pdf")
    plt.show()

    pass

################################################################################
# Helper Functions
################################################################################

################################################################################
# Part A.)
################################################################################

def fair_expected_val(vals):
    """
    getting the expected value

    vals: probabilities for each label (face of the coin)
    return: output (expected value)
    """
    output = 0
    for key in vals:
        output += key*vals[key]

    return output

def find_variance(vals):
    """
    getting the variance

    vals: probabilities for each label (face of the coin)
    return: variance
    """
    mu = fair_expected_val(vals)

    variance = 0
    for key in vals:
        variance += vals[key]*pow((key - mu), 2)

    return variance

def get_z_score(n, sample_mean, vals):
    """
    calculating the z-score

    n: the number of tosses
    sample_mean: sample mean from true data
    vals: probabilities for each label (face of the coin)
    return: math.sqrt(n)*((sample_mean - mu)/sigma) (the z-score)
    """
    mu = fair_expected_val(vals)
    sigma = math.sqrt(find_variance(vals))

    return math.sqrt(n)*((sample_mean - mu)/sigma)

def get_p_val(z_score):
    """
    getting the p-val

    z_score: the z-score for the data
    return: (result*2) (multiplying by 2 b/c 2-sided)
    """
    positive_infinity = float('inf')
    func = norm.pdf

    result, error = quad(func, z_score, positive_infinity)

    return(result*2)
    pass

################################################################################
# Part B.) Randomized Trials
################################################################################

def one_trial(n):
    '''
    Running one trial for coin flipping
    n: number of times the coin will be flipped
    return: the chance of getting heads (# of heads/total flips)

    n: the number of tosses
    return: probabilities[1]/n (the number of heads in the trial/total tosses)
    '''
    probabilities = {0: 0, 1: 0}

    for i in range(n):
        val = random.randrange(2)
        probabilities[val] += 1

    return probabilities[1]/n

def run_trials(n):
    '''
    Running trials num_trials 100000 amount of times

    n: the number of tosses (in one trial)
    return: trials (the probabilities from each trial in a list)
    '''
    trials = []

    for i in range(100000):
        trials.append(one_trial(n))

    return trials

def extreme_count(trials, sample_mean):
    """
    taking count of the number of extremes (more than the mean and less than
    left bound)

    trials: list of the probabilities from each trial
    sample_mean:
    return ec (count of extremes)
    """

    ec = 0
    # other side of 2-sided
    left_bound = 26/80

    for hc in trials:
        if hc >= sample_mean:
            ec+=1
        # also take into account the other case (two-sided)
        elif hc <= left_bound:
            ec+=1

    return ec


if __name__ == '__main__':
    main()
