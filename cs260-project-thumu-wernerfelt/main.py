"""
Author      : Neha Thumu, Annie Wernerfelt
Class       : CS260 Project
Date        : 12/09/21
Description : This is the main class for the project. Here, we read in the data
and use KBinsDiscretizer to discretize the data. To make it easier to work on
our individual methods (entropy and ROC curves), we created two test and train
partition sets.
"""

################################################################################
# IMPORTS
################################################################################

from Partition import *
from run_roc import *

import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer

import collections


################################################################################
# MAIN
################################################################################

def main():
    """
    The main method calls the read csv methods which return instances of
    the partitoin class. It also calls methods from other classes to run the
    algorithms and it creates plots.
    """

    # Create instances of the partition class by reading in the data
    train_partition = read_csv_with_binning(\
                      "data/SpotifyAudioFeaturesApril2019.csv", 1, 8001)
    test_partition = read_csv_with_binning(\
                     "data/SpotifyAudioFeaturesApril2019.csv", 8001, 10001)

     # sanity check
    print("num train =", train_partition.n, ", num classes =", \
        train_partition.K)
    print("num test =", test_partition.n, ", num classes =", test_partition.K)

    # ENTROPY: return best feature
    best_f=train_partition.best_feature()
    print("ENTROPY--> best feature:", best_f)

    # Create more instances of partition for the ROC curve. Currently they are
    # the same instances as above
    train_partition_roc = read_csv_with_binning(\
                          "data/SpotifyAudioFeaturesApril2019.csv", 1, 8001)
    test_partition_roc = read_csv_with_binning(\
                        "data/SpotifyAudioFeaturesApril2019.csv", 8001, 10001)

    features = test_partition_roc.F.keys()


    # TODO: for each feature, call create_roc to make the roc curve
    dict={}
    for feature in features:
        create_roc(dict,train_partition_roc, test_partition_roc, feature)

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve for Spotify Dataset")
    plt.legend()

    plt.show()

    plt.clf()


    # create_roc returns a dictionary of areas under the curve for each feature
    # sort this dictionary and add the areas to a bar plot
    sorted_dict=collections.OrderedDict(sorted(create_roc(dict, \
                train_partition, test_partition, feature).items()))
    x_vals=sorted_dict.values()
    y_vals=sorted_dict.keys()
    plt.clf()
    plt.bar(x_vals, y_vals, color='#00dc4d', edgecolor='black')
    plt.title("Area under the ROC Curve for each feature")
    plt.xlabel("feature")
    plt.ylabel("Area under ROC curve")
    plt.show()
    plt.clf()


################################################################################
# HELPER FUNCTIONS
################################################################################

def read_csv_with_binning(filename, startline, endline):
    """
    Read the CSV file (from the str filename) into the Partition format.
    Use KBinsDiscretizer to put data into 5 bins for each feature
    filename: the name of the data file
    startline: the first row of data
    endline: the last row of data. We used the first 10,000 features
    return: Partition(examples, features, K) (data in partition form)
    """
    file = open(filename, encoding="utf8")
    lines = file.readlines()

    # getting feature names from first line of csv file
    feature_names = lines[0].rstrip().split(",")[-14:-1]

    # implement KBinsDiscretizer
    bin_data = np.zeros((endline-startline, 13))
    line_counter = 0
    labels = []
    for line in lines[startline:endline]:
        tokens = list(map(lambda x: float(x), line.rstrip().split(",")[-14:]))
        bin_data[line_counter] = tokens[:-1]
        if tokens[-1] < 10: #threshold for popularity
            labels.append(0)
        else:
            labels.append(1)
        line_counter += 1

    # We picked 5 bins for each feature
    num_bins = 5

    # intializing the discretizer
    kbins = KBinsDiscretizer(n_bins=num_bins, encode='ordinal', \
            strategy='uniform')

    # organizing the data into num bins --> discretizing them
    data_trans = kbins.fit_transform(bin_data)

    examples = []

    # making data for parition obj
    for row in data_trans:
        values = row.tolist()
        # associate a value to feature name to make map & converting floats to
        # ints
        example_features = dict(zip(feature_names, list(map(int, values))))
        example = Example(example_features, labels[0])
        examples.append(example)
        labels = labels[1:]


    # initializing values of features dict as empty lists to fill in with feat
    # values in next step
    features = dict.fromkeys(feature_names, list(range(0, num_bins)))
    popularity_ls = [0, 1]
    K = len(popularity_ls)

    return Partition(examples, features, K)


if __name__ == "__main__":
    main()
