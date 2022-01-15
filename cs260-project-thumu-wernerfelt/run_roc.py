"""
Author: Neha Thumu, Annie Wernerfelt
Class: CS260
Date: 12/9/21
Description: This file creates a ROC curve for each given feature using the test
and train partitions.

Note:
Used this code for the final project. The one change from the lab code is the
Area under the curve function which was made by Annie. (Her code from the lab)
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
# HELPER FUNCTIONS
################################################################################

def create_roc(dict, train_partition, test_partition, feature):
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
    if feature not in dict.values():
        dict[extension(x_vals, y_vals, feature)]=feature
    return dict


def extension(fpr, tpr, feature):
    """
    This method calculates the area under the curve for different ROC curves
    using an algorithm that splits the areas into trapezoids and agregates
    them.
    """
    x = []
    y = []
    area = 0
    for i in range(len(tpr)):
        x.append(fpr[i])
        y.append(tpr[i])
    for i in range(len(x)-1):
        area+=(x[i]-x[i+1])*((y[i]+y[i+1])/2)
    # print("Area under curve for", feature, area)
    return area
