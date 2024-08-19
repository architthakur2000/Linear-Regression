# import the necessary packages to the file. 

import pandas as pd
from sklearn.datasets import fetch_california_housing

def load_housing_data():

    # create a variable to store the dataset stored in the object returned by the fetch function. 
    housing_data = fetch_california_housing() 

    # Convert the data to pandas dataframe. 
    housing_df = pd.DataFrame(housing_data.data, columns=housing_data.feature_names)

    # Set the target of the housing data set to the medianHouse column of the Dataframe
    housing_df['MedHouseVal'] = housing_data.target

    return housing_df







