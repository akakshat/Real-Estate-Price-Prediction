import json
import pickle

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

# this function will load the saved artifacts
def load_saved_artifacts():
    print("loading saved artifacts...start")
    # Creating global variables
    global __locations
    global __data_columns

    with open("./artifacts/columns.json" , 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    #  since it is a binary model it is rb
    with open("./artifacts/banglore_house_data_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
