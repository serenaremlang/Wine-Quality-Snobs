def red_model(user_input_array):
    import pickle
    import xgboost as xgb
    # from sklearn.preprocessing import StandardScaler
    import numpy as np
    #Load Model
    with open('red_model.pkl', 'rb') as file:
        red_model = pickle.load(file)
    with open('scaler_red.pkl', 'rb') as file:
        scaler = pickle.load(file)

    X = user_input_array.reshape(1,-1)
    X_scaled = scaler.transform(X)

    # Calculate Wine quality
    y_pred_red = red_model.predict(X_scaled)

    return y_pred_red