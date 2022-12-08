# Import Numpy, keras and MNIST data
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
from extra_keras_datasets import emnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint

from PIL import Image
import os
import cv2
import math
from scipy import ndimage
import pandas as pd

batch_size = 256
num_classes = 10
epochs = 7

'''Emnist_file_path = 'D:/G/UNPAD/Internship/Paper/emnist/'
All_train = Emnist_file_path + 'emnist-byclass-train.csv'
All_test = Emnist_file_path + 'emnist-byclass-test.csv'''
# Retrieve the training and test data
#(X_train, y_train), (X_test, y_test) = emnist.load_data(type='letters')
(X_train, y_train), (X_test, y_test) = mnist.load_data()
'''All_train_data = pd.read_csv(All_train)
All_test_data = pd.read_csv(All_test)

All_training_data = All_train_data.values
All_testing_data = All_test_data.values
#print(All_training_data)
#print(All_testing_data)

X_train = All_training_data[:, 1:].astype('float32')
y_train = All_training_data[:, 0:1]
X_test = All_testing_data[:, 1:].astype('float32')
y_test = All_testing_data[:, 0:1]'''

print('X_train shape:', X_train.shape)
print('X_test shape: ', X_test.shape)
print('y_train shape:',y_train.shape)
print('y_test shape: ', y_test.shape)

#%matplotlib inline

# Function for displaying a training image by it's index in the MNIST set
'''def display_digit(index):
    label = y_train[index].argmax(axis=0)
    image = X_train[index]
    plt.title('Training data, index: %d,  Label: %d' % (index, label))
    plt.imshow(image, cmap='gray_r')
    plt.show()
'''    
# Display the first (index 0) training image
#display_digit(17)

X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
'''
X_train = np.array(list(map(lambda x: x.reshape(28,28).transpose().flatten(), X_train)))
X_test = np.array(list(map(lambda x: x.reshape(28,28).transpose().flatten(), X_test)))'''
X_train /= 255
X_test /= 255
print("Training matrix shape", X_train.shape)
print("Testing matrix shape", X_test.shape)

#One Hot encoding of labels.
from keras.utils.np_utils import to_categorical
print(y_train.shape)
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)
print(y_train.shape)

# Define the neural network
def build_model():
    model = Sequential()
    model.add(Conv2D(32, (5, 5), input_shape=(28,28,1), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, (4, 4), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(num_classes, activation='softmax'))
    return model

# Build the model
model = build_model()

model.compile(optimizer='rmsprop',
          loss='categorical_crossentropy',
          metrics=['accuracy'])

# Training
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1,validation_data=(X_test, y_test))

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

categ = [4,1,7,9,0,5,6,2,8,3]   
categ = [str(i) for i in categ]  
pred = []
for cat in categ:
    print('Validate', cat)
    gray = cv2.imread('coba_' + cat + '.png', 0)
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
    cv2.imwrite('image_' + cat + '.png', gray)

    img = Image.open('image_'+ cat +'.png').convert('L')
    img = np.resize(img, (28,28,1))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)

    #y_pred = model.predict_step(im2arr)
    y_pred = np.argmax(model.predict(im2arr), axis=-1)
    pred.append(y_pred)
print(pred)
pred = [str(int(i)) for i in pred]
print('\n------')
print('Expected')
print('------')
for i in range(len(categ)):
    print(categ[i], end= ' ')
print('\nPredicted')
print('------')
acc = 0
count = 0
for i in range(len(pred)):
    if pred[i] == categ[i]:
        count += 1
acc = (count/len(categ))*100
for i in range(len(pred)):
    print(pred[i], end=' ')
print('\nAccuracy: %.2f' %acc + '%')