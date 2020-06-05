# 170541302
# Hamit FIRAT
# 05.06.2020

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def sinif(havakalite):
    if havakalite <= 70:
        return 1
    elif havakalite >70:
        return 2

haftaici=[]
haftasonu=[] 

hava=pd.read_csv("rizeveri2.csv" )
gunler=hava.groupby("Tarih")
gunler=gunler.mean()

gunler=hava.sort_values(["Tarih"], ascending = True)
y=gunler[["PM10"]].iloc[::-1]
x= range(0,len(gunler))
plt.subplot(221),
plt.plot(x,y,"r"),
plt.ylabel("PM10"),
plt.title("Günlere göre ortalama PM10 değerleri")

y=gunler[["NO2"]].iloc[::-1]
x= range(0,len(gunler))
plt.subplot(222),
plt.plot(x,y,"b"),
plt.ylabel("NO2"),
plt.title("Günlere göre ortalama NO2 değerleri")

y=gunler[["SO2"]].iloc[::-1]
x= range(0,len(gunler))
plt.subplot(223),
plt.plot(x,y,"y"),
plt.xlabel("2016/4/1 - 2020/4/1"),
plt.ylabel("SO2"),
plt.title("Günlere göre ortalama SO2 değerleri")

y=gunler[["O3"]].iloc[::-1]
x= range(0,len(gunler))
plt.subplot(224),
plt.plot(x,y,"g"),
plt.xlabel("2016/4/1 - 2020/4/1"),
plt.ylabel("O3"),
plt.title("Günlere göre ortalama O3 değerleri")
plt.show()


havakalite=gunler.max(axis=1).apply(sinif)
sec=gunler.drop(["Tarih"],axis=1).idxmax(axis=1)

gunler["sec"]=sec
gunler["havakalite"]=havakalite

veri=[]
sayi=0
for x in enumerate(gunler.iloc[:,-1]):
 
  haftasonumu= x[0]%7==0 or x[0]%7==6
  
  if kalite[sayi]!=1 and haftasonumu==False:
    artis=1
  elif kalite[sayi]==1 and haftasonumu==False:
    artis=2
  elif kalite[sayi]!=1 and haftasonumu==True: 
    artis=3
  elif kalite[sayi]==1 and haftasonumu==True:
    artis=4

     
  sayi+=1
  veri.append(artis)
gunler["Durum"]=veri
veri=gunler.drop(['sec'],axis=1)
label_encoder=LabelEncoder().fit(veri.Durum)
labels=label_encoder.transform(veri.Durum)
classes=list(label_encoder.classes_)

X=veri.drop(["Durum","Tarih"],axis=1)
y=labels

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.23)
X_train=np.asarray(X_train).astype(np.float32)
from tensorflow.keras.utils import to_categorical
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model=Sequential()
model.add(Dense(4,input_dim=5,activation="relu"))
model.add(Dense(4,activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(4,activation="relu"))
model.add(Dense(2,activation="relu"))
model.add(Dense(4,activation="softmax"))
model.summary()

model.compile(loss="categorical_crossentropy",optimizer="SGD",metrics=["accuracy"])
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs =75)

print("Ortalama Eğitim Kaybı : ",np.mean(model.history.history["loss"]))
print("Ortalama Eğitim Başarımı : ",np.mean(model.history.history["accuracy"]))
print("Ortalama Doğrulama Kaybı : ",np.mean(model.history.history["val_loss"]))
print("Ortalama Doğrulama Başarımı : ",np.mean(model.history.history["val_accuracy"]))

plt.plot(model.history.history["accuracy"])
plt.plot(model.history.history["val_accuracy"])
plt.title("Model Başarımları : ")
plt.ylabel("Başarım : ")
plt.xlabel("Epok sayısı : ")
plt.legend(["Eğitim","Test"],loc="upper left")
plt.show()
