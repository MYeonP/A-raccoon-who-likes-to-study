import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM

# 1. 데이터
x = np.array([[1,2,3], [2,3,4], [3,4,5],
              [4,5,6], [5,6,7], [6,7,8],
              [7,8,9], [8,9,10], [9,10,11],
              [10,11,12],[20,30,40],
              [30,40,50],[40,50,60]])
y = np.array([4,5,6,7,8,9,10,11,12,13,50,60,70])
x_predict = np.array([50,60,70])

print(x.shape, y.shape) # (13, 3) (13,)

x = x.reshape(13, 3, 1)     # -> [[[1],[2],[3]], 
                            #    [[2],[3],[4]], ...]
print(x.shape)              # (13, 3, 1) 

#2. 모델구성
model = Sequential()        # (N , 3, 1)
# model.add(SimpleRNN(units = 10, input_shape=(3, 1)))
#                     # (N , 3, 1) -> ([batch, timesteps, feature])
model.add(LSTM(units = 64, input_shape=(3, 1), 
               return_sequences=True))     # (N , 3, 64)
model.add(LSTM(32))
model.add(Dense(50, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

model.summary()


"""
#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=200)

#4. 평가, 예측 
loss = model.evaluate(x, y)
print('loss : ', loss)

y_pred = np.array([50,60,70]).reshape(1, 3, 1)
result = model.predict(y_pred)
print('[50,60,70]의 결과 : ', result)


# loss :  0.007041578181087971
# [50, 60, 70]의 결과 :  [[78.691086]]

# loss :  0.0037496215663850307
# [50,60,70]의 결과 :  [[78.863716]]

"""