from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import re


def execute(url, tag): # Main Method
    words = parse_url(url, tag) # Get words contained in the tag
    words = validate_words(words) # Validate the words using a regular expression
    result = count_words(words) # Analyze the frequency the repetition of the words
    return result


def parse_url(url, tag):
    content = load_url(url) # Download the content of the url
    soup = BeautifulSoup(content, 'html.parser') # Parse the containt

    words = [] # result

    for item_tag in soup.find_all(tag):
        temp = str(item_tag.text).split(' ') # Separate the words
        words.extend(temp) # Merge the lists
        item_tag.next_sibling

    return words


def load_url(url): # Download the content of the url
    r = requests.get(url)
    return r.text


def count_words(words):
    x = np.array(words)
    unique, counts = np.unique(x, return_counts=True) # Analyze the frequency the repetition of the words

    data = {'frecuency':counts}
    dataframe = pd.DataFrame(data, index = unique) # Create the DataFrame
    dataframe = dataframe.sort_values(by='frecuency', ascending=0) # Order by frecuency

    return dataframe


def validate_words(words): # Validate the words using a regular expression
    result_words = []

    for word in words:
        if validate_word(word):
            word = str(word).replace('\n', '')
            result_words.append(word)

    return result_words


def validate_word(word):# Validate the word using a regular expression
    pattern = re.compile('[a-zA-Z]')
    result = pattern.match(word) # Validate expresion
    if result:
        return True
    else:
        return False




