#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: Implementation of Word-based features: number of words, average word
length (characters) and number of stopwords.

"""

import numpy as np
from tabulate import tabulate
from text_classification.AbcFeatures import Features
from nltk.corpus import stopwords


class WordBasedFeatures(Features):
    """
    A class to implement some word-based features.

    Attributes
    ----------
    text
        Tokenizes a given text. An inherited attribute from an abstract class
        Features().

    Methods
    -------
    number_of_words
        Computes number of words for each sentence of a text.

    average_length
        Computes average length of words in a sentence.

    number_of_stopwords
        Counts stopwords in a sentence.

    outputter(n_of_words: list, average: list, n_stopwords: list)
        Collects results of number_of_words, average_length and
        number_of_stopwords functions and creates an appropriate output.
        An inherited method from an abstract class Features().

    """

    def __init__(self, text):
        super().__init__(text)

    def number_of_words(self):
        """
        Count words per sentence and create an analagous column in a data frame
        for results.

        """
        self.text["number_of_words"] = self.text["tweet text"].str.len()

    def average_length(self):
        """Compute average length of words for a sentence."""
        av = self.text["tweet text"].apply(lambda x:
                                           np.mean([len(w) for w in
                                                    x.split()]))
        self.text['word_avg_length'] = av

    def number_of_stopwords(self) -> list:
        """Count stopwords in a sentence."""
        stop_words = stopwords.words("english")
        n_stopwords = self.text["tweet text"].apply(lambda x:
                                                    len([i for i in x.split()
                                                         if i.lower() in
                                                         stop_words]))
        self.text["n_of_stopwords"] = n_stopwords

    def outputter(self):
        """Make an appropriate output."""
        print(tabulate(self.text, headers='keys', tablefmt='psql'))
