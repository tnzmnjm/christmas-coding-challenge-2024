### 2/8 Tokenising text

Split input text into individual tokens. These tokens can be individual 
words, or special characters, including punctuation characters.

<img src="/docs/images/text_tokenization.png" alt="A view of the text 
processing steps in the context of an LLM. Here, we split an input text into individual tokens, which are either words or special characters, such as punctuation characters.">

The text we will tokenize for LLM training is `“The Verdict,”` a short story 
by Edith Wharton, which has been released into the public domain and is thus 
permitted to be used for LLM training tasks. The file is in 
`data/the-verdict.txt` in the repository.

Please now continue by following `chapter_2.py`.

Our tokenization scheme can now handle the various special characters in the 
text successfully.

<img src="/docs/images/simple_tokeniser_scheme.png">

The tokenization scheme we implemented so far splits text into individual 
words and punctuation characters. In this specific example, the sample text 
gets split into 10 individual tokens.

Now that we have a basic tokenizer working, let’s apply it to Edith 
Wharton’s entire short story. Please go back to `chapter_2.py`.