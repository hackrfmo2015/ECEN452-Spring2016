import numpy as np
import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
x = []      #frequency
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('S_Parameters_dB_LPF_TappedStubs_Lab6.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        x.append(float(row['Freq [GHz]']))
        y1.append(float(row['S11 LPF Tap']))
        y2.append(float(row['S11 LPF T']))
        y3.append(float(row['S11 LPF Milled']))
        y4.append(float(row['S21 LPF Tap']))
        y5.append(float(row['S21 LPF T']))
        y6.append(float(row['S21 LPF Milled']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(x, y1, 'b', label="S11 LPF Tapped")
ax1.plot(x, y2, 'g', label="S11 LPF T-Line")
ax1.plot(x, y3, 'r', label="S11 LPF Milled")
ax1.plot(x, y4, 'c', label="S21 LPF Tapped")
ax1.plot(x, y5, 'm', label="S21 LPF T-Line")
ax1.plot(x, y6, 'k', label="S21 LPF Milled")

ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=3) #add legend at location #1 (top-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('LPF Magnitude') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('Magnitude [dB]') #add y-axis title

plt.show() #required to display plots