import numpy as np
import tensorflow as tf
from keras.models import Model
from keras.layers import Input, Activation, Dense, Conv2D, MaxPooling2D, ZeroPadding2D, Flatten
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical
from keras.callbacks import TensorBoard
from keras.datasets import fashion_mnist

(train_x, train_y), (test_x, test_y) = fashion_mnist.load_data()

train_x = train_x.astype('float32') / 255.
test_x = test_x.astype('float32') / 255.

train_x = np.reshape(train_x, (len(train_x), 28, 28, 1))
test_x = np.reshape(test_x, (len(test_x), 28, 28, 1))

train_y = to_categorical(train_y)
test_y = to_categorical(test_y)

#Feature Extraction Layer
inputs = Input(shape=(28, 28, 1))
conv_layer = ZeroPadding2D(padding=(2,2))(inputs)
conv_layer = Conv2D(16, (5, 5), strides=(1,1), activation='relu')(conv_layer)
conv_layer = MaxPooling2D((2, 2))(conv_layer)
conv_layer = Conv2D(32, (3, 3), strides=(1,1), activation='relu')(conv_layer)
conv_layer = MaxPooling2D((2, 2))(conv_layer)
conv_layer = Conv2D(64, (3, 3), strides=(1,1), activation='relu')(conv_layer)

#Flatten feature map to Vector with 576 elements.
flatten = Flatten()(conv_layer)

#Fully Connected Layer
fc_layer = Dense(256, activation='relu')(flatten)
fc_layer = Dense(64, activation='relu')(fc_layer)
outputs = Dense(10, activation='softmax')(fc_layer)

model = Model(inputs=inputs, outputs=outputs)

#Adam Optimizer and Cross Entropy Loss
adam = Adam(lr=0.0001)
model.compile(optimizer=adam, loss='categorical_crossentropy', matrics=['accuracy'])

#Print Model Summary
print(model.summary())

#Use Tensorboard
callbacks = TensorBoard(log_dir='./Graph')

#Train for 100 Epochs and use Tensorboard Callback
model.fit(train_x, train_y, batch_size=256, epochs=100, verbose=1, validation_data=(test_x, test_y), callbacks=[callbacks])

#Save Weights
model.save_weights('weights.h5')
