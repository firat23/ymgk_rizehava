# 170541302
# Hamit FIRAT
# 17.04.2020

import matplotlib.pyplot as plt
import pandas as pd

veri=pd.read_csv("rizeveri.csv" )
gunler=veri.groupby("Tarih")
gunler=gunler.mean()
gunler=gunler.sort_values(["Tarih"], ascending = True)
####################
y=gunler[["PM10"]].iloc[::-1]
x= range(0,len(gunler))
plt.plot(x,y,"r")
plt.xlabel("2016/4/1 - 2020/4/1")
plt.ylabel("PM10")
plt.title("Son 4 Yılın Ortalama PM10 Değerleri")
plt.show()
####################
y=gunler[["NO2"]].iloc[::-1]
x= range(0,len(gunler))
plt.plot(x,y,"b")
plt.xlabel("2016/4/1 - 2020/4/1")
plt.ylabel("NO2")
plt.title("Son 4 Yılın Ortalama NO2 Değerleri")
plt.show()
####################
y=gunler[["SO2"]].iloc[::-1]
x= range(0,len(gunler))
plt.plot(x,y,"y")
plt.xlabel("2016/4/1 - 2020/4/1")
plt.ylabel("SO2")
plt.title("Son 4 Yılın Ortalama SO2 Değerleri")
plt.show()
####################
y=gunler[["O3"]].iloc[::-1]
x= range(0,len(gunler))
plt.plot(x,y,"g")
plt.xlabel("2016/4/1 - 2020/4/1")
plt.ylabel("O3")
plt.title("Son 4 Yılın Ortalama O3 Değerleri")
plt.show()
