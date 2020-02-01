import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import matplotlib     
matplotlib.rc('xtick', labelsize=20)     
matplotlib.rc('ytick', labelsize=20)

#df=pd.read_csv('Updates_NC.csv',encoding='GB2312') # 1/31, encoding changed from utf-8 to gb2312.
df=pd.read_csv('Updates_NC.csv',encoding='utf-8') # 2/1, encoding changed back to utf-8
# assuming the date format of "month月day日'
columns={'year','month','day'}
df1=pd.DataFrame(index=df.index, columns=columns)
#df1['month']=pd.to_numeric(df['确诊/出院'].str.replace('月[0-9].','').str.replace('日',''))
#df1['day']=pd.to_numeric(df['确诊/出院'].str.replace('[0-9]*月','').str.replace('日',''))
# 1/31 new data format 
df1['month']=pd.to_numeric(df['报道时间'].str.replace('月[0-9].','').str.replace('日',''))
df1['day']=pd.to_numeric(df['报道时间'].str.replace('[0-9]*月','').str.replace('日',''))
df1['year']=df1['month'] # initiate
df1['year']=2020 # year
# add datetime columns
df['dt']=pd.to_datetime(df1) 

# df2 holds the processed data. not optimized. 
dt_min=df['dt'].min()
dt_max=df['dt'].max()
index=range((dt_max-dt_min).days+1)
columns={'dt','infection', 'death'}
df2=pd.DataFrame(index=index, columns=columns)

df2['dt']=pd.date_range(dt_min, periods=(dt_max-dt_min).days+1, freq='D')

for k in  index:
    df3=df[df['dt'] <= df2['dt'][k]] # select the data with date <= to target date
    df2['infection'][k]=df3['新增确诊'].sum() # add up the infection
    df2['death'][k]=df3['新增死亡'].sum() # add up the death
print(df2)

# overall data average slope

# plot
fig, ax1 = plt.subplots(figsize=(12,8))
ax1.semilogy(df2['dt'],df2['infection'],'bo-', df2['dt'],df2['death'],'co-', linewidth=3)
ax1.legend(['infection', 'death'], fontsize=20)

from scipy.stats import linregress
# calculated the growth rate for each day from the previous N_ave days
def growthRate(df, list, N_ave):
    for item in list:
        x=pd.to_numeric(df['dt'])/86400e9
        y=np.log(pd.to_numeric(df[item]))
        df[item+'_gr']=df['dt'] #initiate
        df[item+'_gr']=0
        for k in range(len(df.index)):
            if k >= N_ave:
                stats=linregress(x[k-N_ave+1:k+1],y[k-N_ave+1:k+1])
                df[item+'_gr'].loc[k]=stats.slope
    return df

def aveGrowthRate(df, list): # overall slope
    result=[]
    for item in list:
        x=pd.to_numeric(df['dt'])/86400e9
        y=np.log(pd.to_numeric(df[item]))
        stats=linregress(x.iloc[[0, -1]], y.iloc[[0, -1]])
        result.append(stats.slope)
    return result

N_ave=5 # number of days to average from past data points (including the current data point)    
growthRate(df2, ['infection', 'death'], N_ave)
print(df2)
print("The Average Growth rate for"+" infection and death with all data points"+ " are:")
print(aveGrowthRate(df2, ['infection', 'death']))  # print the over all growth rate with all the available data

ax2=ax1.twinx()
ax2.plot(df2['dt'], df2['infection_gr'], 'bo-.', df2['dt'], df2['death_gr'], 'co-.', linewidth=2)
ax2.legend(['infection growth rate', 'death growth rate'], loc='lower right', fontsize=20)
#ax1.grid(b=True, which='major')
#ax2.grid(b=True, which='both', axis='y', color='k', linestyle='-.', linewidth=1)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.savefig(df2['dt'].iloc[-1].strftime("%Y%m%d")+'.png', format='png')
plt.show()
