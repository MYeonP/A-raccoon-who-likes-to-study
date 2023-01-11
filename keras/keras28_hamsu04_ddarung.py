import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential, Model 
from tensorflow.keras.layers import Dense, Input  # (Model, Input : 함수형)
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler


#1. 데이터
path = './_data/ddarung/'
train_csv = pd.read_csv(path + 'train.csv', index_col=0)
# train_csv = pd.read_csv('./_data/ddarung/train.csv', index_col=0)
test_csv = pd.read_csv(path + 'test.csv', index_col=0)
submission = pd.read_csv(path + 'submission.csv', index_col=0)

print(train_csv)
print(train_csv.shape)  #(1459, 10)
print(submission.shape) #(715, 1)

print(train_csv.columns)
# Index(['hour', 'hour_bef_temperature', 'hour_bef_precipitation',
#       'hour_bef_windspeed', 'hour_bef_humidity', 'hour_bef_visibility',
#       'hour_bef_ozone', 'hour_bef_pm10', 'hour_bef_pm2.5', 'count'],
#        dtype='object')

print(train_csv.info())
print(test_csv.info())
print(train_csv.describe())

##### 결측치 처리 1. 제거 #####
print(train_csv.isnull().sum())
train_csv = train_csv.dropna()  #null, nan 등의 결측치 삭제 함수
print(train_csv.isnull().sum())
print(train_csv.shape)

x = train_csv.drop(['count'], axis=1)    #test에는 count가 없어서 맞추기 위해 삭제
print(x)        #[1459 rows x 9 columns]

y = train_csv['count']
print(y)        
print(y.shape)  #(1459,)


x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.8, shuffle=True, random_state=1234)

# scaler = MinMaxScaler()
scaler = StandardScaler()
scaler.fit(x_train)
# x_train = scaler.fit_transform(x_train)
# x_tset = scaler.transform(x_test)
x_train = scaler.transform(x_train)
x_tset = scaler.transform(x_test)
test_csv = scaler.transform(test_csv)

print(x_train.shape, x_test.shape)  #(1021, 9) (438, 9)
print(y_train.shape, y_test.shape)  #(1021,) (438,)

#2. 모델구성
# model = Sequential()
# model.add(Dense(1, input_dim=9, activation = 'relu'))
# model.add(Dense(10, activation ='relu'))
# model.add(Dense(10, activation ='relu'))
# model.add(Dense(10, activation ='relu'))
# model.add(Dense(10, activation ='relu'))
# model.add(Dense(5, activation ='relu'))
# model.add(Dense(5, activation ='relu'))
# model.add(Dense(5, activation ='relu'))
# model.add(Dense(1, activation = 'linear'))


#2. 모델구성(함수형)
input1 = Input(shape=(9,))
dense1 = Dense(50, activation = 'relu')(input1)
dense2 = Dense(40, activation = 'relu')(dense1)
dense3 = Dense(30, activation = 'relu')(dense2)
dense4 = Dense(20, activation = 'relu')(dense3)
output1 = Dense(1, activation = 'linear')(dense4)
model = Model(inputs=input1, outputs=output1)
model.summary()


#3. 컴파일, 훈련
import time
model.compile(loss='mse', optimizer='adam') 
start = time.time()
model.fit(x_train, y_train, epochs=1500, batch_size=32)
end = time.time()

#4.평가, 예측 
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)
# print(y_predict)


def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
rmse = RMSE(y_test, y_predict)
print("RMSE : ", RMSE(y_test, y_predict))


print("걸린시간 : ", end - start)

#5.제출
y_submit = model.predict(test_csv)
# print(y_submit)
# print(y_submit.shape) #(715, 1)


# .to_csv()를 사용해서
# submission_0105.csv를 완성하시오!

# print(submission)
submission['count'] = y_submit
# print(submission)

submission.to_csv(path + 'submission_01112003.csv')


"""
1. MinMaxScaler
loss :  652106.5
RMSE :  807.5311539481501
걸린시간 :  26.26568841934204

2. StandardScaler
loss :  247.64735412597656
RMSE :  263.2988706053793
걸린시간 :  26.459192752838135

"""
