## 2/7 Applications of LLMs
As long as `paesing` and `generating tesxt` is involved, LLms can automate them

Some applications are:
- machine translation
- sentiment analysis
- text summarisation
- content creating(writing fiction)
- retrieve from vast volume of text in specialised areas like medicine and law
- augment traditional search engines
- power sophisticated chatbots and virtual assistants, such as OpenAI’s 
  ChatGPT or Google’s Gemini


## 3/7 Stages of building and using LLMs

### Why should we build our own LLMs? 
- excellent exercise to understand its mechanics and limitations
- equips us with the required knowledge for pretraining or fine-tuning 
  existing open source LLM architectures to our own domain-specific datasets 
  or tasks.


Custom-built LLMs—those tailored for specific tasks or domains—can 
outperform general-purpose LLMs, such as those provided by ChatGPT, which 
are designed for a wide array of applications (like BloombergGPT--> 
(specialised for finance) and LLMs tailored for medical question answering. 

Some advantages of having a custom-built LLM:
- from the data privacy aspect you can fine-tune an LLM on your data and 
  avoid sharing your data with a third-party providing the LLM 
- developing smaller custom LLMs enables the direct deployment on  customer 
  devices(laptops of phones) - Local deployment --> reduces latency and 
  server related costs
- grand developers complete autonomy(controlling updates, model modifications)


### General process of creating an LLM
- `pretraining` -->  a model like an LLM is trained on a large, diverse 
  dataset to develop a broad understanding of language --> `base` or 
  `foundation model`. Example: GPT-3 model. This model can do `text 
  completion`+ has limited `few-shot` capability (it can learn to perform 
  new tasks based on only a few examples instead of needing extensive 
  training data.)
- `fine-tuning` --> This pretrained model then serves as a foundational 
  resource that can be further refined through fine-tuning, a process where 
  the model is specifically trained on a narrower dataset that is more 
  specific to particular tasks or domains. 

  <img src="/docs/images/pretraining_and_finetuning.png">

Pretraining an LLM involves next-word prediction on large text datasets (raw 
text). A pretrained LLM can then be fine-tuned using a smaller labeled dataset.

**Important note**: LLMs use self-supervised learning, where the model 
generates its own labels from the input data.

The two most popular categories of fine-tuning LLMs are:
- `instruction fine-tuning` -->  the **labeled dataset** consists of 
  instruction and answer pairs, such as a query to translate a text 
  accompanied by the correctly translated text. 
- `classification fine-tuning` --> the labeled dataset consists of 
  texts and associated class labels—for example, emails associated with 
  “spam” and “not spam” labels.  