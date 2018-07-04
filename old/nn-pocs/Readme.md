Will contain proof-of-concept of the target NN.

Approaches used so far
----------------------
* seq2seq 
  - feed a seq2seq network with pairs of unsorted numbers and pairs of right swaps (not working well)
* create a network that generates a single swap, this means a chain of these networks (the preferred sollution so far)


Components
----------

* loss functions
  - `(j - i)` where `j` and `i` are the positions of swaps in the sequence
