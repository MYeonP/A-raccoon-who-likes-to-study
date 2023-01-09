import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

#1. 데이터
datasets = fetch_california_housing()
x = datasets.data
y = datasets.target

print(x.shape, y.shape)     #(506, 13) (506,)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, random_state=333, test_size=0.2)

#2. 모델구성
model = Sequential()
# model.add(Dense(5, input_dim=13))       # 다차원일 경우 input_shape를 쓴다
model.add(Dense(5, input_shape=(8,)))    # (ex: (100,10,3) -> input_shape=(10, 3) / 행 무시)
model.add(Dense(4))
model.add(Dense(3))
model.add(Dense(2))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')

from tensorflow.keras.callbacks import EarlyStopping
EarlyStopping = EarlyStopping(monitor='val_loss', mode='min',
                patience=10, restore_best_weights=True,
                verbose=1)
# loss, vai_ioss : mode='min'(최소) / accuracy : mode='max'(최대)

hist = model.fit(x_train, y_train, epochs=300, batch_size=32,
          validation_split=0.2, callbacks=[EarlyStopping], verbose=1)  # True = 1 / False = 0

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)


print("=====================================")
print(hist)     #<keras.callbacks.History object at 0x00000203493BAAC0>
print("=====================================")
print(hist.history)     # loss와 val_loss의 변화값을 리스트 형태로 보여줌
print("=====================================")
print(hist.history['loss'])
print("=====================================")
print(hist.history['val_loss'])

import matplotlib.pyplot as plt

plt.figure(figsize=(9,6))
plt.plot(hist.history['loss'], c='red', 
         marker='.', label = 'loss')
plt.plot(hist.history['val_loss'], c='blue', 
         marker='.', label = 'val_loss')
plt.grid()
plt.xlabel('epochs')
plt.ylabel('loss')
plt.title('california loss')
plt.legend()        # 그래프 없는 곳에 라벨 이름 표시
# plt.legend(loc='upper right')        # 위 쪽의 오른쪽에 표시
# plt.legend(loc='upper left')        # 위 쪽의 왼쪽에 표시
plt.show()

"""
1. val_loss : 0.9494094252586365

"""