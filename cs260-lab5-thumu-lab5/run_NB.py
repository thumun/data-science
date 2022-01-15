"""
CS260 Lab 4: Reading the data and organizing it as objects of Parition class.
             Running NaiveBayes on the data to predict the labels.
             Constructing the Confusion Matrix. Then printing the confusion
             matrix and the accuracy.
Author: Neha Thumu
Date: 10/21/21
"""

import optparse
from NaiveBayes import *

################################################################################
# CLASSES
################################################################################

class Example:

    def __init__(self, features, label):
        """Helper class (like a struct) that stores info about each example."""
        # dictionary. key=feature name: value=feature value for this example
        self.features = features
        self.label = label # in {0, 1}

class Partition:

    def __init__(self, data, F, K):
        """Store information about a dataset"""
        # list of Examples
        self.data = data
        self.n = len(self.data)

        # dictionary. key=feature name: value=list of possible values
        self.F = F

        # number of classes
        self.K = K

################################################################################
# MAIN
################################################################################

def main():
    """
    read in the data, run Naive Bayes, make predictions about the test
    data, then print the accuracy and a confusion matrix
    """

    opts = parse_args()
    train_partition = read_csv(opts.train_filename)
    test_partition = read_csv(opts.test_filename)

     # sanity check
    print("num train =", train_partition.n, ", num classes =",
    train_partition.K)
    print("num test  =", test_partition.n, ", num classes =", test_partition.K)

    # print(countSex(train_partition))

    nb_model = NaiveBayes(train_partition)
    nb_conf_matrix = make_conf_matrix(nb_model, test_partition)

    pass

################################################################################
# HELPER FUNCTIONS
################################################################################

def parse_args():
    """Parse command line arguments (train and test csv files)."""
    parser = optparse.OptionParser(description='run Naive Bayes method')

    parser.add_option('-r', '--train_filename', type='string', help='path to' +\
        ' train csv file')
    parser.add_option('-e', '--test_filename', type='string', help='path to' +\
        ' test arff file')

    (opts, args) = parser.parse_args()

    mandatories = ['train_filename', 'test_filename',]
    for m in mandatories:
        if not opts.__dict__[m]:
            print('mandatory option ' + m + ' is missing\n')
            parser.print_help()
            sys.exit()

    return opts

def read_csv(filename):
    """
    read the CSV file (from the str filename) into the Partition format.
    filename: the name of the data file
    return: Partition(examples, features, K) (data in partition form)
    """
    file = open(filename,'r')
    lines = file.readlines()

    # getting feature names from first line of csv file
    feature_names = lines[0].rstrip().split(",")

    features = dict.fromkeys(feature_names)

    examples = []

    # initializing values of features dict as empty lists to fill in with feat
    # values in next step
    for i in feature_names:
        features[i] = []


    for line in lines[1:]:
        tokens = line.rstrip().split(",")
        counter = 0

        example_features = dict.fromkeys(feature_names)

        # getting the different feature values for the features dict and the
        # features of each example in a different dict
        for key in features:
            if features[key].count(tokens[counter]) == 0:
                features[key].append(tokens[counter])

            example_features[key] = tokens[counter]

            counter+=1

        # getting rid of sex as a feature (making it as a label)
        label = example_features.pop('sex')
        if label == "Female":
            label = 1
        else:
            label = 0

        example = Example(example_features, label)
        examples.append(example)


    sex_ls = features.pop('sex')
    K = len(sex_ls)

    return Partition(examples, features, K)

    pass


def countSex(partition):
    """
    counting the number of females and males within the data (based on the
    labels of each example)
    partition: data as an object of Partition
    return: the two counts as a tuple
    """
    femaleCount = 0
    maleCount = 0
    total = 0

    for example in partition.data:
        if example.label == 1:
            femaleCount+=1
        else:
            maleCount+=1

    return (femaleCount/len(partition.data), maleCount/len(partition.data))


def make_conf_matrix(nb_model, partition):
    """
    constructing the confusion matrix.
    printing the matrix and the accuracy.

    nb_model: object of NaiveBayes
    partition: data as an object of Partition
    """

    true_negative = 0
    false_positive = 0
    false_negative = 0
    true_positive = 0

    # getting the pred and true from the classify method in NaiveBayes
    for example in partition.data:
        y_hat = nb_model.classify(example.features)
        if y_hat == 0 and example.label == 0:
            true_negative += 1
        elif y_hat == 1 and example.label == 0:
            false_positive += 1
        elif y_hat == 0 and example.label == 1:
            false_negative += 1
        elif y_hat == 1 and example.label == 1:
            true_positive += 1

    total_correct = true_negative + true_positive
    accuracy = (total_correct)/partition.n

    print("\n")
    print("\t   prediction")
    print("\t       0        1")
    print("\t   -----------------")
    print(f'true     0|    {true_negative}    {false_positive}')
    print(f'\t 1|    {false_negative}    {true_positive}')

    print(f'\naccuracy: {accuracy} ({total_correct} out of {partition.n}'+
     ' correct)')

if __name__ == "__main__":
    main()
