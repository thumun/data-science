"""
CS260 Lab 4:
Author: Neha Thumu
Class: CS260
Date: 9/28/21
Description: This file creates ROC curves for the features in the data. The top
5 best ROC curves are saved. 
"""

# python imports
import numpy as np
import matplotlib.pyplot as plt
import random

# own imports
import util
from Partition import *
from FeatureModel import *

################################################################################
# MAIN
################################################################################

def main():
    # TODO: parse args and then call util.read_arff to read both train/test data
    opts = util.parse_args()

    train = util.read_arff(opts.train_filename)
    test = util.read_arff(opts.test_filename)

    print("train examples, n=", train.n)
    print("test examples, m=", test.n)

    features = test.F.keys()

    # TODO: for each feature, call create_roc to
    for feature in features:
        create_roc(train, test, feature)

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve for Mushroom Dataset")
    plt.legend()

    plt.show()

    plt.clf()

    feature_list = ["odor", "spore-print-color", "gill-color", "ring-type",
                    "population"]
    best_features(train, test, feature_list)

    pass


################################################################################
# HELPER FUNCTIONS
################################################################################

def create_roc(train_partition, test_partition, feature):
    """
    creates the ROC curve by first creating data points by cycling through
    thresholds and getting TPR and FPR for each threshold. Each (TPR, FPR)
    point is then plotted to create the curve.
    train_partition: the partition object created from the train file
    test_partition: the partition object created from the test file
    feature: name of a feature present in the data
    """

    # TODO: create a model based on the training data and the given feature
    feature_model = FeatureModel(train_partition, feature)


    # TODO: for a variety of thresholds, classify all test examples and create
    # a ROC curve based on the resulting confusion matrices
    thresholds = np.linspace(-0.0001,1.1,20)
    x_vals = []
    y_vals = []

    # getting the values of the ROC curve by cycling through
    # thresholds and getting TPR and FPR for each threshold.
    for threshold in thresholds:
        true_positive, true_negative, false_negative, false_positive = \
        values_confusion_matrix(train_partition, test_partition, feature_model,
        threshold)

        TPR, FPR = get_TPR_FPR(true_positive, true_negative, false_negative,
        false_positive)
        y_vals.append(TPR)
        x_vals.append(FPR)

    # TODO: plot the ROC curve using plt.plot

    # random color generator
    r = random.random()
    b = random.random()
    g = random.random()

    # labels and such in main
    plt.plot(x_vals, y_vals, label=feature, marker="o", color=(r, g, b))

    pass

def best_features(train, test, feature_list):
    """
    creating and saving the best ROC curves. (got the features that have the
    best ROC curves above)
    train_partition: the partition object created from the train file
    test_partition: the partition object created from the test file
    feature_list: the features that have the best ROC curves
    """

    for feature in feature_list:
        create_roc(train, test, feature)

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve for Mushroom Dataset")
    plt.legend()
    plt.savefig("figures/roc_curve_top5.pdf", format='pdf')

    pass


if __name__ == "__main__":
    main()
