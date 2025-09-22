from sklearn.linear_model import LogisticRegression
import joblib
from data import load_data, split_data

def fit_model(X_train, y_train):
    """
    Train a Logestic Regression model and save the model to a file.
    Args:
        X_train (numpy.ndarray): Training features.
        y_train (numpy.ndarray): Training target values.
    """
    log_reg = LogisticRegression(
        solver="lbfgs",             
        max_iter=5000,              
        random_state=12
    )
    log_reg.fit(X_train, y_train)
    joblib.dump(log_reg, "/Users/vishaknair/Downloads/MLOps-main/Labs/API_Labs/FastAPI_Labs/fastapi_lab1/model/wine_model1.pkl")

if __name__ == "__main__":
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    fit_model(X_train, y_train)
