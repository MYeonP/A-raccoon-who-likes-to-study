
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Dense, Input  # (Model, Input : 함수형)
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler

path = './_save/'
# path = '../_save/'
# path = 'c:/study/_save/'


#1. 데이터
datasets = load_boston()
x = datasets.data
y = datasets['target'] 

x_train, x_test, y_train, y_test = train_test_split(x, y,
    shuffle=True, random_state=100000, test_size=0.2)

# scaler = StandardScaler()
# scaler.fit(x_train)
# x_train = scaler.transform(x_train)
# x_tset = scaler.transform(x_test)

# print(x)
# print(type(x))  # <class 'numpy.ndarray'>



#2. 모델구성(함수형)
input1 = Input(shape=(13,))
dense1 = Dense(50, activation = 'relu')(input1)
dense2 = Dense(40, activation = 'relu')(dense1)
dense3 = Dense(30, activation = 'relu')(dense2)
dense4 = Dense(20, activation = 'linear')(dense3)
output1 = Dense(1, activation = 'linear')(dense4)
model = Model(inputs=input1, outputs=output1)
model.summary()
# Total params: 4,611

# model.save(path + 'keras29_1_save_model.h5')
# model.save('./_save/keras29_1_save_model.h5')

#3. 컴파일, 훈련

model.compile(loss='mse', optimizer = 'adam', metrics = ['mae'])

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

es = EarlyStopping(monitor='val_loss', mode='min',
                              patience=20, restore_best_weights=False,
                              verbose=1)       # loss = mode ='min' / accuracy = mode ='auto'  //restore_best_weights의 defalut값은 False

mcp = ModelCheckpoint(monitor='val_loss', mode='auto', verbose=1, 
                      save_best_only=True, filepath=path + 'MCP/keras30_ModelCheckPoint3.hdf5')

model.fit(x_train, y_train, epochs=5000, batch_size=8,     
        validation_split=0.2, callbacks=[es, mcp], #   EarlyStopping 치명적 단점 == 끊은시점에 weight로 저장된다.
        verbose=1)        #   verbose = 0 일때 속도가 더 빠르다. // verbose = 2 간략하게 보임(progress bar X) // verbose >=3 훈련 횟수만 보임

model.save(path + "keras30_ModelCheckPoint3_save_model.h5")

# model = load_model(path + 'MCP/keras30_ModelCheckPoint1.hdf5')


#4. 평가, 예측
print("========================= 1. 기본 출력 =========================")

mse, mae = model.evaluate(x_test, y_test)
print('mse : ', mse)

y_predict = model.predict(x_test)
r2 = r2_score(y_test, y_predict)
print("R2 스코어 : ", r2)


print("========================= 2. load_model 츨력 =========================")
model2 = load_model(path + 'keras30_ModelCheckPoint3_save_model.h5')
mse, mae = model2.evaluate(x_test, y_test)
print('mse : ', mse)


y_predict = model2.predict(x_test)
r2 = r2_score(y_test, y_predict)
print("R2 스코어 : ", r2)


print("========================= 3. ModelCheckPoint 츨력 =========================")
model3 = load_model(path + 'MCP/keras30_ModelCheckPoint3.hdf5')
mse, mae = model3.evaluate(x_test, y_test)
print('mse : ', mse)


y_predict = model3.predict(x_test)
r2 = r2_score(y_test, y_predict)
print("R2 스코어 : ", r2)
# R2 :  -0.5498986998888116

#MCP 저장 : R-18.899792109086487

"""

MinMaxScaler
loss :  6758.6201171875
RMSE :  7244.290064453451
R2 :  -715627.4085768127

StandardScaler
loss :  2.379150629043579
RMSE :  3.740777006497933
R2 :  0.8091819075834242

"""
