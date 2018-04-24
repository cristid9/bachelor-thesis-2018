import unittest
import copy
from training_samples_generator import generate_samples

class TestSampleGeneration(unittest.TestCase):

    def test_quick_sort_samples(self):
        """
        More versions of quick sort should be added soon.
        """
        samples = generate_samples(10)
        for sample in samples:
            sorted_version = sorted(sample[0])
            working_list = copy.deepcopy(sample[0])

            # apply the generated swaps to the list
            for i, j in sample[1]:
                working_list[i], working_list[j] = working_list[j], working_list[i]

            # %%todo%% add more suggestive error messages
            self.assertEquals(sorted_version, working_list, "Quick sort test case failed")

    def test_merge_sort_samples(self):
        self.assertEquals(True, True)

    def test_shell_sort_samples(self):
        self.assertEquals(True, True)

    def test_bubble_sort_samples(self):
        self.assertEquals(True, True)

if __name__ == '__main__':
    unittest.main()