from numpy.random import *
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt #%matplotlib inline
import matplotlib.dates as mdates

#Load a data file
df1 = pd.read_csv("OfficialRate-2011-xx.csv", #to read CSV file into df1 = DataFrame.
		sep=",", 
		engine = "python", #to load Japanese CSV file.
		encoding = "utf-8",
        header=[10], #header=[1] = use the second row for comlumn headers, header=[0] = use the first row for comlumn headers. PANDAS count 0 for the first row, 1 for the second row.  
		#index_col=[0], 
		)

#Data Check
print("\nHello, this is the checking part before visualizeing your data.\n")
print("\nThis is the overall information of your data.\n")
print(df1.info()) 
print("\nThis is the first three rows and columns of your data.\n")
print(df1.head(3))
print("\nThis is the data type of your first column.\n")
print(type(df1["Series ID"]))
print("\nThis is the column with header name FIRMMCRTD.\n")
print(df1["FIRMMCRTD"])
print("\nThis is the data type of the column with header name ""FIRMMCRTD"".\n")
print(type(df1["FIRMMCRTD"]))

print("\nNow let's change the datatype to prepare for our visualization.\n")
print("\nChanging obeject to datetime.\n")
#df1["Series ID"] = pd.to_datetime(df1["Series ID"])
df1["Series ID"] = pd.to_datetime(df1["Series ID"], infer_datetime_format=True)
print("\nYou can see the converted datatypes.\n")
print(df1.info())
print("\nYou can see the converted dataframe.\n")
print(df1)
print("\nThen, we set Series ID as index.\n")
df1 = df1.set_index("Series ID")
print("\nSee how set_index works.\n")
print(df1.info())
print(df1)






#Load a data file
print("\nNext, we make the second datadrame as df2.\n")
df2 = pd.read_csv("OfficialRate-1990-2010.csv", #to read CSV file into df2 = DataFrame.
		sep=",", 
		engine = "python", #to load Japanese CSV file.
		encoding = "utf-8",
        header=[10], #header=[1] = use the second row for comlumn headers, header=[0] = use the first row for comlumn headers. PANDAS count 0 for the first row, 1 for the second row.  
		#index_col=[0], 
		)
print("\nThis is the overall information of your data.\n")
print(df2.info()) 
print("\nThis is the rows and columns of your data.\n")
print(df2.head(3))
df2["Series ID"] = pd.to_datetime(df2["Series ID"], infer_datetime_format=True)
print("\nYou can see the converted datatypes.\n")
print(df2.info())
print("\nYou can see the converted dataframe.\n")
print(df2)
print("\nThen, we set Series ID as index.\n")
df2 = df2.set_index("Series ID")
print("\nSee how set_index works.\n")
print(df2.info())
print(df2)

print("\nLet's merge df1 and df2.\n")
DFMerge = pd.concat([df1, df2], axis=0, ignore_index=False)
print("\nSee how concat works to merge two dataframes.\n")
print(DFMerge.info())
print(DFMerge)
print("\nLet's sort the dataframe.\n")
DFMerge = DFMerge.sort_index()#use sort_index after merging data. 
print(DFMerge)

print("\nCut out the part of dataframes before rendering.\n")
DATERANGE = DFMerge.loc['1990-09-01':'2024-11-01']
print("\nYou can see the DATERANGE.\n")
print(DATERANGE.info())
print("\nYou can see the DATERANGE dataframe.\n")
print(DATERANGE)

print("\nThe datatype of FIRMMCRTD is object and it is not suitable for plotting. Let's change the datatype of FIRMMCRTD from object to float.\n")
DATERANGE['FIRMMCRTD'] = pd.to_numeric(DATERANGE['FIRMMCRTD'])
print(DATERANGE.info())

print("\nWell done, you finished the checking part.\n")





















#Load FEDFUNDS data file
FEDFUNDSDF = pd.read_csv("FFRate1954to2024.csv", #to read CSV file into FEDFUNDSDF = DataFrame.
		sep=",", 
		engine = "python", #to load Japanese CSV file.
		encoding = "utf-8",
        header=[0], #header=[1] = use the second row for comlumn headers, header=[0] = use the first row for comlumn headers. PANDAS count 0 for the first row, 1 for the second row.  
		#index_col=[0], 
		)

#Check Pandas dataframe
print("\nHello, this is the checking part of FEDFUNDSDF data.\n")
print("\nThis is the overall information of your data.\n")
print(FEDFUNDSDF.info()) 
print("\nThis is the rows and columns of your data.\n")
print(FEDFUNDSDF)
print("\nThis is your first column.\n")
print(FEDFUNDSDF["DATE"])
print("\nThis is the data type of your first column.\n")
print(type(FEDFUNDSDF["DATE"]))
print("\nThis is the column with header name ""FEDFUNDS"".\n")
print(FEDFUNDSDF["FEDFUNDS"])
print("\nThis is the data type of the column with header name ""FEDFUNDS"".\n")
print(type(FEDFUNDSDF["FEDFUNDS"]))

print("\nNow let's change the datatype to prepare for our visualization.\n")
print("\nChanging obeject to datetime.\n")
FEDFUNDSDF['DATE'] = pd.to_datetime(FEDFUNDSDF['DATE'], infer_datetime_format=True)
print("\nYou can see the converted datatypes.\n")
print(FEDFUNDSDF.info())
print("\nYou can see the converted dataframe.\n")
print(FEDFUNDSDF)
#print("\nGood. Then, we want to use only months and years in the dtaframe.\n")
#FEDFUNDSDF['YEAR_MONTH'] = FEDFUNDSDF['DATE'].dt.strftime('%Y年%m月')
#print(FEDFUNDSDF.info())
#print(FEDFUNDSDF)
print("\nLet's use DATE as DatetimeIndex.\n")
FEDFUNDSDF = FEDFUNDSDF.set_index("DATE")
print(FEDFUNDSDF.info())
print(FEDFUNDSDF)
FEDFUNDSDF = FEDFUNDSDF.loc['1990-01-01':'2024-11-01']
print(FEDFUNDSDF.info())
print(FEDFUNDSDF)
print("\nWell done, you finished the checking part.\n")













#Styling
"""
color = 
b	青 (Blue)
g	緑 (Green)
r	赤 (Red)
c	シアン (Cyan)
m	マゼンタ (Magenta)
y	黄 (Yellow)
k	黒 (Black)
w	白 (White)
"""

"""
#Add Annotation and Arrow
plt.annotate('local max', xy=(1950, 100),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            # arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
"""

#Rendering section
sns.set_style("whitegrid") #Preset styling template.
#plt.grid(True) 
plt.rcParams["font.family"] = "Noto Sans CJK JP" #Set a font after set_style to overwrite.
fig, ax1 = plt.subplots(1,1) #Make a place for figure and add simple xy axes. 

plt.plot(DATERANGE.index, DATERANGE["FIRMMCRTD"], color ='orange',
         marker ='o', markersize = 0.1, 
         label ='Australia Cash Rate')
ax1.tick_params(axis='y', labelcolor='orange')
#plt.plot(df1["Series ID"], df1["Series ID"], color ='g',
#         linestyle ='dashed', linewidth = 2,
#         label ='JGB10YearYield')
ax1.set_ylim(bottom=0, top=11, emit=True, auto=False, ymin=None, ymax=None) #Y-Axis
fig = plt.legend(loc="upper left", fontsize=10) #Location of the legend.


#fig = plt.xlabel("Series ID") #Unit of X-Axis
#fig = plt.ylabel("-") #Unit of Y-Axis
#fig = plt.xlim(900, 2000) #X-Axis (Min,Max)
#fig = plt.ylim(0, 1.5) #Y-Axis (Min,Max)
#fig = plt.xticks([0, 250, 500, 750])
#fig = plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4])

#fig = plt.xticks(rotation='vertical') #Rotate strings(=words) at Xticks in case they appear inappropriately.


# instantiate a second Axes that shares the same x-axis
ax2 = ax1.twinx()  
ax2.plot(FEDFUNDSDF.index, FEDFUNDSDF["FEDFUNDS"], color ='blue', label ='FEDFUNDS')
ax2.set_ylabel('FEDFUNDSRATE', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
ax2.set_ylim(bottom=0, top=11, emit=True, auto=False, ymin=None, ymax=None) #Y-Axis
#fig.tight_layout()  # otherwise the right y-label is slightly clipped
fig = plt.legend(loc="upper right", fontsize=10) #Location of the legend.






#Data Save Section
plt.savefig('CashRatevsFFRate-1990--xx.pdf')
plt.savefig('CashRatevsFFRate-1990--xxb.png', dpi=300)
plt.savefig('CashRatevsFFRate-1990--xxc.png', dpi=600) #Save files in multiple resolution at once.
plt.show()