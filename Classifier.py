#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: Implementation of syntactic features: number of function words.
"""


import pandas as pd
import numpy as np
from text_classification.AbcFeatures import Features


class Classifier():
    """A class to train and predict models."""

    def __init__(self, df):
        self.df = df
        
        means = self.df[['Label', 'Words', 'Stop words', 'Function words',
                         'Emoticons', 'Word average length']].groupby(
                             ["Label"]).mean()

        self.zero_mean = means.loc[0,:]
        self.one_mean = means.loc[1,:]
        
        print(self.zero_mean)

    def predict(self, dataset):
        """Predict a class."""
        data = dataset[['Words', 'Stop words', 'Function words', 'Emoticons',
                        'Word average length']].values
        distances_to_zero = np.sum(np.abs(data - self.zero_mean.values.T),
                                   axis=1)
        distances_to_one = np.sum(np.abs(data - self.one_mean.values.T),
                                  axis=1)

        data_zero = distances_to_zero > distances_to_one
        print(pd.DataFrame(data_zero, columns=["Class"]))

        return self.df.assign(Class=data_zero)
