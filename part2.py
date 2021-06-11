from part1 import create_dict
import json
import nltk
import string

punctuation = string.punctuation  # Retrieve all punctuation symbols from string library
stopwords = nltk.corpus.stopwords.words('english')  # Retrieve stopwords from nltk library

stemmer = nltk.stem.lancaster.LancasterStemmer()  # Initialize the stemmer (Lancaster)


def clean_text(text):
    """
    Given a text, return its clean version (i.e., lowercase, remove punctuation
    & stopwords, tokenize, stem words).
    """
    tokens = nltk.word_tokenize(text.lower())  # Tokenize lowercase query
    new_text = ''  # Initialize empty string
    
    # Iterate over each token in query
    for token in tokens:
        # Filter out punctuation symbols and stopwords
        if not(token in punctuation or token in stopwords):
            stemmed_token = stemmer.stem(token)  # Stem each token
            new_text += stemmed_token + ' '  # Append to string
    
    return new_text.strip()  # Return clean version, removing trailing space


def load_dict(filename):
    """
    Given a json filename, open it and save to a dictionary. Return input-output
    data structures.
    """
    master = create_dict(filename)  # Load dictionary

    docs_x = []  # Initialize empty list
    docs_y = []  # Initialize empty list
    
    # Iterate over each category
    for category in master['intents']:
        x = []  # Initalize empty list for inputs in category
        y = []  # Initalize empty list for outputs in category
        
        # Iterate over each intent in category
        for intent in master['intents'][category]: 
            # For each query
            for query in intent['queries']:
                # Filter out empty queries
                if not query:
                    continue
                clean = clean_text(query)  # Clean query
                x.append(clean)  # Append input (query)
                y.append(intent['tag'])  # Append output (tag)
        
        docs_x.append(x)  # Append input list for category
        docs_y.append(y)  # Append output list for category
    
    return master, docs_x, docs_y