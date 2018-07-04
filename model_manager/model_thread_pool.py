import threading
from asyncio import Queue, sleep


class ModelThreadPool:

    def __init__(self):
        self.bs_in_queue = Queue()
        self.bs_out_queue = Queue()

        thread = threading.Thread(target=self.bubble_sorter, args=())
        thread.daemon = True
        thread.start()

        # Repeat the process for the rest of the threads

    def input_converter(self):
        pass


    def bubble_sorter(self):
        fn = lambda x: 1

        while True:
            if self.bs_queue.empty(): continue
            num_wires = self.bs_queue.get()
            self.bs_out_queue.put(fn(num_wires))


    def query_bubble_sorter(self, num_wires):
        self.bs_in_queue.put(num_wires)
        sleep(2)
        return self.bs_out_queue.get()