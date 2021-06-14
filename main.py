#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: code execution

"""


from DataPreprocessing import DataPreprocessing
from text_classification.WordBasedFeatures import WordBasedFeatures
from text_classification.SyntacticFeatures import SyntacticFeatures

def main():
    # split data
    training, validation, test = DataPreprocessing().split_data()
    print(type(training))
    df = DataPreprocessing().prepare_data_for_statistics("train")
    # compute word-based features
    # WordBasedFeatures(df).number_of_words()
    # # compute average length of words in a sentence
    # WordBasedFeatures(df).average_length()
    # # number of stopwords in a sentence
    # WordBasedFeatures(df).number_of_stopwords()
    # WordBasedFeatures(df).number_of_emojis()
    # # print result
    # WordBasedFeatures(df).outputter()
    # SyntacticFeatures(df).number_of_function_words()
    # SyntacticFeatures(df).outputter()
    WordBasedFeatures(df).features()
    SyntacticFeatures(df).features()
    WordBasedFeatures(df).outputter()
        # SyntacticFeatures(df).number_of_function_words()
    SyntacticFeatures(df).outputter()


if __name__ == "__main__":
    main()
