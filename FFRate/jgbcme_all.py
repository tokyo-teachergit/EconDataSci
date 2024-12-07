from numpy.random import *
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt #%matplotlib inline
import matplotlib.dates as mdates

#Set font in Japanese
plt.rcParams["font.family"] = "Noto Sans CJK JP"

#Load a data file
df = pd.read_csv("FFRate1954to2024.csv", #to read CSV file into df = DataFrame. Bank Of Japan data set is here. https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/index.htm
		sep=",", 
		engine = "python", #to load Japanese CSV file.
		encoding = "utf-8",
        header=[0], #header=[1] = use the second row for comlumn headers, header=[0] = use the first row for comlumn headers. PANDAS count 0 for the first row, 1 for the second row.  
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
print(df["DATE"])
print("\nThis is the data type of your first column.\n")
print(type(df["DATE"]))
print("\nThis is the column with header name ""FEDFUNDS"".\n")
print(df["FEDFUNDS"])
print("\nThis is the data type of the column with header name ""FEDFUNDS"".\n")
print(type(df["FEDFUNDS"]))

#print("\nNow let's change the datatype to prepare for our visualization.\n")
#print("\nChanging obeject to datetime.\n")
#df['Date_Time'] = pd.to_datetime(df['Date_Time'])

print("\nNow let's change the datatype to prepare for our visualization.\n")
print("\nDropping the last 3 strings.\n")
df["DATE"] = df["DATE"].str[:-3] 

#print("\nNow let's change the datatype to prepare for our visualization.\n")
#print("\nDropping rows with ""-"".\n")
#df = df[df["FEDFUNDS"].str.contains("-") == False] #Check the column with header ""FEDFUNDS"" then drop the row with value ""-"". 

df["FEDFUNDS"] = pd.to_numeric(df["FEDFUNDS"]) #Convert datatype from obeject to int or float. Note that this "to_numeric" command didn't work with "-" simbol.
print("\nYou can see the converted datatypes.\n")
print(df.info())
print("\nWell done, you finished the checking part.\n")

#Styling
sns.set_style("whitegrid") #Preset styling template.
#plt.grid(True) 
plt.rcParams["font.family"] = "Noto Sans CJK JP" #Set a font after set_style to overwrite.

plt.plot(df["DATE"], df["FEDFUNDS"], color ='orange',
         marker ='o', markersize = 0.1, 
         label ='FEDFUNDS')
 
#plt.plot(df["DATE"], df["DATE"], color ='g',
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
fig = plt.xlabel("DATE") #Unit of X-Axis
#fig = plt.ylabel("-") #Unit of Y-Axis
fig = plt.xlim(0, 1000) #X-Axis (Min,Max)
fig = plt.ylim(0, 10) #Y-Axis (Min,Max)
fig = plt.xticks([0, 250, 500, 750, 1000])
fig = plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9])

#fig = plt.xticks(rotation='vertical') #Rotate strings(=words) at Xticks in case they appear inappropriately.  
plt.savefig('FFRate1954to2024.pdf')
plt.savefig('FFRate1954to2024a.png', dpi=72)
plt.savefig('FFRate1954to2024b.png', dpi=300)
plt.savefig('FFRate1954to2024c.png', dpi=600) #Save files in multiple resolution at once.
plt.show()
