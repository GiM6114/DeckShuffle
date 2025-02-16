# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:37:09 2025

@author: hugom
"""

from einops import repeat
import numpy as np

class Deck:
    def __init__(self, deck=None, n_cards_per_type=None):
        self.deck = deck
        if self.deck is None:
            self.n_types = len(n_cards_per_type)
            try:
                # same number of cards per type
                self.deck = repeat(np.arange(self.n_types), 'n -> (n repeat)', repeat=n_cards_per_type)
                self.n_cards_per_type = [n_cards_per_type] * self.n_types
            except Exception:
                # list of number of cards
                self.deck = np.concatenate([[i]*n_card for i,n_card in enumerate(n_cards_per_type)])
            self.n_cards_per_type = np.array(n_cards_per_type)
        else:
            types,self.n_cards_per_type = np.unique(self.deck, return_counts=True)
            self.n_types = len(types)
    
    def get_proba_matrix(self):
        return repeat(self.n_cards_per_type/len(self.deck), 'k -> n k', n=self.n_types)
    
    # TODO: slightly scrambled good order
    def small_scramble(self, bias):
        n_cards = len(self.deck)
        self.deck = np.zeros(n_cards)
        for i in range(n_cards):
            self.deck[i] = np.random.choice(self.n_types, size=1, p=self.n_cards_per_type/n_cards)
    
def get_Commander_deck():
    return Deck(n_cards_per_type=[36,64]) # 36 Lands, 64 non-Lands