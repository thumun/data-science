"""
Author      : Annie Wernerfelt, Neha Thumu
Class       : CS260 Project
Date        : 12/09/21
Description : This is the Partition class for the project. It contains a method
which calculates entropy to return the best feature. It also contains are method
which uses classification to find the best feature.
"""

import math
import matplotlib.pyplot as plt
import collections

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

    """
    End of generic Partition code. Start of entropy code
    """
    def best_feature(self):
        """
        This class calculates a dictionary of entropies for each feature
        return: the best feature
        """
        pos_count=0
        prob_pos=0

        #calculate the entropy of the data as a whole
        for i in self.data:
            if i.label==1:
                pos_count+=1
        prob_pos = pos_count / self.n

        entropy = self.calc_entropy(prob_pos)

        dict_prob={}
        dict_total={}
        sum_lst=[]

        # create a dictionary of probabilities that a feature value is positive
        for i in self.F:
            dict_prob[i]={}
            dict_total[i]={}
            for x in range(len(self.F[i])):
                dict_prob[i][self.F[i][x]]=self.calc_prob(i, self.F[i][x])
                dict_total[i][self.F[i][x]]=self.calc_total(i, self.F[i][x])

        entropy_dict={}

        # calculate entropy * probability and put them in a dictionary
        for i in self.F:
            sum=0
            for x in range(len(dict_prob[i].values())):
                ent = self.calc_entropy(list(dict_prob[i].values())[x])
                # print(list(dict_total[i].keys())[x])
                prob = self.calc_total(i, list(dict_total[i].keys())[x])
                sum+=ent*prob
            entropy_dict[i]=entropy-sum

        # (this line calls the classification method)
        print("CLASSIFICATION-->", self.classification())

        # swap keys and values of the entropy dictionary. This is necessary
        # to plot the entropy values in ascending order
        new_dict = {value : key for (key, value) in entropy_dict.items()}
        sorted_dict=collections.OrderedDict(sorted(new_dict.items()))
        x_vals=sorted_dict.values()
        y_vals=sorted_dict.keys()

        # plot entropy values using bar plot
        plt.bar(x_vals, y_vals, color='#00dc4d', edgecolor='black')
        plt.title("Entropy for each feature, n=%i" %int(self.n*5/4))
        plt.xlabel("Feature")
        plt.ylabel("Entropy")
        # plt.savefig("figures/Entropy.pdf", format='pdf')
        plt.show()
        plt.clf()

        # this line calls the method to find the best feature based on the
        # dictionary created above. We return the best feature
        return self.find_best(entropy_dict)


    def calc_entropy(self, pct):
        """
        This helper method takes in a percentage and implements the entropy
        equation
        pct: the percentage of time the label is positive
        return: the entropy
        """
        if pct==0:
            return -(1-pct)*math.log2(1-pct)
        if pct==1:
            return -pct*math.log2(pct)
        else:
            return -pct*math.log2(pct)-(1-pct)*math.log2(1-pct)


    def calc_prob(self, feature_name, feature_val):
        """
        This helper method calculates the probability that a feature value is
        positive  by counting the number of times it shows up in the data and,
        of those times, how many are have a positive label
        feature_name: the feature name
        feature_val: the feature value
        return: the probability
        """
        total_count=0
        pos_count_indiv=0
        for i in range(self.n):
            if self.data[i].features[feature_name] == feature_val:
                total_count+=1
                if self.data[i].label==1:
                    pos_count_indiv+=1
        if(total_count==0):
            total_count=1
        return pos_count_indiv/total_count


    def calc_total(self, feature_name, feature_val):
        """
        This helper method calculates the percentage of times a feature value
        appears for a given feature name
        feature_name: the feature name
        feature_val: the feature value
        return: the percentage
        """
        feature_val_count=0
        for i in range(self.n):
            if self.data[i].features[feature_name] == feature_val:
                feature_val_count+=1
        return feature_val_count / self.n

    def find_best(self, dict):
        """
        This helper method finds the highest percentage in the dictionary of
        entropies to return the best feature
        dict: the dictionary of entropy increases
        return: the feature with the highest entropy increase
        """
        best=list(dict)[0]
        for i in dict:
            if dict[i] > dict[best]:
                best=i
        return best

    def classification(self):
        """
        This method finds the maximum classification accuracy of each feature.
        The goal is to compare the results of classification to the results of
        entropy.
        return: the feature with the highest accuracy
        """
        # this dictionary classifies each example as 1 or 0 based on if the
        # probability of it being positive is above or below 50%
        dict={}
        for i in self.F:
            dict[i]={}
            for x in range(len(self.F[i])):
                if self.calc_prob(i, self.F[i][x]) >= 0.5:
                    dict[i][self.F[i][x]] = 1
                else:
                    dict[i][self.F[i][x]] = -1

        # declare variables to be used later
        accurate=0
        inaccurate=0
        accuracy = 0
        best_feature = ''
        accuracies_list=[]
        features_list=[]
        accuracies_dict={}
        # this calculates the classification accuracy for each feature by
        # counting how many times the label is correct
        for x in (self.F):
            features_list.append(x)
            for i in range(self.n):
                for j in self.F[x]:
                    if self.data[i].features[x] == j:
                        if(dict[x][j] == self.data[i].label):
                            accurate+=1
                        else: inaccurate+=1
            if accurate+inaccurate==0:
                accurate+=1
            accuracies_dict[x]=accurate/(accurate+inaccurate)
            # if the previous highest accuracy is less than the current
            # accuracy, the best feature is the current feature
            if accurate/(accurate+inaccurate) > accuracy:
                accuracy = accurate/(accurate+inaccurate)
                best_feature=x
            accuracies_list.append(accurate/(accurate+inaccurate))

        # swap keys and values of dictionary. this is again used for sorting
        # the bar plot in ascending order
        new_dict = {value : key for (key, value) in accuracies_dict.items()}
        sorted_dict=collections.OrderedDict(sorted(new_dict.items()))
        x_vals=sorted_dict.values()
        y_vals=sorted_dict.keys()

        # plot the classification accuracy results
        plt.bar(x_vals, y_vals, color='#00dc4d', edgecolor='black')

        plt.ylim(0.6, 0.72)
        plt.title("Classification accuracy for each feature, n=%i" \
        %int(self.n*5/4))
        plt.xlabel("Feature")
        plt.ylabel("Classification accuracy")
        # plt.savefig("figures/ClassificationAccuracy.pdf", format='pdf')
        plt.show()
        plt.clf()
        return best_feature
