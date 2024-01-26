import pickle
import pandas as pd
import json

def predict_mpg(config):
    # Loading the model from the saved file
    pkl_filename = "model.pkl"
    with open(pkl_filename, 'rb') as f_in:
        loaded_data = pickle.load(f_in)

    # Access the preprocessor and model from the loaded dictionary
    loaded_preprocessor = loaded_data['preprocessor']
    loaded_model = loaded_data['model']

    if type(config) == dict:
        df = pd.DataFrame([config])
        df = loaded_preprocessor.transform(df)
        # print(df)  # Use transform instead of fit_transform
    else:
        df = config

    y_pred = loaded_model.predict(df)
    #y_pred_list = y_pred.tolist()

    #print(y_pred_list)
    #return y_pred_list
    return str(y_pred)
    

# Example usage:
# config = ...  # your input data
# result = predict_mpg(config)
