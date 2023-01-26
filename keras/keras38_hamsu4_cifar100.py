from tensorflow.keras.datasets import cifar10, cifar100
from tensorflow.keras import layers
import numpy as np
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D, Dropout, Input

#1. 데이터
(x_train, y_train), (x_test, y_test) = cifar100.load_data()
# print(x_train.shape, y_train.shape) #   (50000, 32, 32, 3) (50000, 1)
# print(x_test.shape, y_test.shape)   #   (10000, 32, 32, 3) (10000, 1)

# x_train = x_train.reshape(50000, 32*32*3)
# x_test = x_test.reshape(10000, 32*32*3)

# x_train = x_train/255.
# x_test = x_test/255.

# import matplotlib.pyplot as plt
# plt.imshow(x_train[10], 'gray')
# plt.show()

x_train = x_train/255.
x_test = x_test/255.

#2. 모델

inputs = Input(shape=(32, 32 ,3))
hidden1 = Dense(1024, activation='linear') (inputs)
hidden2 = Dense(256) (hidden1)
hidden3 = (Dropout(0.2)) (hidden2)
hidden4 = Dense(32) (hidden3)
hidden5 = Dense(16) (hidden4)
hidden6 = Flatten() (hidden5)
output = Dense(100, activation='softmax') (hidden6)
model = Model(inputs=inputs, outputs=output)

#3. 컴파일, 훈련
model.compile(loss = 'sparse_categorical_crossentropy', optimizer='adam',
              metrics = ['acc'])

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
es = EarlyStopping(monitor='val_loss', mode='min',patience=50, 
                  restore_best_weights=True,              
                   verbose=1)
import datetime                                             # 데이터 형식으로
date = datetime.datetime.now()
date = date.strftime("%m%d_%H%M")
filepath = './_save/MCP/'
filename = '{epoch:04d}-{val_loss:.4f}.hdf5'
mcp = ModelCheckpoint(monitor='val_loss', mode = 'auto', verbose = 1,
                      save_best_only=True,
                      filepath = filepath + 'k38_04_' + date +'_'+ filename)
model.fit(x_train, y_train, epochs=1000, 
            verbose= 1, 
            batch_size=250,
            validation_split=0.33,
            callbacks=[es,mcp])

#4. 평가, 예측
result = model.evaluate(x_test, y_test)
print('loss : ', result[0])
print('acc : ', result[1])

# acc :  0.2280000001192093