# Import Numpy, keras and MNIST data
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

from PIL import Image
import os
import cv2
import math
from scipy import ndimage

# Retrieve the training and test data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print('X_train shape:', X_train.shape)
print('X_test shape: ', X_test.shape)
print('y_train shape:',y_train.shape)
print('y_test shape: ', y_test.shape)

# Visualizing the data
import matplotlib.pyplot as plt
#%matplotlib inline

# Function for displaying a training image by it's index in the MNIST set
'''def display_digit(index):
    label = y_train[index].argmax(axis=0)
    image = X_train[index]
    plt.title('Training data, index: %d,  Label: %d' % (index, label))
    plt.imshow(image, cmap='gray_r')
    plt.show()
    
# Display the first (index 0) training image
display_digit(0)'''

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
print("Training matrix shape", X_train.shape)
print("Testing matrix shape", X_test.shape)

#One Hot encoding of labels.
from keras.utils.np_utils import to_categorical
print(y_train.shape)
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
print(y_train.shape)

# Define the neural network
def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation('relu')) # An "activation" is just a non-linear function applied to the output
                              # of the layer above. Here, with a "rectified linear unit",
                              # we clamp all values below 0 to 0.
                           
    model.add(Dropout(0.2))   # Dropout helps protect the model from memorizing or "overfitting" the training data
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10))
    model.add(Activation('softmax')) # This special "softmax" activation among other things,
                                 # ensures the output is a valid probaility distribution, that is
                                 # that its values are all non-negative and sum to 1.
    return model

# Build the model
model = build_model()

model.compile(optimizer='rmsprop',
          loss='categorical_crossentropy',
          metrics=['accuracy'])

# Training
model.fit(X_train, y_train, batch_size=128, epochs=4, verbose=1,validation_data=(X_test, y_test))

# Compare the labels that our model predicts with the actual labels

score = model.evaluate(X_test, y_test, batch_size=32, verbose=1,sample_weight=None)
# Print out the result
print('Test score:', score[0])
print('Test accuracy:', score[1])

def getBestShift(img):
    cy,cx = ndimage.center_of_mass(img)

    rows,cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)

    return shiftx,shifty

def shift(img,sx,sy):
    rows,cols = img.shape
    M = np.float32([[1,0,sx],[0,1,sy]])
    shifted = cv2.warpAffine(img,M,(cols,rows))
    return shifted

numbers = [0,1,2,3,4,5,6,7,8,9]
pred = []
for no in numbers:
    print('Validate', no)
    gray = cv2.imread('coba_' + str(no) + '.png', 0)
    # rescale it
    gray = cv2.resize(255-gray, (2048, 2048))
    # better black and white version
    (thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    while np.sum(gray[0]) == 0:
        gray = gray[1:]
        
    while np.sum(gray[:,0]) == 0:
        gray = np.delete(gray, 0, 1)
        
    while np.sum(gray[-1]) == 0:
        gray = gray[:-1]
        
    while np.sum(gray[:,-1]) == 0:
        gray = np.delete(gray,-1,1)
        
    rows,cols = gray.shape

    if rows > cols:
        factor = 20.0/rows
        rows = 20
        cols = int(round(cols*factor))
        # first cols then rows
        gray = cv2.resize(gray, (cols,rows))
    else:
        factor = 20.0/cols
        cols = 20
        rows = int(round(rows*factor))
        # first cols then rows
        gray = cv2.resize(gray, (cols, rows))
        
    colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
    rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
    gray = np.lib.pad(gray, (rowsPadding,colsPadding), 'constant')

    shiftx, shifty = getBestShift(gray)
    shifted = shift(gray, shiftx, shifty)
    gray = shifted

    # save the processed image
    cv2.imwrite('image_' + str(no) + '.png', gray)

    img = Image.open('image_'+ str(no) +'.png').convert('L')
    img = np.resize(img, (28,28,1))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,784)

    #y_pred = model.predict_step(im2arr)
    y_pred = np.argmax(model.predict(im2arr), axis=-1)
    pred.append(y_pred)
pred = [int(i) for i in pred]
print('\n------')
print('Expected')
print('------')
for i in range(len(numbers)):
    print(numbers[i], end= ' ')
print('\nPredicted')
print('------')
acc = 0
count = 0
for i in range(len(pred)):
    if pred[i] == numbers[i]:
        count += 1
acc = (count/len(numbers))*100
for i in range(len(pred)):
    print(pred[i], end=' ')
print('\nAccuracy: %.2f' %acc + '%')