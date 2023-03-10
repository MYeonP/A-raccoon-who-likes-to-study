
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler

#1. 데이터
datasets = load_boston()
x = datasets.data
y = datasets['target']  #가격 데이터

scaler = MinMaxScaler()
scaler.fit(x)
x = scaler.transform(x)

print(x)
print(type(x))  # <class 'numpy.ndarray'>

print("최소값 : ", np.min(x))
print("최대값 : ",np.max(x))


# print(x)
# print(x.shape)  # (506, 13)
# print(y)
# print(y.shape)  # (506,)

# print(dataset.feature_names)
# # ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']
# print(dataset.DESCR)

x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.8, shuffle=True, random_state=42)
  
#2. 모델구성
model = Sequential()
model.add(Dense(26, input_shape=(13,), activation='relu'))     # input_shape
model.add(Dense(15, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(1, activation = 'linear'))

#3. 컴파일, 훈련

model.compile(loss='mae', optimizer = 'adam')
from tensorflow.keras.callbacks import EarlyStopping
earlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                              patience=30, restore_best_weights=True,
                              verbose=1)       # loss == mode ='min' / accuracy == mode ='auto'  //restore_best_weights의 defalut값은 False

hist = model.fit(x_train, y_train, epochs=3000, batch_size=1,     
                validation_split=0.2, callbacks=[earlyStopping], #   EarlyStopping 치명적 단점 == 끊은시점에 weight로 저장된다.
                verbose=1)        #   verbose = 0 일때 속도가 더 빠르다. // verbose = 2 간략하게 보임(progress bar X) // verbose >=3 훈련 횟수만 보임



#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)

def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

print("RMSE : ", RMSE(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)


"""
x_train, x_test, y_train, y_test = train_test_split(
    x,y, shuffle=True, random_state=333, test_size=0.2)
    
model.add(Dense(26, input_shape=(13,), activation='relu'))     # input_shape
model.add(Dense(15, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(1, activation = 'linear'))
hist = model.fit(x_train, y_train, epochs=3000, batch_size=1,     
                validation_split=0.2, callbacks=[earlyStopping], 
                verbose=1)
                
hist = model.fit(x_train, y_train, epochs=3000, batch_size=1,     
                validation_split=0.2, callbacks=[earlyStopping],
                verbose=1)
loss :  2.978041648864746
RMSE :  4.64257573132047
R2 :  0.7802433152410027

loss :  2.3680195808410645
RMSE :  4.105787142276368
R2 :  0.770126572894406
"""

