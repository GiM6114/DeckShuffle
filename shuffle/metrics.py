# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:25:56 2025

@author: hugom
"""

from einops import reduce
import numpy as np

def next_type_probability(deck):
    """
        For every type gives the conditional probability distribution of next type
        Best shuffle if entry in i,j is 1/proportion of cards of type j
    """
    n_types,deck_arr = deck.n_types,deck.deck
    next_card_counts = np.zeros((n_types,n_types))
    for i in range(len(deck_arr) - 1):
        next_card_counts[deck_arr[i],deck_arr[i+1]] += 1
    return next_card_counts / reduce(next_card_counts, 'k n -> k 1', np.sum)

def _mean_entropy(proba_matrix):
    """
     proba_matrix: n x n, each row a proability distribution
     Valid metric iff equal number of each cards
    """
    logs = np.log(proba_matrix, where=proba_matrix!=0) # where avoids computing log of 0 and getting warnings
    return np.mean(-reduce(proba_matrix * logs, 'k n -> k', np.sum))

def mean_deck_next_card_entropy(deck):
    return _mean_entropy(next_type_probability(deck))

