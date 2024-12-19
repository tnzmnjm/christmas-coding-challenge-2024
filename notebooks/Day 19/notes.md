# Chapter 1: Understanding large language models
    * High-level explanations of the fundamental concepts behind large language models (LLMs)
    * Insights into the transformer architecture from which LLMs are derived
    * A plan for building an LLM from scratch

- LLMs are deep neural network models
- before the advent of the LLMs, traditional methods excelled at categorisation tasks( like email spam classification) and straightforward pattern recognition that could be captured with handcrafted rules or simpler models

What traditional methods couldn't do --> underperformed tasks that demanded complex understanding <sup>1</sup> and generating abilities like:
-   parsing detailed instructions
-   conducting contextual analysis
-   create coherent and contextually appropriate original text

Advancements in deep learning --> LLMs capture deeper contextual information and subtleties of human language compared to previous approaches --> LLMs have significantly improved performance in a wide range of NLP tasks, including text translation, sentiment analysis, question answering, and many more.

Earlier NLP models is that earlier NLP models were typically designed for specific tasks, such as text categorisation, language translation, LLMs demonstrate a broader proficiency across a wide range of NLP tasks.

Success behind the LLMs can be attributed to --> transformer architecture allowing them to capture a wide variety of linguistic nuances, contexts, and patterns that would be challenging to encode manually.

## 1/7 What is an LLM?
- an LLM is a deep neural network designed to understand, generate, and respond to human-like text. 
- trained on massive amounts of text data, sometimes encompassing large portions of the entire publicly available text on the internet.
- The “large” in “large language model” refers to both :
  - the model’s size in terms of parameters 
  - the immense dataset on which it’s trained. 
- Models like this often have tens or even hundreds of billions of parameters, which are the adjustable weights in the network that are optimised during training to predict the next word in a sequence. 

Next-word prediction is sensible because it harnesses the inherent sequential nature of language to train models on understanding context, structure, and relationships within text. Yet, it is a very simple task, and so it is surprising to many researchers that it can produce such capable models.

LLMs utilise an architecture called the `transformer`, which allows them to pay selective attention to different parts of the input when making predictions, making them especially adept at handling the nuances and complexities of human language.

Since LLMs are capable of generating text, LLMs are also often referred to as a form of generative artificial intelligence, often abbreviated as `generative AI` or `GenAI`.

<img src="/docs/images/1-1.png" alt="This image illustrates the  hierarchical depiction of the relationship between the different fields suggests, LLMs represent a specific application of deep learning techniques, using their ability to process and generate human-like text. `Deep learning` is a specialised branch of machine learning that focuses on using `multilayer neural networks`. Machine learning and deep learning are fields aimed at implementing algorithms that enable computers to learn from data and perform tasks that typically require human intelligence.">

This image illustrates the  hierarchical depiction of the relationship between the different fields suggests, LLMs represent a specific application of deep learning techniques, using their ability to process and generate human-like text. `Deep learning` is a specialised branch of machine learning that focuses on using `multilayer neural networks`. Machine learning and deep learning are fields aimed at implementing algorithms that enable computers to learn from data and perform tasks that typically require human intelligence.

In contrast to deep learning, traditional machine learning requires manual feature extraction. This means that human experts need to identify and select the most relevant features for the model.
Both traditional machine learning and deep learning for spam classification still require the collection of labels, such as spam or non-spam, which need to be gathered either by an expert or users.




-------------
1. they can process and generate text in ways that appear coherent and contextually relevant, not that they possess human-like consciousness or comprehension.