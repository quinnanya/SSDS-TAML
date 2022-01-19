#!/usr/bin/env python
# coding: utf-8

# # Jan 19 - text preprocessing basics

# ![text](img/text.png)

# 
# * Remove punctuation and special characters/symbols
# * Remove stop words
# * Stem or lemmatize: convert all non-base words to their base form 

# In[1]:


from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from string import punctuation
import pandas as pd
import seaborn as sns
from collections import Counter
import regex as re


# In[2]:


# ensure you have the proper nltk modules
import nltk
nltk.download('words')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')


# In[3]:


text = open("data/dracula.txt").read()

# print just the first 100 characters
print(text[:100])


# ## Remove punctuation
# 
# Remember that Python methods can be chained together. 
# 
# Below, a standard for loop loops through the `punctuation` module to replace any of these characters with nothing 
# 
# `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`

# In[4]:


for char in punctuation:
    text = text.lower().replace(char, "")


# In[5]:


print(text[:100])


# ### Tokenize the text
# 
# Split each word on spaces.

# In[6]:


tokens = text.split()


# In[7]:


print(tokens[:20])


# ### Remove stop words
# 
# 
# 
# Below is a list comprehension (a sort of shortcut for loop) that can accomplish this task for us.

# In[8]:


filtered_text = [word for word in tokens if word not in stopwords.words('english')]


# In[9]:


# show only the first 100 words
print(filtered_text[:100])


# ### Lemmatize
# 
# Examples include: 
# * Plural to singular (corpora to corpus)
# * Condition (better to good)
# * Gerund (running to run)

# In[10]:


lmtzr = nltk.WordNetLemmatizer()


# In[11]:


token_lemma = [ lmtzr.lemmatize(token) for token in filtered_text ]


# ### Part of speech tags

# In[12]:


tagged = nltk.pos_tag(token_lemma)


# In[13]:


chunked = nltk.chunk.ne_chunk(tagged)


# ### Wrangle your text into a dataframe

# In[14]:


df = pd.DataFrame(chunked, columns=['word', 'pos'])


# In[15]:


df.head()


# In[16]:


df.shape


# ### Visualize the 20 most frequent words

# In[17]:


top = df.copy()

count_words = Counter(top['word'])
count_words.most_common()[:20]


# In[18]:


words_df = pd.DataFrame(count_words.items(), columns=['word', 'count']).sort_values(by = 'count', ascending=False)


# In[19]:


words_df[:20]


# In[20]:


top_plot = sns.barplot(x = 'word', y = 'count', data = words_df[:20])
top_plot.set_xticklabels(top_plot.get_xticklabels(),rotation = 40);


# ![redwood](img/redwood.png)

# ## Quiz: Redwood webscraping
# 
# This also works with data scraped from the web. Below is very brief BeautifulSoup example to save the contents of the Sequoioideae (redwood trees) Wikipedia page to a variable named `text`. 
# 
# 1. Read through the code below
# 2. Practice by repeating for a webpage of your choice
# 3. Combine methods on this page to produce a ready-to-be analyzed copy of "Frankenstein.txt". This file is located in the `/data` folder

# In[21]:


# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
import nltk


# ### Three variables will get you started
# 
# 1. `url` - define the URL to be scraped 
# 2. `response` - perform the get request on the URL 
# 3. `soup` - create the soup object so we can parse the html 

# In[22]:


url = "https://en.wikipedia.org/wiki/Sequoioideae"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html')


# ### Parse the text
# 
# HTML (hypertext markup language) is used to structure a webpage and the content it contains - including text.
# 
# Below is a handy for loop that finds all everything within paragraph `<p>` tags. 

# In[23]:


text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text


# In[24]:


print(text)


# ### Remove extraneous elements
# 
# Remember how we did preprocessing the long way above? 

# In[25]:


text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = re.sub(r'\d',' ',text)
text = re.sub(r'[^\w\s]','',text)
text = text.lower()


# In[26]:


print(text)

