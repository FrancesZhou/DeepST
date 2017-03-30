from keras import backend as K
from keras.engine.topology import Layer
# from keras.layers import Dense
import numpy as np


class iLayer(Layer):
    def __init__(self, **kwargs):
        # self.output_dim = output_dim
        super(iLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        #initial_weight_value = np.random.random(input_shape[1:])
	print(input_shape)
        initial_weight_value = np.random.random(input_shape[1:3])
        self.W = K.variable(initial_weight_value)
        self.trainable_weights = [self.W]

    def call(self, x, mask=None):
        #return x * self.W
        return x*K.tile(K.expand_dims(self.W, axis=-1),[1,1,x.get_shape().as_list()[-1]])

    def get_output_shape_for(self, input_shape):
        return input_shape
