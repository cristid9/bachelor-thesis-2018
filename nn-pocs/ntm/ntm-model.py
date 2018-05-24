import theano
import theano.tensor as T
import numpy as np

from lasagne.layers import InputLayer, DenseLayer, ReshapeLayer
import lasagne.layers
import lasagne.nonlinearities
import lasagne.updates
import lasagne.objectives
import lasagne.init

from ntm.layers import NTMLayer
from ntm.memory import Memory
from ntm.controllers import GRUController
from ntm.heads import WriteHead, ReadHead
from ntm.updates import graves_rmsprop

from utils.generators import SortTask
from utils.visualization import Dashboard


def model(input_var, batch_size=1, size=8, num_units=100, memory_shape=(1024, 160)):

    l_input = InputLayer((batch_size, None, size + 1), input_var=input_var)
    _, seqlen, _ = l_input.input_var.shape

    memory = Memory(memory_shape, name='memory', memory_init=lasagne.init.Constant(1e-6), learn_init=False)
    controller = GRUController(l_input, memory_shape=memory_shape,
        num_units=num_units, num_reads=1,
        nonlinearity=lasagne.nonlinearities.rectify,
        name='controller')
    heads = [
        WriteHead(controller, num_shifts=3, memory_shape=memory_shape, name='write', learn_init=False,
            nonlinearity_key=lasagne.nonlinearities.rectify,
            nonlinearity_add=lasagne.nonlinearities.rectify),
        ReadHead(controller, num_shifts=3, memory_shape=memory_shape, name='read', learn_init=False,
            nonlinearity_key=lasagne.nonlinearities.rectify)
    ]
    l_ntm = NTMLayer(l_input, memory=memory, controller=controller, heads=heads)

    l_output_reshape = ReshapeLayer(l_ntm, (-1, num_units))
    l_output_dense = DenseLayer(l_output_reshape, num_units=size + 1, nonlinearity=lasagne.nonlinearities.sigmoid, \
        name='dense')
    l_output = ReshapeLayer(l_output_dense, (batch_size, seqlen, size + 1))

    return l_output, l_ntm


if __name__ == '__main__':
    input_var = T.tensor3('input')
    target_var = T.tensor3('target')


    generator = SortTask(batch_size=1, max_iter=25, size=8, max_length=5, end_marker=True)
    l_output, l_ntm = model(input_var, batch_size=generator.batch_size, \
    size=generator.size, num_units=100, memory_shape=(1024, 160))

    pred_var = T.clip(lasagne.layers.get_output(l_output), 1e-6, 1. - 1e-6)
    loss = T.mean(lasagne.objectives.binary_crossentropy(pred_var, target_var))

    params = lasagne.layers.get_all_params(l_output, trainable=True)
    updates = graves_rmsprop(loss, params, learning_rate=1e-2)

    train_fn = theano.function([input_var, target_var], loss, updates=updates)
    ntm_fn = theano.function([input_var], pred_var)
    ntm_layer_fn = theano.function([input_var], lasagne.layers.get_output(l_ntm, get_details=True))

    try:
        scores, all_scores = [], []
        for i, (example_input, example_output) in generator:
            score = train_fn(example_input, example_output)
            print("=" * 100)
            print(i)
            print(score)
            print("=" * 100)
            scores.append(score)
            all_scores.append(score)
            if i % 500 == 0:
                mean_scores = np.mean(scores)
                print ('Batch #%d: %.6f' % (i, mean_scores))
                scores = []
    except KeyboardInterrupt:
        pass

    print("Debug point")

    markers = [
            {
            'location': (lambda params: params['length']),
            'style': {'color': 'red'}
        }
    ]

    dashboard = Dashboard(generator=generator, ntm_fn=ntm_fn, ntm_layer_fn=ntm_layer_fn, \
        memory_shape=(128, 20), markers=markers, cmap='bone')

    params = generator.sample_params()
    dashboard.sample(**params)
