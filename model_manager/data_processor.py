from .model_thread_pool import ModelThreadPool
from .model_predef import MODEL_TYPES

class DataProcessor:
    def __init__(self):
        self.pool = ModelThreadPool()

    def dispatch_request(self, model_type, num_wires):
        if model_type not in MODEL_TYPES:
            print("[WARNING] Attempt to run unrecognized model")
        swaps = self.pool.get_result_for(model_type, num_wires)

        # approximate swaps probabilities