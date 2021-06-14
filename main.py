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
from Classifier import Classifier


def main():
    # split data
    training, validation, test = DataPreprocessing().split_data()
    print(type(training))
    df = DataPreprocessing().prepare_data_for_statistics("train")
    # apply word-based features
    WordBasedFeatures(df).features()
    # apply syntactic features
    SyntacticFeatures(df).features()
    SyntacticFeatures(df).outputter()
    # train model
    model = Classifier(df)


    print(model.predict(df))
    




if __name__ == "__main__":
    main()
