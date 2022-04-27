#-----------------------------------------------------------
#Program    :Ray_Sebastian_91044_Aufgabe_1_Programmcode.py
#Written by :Sebastian Ray
#Date       :05.04.2022
#Description:Various Kaplan Meier Calculations.
#-----------------------------------------------------------

#Further Information:
"""
Excel File: Aufgabe1_data.xlsx
Header column 'A' was labeled 'number'.
Header column 'B' was labeled 'failured'.

Excel File: Aufgabe1_data_cens.xlsx
Header column 'A' was labeled 'number'.
Header column 'B' was labeled 'failured.
"""

# In[1] --------------------------------------------------------------------------------------
#Import Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from lifelines import KaplanMeierFitter


# In[2] --------------------------------------------------------------------------------------
#Aufgabe 1 a)

df = pd.read_excel("Aufgabe1_data.xlsx")        #import an Excel file

kmf = KaplanMeierFitter()

failures = df['failures']

kmf.fit(failures)           #Fit the model to a right-censored datset
kmf.plot()

plt.title('Kaplan Meier estimates Task a)')     #named the title
plt.xlabel('years')                     #named the x-coordinates
plt.ylabel('failures')                  #named the y-coordinates
plt.show()


# In[3] --------------------------------------------------------------------------------------
#Aufgabe 1 b)

len_df = len(df)                             #Gives me the number of Excel entries
meanFailures = len_df/sum(df['failures'])    #Gives me the mean of the erros

xValue=np.linspace(0,2,200)             #x-axis scaling (start,end,count Values)
yValue=np.exp(-meanFailures*xValue)     #Calculate the exponetial of all elements in the input array

plt.plot(xValue,yValue)

plt.title('Kaplan Meier estimates Task b)')     #named the title
plt.xlabel('years')                     #named the x-coordinates
plt.ylabel('failures')                  #named the y-coordinates
plt.show()



# In[4] --------------------------------------------------------------------------------------
#Aufgabe 1 c)
#https://www.youtube.com/watch?v=XQfxndJH4UA&ab_channel=Montreal-Python

df2 = pd.read_excel("Aufgabe1_data_cens.xlsx")  #import an Excel file

kmf2 = KaplanMeierFitter()

dfMask = df2['failures'] < 0.25         #Creates a mask. Values less than 0.25 are returned as true, else false

failures = df2['failures']

kmf2.fit(failures,dfMask)                 #Fit the model to a right-censored datset
kmf2.plot()

plt.title("Kaplan Meier estimate cens Task c)")
plt.xlabel('years')
plt.ylabel('failures')
plt.show()



# In[4] --------------------------------------------------------------------------------------
#Aufgabe 1 d)

len_df = len(df2)                       #Gives me the number of Excel entries

filtered = df2[dfMask]                  #All true values are filtered by using the previous mask
lenDf2 = len(filtered)

sumFailures2 = sum(df2['failures'])     #Gives me the sum of the erros

resultKmf2 = lenDf2/sumFailures2        #KMF = n/sum(n)

xValue2=np.linspace(0,2,200)            #x-axis scaling (start,end,count Values)
yValue2=np.exp(-resultKmf2*xValue2)     #Calculate the exponetial of all elements in the input array


plt.plot(xValue2,yValue2)
plt.title("Kaplan Meier estimate cens Task d)")
plt.xlabel('years')
plt.ylabel('failures')
plt.show()