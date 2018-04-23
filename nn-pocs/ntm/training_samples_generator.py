import random
import json

# Number of training samples
NUM_SAMPLES = 100000

# Quite dangerous habit, globals are evil, but this is a proof-of-concept.
swaps = []

def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    swaps.append((pivot, begin))
    return pivot



def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)



def generate_samples():
    """
    The samples are composed of:
      1. a list of unordered numbers
      2. a list tuples representing the swaps that we should do to
      sort the original list.
    
    Thus, we have a tuple of 2 things: the unsorted lisr and the swaps.
    """

    samples = []
    global swaps

    for i in range(0, NUM_SAMPLES):
        # List of ten numbers should suffice for the beginning
        sample = random.sample(range(255), 10) 
        quicksort(sample)
        samples.append((sample, swaps))
        swaps = []
    
    return samples

if __name__ == "__main__":
    samples = generate_samples()

    # This should be the initial training data
    with open("training-data-ntm.json", "w") as f:
        f.write(json.dumps(samples))
