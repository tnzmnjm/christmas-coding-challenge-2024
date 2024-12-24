
import re
from pathlib import Path
import subprocess
from loguru import logger

"""
Utility module for working with Git repositories in Python scripts.
Provides functions to determine the root of the current Git repository
and to handle decisions related to repository processing tasks.
"""


def git_codebase_root():
    """
    Determine the root directory of the current Git repository.

    Uses the `git rev-parse --show-toplevel` command to find the root directory.

    Returns:
        pathlib.Path: The path to the top-level directory of the current Git
        repository.

        None: If the current directory is not within a Git repository.
    """

    try:
        root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], stderr=subprocess.DEVNULL
        )
        return Path(root.decode().strip())
    except subprocess.CalledProcessError:
        logger.warning("Not inside a Git repository.")
        return None


def get_working_directory_or_git_root():
    """
    Obtain the Git repository root or the current working directory.

    This is a wrapper function that calls `git_codebase_root()` and falls back
    to the current working directory if the former returns None, indicating
    that the current directory is not a Git repository.

    Returns:
        pathlib.Path: The top-level directory of the Git repository if inside a
        Git repo, otherwise the current working directory.
    """
    git_root = git_codebase_root()
    return git_root if git_root is not None else Path.cwd()



root_dir = get_working_directory_or_git_root()
logger.info(f'Root directory is: {root_dir}')

# Reading the short story (text file )in Python.
with open(root_dir/'data/the-verdict.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()
    logger.info(f" Total number of characters: {len(raw_text)}")
    # Printing the first 100 characters of this file
    print(raw_text[:99])

# output:
# Total number of characters: 20479
# I HAD always thought Jack Gisburn rather a cheap genius--though a good
# fellow enough--so it was no

# Our goal is to tokenise this 20,479-character short story into individual
# words and special characters that we can then turn into embeddings for LLM
# training.

# How can we best split this text to obtain a list of tokens? For this,
# we go on a small excursion and use Python’s `regular expression` library
# `re` for illustration purposes.

text = 'Hello, world. This is a test.'
result = re.split(r'\s', text)
print(result)
# The result is a list of individual words, whitespaces, and punctuation
# characters: ['Hello,', 'world.', 'This', 'is', 'a', 'test.']

# Some words are still connected to punctuation characters that we want to
# have as separate list entries. We also refrain from making all text
# lowercase because capitalisation helps LLMs distinguish between proper
# nouns and common nouns, understand sentence structure, and learn to
# generate text with proper capitalisation.

# Let’s modify the regular expression splits on whitespaces `(\s)`, `commas`,
# and periods `([,.])`:

result = re.split(r'([,.]|\s)', text)
print(result)
# ['Hello', ',', '', ' ', 'world', '.', '', ' ', 'This', ' ', 'is', ' ', 'a',
# ' ', 'test', '.', '']

# Optionally, we can remove the whitespaces
result = [item for item in result if item.strip()]
print(result)

# Note  When developing a simple tokeniser, whether we should encode
# whitespaces as separate characters or just remove them depends on our
# application and its requirements. Removing whitespaces reduces the memory
# and computing requirements. However, keeping whitespaces can be useful for
# example, Python code, which is sensitive to indentation and spacing.

# Including more special characters
text = "Hello, world. Is this-- a test?"
result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
result = [item for item in result if item.strip()]
print(result)
# ['Hello', ',', 'world', '.', 'Is', 'this', '--', 'a', 'test', '?']

# Now go back to the docs/chapter_notes/chapter2/notes.md !

# Let’s apply our basic tokeniser to Edith Wharton’s entire short story:
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item for item in preprocessed if item.strip()]
logger.info(f"Number of tokens in the short story(without whitespaces):"
            f" {len(preprocessed)}")

# Printing the first 30 tokens:
print(preprocessed[:30])
# ['I', 'HAD', 'always', 'thought', 'Jack', 'Gisburn', 'rather', 'a',
# 'cheap', 'genius', '--', 'though', 'a', 'good', 'fellow', 'enough', '--',
# 'so', 'it', 'was', 'no', 'great', 'surprise', 'to', 'me', 'to', 'hear',
# 'that', ',', 'in']


