"""
Running the CLT and the Permutation testing method on the populations from the
genome sizes dataset. Goal is to get the p-value to find if the two populations
have approximately the same size (or not).
Author: Neha Thumu
Date: 11/11/21
"""

################################################################################
# Imports
################################################################################
import pandas as pd
from scipy.stats import ttest_ind
import random

################################################################################
# Main
################################################################################
def main():
    # the two populations from the data - "true data"
    pop_1, pop_2 = get_genome_populations("data/SSuis_Stats.xlsx")

    # the p-value using CLT (through the t-test)
    result = ttest_ind(pop_1, pop_2)

    print(f"CLT p-value: {result[1]}")

    # diff_means = run_trials(pop_1, pop_2)

    p_val_resampled = get_extreme_count(pop_1, pop_2)

    print(f"Permutation testing p-value: {p_val_resampled}")

    pass

################################################################################
# Helper Functions
################################################################################

def get_genome_populations(filename):
    """
    getting the data for each population

    fileneame: the name fo the data file
    return: (pop_1, pop_2)  the two populations as a tuple
    """
    data_frame = pd.read_excel(filename, header=0) # header on line 0
    #print(data_frame)

    population_1 = \
        data_frame.loc[data_frame["Population"] == 1, "Total Genome Size"]
    population_2 = \
        data_frame.loc[data_frame["Population"] == 2, "Total Genome Size"]

    # converting to list
    pop_1 = population_1.values.tolist()
    pop_2 = population_2.values.tolist()

    return (pop_1, pop_2)

    pass


def get_extreme_count(pop_1, pop_2):
    """
    counting the number of the means that are over the true difference.
    Getting the extremes.

    pop_1: population 1
    pop_2: population 2
    return: count/len(diff_means) (average of the number of values over true)
    """
    count = 0

    diff_means = run_trials(pop_1, pop_2)
    # print(diff_means)
    true_diff = get_true_diff(pop_1, pop_2)
    # print(true_diff)

    # going through the means from the different trials and seeing which means
    # are greater than the true
    for mean in diff_means:
        if mean >= true_diff:
            count += 1
    return count/len(diff_means)*2


def get_true_diff(pop_1, pop_2):
    """
    getting the difference of the means of the true data

    pop_1: population 1
    pop_2: population 2
    return: abs(mean_pop_1 - mean_pop_2)  (the absolute value of the difference)
    """
    mean_pop_1 = 0
    mean_pop_2 = 0

    for j in pop_1:
        mean_pop_1 += j

    for k in pop_2:
        mean_pop_2 += k

    mean_pop_1 = mean_pop_1/len(pop_1)
    mean_pop_2 = mean_pop_2/len(pop_2)

    return (abs(mean_pop_1 - mean_pop_2))


def run_trials(pop_1, pop_2):
    """
    running the trials 100000 times on the data

    pop_1: population 1
    pop_2: population 2
    return: diff_means (a list of the different means from each trial)
    """
    diff_means = []

    for i in range(100000):
        # recreating the populations in each trial
        population_1, population_2 = permutation_labels(pop_1, pop_2)

        mean_pop_1 = 0
        mean_pop_2 = 0

        for j in population_1:
            mean_pop_1 += j

        for k in population_2:
            mean_pop_2 += k

        mean_pop_1 = mean_pop_1/len(population_1)
        mean_pop_2 = mean_pop_2/len(population_2)

        # calculating the means and adding them to the list
        diff_means.append(abs(mean_pop_2 - mean_pop_1))

    return diff_means


def permutation_labels(pop_1, pop_2):
    """
    Algorithm for the permutation testing method

    pop_1: population 1
    pop_2: population 2
    return (population_1, population_2) (new populations - with the data mixed
        about)
    """
    pop_1_length = len(pop_1)

    # merging the populations into one list to help with resampling
    all_pop = pop_1 + pop_2

    population_1 = []
    population_2 = []

    # will continue until all_pop is empty
    while (len(all_pop) > 0):
        # picking a random index (and thereby value) in all_pop
        rand_val = random.randrange(len(all_pop))

        # fill population one with random values from all_pop until full
        if (len(population_1) <= pop_1_length):
            population_1.append(all_pop[rand_val])
            del all_pop[rand_val]

        # do the same with population 2
        else:
            population_2.append(all_pop[rand_val])
            del all_pop[rand_val]

    return (population_1, population_2)


if __name__ == '__main__':
    main()
