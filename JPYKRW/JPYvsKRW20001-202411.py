from numpy.random import *
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt #%matplotlib inline
import matplotlib.dates as mdates

#Load a data file
df1 = pd.read_csv("JPYKRW200001-202411.csv", #to read CSV file into df1 = DataFrame.
		sep=",", 
		engine = "python", #to load Japanese CSV file.
		encoding = "utf-8",
        header=[0], #header=[1] = use the second row for comlumn headers, header=[0] = use the first row for comlumn headers. PANDAS count 0 for the first row, 1 for the second row.  
		#index_col=[0], 
		)

#Data Check
print("\nHello, this is the checking part before visualizeing your data.\n")
print("\nThis is the overall information of your data.\n")
print(df1.info()) 
print("\nThis is the first three rows and columns of your data.\n")
print(df1.head(3))
print("\nThis is the data type of your first column.\n")
print(type(df1["日付け"]))
print("\nThis is the column with header name 終値.\n")
print(df1["終値"])
print("\nThis is the data type of the column with header name ""終値"".\n")
print(type(df1["終値"]))

print("\nNow let's change the datatype to prepare for our visualization.\n")
print("\nChanging obeject to datetime.\n")
#df1["日付け"] = pd.to_datetime(df1["日付け"])
df1["日付け"] = pd.to_datetime(df1["日付け"], infer_datetime_format=True)
print("\nYou can see the converted datatypes.\n")
print(df1.info())
print("\nYou can see the converted dataframe.\n")
print(df1)
print("\nThen, we set 日付け as index.\n")
df1 = df1.set_index("日付け")
print("\nSee how set_index works.\n")
print(df1.info())
print(df1)





""""
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
df2["日付け"] = pd.to_datetime(df2["日付け"], infer_datetime_format=True)
print("\nYou can see the converted datatypes.\n")
print(df2.info())
print("\nYou can see the converted dataframe.\n")
print(df2)
print("\nThen, we set 日付け as index.\n")
df2 = df2.set_index("日付け")
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

print("\nThe datatype of 終値 is object and it is not suitable for plotting. Let's change the datatype of 終値 from object to float.\n")
DATERANGE['終値'] = pd.to_numeric(DATERANGE['終値'])
print(DATERANGE.info())

"""

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

plt.plot(df1.index, df1["終値"], color ='Green',
         marker ='o', markersize = 0.1, 
         label ='JPY/KRW 日本円/韓国ウォン')
ax1.tick_params(axis='y', labelcolor='Green')
#plt.plot(df1["日付け"], df1["日付け"], color ='g',
#         linestyle ='dashed', linewidth = 2,
#         label ='JGB10YearYield')
ax1.set_ylim(bottom=7, top=16, emit=True, auto=False, ymin=None, ymax=None) #Y-Axis
fig = plt.legend(loc="upper left", fontsize=10) #Location of the legend.


#fig = plt.xlabel("日付け") #Unit of X-Axis
#fig = plt.ylabel("-") #Unit of Y-Axis
#fig = plt.xlim(900, 2000) #X-Axis (Min,Max)
#fig = plt.ylim(0, 1.5) #Y-Axis (Min,Max)
#fig = plt.xticks([0, 250, 500, 750])
#fig = plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4])

#fig = plt.xticks(rotation='vertical') #Rotate strings(=words) at Xticks in case they appear inappropriately.




#Data Save Section
plt.savefig('JPYvsKRW20001-202411.pdf')
plt.savefig('JPYvsKRW20001-202411b.png', dpi=300)
plt.savefig('JPYvsKRW20001-202411c.png', dpi=600) #Save files in multiple resolution at once.
plt.show()