import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Updates_NC.csv')
from datetime import datetime, timedelta

# assuming the date format of "month月day日'
columns={'year','month','day'}
df1=pd.DataFrame(index=df.index, columns=columns)
df1['month']=pd.to_numeric(df['确诊/出院'].str.replace('月[0-9].','').str.replace('日',''))
df1['day']=pd.to_numeric(df['确诊/出院'].str.replace('[0-9]*月','').str.replace('日',''))
df1['year']=df1['month'] # initiate
df1['year']=2020 # year
# add datetime columns
df['dt']=pd.to_datetime(df1) # ['year'], pd.to_numeric(df['month']), pd.to_numeric(df['day']))

# df2 holds the processed data. not optimzed. 
dt_min=df['dt'].min()
dt_max=df['dt'].max()
index=range((dt_max-dt_min).days+1)
columns={'dt','infected', 'death'}
df2=pd.DataFrame(index=index, columns=columns)

df2['dt']=pd.date_range(dt_min, periods=(dt_max-dt_min).days+1, freq='D')

for k in  index:
    df3=df[df['dt'] <= df2['dt'][k]] # select the data with date <= to target date
    df2['infected'][k]=df3['新增确诊病例'].sum() # add up the infected
    df2['death'][k]=df3['新增死亡数'].sum() # add up the death
print(df2)

# plot
plt.figure(figsize=(12,8))
plt.semilogy(df2['dt'],df2['infected'],'o-', df2['dt'],df2['death'],'o-', linewidth=2)
plt.legend(['infected', 'death'])
plt.setp(plt.gca().xaxis.get_majorticklabels(),'rotation', 45)
plt.grid(b=True, which='both')

# supplemental lines to illustrate the significance. manually tuned for data up to 1/27/2020 
sn=6 #start
en=17 # end
yscale=0.85
tn=11 # text
plt.semilogy([df2['dt'][sn], df2['dt'][en]], [yscale*df2['infected'][sn], yscale*df2['infected'][en]], 'k-.', linewidth=2)
plt.text(df2['dt'][tn], 1.5*df2['infected'][tn], '10x growth in ~6 days', rotation= 29, bbox=dict(facecolor='red', alpha=0.5))
sn=7
en=15
yscale=0.95
tn=14
plt.semilogy([df2['dt'][sn], df2['dt'][en]], [yscale*df2['infected'][sn], yscale*df2['infected'][sn]], 'm-.', linewidth=2)
plt.text(df2['dt'][sn+1]+timedelta(hours=14), 0.8*df2['death'][tn], 'survival time in fatal infection, \n ~8 days after diagnosis', rotation= 0, bbox=dict(facecolor='red', alpha=0.5))

sn=16
tn=17
plt.semilogy([df2['dt'][sn], df2['dt'][sn]], [df2['infected'][sn], df2['death'][sn]], 'g-.', linewidth=2)
plt.text(df2['dt'][tn]-timedelta(hours=14), 0.45*df2['infected'][sn], '~40x -> 2.5% fatality', rotation= 90, bbox=dict(facecolor='red', alpha=0.5))
plt.title('2019-nCoV')
plt.show()

# fit data
# TBD