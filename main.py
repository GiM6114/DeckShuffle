# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:23:49 2025

@author: hugom
"""

import matplotlib.pyplot as plt
import numpy as np

from shuffle.metrics import mean_deck_next_card_entropy, next_type_probability, distance_to_random
from shuffle.shuffle_methods import overhand, overhand_time, piles, piles_time, random
from decks import get_Commander_deck, Deck

if __name__ == '__main__':
    
    seeds = range(20)
    dist_random_oh_seeds = np.zeros((len(seeds)))
    for seed in seeds:
        np.random.seed(seed)
        
        fig, axs = plt.subplots(2, 1, figsize=(10, 8))
        deck = get_Commander_deck()
        n_shuffles = 50
        dist_random_oh,milestones,time_until_oh = distance_to_random(deck, n_shuffles, overhand, 0.1, overhand_time)
        axs[0].plot(dist_random_oh, color='blue')
        
        deck = get_Commander_deck()
        n_piles = 5
        dist_random_p,milestones,time_until_p = distance_to_random(deck, n_shuffles, piles, 0.1, piles_time, n_piles=n_piles, pick_randomly=True)
        axs[0].plot(dist_random_p, color='red')
        
        axs[0].set_xlabel('Time (s)')
        axs[0].set_ylabel('Distance to randomness')
    
    # plot nb of time necessary to reach closeness
    axs[1].plot(milestones, time_until_oh, color='blue')
    axs[1].plot(milestones, time_until_p, color='red')
    axs[1].xaxis.set_inverted(True)
    axs[1].set_xlabel('Distance to randomness')
    axs[1].set_ylabel('Time (s)')
    axs[1].set_title('Minimal time to reach randomness')