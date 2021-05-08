#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: Implementation of Word-based features: number of words, average word
length (characters) and number of stopwords.

"""

from text_classification.abc_features import Features
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

    def __init__(self, text: list):
        super().__init__(text)

    def number_of_words(self) -> list:
        """
        Count words in a sentence.

        Parameters
        ----------
        tokenized_text : list
            List of tokens for each sentence.

        Returns
        -------
        n_words : list
            Number of words for each sentence.

        """
        n_words = []
        for string in self.text:
            n_words.append(len(string))

        return n_words

    def average_length(self) -> list:
        """
        Compute average length of words for a sentence.

        Parameters
        ----------
        tokenized_text : list
            Tokenized strings.

        Returns
        -------
        average : list
            Computed values for each sentence.

        """
        average = []
        for string in self.text:
            average.append(sum(map(len, string)) / len(string))

        return average

    def number_of_stopwords(self) -> list:
        """
        Count stopwords in a sentence.

        Parameters
        ----------
        tokenized_text : list
            Tokenized strings.

        Returns
        -------
        n_stopwords : list
            Number of stopwords in a sentence.

        """
        stop_words = stopwords.words("english")
        n_stopwords = []
        for sent in self.text:
            sent = [w.lower() for w in sent]
            counter = 0
            for stop_w in stop_words:
                if stop_w in sent:
                    counter += 1
            n_stopwords.append(counter)

        return n_stopwords

    def outputter(self, n_of_words: list, average: list,
                  n_stopwords: list) -> list:
        """
        Make an appropriate output.

        An auxiliary method.

        Parameters
        ----------
        n_of_words : list
            Number of words in a sentence.
        average : list
            Average length of words in a sentence.
        n_stopwords : list
            Number of stopwords in a sentence.

        Returns
        -------
        out : list
            Nested list with number of words, average length of words and
            number of stopwords for a sentence in a given text.

        """
        res = list(zip(n_of_words, average, n_stopwords))
        out = [list(el) for el in res]

        return out
