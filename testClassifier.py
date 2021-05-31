#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: unit testing of a Classifier class.
"""


import unittest


class Classifier():
    def data_getter(self, folder_name: str) -> list:
        """Get data from a given folder and convert it into tokens."""
        pass

    def filter_data(self, corpus: list) -> list:
        """
        Remove punctuation if needed, convert in a lower case, filter out
        numbers, stop words and the words, which occur less than n times.
        """
        pass

    def training_validation_test(self, corpus: list) -> tuple:
        """
        Divide a given corpus into training, validation and test datasets.
        """
        pass

    def features_statistics(self, corpus: list) -> tuple:
        """
        Call needed feautures classes and store results as a list for each
        dataset.
        """
        pass

    def evaluation(self, predicted: list, correct: list) -> float:
        """Evaluate an accuracy."""
        pass


class TestClassifier(unittest.TestCase):
    def test_data_getter(self):
        """Check if the method can get data from a given folder."""
        text = ["Hello", "world"]
        self.assertEqual(Classifier().data_getter(), text,
                         "incorrect. May be caused by hidden files like \
                         .DS_Store on MacOS, etc.")

    def test_filter_data(self):
        corpus = ['to', 'the', 'Moon', 'and', 'back']
        expected_res = ['moon', 'back']
        self.assertEqual(Classifier().filter_data(corpus), expected_res,
                         "incorrect result.")

    def test_traning_validation_test(self):
        training, validation, test = Classifier().training_validation_test()
        self.assertLess(len(validation), len(test))
        self.assertLess(len(validation), len(training))
        self.assertGreater(len(training), len(test))

    def test_features_statistics(self):
        training, validation, test = Classifier().training_validation_test()
        training_after, v_after, test_after = Classifier().features_statistics()
        self.assertNotEqual(training, training_after)
        self.assertNotEqual(test, test_after)

    def test_evaluation(self):
        predicted = ['a', 'b', 'c']
        correct = ['a', 'b', 'c', 'd', 'e', 'f']
        expect = 0.6
        self.assertEqual(Classifier().evaluation(predicted,correct), expect)
