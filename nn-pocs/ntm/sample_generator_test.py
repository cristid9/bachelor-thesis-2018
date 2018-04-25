import unittest
import copy
from training_samples_generator import QuickSortSamplesGenerator
from training_samples_generator import BubbleSortSamplesGenerator

class TestSampleGeneration(unittest.TestCase):

    def assert_helper(self, samples):
         for sample in samples:
            sorted_version = sorted(sample[0])
            working_list = copy.deepcopy(sample[0])

            # apply the generated swaps to the list
            for i, j in sample[1]:
                working_list[i], working_list[j] = working_list[j], working_list[i]

            # %%todo%% add more suggestive error messages
            self.assertEquals(sorted_version, working_list)


    def test_quick_sort_samples(self):
        samples = QuickSortSamplesGenerator().generate_samples(10)
        self.assert_helper(samples)


    def test_merge_sort_samples(self):
        self.assertEquals(True, True)

    def test_shell_sort_samples(self):
        self.assertEquals(True, True)

    def test_bubble_sort_samples(self):
        samples = BubbleSortSamplesGenerator().generate_samples(10)
        self.assert_helper(samples)


if __name__ == '__main__':
    unittest.main()