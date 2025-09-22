import joblib

def predict_data(X):
    """
    Predict the class labels for the input data.
    Args:
        X (numpy.ndarray): Input data for which predictions are to be made.
    Returns:
        y_pred (numpy.ndarray): Predicted class labels.
    """
    model = joblib.load("/Users/vishaknair/Downloads/MLOps-main/Labs/API_Labs/FastAPI_Labs/fastapi_lab1/model/wine_model1.pkl")
    y_pred = model.predict(X)
    return y_pred
