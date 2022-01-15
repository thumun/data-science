"""
Command line and file reading utils for Lab 4.
Authors: Sara Mathieson + Allison Gong
Date: 8/26/2021
"""

from collections import OrderedDict
import optparse
import sys

# our imports
from Partition import *

def parse_args():
    """Parse command line arguments (train and test arff files)."""
    parser = optparse.OptionParser(description='parsing command line arguments')

    parser.add_option('-r', '--train_filename', type='string', help='path to' +\
        ' train arff file')
    parser.add_option('-e', '--test_filename', type='string', help='path to' + \
        ' test arff file')

    (opts, args) = parser.parse_args()

    mandatories = ['train_filename', 'test_filename']
    for m in mandatories:
        if not opts.__dict__[m]:
            print('mandatory option ' + m + ' is missing\n')
            parser.print_help()
            sys.exit()

    return opts

def read_arff(filename):
    """Read arff file into Partition format."""
    arff_file = open(filename,'r')
    data = [] # list of Examples
    F = OrderedDict() # dictionary

    header = arff_file.readline()
    line = arff_file.readline().strip()

    # read the attributes
    while line != "@data":
        line = line.replace('{','').replace('}','').replace(',','')
        tokens = line.split()
        name = tokens[1][1:-1]
        features = tokens[2:]

        # label
        if name != "class":
            F[name] = features
        else:
            first = tokens[2]
        line = arff_file.readline().strip()

    # read the examples
    for line in arff_file:
        tokens = line.strip().split(",")
        X_dict = {}
        i = 0
        for key in F:
            val = tokens[i]
            X_dict[key] = val
            i += 1
        label = -1 if tokens[-1] == "e" else 1 # 'e'=edible, 'p'=poisonous
        data.append(Example(X_dict, label))

    arff_file.close()

    partition = Partition(data, F)
    return partition
