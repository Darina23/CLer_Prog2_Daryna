#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: an abstract class implementation.

"""


from abc import ABC, abstractmethod


class Features(ABC):
    """
    An abstract class to implement some features.

    Attributes
    ----------
    df:
        Tokenizes a given text in a dataframe.

    Methods
    -------
    outputter:
        Creates an appropriate output.
    """

    def __init__(self, df):
        self.df = df
        super().__init__()

    @abstractmethod
    def features(self):
        """Implement features."""
        pass
