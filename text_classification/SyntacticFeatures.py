#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: Implementation of syntactic features: number of function words.

Reflection:
    There were no internal changes in the feature classes. I created a new
    class for syntactic features. I seems, that the outputter() method is
    redundant in the feature classes, so I substituted features() method for
    outputter().
"""


from nltk import pos_tag
from text_classification.AbcFeatures import Features


class SyntacticFeatures(Features):
    """
    A class to implement some syntactic features.

    Attributes
    ----------
    df
        A data frame. An inherited attribute from an abstract class
        Features().

    Methods
    -------
    features
        Computes number of emoticons for each sentence of a text.
        A static method.

    """

    def __init__(self, df):
        super().__init__(df)

    def features(self):
        """Implement syntactic features."""
        # count emoticons
        func_w_tags = ["CC", "DT", "IN", "POS", "TO", "WDT", "WP", "WP$",
                       "WRB", "PDT", "RP", "PRP", "PRP$"]
        pos_tags = self.df["Tweet text"].str.split().apply(
            lambda x: len([i[1] for i in pos_tag(x) if i[1] in func_w_tags]))

        self.df["Function words"] = pos_tags
