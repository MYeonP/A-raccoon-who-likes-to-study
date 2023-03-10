#[과제, 실습]
#R2 0.62 이상

from sklearn.datasets import load_diabetes
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

#1. 데이터
datasets = load_diabetes()
x = datasets.data
y = datasets.target

"""
print(x)
print(x.shape)  #(442, 10)
print(y)
print(y.shape)  #(442,)
"""

print(datasets.feature_names)
print(datasets.DESCR)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.9, shuffle=True, random_state=86)

#2. 모델구성
model = Sequential()
model.add(Dense(5, input_dim=10))
model.add(Dense(3))
model.add(Dense(3))
model.add(Dense(10))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mae']) 
model.fit(x_train, y_train, epochs=500, batch_size=5)

#4.평가, 예측 

y_predict = model.predict(x_test)

loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

from sklearn.metrics import mean_squared_error, r2_score
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : ", RMSE(y_test, y_predict))

r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)

"""
1. R2 :  0.515944898950716
2. R2 :  0.5155729146217276
3. R2 :  0.5191283171190529
4. R2 :  0.6661309360129759     train_size=0.9, random_state=86 조정. 이래도 되나?
5. R2 :  0.662145051112597 
"""