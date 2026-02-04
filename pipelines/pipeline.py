import pandas as pd

from src.ingestion import ingest_prf_data
from src.preprocessing import preprocess_prf_data, save_processed_data
from src.feature_engineering import create_features, save_features_data
from src.train import train_model
import joblib


def run_pipeline():
    print("Iniciando pipeline de dados...")

    # 1. Ingestão
    df_raw = ingest_prf_data("datasets/acidentes_prf.csv")
    print("Ingestão concluída")

    # 2. Preprocessamento
    df_processed = preprocess_prf_data(df_raw)
    save_processed_data(df_processed)
    print("Preprocessamento concluído")

    # 3. Feature Engineering
    df_features = create_features(df_processed)
    save_features_data(df_features)
    print("Feature engineering concluído")

    # 4. Treinamento
    model, X_test, y_test = train_model(df_features)
    joblib.dump(model, "models/modelo_acidentes_prf.pkl")
    print("Modelo treinado e salvo")

    print("Pipeline finalizado com sucesso!")


if __name__ == "__main__":
    run_pipeline()
