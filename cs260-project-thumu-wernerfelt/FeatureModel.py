"""
Author: Neha Thumu, Annie Wernerfelt
Class: CS260
Date: 12/9/21
Description: This file creates a feature model (list of probabilities for each
feature value and the classify method handles comparison with threshold).
It also creates a confusin matrix for the data.

Note:
Used this code for the final project. There were not any
significant changes (if any).

"""

# own imports
import util
from cont_to_discrete import *
# from Partition import *

################################################################################
# CLASSES
################################################################################

class FeatureModel:

    def __init__(self, partition, feature):
        """
        The contructor takes a partition (Partition of the training dataset) and
        a feature (string) which is the sole feature that will be used for
        predictions.
        partition: object of the partition class
        feature: name of a feature present in the data
        """

        # getting the splits
        # cont_to_discrete(partition, feature)

        feature_values = partition.F.get(feature)
        feature_counter = dict.fromkeys(feature_values, (0, 0))

        # cycling through examples in order to count number of popular and
        # unpopular songs in each feature value. Also adding these counts
        # to a dictionary for future reference
        for example in partition.data:
            value_in_data = example.features[feature]
            u, p = feature_counter[value_in_data]

            if example.label == 0:
                feature_counter[value_in_data] = (u+1, p)
            else:
                feature_counter[value_in_data] = (u, p+1)

        probabilities = dict.fromkeys(feature_values, 0.0)

        # creating probabilities dictionary by using feature_counter to find
        # out chance of finding if a song is popular for each feature value
        for key in feature_counter:
            (u, p) = feature_counter[key]
            # there are no examples with a feature value in some cases
            if (u+p == 0):
                probabilities[key] = p/1
            else:
                probabilities[key] = p/(u+p)

        self.probabilities = probabilities
        self.feature = feature


        pass

    def classify(self, example, threshold):
        """
        This helper method classifies one example (Example from the test
        dataset) as 1 or 0 using the given threshold.
        example: a given example in the data
        threshold: value determining the validity of data points
        return: 1 or 0 (based on if probability is greater than threshold for
                a feature in an example)
        """
        value_in_data = example.features[self.feature]
        prob_pos = self.probabilities[value_in_data]

        if prob_pos >= threshold:
            return 1
        else:
            return 0


################################################################################
# HELPER FUNCTIONS
################################################################################

def values_confusion_matrix(train, test, feature_model, threshold):
    '''
    Filling in the confusion matrix by checking the label and classification of
    each example in test
    train: partition object from train file
    test: partition object from test file
    feature_model: object of featureModel class
    threshold: value determining the validity of data points
    return: (true_positive, true_negative, false_negative, false_positive)
            a tuple containing the vals of TP, TN, FN, FP)
    '''
    true_positive = 0
    true_negative = 0
    false_negative = 0
    false_positive = 0

    for example in test.data:
        value_in_data = example.features[feature_model.feature]
        label =  example.label
        classification = feature_model.classify(example, threshold)

        if label == 0 and classification == 0:
            true_negative += 1
        elif  label == 0 and classification == 1:
            false_positive += 1
        elif label == 1 and classification == 0:
            false_negative += 1
        elif  label == 1 and classification == 1:
            true_positive += 1

    return (true_positive, true_negative, false_negative, false_positive)

def get_TPR_FPR(true_positive, true_negative, false_negative, false_positive):
    '''
    calculating the FPR and the TPR using the values from the confusion matrix
    true_positive: TP values (calculated in values_confusion_matrix)
    true_negative: TN values (calculated in values_confusion_matrix)
    false_negative: FN values (calculated in values_confusion_matrix)
    false_positive: FP values (calculated in values_confusion_matrix)
    return: (TPR, FPR) (a tuple containing the vals of TPR and FPR)
    '''
    FPR = false_positive/(false_positive + true_negative + 1)
    TPR = true_positive/(false_negative + true_positive + 1)

    # NOTE: added +1 to denominator to prevent zero-ing out

    return (TPR, FPR)
