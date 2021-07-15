import numpy as np
from part2 import load_dict, clean_text
from part3 import bag_of_words_category, bag_of_words_response
from part4 import get_model

CATEGORIES = ['password', 'conference', 'security', 'network', 'hardware']
N_OF_CATEGORIES = len(CATEGORIES)


def determine(query, model, cv):
    """
    Given a query, transform it to its vectorized form  using a CountVectorizer
    and then predict its output using a TF's Sequential model.
    
    Establish a certainty threshold (0.0 - 1.0).
    
    Return the index of the prediction if it reaches the threshold, else return
    None.
    """
    predictions = model.predict(cv.transform([query]).toarray())
    predicted_index = np.argmax(predictions)
    certainty = predictions.max(1)[0]
    print(f'Report 1: {predicted_index} at {certainty*100}% of certainty.')
    
    if certainty < 0.80:
        return None
    else:
        return predicted_index


def main():
    # Load your dictionary and corpus using part2's function
    data, docs_x, docs_y = load_dict('intents.json')
    
    # Use part3 to retrieve all your categories-general components
    cv_cat, train_x_cat, train_y_cat = bag_of_words_category(docs_x)
    
    # Use part4 to obtain the categories-general model
    model_cat = get_model(train_x_cat, train_y_cat, 'category')
    
    # In the holder variable, store the category-specific components
    holder = [("category 0 components"), ("category 1 components"), 
              ("category 2 components"), ("category 3 components"), 
              ("category 4 components")]
    for i in range(N_OF_CATEGORIES):
        cv, train_x, train_y, tags = bag_of_words_response(docs_x, docs_y, i)
        model = get_model(train_x, train_y, CATEGORIES[i]) 
        holder[i] = (model, cv)
    
    
    # This is the main while loop where all the user-bot interaction takes place
    while True:
        # Take an input
        query = input('You: ')
        # Use part2's function to clean the query
        clean_query = None
        
        # Check for quitting option
        if query.lower() == 'quit':
            break
        
        # Determine the index of the category (pass the clean query and the 
        # categories-general components)
        index = determine(clean_query, model_cat, cv_cat)
        
        # If index is None (i.e. it didn't reach certainty threshold) print
        # a custom error message and skip
        if index is None:
            pass
        
        # Determine the tag of the answer (pass the clean query and the 
        # category-specific components)
        tag = determine(clean_query, holder[index][0], holder[index][1])
        
        # If tag is None (i.e. it didn't reach certainty threshold) print
        # a custom error message and skip
        if tag is None:
            pass
        # Else, print the predicted answer (access to it in data dictionary)
        else:
            # Be aware that some queries are different than others, be sure to
            # handle all possible cases
            answer = None  # Locate the answer in data using the predicted index and tag
            print(answer)
        
main()