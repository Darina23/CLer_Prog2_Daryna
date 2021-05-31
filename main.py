#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: code execution

"""


from Classifier import Classifier
from text_classification.WordBasedFeatures import WordBasedFeatures


def main():
    # split data
    training, validation, test = Classifier().split_data()
    print(type(training))
    text = Classifier().prepare_data_for_statistics("train")
    # compute number of words in a sentence
    WordBasedFeatures(text).number_of_words()
    # compute average length of words in a sentence
    WordBasedFeatures(text).average_length()
    # number of stopwords in a sentence
    WordBasedFeatures(text).number_of_stopwords()
    # print result
    WordBasedFeatures(text).outputter()


if __name__ == "__main__":
    main()
