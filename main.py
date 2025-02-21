# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:23:49 2025

@author: hugom
"""

import matplotlib.pyplot as plt
import numpy as np
from einops import reduce

from shuffle.metrics import mean_deck_next_card_entropy, next_type_probability, distance_to_random
from shuffle.shuffle_methods import overhand, overhand_time, piles, piles_time, random
from decks import get_Commander_deck, Deck

if __name__ == '__main__':
    
    seeds = range(20)
    n_shuffles = 100
    milestones_granularity = 0.05
    n_piles = 5
    shuffle_techniques = ((overhand, overhand_time, 'Overhand', {}),
                          (piles, piles_time, 'Piles', {'n_piles':n_piles,'pick_randomly':True}))
    n_techniques = len(shuffle_techniques)
    dist_random_seeds = np.zeros((n_techniques,len(seeds),n_shuffles+1))
    time_seeds = np.zeros((n_techniques,len(seeds),n_shuffles+1))
    time_until_seeds = np.zeros((n_techniques,len(seeds),len(np.arange(milestones_granularity,1,milestones_granularity))))
    for i,(shuffle_fn,time_fn,_,kwargs) in enumerate(shuffle_techniques):
        for seed in seeds:        
            deck = get_Commander_deck()
            dist_random,time,milestones,time_until = distance_to_random(
                deck, n_shuffles, shuffle_fn, milestones_granularity, time_fn, seed=seed, **kwargs)
            dist_random_seeds[i,seed] = dist_random
            time_seeds[i,seed] = time
            time_until_seeds[i,seed] = time_until
            
    fig, axs = plt.subplots(3, 1, figsize=(10, 16))
    
    means_dists = reduce(dist_random_seeds, 't s n -> t n', np.mean)
    stds_dists = reduce(dist_random_seeds, 't s n -> t n', np.std)
    means_time_untils = reduce(time_until_seeds, 't s n -> t n', np.mean)
    stds_time_untils = reduce(time_until_seeds, 't s n -> t n', np.std)
    colors = ['blue','red']
    for i,(means_dist,stds_dist,time,means_time_until,stds_time_until,color) in enumerate(zip(means_dists,stds_dists,time_seeds,means_time_untils,stds_time_untils,colors)):
        axs[0].plot(means_dist, color=color, label=shuffle_techniques[i][2])
        axs[0].fill_between(
            x=np.arange(len(means_dist)),
            y1=means_dist-stds_dist, 
            y2=means_dist+stds_dist, alpha=0.4, color=color)
        
        axs[1].plot(time[0], means_dist, color=color, label=shuffle_techniques[i][2])
        axs[1].fill_between(
            x=time[0], 
            y1=means_dist-stds_dist, 
            y2=means_dist+stds_dist, alpha=0.4, color=color)
        # plot of time necessary to reach each closeness state (given granularity)
        # if nb of shuffles not enough to reach desired smallest granularity, then the results will look wrong
        # as not reached = 0
        axs[2].plot(milestones, means_time_until, color=color, label=shuffle_techniques[i][2])
        axs[2].fill_between(
            x=milestones, 
            y1=means_time_until-stds_time_until, 
            y2=means_time_until+stds_time_until, alpha=0.4, color=color)
        axs[0].legend()
        axs[1].legend()
        axs[2].legend()

    axs[0].set_title('Distance to random matrix along number of shuffles')
    axs[0].set_xlabel('Number of shuffles')
    axs[0].set_ylabel('Distance to randomness matrix')    
        
    axs[1].set_title('Distance to random matrix along time spent shuffling')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Distance to randomness matrix')

    axs[2].xaxis.set_inverted(True)
    axs[2].set_xlabel('Distance to randomness matrix')
    axs[2].set_ylabel('Time (s)')
    axs[2].set_title('Minimal time to reach randomness matrix')