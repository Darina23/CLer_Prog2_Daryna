#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daryna Ivanova
Mac OS, 2 cores
"""

import os
import pandas as pd
import nltk


# 2.89s user 0.93s system 60% cpu 6.283 total

def pos_tags(text:list):
    return nltk.pos_tag(text)


def main():
    read_data = pd.read_csv(os.getcwd() + '/' + "text.csv")
    s = read_data["Tweet text"].apply(lambda x: x.split())
    s = s.apply(pd.Series).stack().reset_index(drop = True)
    text = s.to_list()
    pos_tags(text)


if __name__ == "__main__":
    main()
