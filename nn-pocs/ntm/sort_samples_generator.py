class SortTask(Task):

    def __init__(self, size, max_length, min_length=1, max_iter=None, \
        batch_size=1, end_marker=False):
        super(SortTask, self).__init__(max_iter=max_iter, batch_size=batch_size)
        self.size = size
        self.min_length = min_length
        self.max_length = max_length
        self.end_marker = end_marker
        self.counter = 2


    def sample_params(self, length=None):
        if length is None:
            length = np.random.randint(self.min_length, self.max_length + 1)
        return {'length': length}


    def dummy_sorter(self, n):
        if n <= 1:
            return []

        ret_val = []
        for i in range(0, n - 1):
            ret_val.append((i, i + 1))
        ret_val += self.dummy_sorter(n - 1)
        return ret_val


    def convert_swaps_in_binary(self, num_wires, swaps):
        num_wires_binary = [float(i) for i in list("{0:>09b}".format(num_wires))]

        swaps_binary = []
        for swap in swaps:
            swap_0 = [float(i) for i in list("{0:>09b}".format(swap[0]))]
            swap_1 = [float(i) for i in list("{0:>09b}".format(swap[1]))]
            swaps_binary.append(swap_0)
            swaps_binary.append(swap_1)

        return num_wires_binary, swaps_binary


    def sample(self, length):
        input_sample, output_sample = self.convert_swaps_in_binary(self.counter,
                                                                   self.dummy_sorter(self.counter))

        multiply = len(output_sample)
        a = []
        for i in range(0, multiply): a.append(input_sample)
        input_sample = np.array([a])
        output_sample = np.array([output_sample])

        self.counter += 1

        return input_sample, output_sample


