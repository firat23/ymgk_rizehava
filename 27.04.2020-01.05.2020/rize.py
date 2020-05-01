import matplotlib.pyplot as plt
import pandas as pd
def sinif(havakalite):
    if havakalite <= 50:
        return "İYİ"
    elif havakalite <=100:
        return "ORTA"
    elif havakalite <=150:
        return "HASSAS"
    elif havakalite <=200:
        return "SAĞLIKSIZ"
    elif havakalite <=300:
        return "KÖTÜ"
    elif havakalite <=500:
        return "TEHLİKELİ"
    else:
        return "-"

haftaici=[]
haftasonu=[]

hava=pd.read_csv("rizeveri.csv" )
gunler=hava.groupby("Tarih")
gunler=gunler.mean()

gunler=gunler.sort_values(["Tarih"], ascending = True)
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
plt.xlabel("2018/10/29 - 2020/4/12"),
plt.ylabel("SO2"),
plt.title("Günlere göre ortalama SO2 değerleri")

y=gunler[["O3"]].iloc[::-1]
x= range(0,len(gunler))
plt.subplot(224),
plt.plot(x,y,"g"),
plt.xlabel("2018/10/29 - 2020/4/12"),
plt.ylabel("O3"),
plt.title("Günlere göre ortalama O3 değerleri")
plt.show()
havakalite=gunler.max(axis=1).apply(sinif)
sec=gunler.idxmax(axis=1)

gunler["sec"]=sec
gunler["havakalite"]=havakalite

for x in enumerate(gunler.iloc[:,-1]):
   
    if x[0]%7==0 or x[0]%7==6:
        haftasonu.append(str(gunler.iloc[x[0],-2])+":"+str(x[1]))
    else:
        haftaici.append(str(gunler.iloc[x[0],-2])+":"+str(x[1]))

haftasonugunu={"PM10":0,"NO2":0,"SO2":0,"O3":0}
haftaicigunu={"PM10":0,"NO2":0,"SO2":0,"O3":0}
for i in haftaici:
    veri=i.split(':')
    if veri[0]=="PM10":
        haftaicigunu["PM10"]+=1
    elif veri[0]=="NO2":
        haftaicigunu["NO2"]+=1
    elif veri[0]=="SO2":
        haftaicigunu["SO2"]+=1
    else:
        haftaicigunu["O3"]+=1
                   
for i in haftasonu:
    veri=i.split(':')
    if veri[0]=="PM10":
        haftasonugunu["PM10"]+=1
    elif veri[0]=="NO2":
        haftasonugunu["NO2"]+=1
    elif veri[0]=="SO2":
        haftasonugunu["SO2"]+=1
    else:
        haftasonugunu["O3"]+=1


Solgini={"PM10":0,"NO2":0,"SO2":0,"O3":0}
Saggini={"PM10":0,"NO2":0,"SO2":0,"O3":0}
Ginij={"PM10":0,"NO2":0,"SO2":0,"O3":0}

toplamhaftaici=haftaici.count("PM10:İYİ")
toplamhaftasonu=haftasonu.count("PM10:İYİ")
tsol=toplamhaftaici+toplamhaftasonu
tsag=haftaicigunu["PM10"]-toplamhaftaici+haftasonugunu["PM10"]-toplamhaftasonu
if toplamhaftaici==0 and toplamhaftasonu==0:
    Solgini["PM10"]=0
else:
    Solgini["PM10"]=1-(((toplamhaftaici/tsol)**2)+(toplamhaftasonu/tsol)**2)
if haftaicigunu["PM10"]-toplamhaftaici==0 and haftasonugunu["NO2"]-toplamhaftasonu==0:
    Saggini["PM10"]=0
else:
    Saggini["PM10"]=1-((((haftaicigunu["PM10"]-toplamhaftaici)/tsag)**2)+((haftasonugunu["PM10"]-toplamhaftasonu)/tsag)**2)

if tsol+tsag>0:
    Ginij["PM10"]=1/(tsol+tsag)*((tsol*Solgini["PM10"])+(tsag*Saggini["PM10"]))
else:
    Ginij["PM10"]=0

toplamhaftaici=haftaici.count("NO2:İYİ")
toplamhaftasonu=haftasonu.count("NO2:İYİ")
tsol=toplamhaftaici+toplamhaftasonu
tsag=haftaicigunu["NO2"]-toplamhaftaici+haftasonugunu["NO2"]-toplamhaftasonu
if toplamhaftaici==0 and toplamhaftasonu==0:
    Solgini["NO2"]=0
else:
    Solgini["NO2"]=1-(((toplamhaftaici/tsol)**2)+(toplamhaftasonu/tsol)**2)
if haftaicigunu["NO2"]-toplamhaftaici==0 and haftasonugunu["NO2"]-toplamhaftasonu==0:
    Saggini["NO2"]=0
else:
    Saggini["NO2"]=1-((((haftaicigunu["NO2"]-toplamhaftaici)/tsag)**2)+((haftasonugunu["NO2"]-toplamhaftasonu)/tsag)**2)

if tsol+tsag>0:
    Ginij["NO2"]=1/(tsol+tsag)*((tsol*Solgini["NO2"])+(tsag*Saggini["NO2"]))
else:
    Ginij["NO2"]=0
    
toplamhaftaici=haftaici.count("SO2:İYİ")
toplamhaftasonu=haftasonu.count("SO2:İYİ")
tsol=toplamhaftaici+toplamhaftasonu
tsag=haftaicigunu["SO2"]-toplamhaftaici+haftasonugunu["SO2"]-toplamhaftasonu
if toplamhaftaici==0 and toplamhaftasonu==0:
    Solgini["SO2"]=0
else:
    Solgini["SO2"]=1-(((toplamhaftaici/tsol)**2)+(toplamhaftasonu/tsol)**2)

if haftaicigunu["SO2"]-toplamhaftaici==0 and haftasonugunu["SO2"]-toplamhaftasonu==0:
    Saggini["SO2"]=0
else:
    Saggini["SO2"]=1-((((haftaicigunu["SO2"]-toplamhaftaici)/tsag)**2)+((haftasonugunu["SO2"]-toplamhaftasonu)/tsag)**2)

if tsol+tsag>0:
    Ginij["SO2"]=1/(tsol+tsag)*((tsol*Solgini["SO2"])+(tsag*Saggini["SO2"]))
else:
    Ginij["SO2"]=0
      
toplamhaftaici=haftaici.count("O3:İYİ")
toplamhaftasonu=haftasonu.count("O3:İYİ")

tsol=toplamhaftaici+toplamhaftasonu
tsag=haftaicigunu["O3"]-toplamhaftaici+haftasonugunu["O3"]-toplamhaftasonu
if toplamhaftaici==0 and toplamhaftasonu==0:
    Solgini["O3"]=0
else:
    Solgini["O3"]=1-(((toplamhaftaici/tsol)**2)+(toplamhaftasonu/tsol)**2)

if tsol+tsag>0:
    Ginij["O3"]=1/(tsol+tsag)*((tsol*Solgini["O3"])+(tsag*Saggini["O3"]))
else:
    Ginij["O3"]=0


print("Haftaiçi Günler : ")
print(haftaici)
print("\nHaftasonu Günler : ")
print(haftasonu)
print("\nGini-J : ")
print(Ginij)
