import random
import json
import copy
import pprint

# Number of training samples
NUM_SAMPLES = 100000



class BubbleSortSamplesGenerator:
    def __init__(self):
        self.swaps = []

    def bubble_sort(self, bad_list):
        length = len(bad_list) - 1
        sorted = False

        while not sorted:
            sorted = True
            for i in range(length):
                if bad_list[i] > bad_list[i+1]:
                    sorted = False
                    bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
                    self.swaps.append((i, i+1))



    def generate_samples(self, num_samples=NUM_SAMPLES):
        samples = []
        
        for i in range(0, NUM_SAMPLES):
            sample = random.sample(range(255), 10)
            save_sample = copy.deepcopy(sample)
            self.bubble_sort(sample)
            samples.append((save_sample, self.swaps))
            self.swaps = []
        
        return samples



class QuickSortSamplesGenerator:

    def __init__(self):
        self.swaps = []


    def partition(self, array, begin, end):
        pivot = begin
        
        for i in xrange(begin+1, end+1):
            if array[i] <= array[begin]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
                self.swaps.append((pivot, i))
        array[pivot], array[begin] = array[begin], array[pivot]
        self.swaps.append((pivot, begin))    
        return pivot



    def quicksort(self, array, begin=0, end=None):
        if end is None:
            end = len(array) - 1
        def _quicksort(array, begin, end):
            if begin >= end:
                return
            pivot = self.partition(array, begin, end)
            _quicksort(array, begin, pivot-1)
            _quicksort(array, pivot+1, end)
        return _quicksort(array, begin, end)



    def generate_samples(self, num_samples=NUM_SAMPLES):
        """
        The samples are composed of:
        1. a list of unordered numbers
        2. a list tuples representing the swaps that we should do to
        sort the original list.
        
        Thus, we have a tuple of 2 things: the unsorted list and the swaps.
        """
        samples = []
        
        for i in range(0, NUM_SAMPLES):
            # List of ten numbers should suffice for the beginning
            sample = random.sample(range(255), 10)
            save_sample = copy.deepcopy(sample)
            self.quicksort(sample)
            samples.append((save_sample, self.swaps))
            self.swaps = []
        
        return samples

if __name__ == "__main__":
    samples_quicksort = QuickSortSamplesGenerator().generate_samples()
    samples_bubble_sort = BubbleSortSamplesGenerator().generate_samples()
    
    # This should be the initial training data
    with open("training-quicksort-data-ntm.json", "w") as f:
        f.write(pprint.pformat(json.dumps(samples_quicksort)))

    with open("training-bubble-sort-data-ntm.json", "w") as f:
        f.write(pprint.pformat(json.dumps(samples_bubble_sort)))
