"""
PCA starter code for 1000 genomes data.
Author: Sara Mathieson, Neha Thumu
Date: 11/5/21
"""

import matplotlib.pyplot as plt
import numpy as np
import optparse
import sys

# for PCA
from sklearn import decomposition
from sklearn import datasets

#-------------------------------------------------------------------------------
# GLOBALS
#-------------------------------------------------------------------------------

# these match the 1000 genomes colors: http://www.internationalgenome.org/
# matplotlib named colors:
# https://matplotlib.org/gallery/color/named_colors.html
POP_COLOR = {'AFR':'gold',
             'AMR':'red',
             'EAS':'green',
             'EUR':'blue',
             'SAS':'purple'}

#-------------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------------

def main():
    # set up and parse files
    opts = parse_args()

    # TODO write a parse_samples function & uncomment below
    sample_dict = parse_samples(opts.sample_filename)

    # parse VCF file to get X (input to PCA)
    # TODO call parse_vcf

    X = parse_vcf(opts.vcf_filename, sample_dict, opts.n, opts.p)

    print("finished reading VCF")

    # run PCA
    pca = decomposition.PCA(n_components=2)
    pca.fit(X[0])
    transformed_X = pca.transform(X[0])

    # getting the variance for each PC
    print(pca.explained_variance_ratio_)

    x_coordinates = transformed_X[:, 0]
    y_coordinates = transformed_X[:, 1]

    y_labels = []

    # creating y_labels based on the populations that exist in the data
    for label in X[1]:
        if label not in y_labels:
            y_labels.append(label)


    # assigning colors to labels
    label_colors_dict = dict.fromkeys(y_labels)
    for key in label_colors_dict:
        label_colors_dict[key] = POP_COLOR[key]
    # print(label_colors_dict)

    # plotting each point as a scatter plot
    count = 0
    for label in X[1]:
        plt.scatter(x_coordinates[count], y_coordinates[count], \
        color=label_colors_dict[label])
        count+=1

    # create legend
    leg_objects = []
    for i in range(len(y_labels)):
        circle, = plt.plot([], 'o', c=label_colors_dict[y_labels[i]])
        leg_objects.append(circle)
    plt.legend(leg_objects, y_labels)

    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("Super Populations of Humans") #think of better name

    plt.savefig("figures/human.pdf")
    plt.show()

#-------------------------------------------------------------------------------
# HELPERS
#-------------------------------------------------------------------------------

def parse_args():
    """Parse and return command-line arguments (only VCF file here)"""
    parser = optparse.OptionParser(description='run PCA on 1000 genomes data')

    parser.add_option('-v', '--vcf_filename', type='string', \
        help='path to input VCF')
    parser.add_option('-s', '--sample_filename', type='string', \
        help='path to input sample names & pops')
    parser.add_option('-n', '--n', type='int', default=20, \
        help='number of samples to use, max=5008')
    parser.add_option('-p', '--p', type='int', default=1000, \
        help='number of features (SNPs) to use, max=600,000 (approx)')
    parser.add_option('-o', '--out_filename', type='string', \
        help='path to output file (plot in pdf format)')
    (opts, args) = parser.parse_args()

    mandatories = ['vcf_filename','sample_filename']
    for m in mandatories:
        if not opts.__dict__[m]:
            print('mandatory option ' + m + ' is missing\n')
            parser.print_help()
            sys.exit()

    return opts

def parse_vcf(filename, sample_dict, n, p):
    """
    Parse a VCF file to create an nxp numpy matrix that we can then input
    into PCA. n is the number of samples (each individual counts as 2 samples)
    and p is the number of features (SNPs in our case). sample_dict should be a
    dictionary that maps sample name to super-population.
    """

    vcf_file = open(filename, 'r')
    num_p = 0 # keep track of the number of snps

    # set up data structures for SNPs and population names
    snp_array = []
    pop_lst = []

    # keep reading while we don't have enough SNPs
    while num_p < p:
        line = vcf_file.readline()
        if not line.startswith("##"): # ignore starting headers
            tokens = line.split()

            # main header shows the sample names
            if line.startswith("#"):
                pop_lst = [sample_dict[sample] for sample in tokens[9:]]
                pop_lst = np.repeat(pop_lst,2)[:n]

            # parse each SNP
            else:
                # get the alleles as a list of 0s and 1s
                alleles = [int(x) for x in "".join(tokens[9:]).replace("|","")]
                alleles = alleles[:n] # keep only n samples
                snp_array.append(alleles)

                # print progress
                if num_p % 10000 == 0:
                    print(num_p,"/",p)
                num_p += 1

    vcf_file.close()
    assert len(pop_lst) == len(snp_array[0])
    # take transpose to make X matrix which is nxp
    return np.transpose(np.array(snp_array)), pop_lst


def parse_samples(filename):
    """
    reading the data to get the samples and their super populations to make
    a dictionary
    filename: the file
    return: the dictionary where each sample is mapped to a super population
    """
    file = open(filename, 'r')
    lines = file.readlines()

    samples = {}

    for line in lines[1:]:
        tokens = line.rstrip().split("\t")
        samples[tokens[0]] = tokens[5]

    return samples

    pass

if __name__ == '__main__':
    main()
