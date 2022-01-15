"""
Author: Neha Thumu
Class: CS260
Date: 12/9/21
Description: This file was an attempt at creating a splits method to make our
data discrete.

Note:
We ended up using the KBinsDiscretizer instead since the splits method was not
working properly.
"""

import copy


def cont_to_discrete(partition, feature_name):
    """
    A method that creates splits for the data. These splits will be used to
    make the continuous data into discrete values.

    Creates the splits by first sorting the data, then merging those with the
    same feature value (and changing their label), and then finally looking at
    the places where the label changes to calculate the splits.

    partition: the partition containing the data and other attributes
    feature_name: feature name
    result: list of splits

    """

    # creating a copy of the data to sort
    sorted = copy.deepcopy(partition)

    # sort by the feature values -- neha's note: is working!
    sorted.data.sort(key = lambda x: x.features[feature_name])

    # gathering those with the same feature value
    feature_duplicates = {}
    for example in sorted.data[0:]:
        if example.features[feature_name] in feature_duplicates:
            feature_duplicates[example.features[feature_name]].append(example)
        else:
            feature_duplicates[example.features[feature_name]] = [example]

    # merging same feature value and changing label to 2 (differentiate from 0
    # or 1)
    updated_data = []
    for key in feature_duplicates:
        if len(feature_duplicates[key]) > 1:
            feature_duplicates[key][0].label = 2

        updated_data.append(feature_duplicates[key][0])

    sorted.data = updated_data

    splits = []

    previous = sorted.data[0]

    # finding the splits by looking at a change in label
    for example in sorted.data[1:]:

        if example.label != previous.label:
            val_one=0
            val_two=0
            # val_one = float(previous.features[feature_name])
            # val_two = float(example.features[feature_name])
            if is_number(previous.features[feature_name]):
                val_one = float(previous.features[feature_name])
            if is_number(example.features[feature_name]):
                val_two = float(example.features[feature_name])

            avg = (val_two + val_one)/2

            splits.append(avg)

            # count = 0 # re-initializing count

        previous = example

    # were going to incorporate the making data discrete based on splits in
    # main/where we handled the methods
    return(splits)

def is_number(s):
    """
    checking if given input is a float or not
    s: input
    return: boolean saying if s is a float
    """
    try:
        float(s)
        return True
    except ValueError:
        return False
