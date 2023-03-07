# Semantic-Search
This code is designed to perform a semantic search on a set of questions and find the most similar questions to the input text. The code uses the Sentence Transformers library, which encodes sentences into a high-dimensional space and allows comparison of the semantic similarity between sentences.

# Loading the Data

The code reads the input data from an Excel file named "Questions.xlsx" in the same directory. The sheet named "Base" contains a list of questions and their corresponding company name. The semantic_search() function reads this file and processes the questions by encoding them using the Sentence Transformers model.

# Finding the Most Similar Questions

The top_similar_question() function takes an input question and finds the top three most similar questions from the dataset. It does this by encoding the input question using the same model and calculating the cosine similarity between the encoded vectors. The function then returns the carriers and questions with the highest similarity scores.

# Model

In the given code, 'all-mpnet-base-v2' is the name of the pre-trained transformer-based model that is used to encode the text data into dense vectors that capture the semantic meaning of the text. Specifically, it refers to the "Multi-lingual Pre-trained Neural network with a Transformer" (mBERT) model, which is a language model that was trained on a large corpus of text data from various languages. This model is provided by the "sentence-transformers" library and is one of the many pre-trained models that can be used for a variety of natural language processing tasks, such as semantic search, text classification, and sentence similarity scoring.

# Output

After running the code, the user is prompted to enter a question. The code then prints the top three most similar questions and their corresponding companies. The output is also saved to a CSV file named "output.csv".

# Cunclusion

Overall, this code is a simple but effective way to perform a semantic search on a dataset of questions and find the most relevant questions based on semantic similarity.
