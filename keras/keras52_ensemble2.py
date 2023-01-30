import numpy as np
x1_datasets = np.array([range(100), range(301, 401)]).transpose()
print(x1_datasets.shape)    # (100, 2) / 위에서 바로 transpose(치환)해 줌
# 삼성전자 시가, 고가

x2_datasets = np.array([range(101, 201), range(411, 511), range(150, 250)]).T
print(x2_datasets.shape)    # (100, 3) / 위에서 바로 T(치환)해 줌
# 아모레 시가, 고가, 종가

x3_datasets = np.array([range(100, 200), range(1301, 1401)]).T

print(x3_datasets.shape)    # (100, 2)


y = np.array(range(2001, 2101)) #(100, )
# 삼성전자의 하루 뒤 종가 예측


from sklearn.model_selection import train_test_split
x1_train, x1_test, x2_train, x2_test, x3_train, x3_test, y_train, y_test = train_test_split(
    x1_datasets, x2_datasets, x3_datasets, y, train_size=0.7, random_state=1234
)

print(x1_train.shape, x2_train.shape, x3_train.shape, y_train.shape)
#(70, 2) (70, 3) (70, 2) (70,)
print(x1_test.shape, x2_test.shape, x3_test.shape, y_test.shape)
#(30, 2) (30, 3) (30, 2) (30,)

# 2. 모델구성
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input

# 2-1. 모델 1
input1 = Input(shape=(2, ))
dense1 = Dense(11, activation='relu', name='ds11')(input1)
dense2 = Dense(12, activation='relu', name='ds12')(dense1)
dense3 = Dense(13, activation='relu', name='ds13')(dense2)
output1 = Dense(14, activation='relu', name='ds14')(dense3)

# 2-2. 모델 2
input2 = Input(shape=(3, ))
dense21 = Dense(21, activation='linear', name='ds21')(input2)
dense22 = Dense(22, activation='linear', name='ds22')(dense21)
output2 = Dense(23, activation='linear', name='ds23')(dense22)

# 2-3. 모델 3
input3 = Input(shape=(2, ))
dense31 = Dense(31, activation='linear', name='ds31')(input3)
dense32 = Dense(32, activation='linear', name='ds32')(dense31)
output3 = Dense(33, activation='linear', name='ds33')(dense32)

# 2-4. 모델 병합
from tensorflow.keras.layers import concatenate     # concatenate : 사슬처럼 엮다 / 붙였다, 연결했다
merge1 = concatenate([output1, output2, output3], name='mg1')
merge2 = Dense(12, activation='relu', name='mg2')(merge1)
merge3 = Dense(13, name='mg3')(merge2)
last_output = Dense(1, name='last')(merge3)

model = Model(inputs=[input1, input2, input3], outputs=last_output)

model.summary()

# 3.  컴파일, 훈련
model.compile(loss = 'mse', optimizer='adam')
model.fit([x1_train, x2_train, x3_train], y_train, epochs=300, batch_size=32)

# 4.평가
loss = model.evaluate([x1_test, x2_test, x3_test], y_test)
print('loss : ', loss)

"""

1. loss :  587.1437377929688
2. loss :  0.002291531767696142

"""