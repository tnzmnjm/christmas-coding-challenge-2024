
## 4/7 Introducing the transformer architecture

A transformer is a deep neural network introduced in the 2017 paper 
"Attention Is All You Need"<sup>2</sup>.

The original transformer was developed for machine translation, translating 
English text to German and French.  

The transformer architecture consists of two submodules:
1. `encoder` -->  processes the input text and encodes it into a series of 
   numerical representations or vectors that capture the contextual 
   information of the input. 
2. `decoder` -->  takes these encoded vectors and generates the output text.

Example: In a translation task, for example, the encoder would encode the 
text from the source language into vectors, and the decoder would decode 
these vectors to generate text in the target language. 

<img src="/docs/images/simplified_original_transformer_architecture.png" alt="A simplified depiction of the original transformer architecture, which is a deep learning model for language translation. The transformer consists of two parts: (a) an encoder that processes the input text and produces an embedding representation (a numerical representation that captures many different factors in different dimensions) of the text that the (b) decoder can use to generate the translated text one word at a time. This figure shows the final stage of the translation process where the decoder has to generate only the final word (“Beispiel”), given the original input text (“This is an example”) and a partially translated sentence (“Das ist ein”), to complete the translation.">

**It would be better if there was an arrow starting from the "output layer" 
of the decoder to the "input text" of the decoder**

A simplified depiction of the original transformer architecture, which is a 
deep learning model for language translation. The transformer consists of 
two parts: 
(a) an encoder that processes the input text and produces an embedding 
representation:
  - a numerical representation that captures many different factors in 
different dimensions) of the text that the 
(b) decoder can use to generate the translated text one word at a time. 

This figure shows the final stage of the translation process where the 
decoder has to generate only the final word (“Beispiel”), given the original 
input text (“This is an example”) and a partially translated sentence (“Das 
ist ein”), to complete the translation.

Both the encoder and decoder consist of many layers connected by a so-called 
`self-attention mechanism`.

A key component of transformers and LLMs is the `self-attention` mechanism 
(not shown), which **allows the model to weigh the importance of different 
words or tokens in a sequence relative to each other**. This mechanism enables 
the model to **capture long-range dependencies and contextual relationships 
within the input data**, enhancing its ability to generate coherent and 
contextually relevant output.

Later variants of the transformer architecture, such as `BERT` (short for 
bidirectional encoder representations from transformers) and the various 
`GPT` models (short for generative pretrained transformers), built on this 
concept to adapt this architecture for different tasks.

`BERT`, which is built upon the original transformer’s `encoder` submodule, 
differs in its training approach from GPT. While GPT is designed for 
generative tasks, BERT and its variants specialise in `masked word prediction`,
where the model predicts masked or hidden words in a given sentence, as 
shown in figure below. This unique training strategy equips BERT with strengths 
in `text classification tasks`, including `sentiment prediction` and 
`document categorisation`. As an application of its capabilities, as of this 
writing, X (formerly Twitter) uses BERT to detect toxic content.

`GPT`, on the other hand, focuses on the `decoder` portion of the original 
transformer architecture and is designed for tasks that require `generating 
texts`. This includes `machine translation`, `text summarization`, `fiction 
writing`, `writing computer code`, and more.

<img src="/docs/images/transformers_encoder_decoder.png">

A visual representation of the transformer’s encoder and decoder submodules. 
On the left, the `encoder` segment exemplifies `BERT-like LLMs`, which focus 
on `masked word prediction` and are primarily used for tasks like `text 
classification`. On the right, the `decoder` segment showcases `GPT-like 
LLMs`, designed for `generative tasks` and `producing coherent text sequences`.

`Zero-shot learning`--> refers to the ability to generalise to completely 
unseen tasks without any prior specific examples. 
`Few-shot learning` --> involves learning from a minimal number of examples the 
user provides as input.

