
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

# Let’s apply our basic tokeniser to Edith Wharton’s entire short story:
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item for item in preprocessed if item.strip()]
logger.info(f"Number of tokens in the short story(without whitespaces):"
            f" {len(preprocessed)}")


# Let’s create a list of all unique tokens and sort them alphabetically to
# determine the vocabulary size
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
logger.info(f'vocab_size: {vocab_size}')

# We create the vocabulary and print its first 51 entries for illustration
# purposes.
vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break

# As we can see, the dictionary contains individual tokens associated with 
# unique integer labels.