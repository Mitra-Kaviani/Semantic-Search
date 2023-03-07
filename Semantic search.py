#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Importing libraries: 
from sentence_transformers import SentenceTransformer, util
import torch
import pandas as pd
import numpy as np
from scipy import spatial


#Load the pre-trained model:
model = SentenceTransformer('all-mpnet-base-v2')

#Functions to load the data set,process and print the most similar sentense and the score, it loads the dataset, processes it, and calculates the embeddings for each sentence:
def semantic_search(file):
    corpus=pd.read_excel('Questions.xlsx', sheet_name= 'Base')
    corpus=corpus.assign(embeddings=corpus['Question'].apply(lambda x: model.encode(x)))
    return corpus

# Define a function to find the top similar sentences:
def top_similar_question(text):
    data=semantic_search('Cyber Carrier Questions.xlsx')
    text_vector=model.encode(text)
    s=data['embeddings'].apply(lambda x: 1 - spatial.distance.cosine(x, text_vector) )
    data=data.assign(similarity=s)
    data=data.sort_values('similarity',ascending=False).head(3)
    data=data[["Carrier", "Question", "similarity"]]
    return(data)

# Run the function on a user input text:
x =input("Enter a question: " )
print(top_similar_question(x))

#Save the output to a CSV file:
top_similar_question(x).to_csv('output.csv')


# In[ ]:




