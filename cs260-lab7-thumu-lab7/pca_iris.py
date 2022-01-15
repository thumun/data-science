"""
PCA for Irises
Author: Neha Thumu
Date: 11/5/21
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn import decomposition
from sklearn import datasets

def main():
    iris = datasets.load_iris()
    X = iris.data

    # info about x: (note to self)
    # sepal length in cm
    # sepal width in cm
    # petal length in cm
    # petal width in cm

    y = iris.target

    # info about y: (note to self)
    # Iris Setosa (label 0)
    # Iris Versicolour (label 1)
    # Iris Virginica (label 2)

    # print(X)
    # print(y)

    # running PCA
    pca = decomposition.PCA(n_components=2)
    pca.fit(X)
    transformed_X = pca.transform(X)

    # getting the values to plot
    x_coordinates = transformed_X[:, 0]
    y_coordinates = transformed_X[:, 1]

    possible_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    y_labels = []

    # creating labels list based on which labels are in the data
    for label in y:
        if label not in y_labels:
            y_labels.append(label)

    # assigning colors to labels
    label_colors_dict = dict.fromkeys(y_labels)
    for key in label_colors_dict:
        label_colors_dict[key] = possible_colors[0]
        possible_colors.pop(0)

    # print(label_colors_dict)

    # plotting the data
    count = 0
    for label in y:
        plt.scatter(x_coordinates[count], y_coordinates[count], \
        color=label_colors_dict[label])
        count+=1

    # create legend
    leg_objects = []
    names=["Iris Setosa", "Iris Versicolour", "Iris Virginica"]
    for i in range(len(y_labels)):
        circle, = plt.plot([], 'o', c=label_colors_dict[i])
        leg_objects.append(circle)
    plt.legend(leg_objects, names)

    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("Iris Flowers")

    # plt.savefig("figures/iris.pdf")
    plt.show()

    pass

if __name__ == "__main__":
    main()
