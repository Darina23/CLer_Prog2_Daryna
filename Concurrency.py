#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daryna Ivanova

Mac OS, 2 cores
"""

import os
import nltk
import pandas as pd
import multiprocessing as mp


# 12.36s user 3.47s system 234% cpu 6.757 total

def pos_tags(text:list):
    return nltk.pos_tag(text)


def main():
    read_data = pd.read_csv(os.getcwd() + '/' + "text.csv")
    s = read_data["Tweet text"].apply(lambda x: x.split())
    mp.Pool().map(pos_tags, s)


if __name__ == "__main__":
    main()