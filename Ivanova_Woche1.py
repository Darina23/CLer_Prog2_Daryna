#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: Implementation of Word-based features: number of words, average word
length (characters) and number of stopwords.

"""

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


class WordBasedFeatures():
    """
    A class to implement some word-based features.

    Methods
    -------
    tokenize_text(text: list)
        Tokenizes sentences of a given text. An auxiliary method.

    number_of_words(tokenized_text: list)
        Computes number of words for each sentence of a text.

    average_length(tokenized_text: list)
        Computes average length of words in a sentence.

    number_of_stopwords(tokenized_text: list)
        Counts stopwords in a sentence.

    outputter(n_of_words: list, average: list, n_stopwords: list)
         Collectt result of number_of_words, average_length and
        number_of_stopwords functions and creates an appropriate output.
        An auxiliary method.

    """

    def tokenize_text(self, text: list) -> list:
        """
        Tokenize a text.

        Parameters
        ----------
        text : list
            List of strings.

        Returns
        -------
        tokenized_text : list
            Tokenized strings.

        """
        tokenizer = RegexpTokenizer(r"\w+")
        tokenized_text = []
        for string in text:
            tokenized_text.append(tokenizer.tokenize(string))

        return tokenized_text

    def number_of_words(self, tokenized_text: list) -> list:
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
        for string in tokenized_text:
            n_words.append(len(string))

        return n_words

    def average_length(self, tokenized_text: list) -> list:
        """
        Compute average lenth of words for a sentence.

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
        for string in tokenized_text:
            average.append(sum(map(len, string)) / len(string))

        return average

    def number_of_stopwords(self, tokenized_text: list) -> list:
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
        for string in tokenized_text:
            counter = 0
            for stop_w in stop_words:
                if stop_w in string:
                    counter += 1
            n_stopwords.append(counter)

        return n_stopwords

    def outputter(self, n_of_words: list, average: list,
                  n_stopwords: list) -> list:
        """
        Make an appropriate output.

        Auxiliary method.

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


def main():
    # toy text
    text = ["hello, world!", "My name is Alice.",
            "Humpty Dumpty had a great fall"]
    # tokenize
    tokenized_text = WordBasedFeatures().tokenize_text(text)
    # compute number of words in a sentence
    n_words = WordBasedFeatures().number_of_words(tokenized_text)
    # compute average length of words in a sentence
    average = WordBasedFeatures().average_length(tokenized_text)
    # number of stopwords in a sentence
    n_stopwords = WordBasedFeatures().number_of_stopwords(tokenized_text)
    # print result
    print(WordBasedFeatures().outputter(n_words, average, n_stopwords))


if __name__ == "__main__":
    main()
