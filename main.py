# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:23:49 2025

@author: hugom
"""

import matplotlib.pyplot as plt
import numpy as np

from shuffle.metrics import mean_deck_next_card_entropy, next_type_probability
from shuffle.shuffle_methods import overhand, piles, random
from decks import get_Commander_deck, Deck

# TODO: compute how much time shuffle requires
if __name__ == '__main__':
    
    
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    deck = get_Commander_deck()
    n_shuffles = 20
    diff_to_types_matrix = np.zeros(n_shuffles + 1)
    for i in range(n_shuffles):
        next_type_prob = next_type_probability(deck)
        diff_to_types_matrix[i] = np.linalg.norm(next_type_prob - deck.get_proba_matrix())
        deck = overhand(deck, n_repetitions=1)
    axs[0].plot(diff_to_types_matrix, color='blue')
    
    deck = get_Commander_deck()
    n_shuffles = 5
    diff_to_types_matrix = np.zeros(n_shuffles + 1)
    for i in range(n_shuffles):
        next_type_prob = next_type_probability(deck)
        print(deck.deck)
        print(next_type_prob)
        diff_to_types_matrix[i] = np.linalg.norm(next_type_prob - deck.get_proba_matrix())
        deck = piles(deck, n_piles=3, pick_randomly=True, n_repetitions=1)
    axs[1].plot(diff_to_types_matrix, color='blue')
