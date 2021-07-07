# Import TF libraries
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model

# You can investigate how to implement these tools into your NN
from tensorflow.keras.layers import Dropout
from tensorflow.keras.optimizers import SGD

# Importing previous code for testing purposes
from part2 import load_dict
from part3 import bag_of_words_category


"""
The variable kind is used to refer to the learning model we want to obtain

kind = [category, password, conference, security, network, hardware]
(0) The model that determines the category. (1-5) The model that determines the
response for each category
"""

def create_model(x, y, kind):
    """
    Given an input array x and an output array y, create a Sequential Neural 
    Network and return it. Save it as kind.h5
    """
    model = Sequential()
    
    ##########################################
    ##########################################
    # Here build the architecture of your NN #
    ##########################################
    ##########################################
    
    ############ Compile your NN #############
    
    ############## Fit your NN ###############
           
    # Save the NN model at kind.h5
    model.save(f'{kind}.h5')
    print('Model succesfully created.')
    
    # Return the model
    return model

def get_model(x, y, kind):
    """
    Return the NN model for given 'kind'. Try to open it, or create it if not 
    found.
    """
    # Try to load model at kind.h5
    try:
        model = load_model(f'{kind}.h5')
    # Create it if not found
    except:
        model = create_model(x, y, kind)
    
    # Return the model
    return model


############################################################################
####### Uncomment these lines when you are ready to test your model ########
############################################################################
# Remember to have previous code saved to be able to import the functions ##
############################################################################
# data, docs_x, docs_y = load_dict('intents.json')
# cv_cat, train_x_cat, train_y_cat = bag_of_words_category(docs_x)
# model_cat = get_model(train_x_cat, train_y_cat, 'category')


