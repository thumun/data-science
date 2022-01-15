"""
Partition class: organizing the data by storing the data as examples. These
examples objects are stored as dictionaries with feature values and labels.
Has a method to determine the best feature of a data set through entropies.
Has a method to determine the best feature of a data set through classification
accuracy.
Author: Neha Thumu
Date: 10/28/21
"""

################################################################################
# IMPORTS
################################################################################

import math

################################################################################
# CLASSES
################################################################################

class Example:

    def __init__(self, features, label):
        """Helper class (like a struct) that stores info about each example."""
        # dictionary. key=feature name: value=feature value for this example
        self.features = features
        self.label = label

class Partition:

    def __init__(self, data, F):
        """Store information about a dataset"""
        # list of Examples
        self.data = data
        self.n = len(self.data)

        # dictionary. key=feature name: value=list of possible values
        self.F = F

    def best_feature(self):
        """
        finding the best feature using entropies
        return: returning the best feature (according to this strategy)
        """

        # couldn't figure out how to not hardcode the labels
        feat_val_count = dict.fromkeys(["-1", "1"])

        # getting the feature names as a list to use later to initialize keys
        # of dictionaries
        feat_names = []
        for key in self.F:
            feat_names.append(key)

        # intiailzing the dictionary that keeps track of the number of feature
        # values that appear in the examples
        for label in feat_val_count:
            feat_val_count[label] = dict.fromkeys(feat_names)
            for feat_name in feat_val_count[label]:
                feat_val_count[label][feat_name] = \
                dict.fromkeys(self.F[feat_name])
                for feat_val in feat_val_count[label][feat_name]:
                    feat_val_count[label][feat_name][feat_val] = 0

        # cycling through the data in order to fill in the feature value count
        # dictionary
        for example in self.data:
            for key in self.F:
                feat_val = example.features[key]

                if example.label == -1:
                    feat_val_count["-1"][key][feat_val] += 1
                else:
                    feat_val_count["1"][key][feat_val] += 1

        # total number of examples in the data
        total = len(self.data)

        # initializng probabibility of each feature value dictionary
        prob_feat_val = dict.fromkeys(feat_names)
        for key in prob_feat_val:
            prob_feat_val[key] = dict.fromkeys(self.F[key])
            for fv in prob_feat_val[key]:
                prob_feat_val[key][fv] = 0

        # calculating the probability of each feature value in the data
        for key in self.F:
            for feat_val in prob_feat_val[key]:
                prob_feat_val[key][feat_val] = \
                feat_val_count["-1"][key][feat_val] \
                + feat_val_count["1"][key][feat_val]
                prob_feat_val[key][feat_val] = \
                prob_feat_val[key][feat_val]/len(self.data)

        # print(feat_val_count)
        # print(prob_feat_val)

        # calculating the entropies for each feature val
        entropy_feat_val = dict.fromkeys(feat_names)
        for key in entropy_feat_val:
            entropy_feat_val[key] = dict.fromkeys(self.F[key])

        # calculating the entropies for the feature values
        for feat_name in feat_val_count["-1"]:
            for feat_val in feat_val_count["-1"][feat_name]:
                true_cond = 0
                false_cond = 0

                true_cond = \
                feat_val_count["1"][feat_name][feat_val]
                false_cond = \
                feat_val_count["-1"][feat_name][feat_val]

                if true_cond == 0 or false_cond == 0:
                    entropy_feat_val[feat_name][feat_val] = 0

                else:
                    prob_true = true_cond/(true_cond+false_cond)
                    prob_false = false_cond/(true_cond+false_cond)

                    entropy_feat_val[feat_name][feat_val] = \
                    -1*(prob_true)*(math.log2(prob_true)) \
                    - prob_false*(math.log2(prob_false))

        # conditional entropy for each feature
        entropies_feat_names = dict.fromkeys(feat_names)
        for key in entropies_feat_names:
            feat_val_entropy_sum = 0
            for feat_val in entropy_feat_val[key]:
                feat_val_entropy_sum += \
                prob_feat_val[key][feat_val]*entropy_feat_val[key][feat_val]
            entropies_feat_names[key] = feat_val_entropy_sum

        # calculating the entropy for each label
        entropy_label = 0
        true_label = 0
        false_label = 0

        for example in self.data:
            if example.label == -1:
                true_label += 1
            else:
                false_label += 1

        prob_true_label = true_label/(true_label+false_label)
        prob_false_label = false_label/(true_label+false_label)

        entropy_label = -1*(prob_false_label)*(math.log2(prob_false_label)) \
        - (prob_true_label)*(math.log2(prob_true_label))


        # calculating the information gain for each feature
        info_gain = dict.fromkeys(feat_names)
        for key in info_gain:
            info_gain[key] = entropy_label - entropies_feat_names[key]

        #print(info_gain)
        print("Info gain:")
        for key in info_gain:
            print(f"\t {key},\t {info_gain[key]}")

        # returns the best feature
        return max(info_gain, key=info_gain.get)

        pass

    def classification_accuracy(self):
        """
        Using the classification accuracy method for figuring out the best
        method
        return: best feature (for classification accuracy)
        """
        feat_names = []
        for key in self.F:
            feat_names.append(key)

        # intialzing the frequency dictionary which keeps track of the
        # number of times a featue value appears in the data
        frequency = dict.fromkeys(feat_names)
        for key in frequency:
            frequency[key] = dict.fromkeys(self.F[key])
            for feat_val in frequency[key]:
                frequency[key][feat_val] = (0, 0)

        # keeping track of how many times the label is 1 and label is -1 for
        # each feature value
        # this information stored in the frequency dictionary
        for example in self.data:
            true_count = 0
            false_count = 0

            if example.label == -1:
                false_count += 1
            else:
                true_count += 1

            for key in self.F:
                feat_val = example.features[key]
                tc,fc = frequency[key][feat_val]
                tc += true_count
                fc += false_count
                frequency[key][feat_val] = (tc, fc)

        # initialzing dictionary for each feature
        # stores information useful for calculating classification
        # accuracy
        majority_labels = dict.fromkeys(feat_names)
        for key in majority_labels:
            majority_labels[key] = (0,0)

        # keeping track of the number of correct/incorrect predicted labels
        for example in self.data:
            for feat_name in example.features:
                feat_val = example.features[feat_name]
                tc, fc = frequency[feat_name][feat_val]
                predicted_label = 0

                if tc >= fc:
                    predicted_label = 1
                else:
                    predicted_label = -1

                true_label = example.label

                right, wrong = majority_labels[feat_name]

                if true_label == predicted_label:
                    majority_labels[feat_name] = (right+1, wrong)

                else:
                    majority_labels[feat_name] = (right, wrong+1)

        # calculating the classification accuracy for each feature
        classification_accuracy = dict.fromkeys(feat_names)

        for feat_name in classification_accuracy:
            tc, fc = majority_labels[feat_name]

            classification_accuracy[feat_name] = tc/(tc+fc)

        # returning the best feature based on classification accuracy
        return max(classification_accuracy, key = classification_accuracy.get)

        pass
