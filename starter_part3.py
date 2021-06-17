from sklearn.feature_extraction.text import CountVectorizer


def bag_of_words_category(docs_x):
    """
    Create a bag of words representation for all queries, maps EVERY query to
    its CATEGORY (0 for password, 1 for conference, ...). 
    """
    # Initialize training lists
    train_x = []
    train_y = []
    
    # Populate your input and output training lists
    # train_x = list containing ALL queries
    # train_y = list containing the category number of each query in train_x

    # Initialize Vectorizer
    cv_x = CountVectorizer()
    
    # Fit and transform input list to its vectorized representation
    # Convert output list to a numpy array
    
    
    # Return the x vectorizer and the training lists
    return cv_x, train_x, train_y

def bag_of_words_response(docs_x, docs_y, index):
    """
    Create a bag of words representation for all queries in category given by
    index, maps every query in that category to its tag.
    """
    # Obtain all unique tags in given category
    tags = sorted(set(docs_y[index]))
    
    # Initialize training lists
    train_x = []
    train_y = []
    
    # Populate your input and output training lists
    # train_x = list containing all queries in category given by index
    # train_y = list containing the respective tag for each query in train_x
    
    # Initialize Vectorizer
    cv_x = CountVectorizer()
    
    # Fit and transform input list to its vectorized representation
    # Convert output list to a numpy array
    
    
    # Return the x vectorizer, the training lists, and the tags
    return cv_x, train_x, train_y, tags