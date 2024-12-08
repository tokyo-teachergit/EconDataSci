from numpy.random import *
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt #%matplotlib inline
import matplotlib.dates as mdates

#Set font in Japanese
plt.rcParams["font.family"] = "Noto Sans CJK JP"

#Load a data file
df = pd.read_csv("AUSUSD-2010--xx.csv", #to read CSV file into df = DataFrame.
		sep=",", 
		engine = "python", #to load Japanese CSV file.
		encoding = "utf-8",
        header=[10], #header=[1] = use the second row for comlumn headers, header=[0] = use the first row for comlumn headers. PANDAS count 0 for the first row, 1 for the second row.  
		#index_col=[0], 
		)

#Check Pandas dataframe, showing first 5 row.
print("\nHello, this is the checking part before visualizeing your data.\n")
#print("This is the first three rows in your data.")
#print(df.head(3))
print("\nThis is the overall information of your data.\n")
print(df.info()) 
print("\nThis is the rows and columns of your data.\n")
print(df)
print("\nThis is the column labels of your data.\n")
print(df.columns)
print("\nThis is your first column.\n")
print(df["Series ID"])
print("\nThis is the data type of your first column.\n")
print(type(df["Series ID"]))
print("\nThis is the column with header name ""FXRUSD"".\n")
print(df["FXRUSD"])
print("\nThis is the data type of the column with header name ""FXRUSD"".\n")
print(type(df["FXRUSD"]))

print("\nNow let's change the datatype to prepare for our visualization.\n")
print("\nChanging obeject to datetime.\n")
#df["Series ID"] = pd.to_datetime(df["Series ID"])
df["Series ID"] = pd.to_datetime(df["Series ID"], infer_datetime_format=True)
print("\nYou can see the converted datatypes.\n")
print(df.info())
print("\nYou can see the converted dataframe.\n")
print(df)
df = df.set_index("Series ID")
print(df.info())
print(df)

DATERANGE = df.loc['2010-01-01':'2024-11-01']
print("\nYou can see the DATERANGE.\n")
print(DATERANGE.info())
print("\nYou can see the DATERANGE dataframe.\n")
print(DATERANGE)

#print("\nGood. Then, we want to use only months and years in the dtaframe.\n")
#df['YEAR_MONTH'] = df["Series ID"].dt.strftime('%Y年%m月')
#print(df.info())
#print(df)


#print("\nNow let's change the datatype to prepare for our visualization.\n")
#print("\nDropping rows with ""-"".\n")
#df = df[df["FXRUSD"].str.contains("-") == False] #Check the column with header ""FXRUSD"" then drop the row with value ""-"". 

#df["FXRUSD"] = pd.to_numeric(df["FXRUSD"]) #Convert datatype from obeject to int or float. Note that this "to_numeric" command didn't work with "-" simbol.
#print("\nYou can see the converted datatypes.\n")
#print(df.info())

print("\nWell done, you finished the checking part.\n")

#Styling
sns.set_style("whitegrid") #Preset styling template.
#plt.grid(True) 
plt.rcParams["font.family"] = "Noto Sans CJK JP" #Set a font after set_style to overwrite.

#plt.plot(df["YEAR_MONTH"], df["FXRUSD"], color ='orange',
#plt.plot(df["Series ID"], df["FXRUSD"], color ='orange',
plt.plot(DATERANGE.index, DATERANGE["FXRUSD"], color ='orange',
         marker ='o', markersize = 0.1, 
         label ='AUDUSD')
 
#plt.plot(df["Series ID"], df["Series ID"], color ='g',
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
plt.savefig('AUSUSD-2010--xx.pdf')
#plt.savefig('AUSUSD-2010--xxa.png', dpi=72)
plt.savefig('AUSUSD-2010--xxb.png', dpi=300)
plt.savefig('AUSUSD-2010--xxc.png', dpi=600) #Save files in multiple resolution at once.
plt.show()
