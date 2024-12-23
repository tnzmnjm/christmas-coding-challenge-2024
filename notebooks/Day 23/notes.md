# Notes and Resources on Large Language Models

This file includes notes and images related to building large language models. 

> **Acknowledgment**: The majority of the notes and images are adapted from 
> the book 
> ["Build A Large Language Model (From Scratch)"](https://www.manning.com/books/build-a-large-language-model-from-scratch) 
> by Sebastian Raschka (ISBN 978-1633437166). 

Some additional notes and annotations have been added by me to expand on 
specific concepts or provide further clarity.


# Chapter 2: Working with text data
This chapter covers:
- Preparing text for large language model training
- Splitting text into word and subword tokens
- Byte pair encoding as a more advanced way of tokenizing text
- Sampling training examples with a sliding window approach
- Converting tokens into vectors that feed into a large language model


During the pretraining stage, LLMs process text one word at a time. This 
chapter will focus on step 1 of the stage 1 --> implementing the data sample 
pipeline

### 1/8 Understanding word embeddings
`text is categorical` --> Deep neural network models, including LLMs, cannot 
process raw text directly as it isn’t compatible with the mathematical 
operations used to implement and train neural networks --> we need a way to 
`represent words as continuous-valued vectors`.

#### Embedding 
- converting data into a `vector` format. Embedding can be 
done using a specific neural network layer or another pretrained neural 
network model.
- is a mapping from discrete objects, such as words, images, or even entire 
  documents, to points in a continuous vector space
- he primary purpose of embeddings is to convert non-numeric data into a 
  format that neural networks can process.

Different data formats require distinct embedding models :

<img src="/docs/images/embedding_different_data_types.png" alt=" Deep learning models cannot process data formats like video, audio, and text in their raw form. Thus, we use an embedding model to transform this raw data into a dense vector representation that deep learning architectures can easily understand and process. Specifically, this figure illustrates the process of converting raw data into a three-dimensional numerical vector.">

There are:
- `word embeddings`
- `sentence embeddings` --> popular choice for `RAG`<sup>1</sup> (Retrieval-Augmented 
  Generation)
- `paragraph embeddings` --> popular choice for `RAG` 
- `whole document embeddings`

We will focus on `word embedding` as we'd like to generate text one word at a 
time.
Word embeddings can have varying dimensions, from one to thousands. A higher 
dimensionality might capture more nuanced relationships but at the cost of 
computational efficiency.

#### Algorithms and frameworks to generate word embeddings
`Word2Vec` --> is a pre-trained neural network architecture to generate 
word embeddings by `predicting the context of a word` given the target word or 
vice versa. The main idea behind `Word2Vec` is that words that appear in 
similar contexts tend to have similar meanings. Consequently, when projected 
into two-dimensional word embeddings for visualisation purposes, similar 
terms are clustered together.

<img src="/docs/images/embedding_different_data_types.png" alt="If word embeddings are two-dimensional, we can plot them in a two-dimensional scatterplot for visualization purposes as shown here. When using word embedding techniques, such as Word2Vec, words corresponding to similar concepts often appear close to each other in the embedding space. For instance, different types of birds appear closer to each other in the embedding space than in countries and cities.">

While pretrained models such as `Word2Vec` to generate embeddings for 
machine learning models can be used, LLMs commonly produce their own embeddings 
that are part of the `input layer` and are `updated during training`. The 
advantage of optimising the embeddings as part of the LLM training instead 
of using Word2Vec is that the embeddings are optimised to the specific task 
and data at hand.  LLMs can also create `contextualized output embeddings`, 
will be discussed in chapter 3.

Our sensory perception and common graphical representations are inherently 
limited to three dimensions or fewer. However, when working with LLMs, we 
typically use embeddings with a much higher dimensionality. For both `GPT-2` 
and `GPT-3`, the `embedding size` (often referred to as `the dimensionality of 
the model’s hidden states`) varies based on the specific model variant and 
size. It is a tradeoff between performance and efficiency. 

The smallest `GPT-2` models (`117M` and `125M` parameters) use an embedding 
size of `768 dimensions` to provide concrete examples. The largest `GPT-3` 
model (`175B parameters`) uses an embedding size of `12,288 dimensions`.

--------------------------------
1. Retrieval-augmented generation combines generation (like producing text) 
   with retrieval (like searching an external knowledge base) to pull 
   relevant information when generating text.
