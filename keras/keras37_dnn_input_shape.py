# 36_1 복붙

import numpy as np
from tensorflow.keras.datasets import mnist

#1. 데이터
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(x_train.shape, y_train.shape) #   (60000, 28, 28) (60000,)
# print(x_test.shape, y_test.shape) #   (10000, 28, 28) (10000,)

x_train = x_train/255.
x_test = x_test/255.

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# print(np.unique(y_train, return_counts = True))     
#(array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8), array([5923, 6742, 5958, 6131, 5842, 5421, 5918, 6265, 5851, 5949],dtype=int64))

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D, Dropout

#2. 모델
model = Sequential()                
model.add(Dense(128, activation = 'relu', input_shape=(28, 28)))             
model.add(Dropout(0.3))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(32, activation='linear'))
model.add(Flatten())            # 중간에 Flatten 사용하여 펼친다. // 2차원 이상도 모두 가능
model.add(Dense(10, activation = 'softmax'))                

model.summary()

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
                      filepath = filepath + 'k37_' + date +'_'+ filename)

model.fit(x_train, y_train, epochs=3000, 
            verbose= 1, 
            batch_size=32,
            validation_split=0.2,
            callbacks=[es,mcp])

#4. 평가, 예측
result = model.evaluate(x_test, y_test)
print('loss : ', result[0])
print('acc : ', result[1])

# loss :  0.10004928708076477
# acc :  0.9708999991416931

#   padding 적용시...
#   acc :  0.9608949349914169

#   MaxPooling2D 적용시...
#   acc :  0.9797999858856201

#   dnn...
#   acc :  0.9717000126838684