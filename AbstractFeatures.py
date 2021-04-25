#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: an abstract class implementation.

"""

from abc import ABC, abstractmethod
from nltk.tokenize import RegexpTokenizer


class Features(ABC):
    """
    An abstract class to implement some features.

    Attributes
    ----------
    text
        Tokenizes a given text.

    Methods
    -------
    outputter
        Creates an appropriate output.

    """

    def __init__(self, text: list):
        tokenizer = RegexpTokenizer(r"\w+")
        tokenized_text = []
        for string in text:
            tokenized_text.append(tokenizer.tokenize(string))
        self.text = tokenized_text
        super().__init__()

    @abstractmethod
    def outputter(self):
        """
        Create an appropriate output.

        Returns
        -------
        None.

        """
        pass
