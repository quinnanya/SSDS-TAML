#!/usr/bin/env python
# coding: utf-8

# # Visualization essentials

# ![viz](img/viz.png)

# After importing data, you should examine it closely. 
# 
# 1. Look at the raw data to perform rough checks of your assumptions
# 2. Computer summary statistics
# 3. Produce visualizations to illustrate obvious - or not so obvious - trends in the data

# ## Plotting with seaborn
# 
# ### First, a note about matplotlib
# There are many different ways to visualize data in Python but they virtually all rely on matplotlib. You should spend some time reading through the tutorial: 
# 
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html. 
# 
# Because many other libraries use matplotlib under the hood, you should familiarize yourself with the basics. For example: 

# In[1]:


import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,20]
plt.scatter(x, y)
plt.title('title')
plt.ylabel('some numbers')
plt.xlabel('x-axis label')
plt.show()


# ## Seaborn makes things easier

# In[2]:


# import seaborn
import seaborn as sns

# import data
penguins = pd.read_csv("data/penguins.csv")

species = penguins['species']

# make a bar graph of bill_length_mm by bill_depth_mm
sns.scatterplot(data = penguins,
                x = 'bill_length_mm', 
                y = 'bill_depth_mm', 
                hue = 'species')

