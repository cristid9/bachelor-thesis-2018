Ideas collected in order to generate the design of the network
===============================================================

Usefull references 
------------------
* Nerual Turin Machine
* Differentiable Neural COmputer
* seq2seq

Abstract
--------
For now I will focus on buolding a network that given an unsorted sequence, it generates the optimal swap for that sequence. That
is, one single swap. This way I have to chain this network multiple times until the full sequence is sorted. Some other implementation 
details are discussed bellow.

* loss function
  - For now, the perfect loss function seems to be `j-i` where `j` and `i` are indexes
   of numbers in the network. The network should stop when I have `i==j`. 
* `POC` capacity
   - for the initial proof of concept of the network, the perfect size of the network seems to be `4`, 
    then I will be increasing the size of the network by powers of 2. Basically, keep doubling it
* initializing weights
  - the weights of the netwokr may be inutialized with the `xavier` technique. That is, using `xavier initialization`
* The real problem
  - while this idea seems fesable, the problem is how do I adapt the network to work on sizes bigger than `16` (that is, because 16!
   is tu much to memorize for every network). There is a handy workaround, using `independent validation set`
   
Todo (priority 0)
------------------
* train the `poc nn` for `n=4` and get it to work.
   
Papers used in making this initial design
------------------------------------------
* http://aclweb.org/anthology/I17-3017

Misc
-----
* There is a tool wich may come handy when developing pocs in this field: `google colab`
