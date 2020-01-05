from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv3D, MaxPooling3D, ZeroPadding3D
from keras.optimizers import SGD
from keras.layers import Input
from keras.models import Model





def get_model():
    """ Return the Keras model of the network
    """
    model = Sequential()
    inputShape=(16, 224, 224,3)  #seq_length, width, height, channels
    numberOfActivities=101
    inputs = Input(inputShape)



        # 1st layer group
    conv1_3d=Conv3D(64, (3, 3, 3), activation='relu', padding='same', name='conv1',strides=(1, 1, 1))
    pool1_3d=MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2), padding='valid', name='pool1')
    
    # 2nd layer group
    conv2_3d=Conv3D(128, (3, 3, 3), activation='relu', padding='same', name='conv2',strides=(1, 1, 1))
    pool2_3d=MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding='valid', name='pool2')
    
    # 3rd layer group
    conv3a_3d=Conv3D(256, (3, 3, 3), activation='relu', padding='same', name='conv3a',strides=(1, 1, 1))
    conv3b_3d=Conv3D(256, (3, 3, 3), activation='relu', padding='same', name='conv3b',strides=(1, 1, 1))
    pool3_3d=MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding='valid', name='pool3')

    # 4th layer group
    conv4a_3d=Conv3D(512, (3, 3, 3), activation='relu', padding='same', name='conv4a',strides=(1, 1, 1))
    conv4b_3d=Conv3D(512, (3, 3, 3), activation='relu', padding='same', name='conv4b',strides=(1, 1, 1))
    pool4_3d=MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding='valid', name='pool4')




    # 5th layer group
    conv5a_3d=Conv3D(512, (3, 3, 3), activation='relu', padding='same', name='conv5a',strides=(1, 1, 1))
    conv5b_3d=Conv3D(512, (3, 3, 3), activation='relu', padding='same', name='conv5b',strides=(1, 1, 1))
    pool5_3d=MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding='valid', name='pool5')


    dense1_3d=Dense(4096, activation='relu', name='fc6')
    model.add(Dropout(.5))
    dense2_3d=Dense(4096, activation='relu', name='fc7')
    model.add(Dropout(.5))
    dense3_3d=Dense(numberOfActivities, activation='softmax', name='fc8')


    x=conv1_3d(inputs)
    x=pool1_3d(x)
    x=conv2_3d(x)
    x=pool2_3d(x)
    x=conv3a_3d(x)
    x=conv3b_3d(x)
    x=pool3_3d(x)
    x=conv4a_3d(x)
    x=conv4b_3d(x)
    x=pool4_3d(x)
    x=conv5a_3d(x)
    x=conv5b_3d(x)
    x=pool5_3d(x)
    x = Flatten()(x)
    x=dense1_3d(x)
    x = Dropout(0.5)(x)
    x=dense2_3d(x)
    x = Dropout(0.5)(x)
    x=dense3_3d(x)



    model = Model(inputs, x)

    return model


model = get_model()
model.summary()
