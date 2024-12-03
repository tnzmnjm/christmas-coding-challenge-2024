# christmas-coding-challenge-2024
<img src="docs/images/Christmas_Coding_Challenge_2024.png">

This project was developed within the framework of the Christmas Coding Challenge 2024, organised by Women Coding Community.

I am taking on this challenge as part of the book [Build a Large Language
Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch) 
to create, train, and fine-tune large language models (LLMs), I’m focused 
on building my PyTorch skills, and this challenge presents a perfect 
opportunity to learn it in a structured and disciplined way. My goal is to 
make consistent progress by committing to this repository daily.

# Appendix A : [Introduction to PyTorch](https://livebook.manning.com/book/build-a-large-language-model-from-scratch/appendix-a/)

### Tensors 

Tensors are multi-dimensional data containers that generalise vectors
and matrices, serving as a fundamental building block in libraries like PyTorch 
for efficient computation and manipulation of data in deep learning models. 

PyTorch is an open source Python-based deep learning library.

### The three core components of PyTorch
<img src= "docs/images/The three core components of PyTorch.png">

PyTorch’s three main components include a tensor library as a fundamental 
building block for computing, automatic differentiation for model 
optimisation, and deep learning utility functions, making it easier to 
implement and train deep neural network models.

First, PyTorch is a tensor library that extends the concept of the 
array-oriented programming library NumPy with the additional feature that 
accelerates computation on GPUs, thus providing a seamless switch between 
CPUs and GPUs. (A tensor library, such as PyTorch, is a computational tool 
that efficiently creates, manipulates, and computes with multi-dimensional 
arrays, serving as a fundamental building block for deep learning by 
supporting GPU computations and automatic differentiation.)

Second, PyTorch is an automatic differentiation engine, also known as 
autograd, that enables the automatic computation of gradients for tensor 
operations, simplifying backpropagation and model optimisation.(Autograd:
Autograd in PyTorch is an automatic differentiation engine that simplifies 
model optimisation by automatically computing gradients for tensor 
operations, facilitating backpropagation without the need for manual 
gradient derivation.) (Gradient: A gradient is a vector containing all the 
partial derivatives of a multivariate function, which is essential for 
training neural networks as it provides the information needed to update 
model parameters to minimise the loss function using methods like gradient 
descent) 

Finally, PyTorch is a deep learning library. It offers modular, flexible, 
and efficient building blocks, including pretrained models, loss functions, 
and optimisers, for designing and training a wide range of deep learning 
models, catering to both researchers and developers.

### Defining deep learning
Deep learning is a subcategory of machine learning that focuses on the 
training and application of deep neural networks. These deep neural 
networks were originally inspired by how the human brain works, 
particularly the interconnection between many neurons. The “deep” in 
deep learning refers to the multiple hidden layers of artificial neurons or
nodes that allow them to model complex, nonlinear relationships in the data.
Unlike traditional machine learning techniques that excel at simple pattern
recognition, deep learning is particularly good at handling unstructured 
data like images, audio, or text, so it is particularly well suited for 
LLMs.

Checking the Python and pip version (Update them if required):
```
python --version
pip --version
pip install --upgrade pip
```
installing Pytorch : 
```
pip3 install torch torchvision torchaudio
```
### PyTorch and Torch
The Python library is named PyTorch primarily because it’s a continuation of the 
Torch library but adapted for Python (hence, “PyTorch”). “Torch” acknowledges 
the library’s roots in Torch, a scientific computing framework with wide 
support for machine learning algorithms, which was initially created using the
Lua programming language.
