"""
CS260 Lab 4: NaiveBayes algorithm implementation.
             Setting up probabilities for feature values in the data based on
             the labels.
             Predicting the labels of the examples in the data in the classify
             method.
Author: Neha Thumu
Date: 10/21/21
"""

import math

class NaiveBayes:

    def __init__(self, partition):
        """
        constructor for the class
        setting up all probabilities for the feature values based on the labels
        """

        self.log_prior = []

        # K holds the number of classes in the example data
        K = dict.fromkeys(range(0,partition.K))

        # intiializing values in K as zeroes
        for key in K:
            K[key] = 0

        # counting the number of examples based on label
        for example in partition.data:
            K[example.label] += 1

        self.prior_prob = []

        for key in K:
            # recording prior probabilities for each label
            self.prior_prob.append((K[key] + 1)/(partition.n + partition.K))
            # calculating the prior probabilities
            self.log_prior.append\
                (math.log(self.prior_prob[len(self.prior_prob)-1]))

        # print(self.log_prior)

        self.prob_dict = dict.fromkeys(range(0,partition.K))

        # creating a feature names dictionary in prob_dict (for each label)
        # then feature values for each feature name
        for sex in self.prob_dict:
            self.prob_dict[sex] = dict.fromkeys(partition.F.keys())
            for feature_name in self.prob_dict[sex]:
                self.prob_dict[sex][feature_name] = \
                    dict.fromkeys(partition.F[feature_name])
                for feat_val in self.prob_dict[sex][feature_name]:
                    self.prob_dict[sex][feature_name][feat_val] = 0

        # tallying up the number of examples that have the different feature
        # values
        for example in partition.data:
            for feat_name in example.features:
                feat_val = example.features[feat_name]
                self.prob_dict[example.label][feat_name][feat_val] += 1

        # updating the prob_dict with the probabilities in log space of each
        # feature value
        for sex in self.prob_dict:
            for feat_name in self.prob_dict[sex]:
                total = K[sex]
                #total = sum(list(self.prob_dict[sex][feat_name].values()))
                for feat_val in self.prob_dict[sex][feat_name]:
                    self.prob_dict[sex][feat_name][feat_val] = \
                        math.log(\
                        (self.prob_dict[sex][feat_name][feat_val] + 1)/\
                        (total+len(partition.F[feat_name])))

        # print(self.prob_dict)

        pass

    def classify(self, x_test):
        """
        based on the dictionary of features x_test, return the most
        likely class (integer)
        x_test: test data partition
        return: the label with the higher probability
        """

        probabilities = {}

        # creating dict to hold probabilities for each example using number of
        # labels
        for label in self.prob_dict:
            probabilities[label] = self.log_prior[label]

        # getting the probabilities for each label by adding the probabilities
        # of each feature value of the example
        for label in self.prob_dict:
            for feat_name in x_test:
                feat_val = x_test[feat_name]
                feat_val_prob = self.prob_dict[label][feat_name][feat_val]
                probabilities[label] += feat_val_prob


        # returning the label with the higher probability
        return max(probabilities, key=probabilities.get)

        pass
