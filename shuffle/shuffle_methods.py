# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:02:07 2025

@author: hugom
"""

from einops import repeat
import numpy as np
import random

from decks import Deck

def overhand(deck, n_repetitions=1):
    """
        Classic shuffle that consist in taking a lot of cards X from the bottom
        and then putting the first cards of X on top of the bottom, iteratively
        until X is empty.
        Can be seen as a roll over X
    """
    deck_arr = deck.deck
    deck_arr = np.copy(deck_arr)
    for _ in range(n_repetitions):
        idx = 0
        while True:
            cut_point = np.random.randint(3, len(deck_arr)//4)
            cut_point = min(len(deck_arr) - idx, cut_point) # make sure not too high
            deck_arr[:len(deck_arr)-idx] = np.roll(deck_arr[:len(deck_arr)-idx], -cut_point)
            idx += cut_point
            if idx >= len(deck_arr):
                break
    return Deck(deck=deck_arr)

def overhand_time(deck, n_repetitions=1):
    """
        3 seconds for a 40 cards deck, and linear scaling
    """
    return n_repetitions * (3 * len(deck)/40)

def piles(deck, n_piles, pick_randomly=False, n_repetitions=1):
    """
        Deterministic shuffle where cards are put on piles one by one. Then the piles are put on top of one another.
        pick_randomly: whether to pick each pile in a random order at the end
    """
    deck_arr = deck.deck
    for _ in range(n_repetitions):
        piles = []
        for i in range(n_piles):
            piles.append(np.flip(deck_arr[i::n_piles]))
        if pick_randomly:
            random.shuffle(piles)      
        shuffled_deck_arr = np.array(np.concatenate(piles))            
        
        deck_arr = shuffled_deck_arr
    return Deck(deck=shuffled_deck_arr)

def piles_time(deck, n_piles, pick_randomly=False, n_repetitions=1):
    """
        Supposes 4 cards are placed in 1 second, 2 piles gathered in 1 second (at the end)
    """
    return n_repetitions * (len(deck) / 4 + n_piles / 2)

def random_permutation(deck):
    return np.random.permutation(deck)

if __name__ == '__main__':
    deck = Deck(n_cards_per_type=[5,5])
    # shuffled_deck = overhand(deck, 5)
    shuffled_deck = piles(deck, 3)
    print(shuffled_deck.deck)
    
