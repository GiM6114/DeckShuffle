In this small project, I define a deck by a number of types of cards and a number of cards per type.
Two deck shuffle methods are simulated: "overhand", the most classic and presumably inefficient shuffle method, and the presumably better method "piles", where cards are put iteratively in piles and then piles are picked up one by one to form the deck. I then define a well shuffled deck by how close the distribution given the current card of the next card is to the distribution of cards in the deck. This can be compared by computing the next card probability for each type of card. This matrix should be close to what I call the "randomness matrix" (which may or may not be a very bad denomination for this), which is a matrix where each row is the distribution of cards in the deck.
An applied example is shuffling Magic The Gathering (MTG) methods, where there are two main types of cards that one should get in the same amount after a shuffle: Land (36) and non-Land (64). In this case the randomness matrix is [[36/100,64/100],[36/100,64/100]].

Here is the results of shuffles after starting with a fully ordered MTG deck (first the non-Land then the Land cards):

![Results](https://github.com/GiM6114/DeckShuffle/blob/main/img/fully_sorted_deck_mtg.png?raw=true)

First plot gives the closeness to the randomness matrix with the number of times the shuffle is performed. The problem with this plot is that it is unfairly biased towards the piles method, as performing one such shuffle is a lot better than performing one shuffle with overhand, but takes a lot more time. Second plot gives the distance to the randomness matrix with respect to time. The last plot clarifies this by showing how much minimal time is required to reach each steps of closeness to the randomness matrix. Shaded area is mean +- std.
It clearly shows that the pile method is more efficient time-wise.
However, it must be mentionned that piles should be taken randomly in the piles method.
