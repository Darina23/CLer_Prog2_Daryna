#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: unit testing of a WordBasedFeatures class.
"""


import unittest
from text_classification.word_based_features import WordBasedFeatures


class TestWordBasedFeatures(unittest.TestCase):
    """A class for WordBasedFeatures units testing."""

    def setUp(self):
        """Create a class object."""
        texts = ["OUrSelves", "Hello!"]
        tokenized_text = WordBasedFeatures(texts)
        self.text = tokenized_text

    def test_number_of_words(self):
        """Check if number of tokens is computed correctly."""
        self.assertEqual(self.text.number_of_words(), [1, 1],
                         "an incorrect result.")
        print("\n", "Number of words testing is done.")

    def test_average_length(self):
        """Check if text is not empty."""
        self.assertIsNot(self.text.average_length(), 0,
                         "a list of tokens is empty.")
        print("\n", "Average length testing is done.")

    def test_number_of_stopwords(self):
        """Check if upper case stop words are recognized"""
        self.assertEqual(self.text.number_of_stopwords(), [1, 0],
                         "stopwords are not recognized.")
        print("\n", "Number of stopwords testing is done.")

    def test_outputter(self):
        n_of_w = [1, 4]
        average = [2, 5]
        n_stop = [3, 6]
        res = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(self.text.outputter(n_of_w, average, n_stop), res,
                         "an output is not appropriate")
        print("\n", "Outputter testing is done.")


if __name__ == "__main__":
    unittest.main()
    print("\n","*************************************")
    print("\n", "Unit testing is successfully executed!")
