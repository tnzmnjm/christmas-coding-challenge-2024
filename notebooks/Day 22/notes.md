# Notes and Resources on Large Language Models

This file includes notes and images related to building large language models. 

> **Acknowledgment**: The majority of the notes and images are adapted from the book 
> ["Build A Large Language Model (From Scratch)"](https://www.manning.com/books/build-a-large-language-model-from-scratch) 
> by Sebastian Raschka (ISBN 978-1633437166). 

Some additional notes and annotations have been added by me to expand on specific concepts or provide further clarity.


## 5/7 Utilising  large datasets
The large training dataset for popular GPT- and BERT-like models cover a 
vast array of topics. See below table summarising the dataset used for 
pretraining GPT-3 which served as the base model for the first version of 
ChatGPT.

<img src="/docs/images/GPT-3_pretraining_dataset.jpg">

Number of `tokens` --> is a unit of text that a model reads and the number 
of tokens in a dataset is roughly equivalent to the number of words and 
punctuation characters in the text.

- GPT-3 was trained not on all the tokens (499 Billion) but on 300 Billion. 
  They did not share the dataset. A comparable dataset that is publicly 
  available is Dolma: An Open Corpus of Three Trillion Tokens for LLM 
  Pretraining Research by Soldaini et al. 2024 (https://arxiv.org/abs/2402.00159)
- CommonCrawl requires 570 GB of storage
- the GPT-3 pretraining cost is estimated to be $4.6 million in terms of 
  cloud computing credits (https://mng.bz/VxEW).
- Good news: many pretrained LLMs, available as open source models, can be 
  used as general-purpose tools to write, extract, and edit texts that were 
  not part of the training data. Also, LLMs can be `fine-tuned` on specific 
  tasks with relatively smaller datasets, reducing the computational 
  resources needed and improving performance.

## 6/7 A closer look at the GPT architecture

- GPT was originally introduced in the paper “Improving Language Understanding 
by Generative Pre-Training” (https://mng.bz/x2qg) by Radford et al. from OpenAI.
- GPT-3 is a scaled-up version of this model that has more parameters and 
  was trained on a larger dataset.
- the original model offered in `ChatGPT` was created by `fine-tuning` 
  `GPT-3` on a large `instruction dataset` using a method from OpenAI’s 
  `InstructGPT` paper (https://arxiv.org/abs/2203.02155). 
- GPT models are pretrained on a relatively simple `next-word prediction` 
  task.
- In the `next-word` prediction pretraining task for GPT models, the system 
  learns to predict the upcoming word in a sentence by looking at the words 
  that have come before it. This approach helps the model understand how 
  words and phrases typically fit together in language, forming a foundation 
  that can be applied to various other tasks.

<img src="/docs/images/img_1.png">

`Next-word prediction` task is a form of `self-supervised` learning --> a 
form of `self-labeling`.

This means that we don’t need to collect labels for the training data 
explicitly but can use the structure of the data itself -->  we can use the 
next word in a sentence or document as the label that the model is supposed 
to predict. Since this next-word prediction task allows us to create labels 
“on the fly,” it is possible to use massive unlabeled text datasets to train 
LLMs.

Since decoder-style models like GPT generate text by predicting text one 
word at a time, they are considered a type of `autoregressive` model -->
`Autoregressive models` incorporate their `previous outputs` as `inputs` for 
future predictions --> Consequently, in GPT, each new word is chosen based 
on the sequence that precedes it, which improves the coherence of the 
resulting text.

- Architectures such as GPT-3 are also significantly larger than the 
  original transformer model.
- the original transformer repeated the encoder and decoder blocks six times.
- `GPT-3` has `96 transformer layers` and `175 billion parameters` in total.

`GPT architecture` is designed for `unidirectional`, `left-to-right` processing, 
making it well suited for text generation and next-word prediction tasks to 
generate text in an iterative fashion, one word at a time.

<img src="/docs/images/GPT_architecture.png">

`Emergent Behavior` --> The ability to perform tasks that the model wasn’t 
explicitly trained to perform --> GPT models were trained primarily on a 
next-word prediction task but have the translation tasks as well.

## 7/7 Building a large language model
We will take the fundamental idea behind GPT as a blueprint and tackle this 
in three stages:
1. implementing the LLM architecture and data preparation process (stage 1) 
   --> data preprocessing steps and code the attention mechanism 
2. pretraining an LLM to create a foundation model (stage 2) --> code and 
   pretrain a GPT-like LLM capable of generating new texts, evaluating LLMs, 
   loading openly available model weights.
3. fine-tuning the foundation model to become a personal assistant or text 
   classifier (stage 3) --> fine-tune it to follow instructions or 
   classifying texts

<img src="/docs/images/3_stages.png">


## Summary
- LLMs have transformed the field of natural language processing, which  
  previously mostly relied on explicit rule-based systems and simpler 
  statistical methods. The advent of LLMs introduced new deep 
  learning-driven approaches that led to advancements in understanding, 
  generating, and translating human language.
- Modern LLMs are trained in two main steps:
  - First, they are pretrained on a large corpus of unlabeled text by using the 
    prediction of the next word in a sentence as a label.
  - Then, they are fine-tuned on a smaller, labeled target dataset to follow 
    instructions or perform classification tasks.
- LLMs are based on the transformer architecture. The key idea of the 
  transformer architecture is an attention mechanism that gives the LLM 
  selective access to the whole input sequence when generating the output 
  one word at a time.
  - The original transformer architecture consists of an encoder for parsing 
  text and a decoder for generating text.
  - LLMs for generating text and following instructions, such as GPT-3 and  
    ChatGPT, only implement decoder modules, simplifying the architecture.
  - Large datasets consisting of billions of words are essential for 
    pretraining LLMs.
  - While the general pretraining task for GPT-like models is to predict the 
    next word in a sentence, these LLMs exhibit emergent properties, such as 
    capabilities to classify, translate, or summarise texts.
  - Once an LLM is pretrained, the resulting foundation model can be 
    fine-tuned more efficiently for various downstream tasks.
  - LLMs fine-tuned on custom datasets can outperform general LLMs on 
    specific tasks.
