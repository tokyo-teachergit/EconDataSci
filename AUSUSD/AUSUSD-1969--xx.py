from numpy.random import *
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt #%matplotlib inline
import matplotlib.dates as mdates

#Set font in Japanese
plt.rcParams["font.family"] = "Noto Sans CJK JP"

#Load a data file
df1 = pd.read_csv("AUSUSD-2010--xx.csv", #to read CSV file into df1 = DataFrame.
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
print("\nThis is the column with header name ""FXRUSD"".\n")
print(df1["FXRUSD"])
print("\nThis is the data type of the column with header name ""FXRUSD"".\n")
print(type(df1["FXRUSD"]))

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
df2 = pd.read_csv("AUSUSD-1969-2009.csv", #to read CSV file into df2 = DataFrame.
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
print("\nLet's sort teh datafrae.\n")
DFMerge = DFMerge.sort_index()#use sort_index after merging data. 
print(DFMerge)

print("\nCut out the part of dataframes before rendering.\n")
DATERANGE = DFMerge.loc['1980-01-01':'2024-11-01']
print("\nYou can see the DATERANGE.\n")
print(DATERANGE.info())
print("\nYou can see the DATERANGE dataframe.\n")
print(DATERANGE)

print("\nWell done, you finished the checking part.\n")

#Styling
sns.set_style("whitegrid") #Preset styling template.
#plt.grid(True) 
plt.rcParams["font.family"] = "Noto Sans CJK JP" #Set a font after set_style to overwrite.

plt.plot(DATERANGE.index, DATERANGE["FXRUSD"], color ='orange',
         marker ='o', markersize = 0.1, 
         label ='AUDUSD')
 
#plt.plot(df1["Series ID"], df1["Series ID"], color ='g',
#         linestyle ='dashed', linewidth = 2,
#         label ='JGB10YearYield')

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
fig = plt.legend(loc="upper left", fontsize=10) #Location of the legend.
#fig = plt.xlabel("Series ID") #Unit of X-Axis
#fig = plt.ylabel("-") #Unit of Y-Axis
#fig = plt.xlim(900, 2000) #X-Axis (Min,Max)
fig = plt.ylim(0, 1.5) #Y-Axis (Min,Max)
#fig = plt.xticks([0, 250, 500, 750])
fig = plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4])

#fig = plt.xticks(rotation='vertical') #Rotate strings(=words) at Xticks in case they appear inappropriately.
plt.savefig('AUSUSD-1969--xx.pdf')
#plt.savefig('AUSUSD-1969--xxa.png', dpi=72)
plt.savefig('AUSUSD-1969--xxb.png', dpi=300)
plt.savefig('AUSUSD-1969--xxc.png', dpi=600) #Save files in multiple resolution at once.
plt.show()