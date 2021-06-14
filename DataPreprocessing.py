#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: data preprocessing.

"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split


class DataPreprocessing():

    def __init__(self):
        """
        Read data as a csv file and converts it into data frame.

        Attributes
        ----------
        data:
            Dataset in csv format.
        df:
            Dataframe.

        """
        path_to_data = os.getcwd() + \
            "/datasets/goldtest_TaskA/SemEval2018-T3_gold_test_taskA_emoji.txt"
        data = pd.read_csv(path_to_data, sep='\t',
                           engine="python", error_bad_lines=False)
        df = pd.DataFrame(data)
        self.data = data
        self.df = df
        # print(df.describe(include=[np.object]))

    def split_data(self) -> tuple:
        """
        Split data into training, validation and test sets and save them in
        separate csv files.

        Returns
        -------
        tuple:
            (train, validation, test).

        """
        train1, test = train_test_split(self.df, test_size=.2,
                                        random_state=42)
        train, validation = train_test_split(train1, test_size=.2,
                                             random_state=42)
        # save train, validation and test datasets as csv files
        train.to_csv(r"datasets/training_data.csv", index=False)
        validation.to_csv(r"datasets/validation_data.csv", index=False)
        test.to_csv(r"datasets/test_data.csv", index=False)

        return train, validation, test

    def prepare_data_for_statistics(self, dataset: str):
        """
        Access an appropriate dataset to extract statistics (features) from.

        Parameters
        ----------
        dataset : str
            User's input.

        Returns
        -------
        df : pandas.DataFrame
            Data frame.

        """
        df = self.split_data()
        if dataset == "train":
            df = df[0]
        elif dataset == "validation":
            df = df[1]
        else:
            df = df[2]
        return df
