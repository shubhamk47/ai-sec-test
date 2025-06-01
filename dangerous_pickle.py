import pickle

def load_data(user_data):
    return pickle.loads(user_data)  # ⚠️ Arbitrary Code Execution Risk
