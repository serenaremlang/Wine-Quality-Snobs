def white_model(user_input_array):
    import pickle
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    import numpy as np
    #Load Model
    with open('white_model.pkl', 'rb') as file:
        white_model = pickle.load(file)
    with open('scaler_white.pkl', 'rb') as file:
        scaler = pickle.load(file)

    X = user_input_array.reshape(1,-1)
    X_scaled = scaler.transform(X)

    # Calculate Wine quality
    y_pred_white = white_model.predict(X_scaled)

    return y_pred_white