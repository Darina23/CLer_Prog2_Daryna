#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MacOS
"""
Author: Daryna Ivanova.

Purpose: Implementation of word-based features: number of words, average word
length (characters), number of stopwords and number of emoticons.

"""

import emoji
import numpy as np
from text_classification.AbcFeatures import Features
from nltk.corpus import stopwords


class WordBasedFeatures(Features):
    """
    A class to implement some word-based features.

    Attributes
    ----------
    df
        A data frame. An inherited attribute from an abstract class
        Features().

    Methods
    -------
    features
        Implements word-based features. An abstract method.
        Computes avrage length of words in a sentence, counts words, stopwords
        and emoticons.
    """

    def __init__(self, df):
        super().__init__(df)

    def features(self):
        """Implement word-based fetures."""
        # count words in a sentence
        self.df["Words"] = self.df["Tweet text"].str.len()

        # compute average length of words for a sentence
        av_len = self.df["Tweet text"].apply(lambda x:
                                             np.mean([len(w) for w in
                                                      x.split()]))
        self.df['Word average length'] = av_len

        # count stop words in a sentence
        stop_words = stopwords.words("english")
        n_stopwords = self.df["Tweet text"].apply(lambda x:
                                                  len([i for i in x.split()
                                                       if i.lower() in
                                                       stop_words]))
        self.df["Stop words"] = n_stopwords

        # count emojis in a sentence
        n_emojis = self.df["Tweet text"].apply(lambda x:
                                               len([i for i in x if i in
                                                    emoji.UNICODE_EMOJI
                                                    ['en'].keys()]))
        self.df["Emoticons"] = n_emojis
