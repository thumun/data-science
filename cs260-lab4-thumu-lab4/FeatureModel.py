"""
CS260 Lab 4:
Author: Neha Thumu
Class: CS260
Date: 9/28/21
Description: This file creates a feature model (list of probabilities for each
feature value and the classify method handles comparison with threshold).
It also creates a confusin matrix for the data.
"""

# own imports
import util
#from Partition import *

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

        feature_values = partition.F.get(feature)
        feature_counter = dict.fromkeys(feature_values, (0, 0))

        # cycling through examples in order to count number of edible and
        # poisonous mushrooms in each feature value. Also adding these counts
        # to a dictionary for future reference
        for example in partition.data:
            value_in_data = example.features[feature]
            e, p = feature_counter[value_in_data]

            if example.label == -1:
                feature_counter[value_in_data] = (e+1, p)
            else:
                feature_counter[value_in_data] = (e, p+1)

        probabilities = dict.fromkeys(feature_values, 0.0)

        # creating probabilities dictionary by using feature_counter to find
        # out chance of getting an poisonous mushroom for each feature value
        for key in feature_counter:
            (e, p) = feature_counter[key]
            # there are no examples with a feature value in some cases
            if (e+p == 0):
                probabilities[key] = p/1
            else:
                probabilities[key] = p/(e+p)

        self.probabilities = probabilities
        self.feature = feature

        pass

    def classify(self, example, threshold):
        """
        This helper method classifies one example (Example from the test
        dataset) as -1 or 1 using the given threshold.
        example: a given example in the data
        threshold: value determining the validity of data points
        return: 1 or -1 (based on if probability is greater than threshold for
                a feature in an example)
        """
        value_in_data = example.features[self.feature]
        prob_pos = self.probabilities[value_in_data]

        if prob_pos >= threshold:
            return 1
        else:
            return -1

        pass


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

        if label == -1 and classification == -1:
            true_negative += 1
        elif  label == -1 and classification == 1:
            false_positive += 1
        elif label == 1 and classification == -1:
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
    FPR = false_positive/(false_positive + true_negative)
    TPR = true_positive/(false_negative + true_positive)

    return (TPR, FPR)


################################################################################
# MAIN
################################################################################

def main():
    # TODO: test your class here

    train = util.read_arff("data/mushroom_train.arff")
    test = util.read_arff("data/mushroom_test.arff")

    feature_model = FeatureModel(train,'cap-shape')

    # print(feature_model.probabilities)

    true_positive, true_negative, false_negative, false_positive = \
    values_confusion_matrix(train, test, feature_model, 0.5)

    TPR, FPR = get_TPR_FPR(true_positive, true_negative, false_negative,
    false_positive)

    total_correct = true_negative + true_positive
    all_examples = true_negative + true_positive + false_negative + \
    false_positive

    accuracy = total_correct/all_examples

    # below is formatting for the confusion matrix

    print("feature: cap-shape, thresh: 0.5\n")
    print("\t   prediction")
    print("\t      -1    1")
    print("\t   -----------")
    print(f'\t-1|    {true_negative}    {false_positive}')
    print(f'\t 1|    {false_negative}    {true_positive}')

    print(f'\naccuracy: {accuracy} ({total_correct} out of {all_examples}' +
    ' correct)')
    print(f'false positive: {FPR}')
    print(f'true positive: {TPR}')

    pass

if __name__ == "__main__":
    main()
