#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: code execution

"""


from text_classification.word_based_features import WordBasedFeatures


def main():
    # toy text
    text = ["hello, world!", "My name is Alice.",
            "Humpty Dumpty had a great fall"]
    # tokenize
    tokenized_text = WordBasedFeatures(text)
    # compute number of words in a sentence
    n_words = tokenized_text.number_of_words()
    # compute average length of words in a sentence
    average = tokenized_text.average_length()
    # number of stopwords in a sentence
    n_stopwords = tokenized_text.number_of_stopwords()
    # print result
    print(tokenized_text.outputter(n_words, average, n_stopwords))


if __name__ == "__main__":
    main()
