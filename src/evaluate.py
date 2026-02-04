import pandas as pd
import joblib

from sklearn.metrics import classification_report, confusion_matrix


def evaluate_model(model, X_test, y_test):
    """
    Avalia o modelo treinado utilizando o conjunto de teste.
    """
    y_pred = model.predict(X_test)

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))


if __name__ == "__main__":
    model = joblib.load("models/modelo_acidentes_prf.pkl")
    X_test = pd.read_csv("data/features/X_test.csv")
    y_test = pd.read_csv("data/features/y_test.csv")

    evaluate_model(model, X_test, y_test)
