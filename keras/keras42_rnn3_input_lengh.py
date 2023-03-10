import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN

#1. 데이터
dataset = np.array([1,2,3,4,5,6,7,8,9,10])  # (10, )
# y = ???

x = np.array([[1,2,3],
              [2,3,4], 
              [3,4,5], 
              [4,5,6], 
              [5,6,7],
              [6,7,8], 
              [7,8,9]])
y = np.array([4, 5, 6, 7, 8, 9, 10])

print(x.shape, y.shape) # (7, 3), (7, )

x = x.reshape(7, 3, 1)      # -> [[[1],[2],[3]], 
                            #    [[2],[3],[4]], ...]
print(x.shape)              # (7, 3, 1) 


#2. 모델구성
model = Sequential()
# model.add(SimpleRNN(units = 64, input_shape=(3, 1)))
#                     # (N , 3, 1) -> ([batch, timesteps, feature])
model.add(SimpleRNN(units = 64, input_length=3, input_dim=1))
# model.add(SimpleRNN(units = 64, input_dim=1, input_length=3))   # 가독성 떨어짐

model.add(Dense(16, activation='relu'))
model.add(Dense(1))

model.summary()
# 64 * (64 + 1 + 1) = 4224
# units * ( feature + bias + units ) = parms







