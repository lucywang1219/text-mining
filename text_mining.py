"""
# Characterizing by Word Frequencies
# Computing Summary Statistics
Beyond simply calculating word frequencies there are some other ways to summarize the words in a text. For instance, what are the top 10 words in each text? What are the words that appear the most in each text that don't appear in other texts?
# Natural Language Processing
# Text Similarity
# Text Clustering
"""

import string
from mediawiki import MediaWiki

wikipedia = MediaWiki()
china_plan = wikipedia.page("Five-year plans of China")
f = china_plan.content

strippables = string.punctuation + string.whitespace
t = 'i am a student at Babson'

def process_file(): 
    f = f.split() 
    return f 

def hist_frequency():
    """Makes a histogram that contains the words"""
    hist = {}
    t = t.split() 
    
    # for word in f:
    #     word = word.replace('=', '')
    #     word = word.replace('-', ' ')
    #     word = word.strip(strippables)
    #     word = word.lower()

        # hist[word] = hist.get(word, 0) + 1
    return t


def main():
    print(process_file())
    print(hist_frequency())
    

if __name__ == "__main__":
    main()
