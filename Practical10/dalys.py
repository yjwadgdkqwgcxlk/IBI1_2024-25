#import the necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set up a list of personnel 
# Modify the file path
os.chdir("D:\Downloads1")
# check the directory
# print("present directory:", os.getcwd())
# print("directory list:", os.listdir())

#Import the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Operate on the dataframe
# Display the third column of the first ten rows
year_first_10 = dalys_data.iloc[0:10, 2]  # the index of columns starts from0, and the third column has the index "2"
print("The data of year for the first ten columns：")
print(year_first_10)
# The 10th recorded year of Afghanistan is 1999.

# Identify the 1990 data using Boolean
mask_1990 = dalys_data['Year'] == 1990
dalys_1990 = dalys_data.loc[mask_1990, 'DALYs']
print("1990 data:")
print(dalys_1990)  # show the 1990 data

# Determine the mean of DALYs of the UK and France
# the Uk
uk_data = dalys_data.loc[dalys_data['Entity'] == "United Kingdom", "DALYs"]
uk_mean = uk_data.mean()
# France
france_data = dalys_data.loc[dalys_data['Entity'] == "France", 'DALYs']
france_mean = france_data.mean()

print(f"The mean of DALYs of the Uk: {uk_mean:.2f}")
print(f"The mean of DALYs of France: {france_mean:.2f}")
# comparing the outcomes of the Uk and France
if uk_mean > france_mean:
    print("The mean of DALYs of the UK is higher than that of France.")
else:
    print("The mean of DALYs of the Uk is lower than that of France.")

# plot the data for the UK over time
# find the data of year and DALYS of the UK
uk_time_series = dalys_data.loc[dalys_data['Entity'] == "United Kingdom", ['Year', 'DALYs']]
# creat the figure and set factors
plt.figure(figsize=(10, 6))
plt.plot(uk_time_series['Year'], uk_time_series['DALYs'], 'b+', label='United Kingdom')  # 'b+'means blue+
plt.xticks(uk_time_series['Year'], rotation=-90)  # Rotating around the x-axis and make it easier to view.
# add figure labels
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Trend in the United Kingdom over Time')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()  # Adjust the layout to prevent labels overlapping.
plt.show()


# self-question: comparing the DALYs of Australia and Andorra over time
# Question: How has the DALYs rate changed in Australia vs. Andorra over time?
#get the data for the two countries respectively
australia_data = dalys_data[dalys_data['Entity'] == "Australia"][['Year', 'DALYs']]
andorra_data = dalys_data[dalys_data['Entity'] == "Andorra"][['Year', 'DALYs']]
# drawing the conparing figure
plt.figure(figsize=(12, 6))
plt.plot(australia_data['Year'], australia_data['DALYs'], 'g-', label='Australia', marker='o')
plt.plot(andorra_data['Year'], andorra_data['DALYs'], 'b-', label='Andorra', marker='s')
plt.xticks(australia_data['Year'], rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs Rate')
plt.title('DALYs Comparison: Australia vs. Andorra (1990-2019)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
# caclulate the means of DALYs
australia_mean = australia_data['DALYs'].mean()
andorra_mean = andorra_data['DALYs'].mean()
#show the output
print(f"\n--- Australia vs. Andorra DALYs Summary ---")
print(f"Australia Average DALYs: {australia_mean:.2f}")
print(f"Andorra Average DALYs: {andorra_mean:.2f}")
if australia_mean > andorra_mean:
    print("The mean of DALYS of Andorra is lower than that of Australia")
else:
    print("The mean of DALYs of Andorra is higher than that of Australia")