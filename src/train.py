import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline # Importante para SMOTE

def train_model(df: pd.DataFrame):
    """
    Treina o modelo RandomForest com Over Sampling (SMOTE).
    """
    #Definição da variável target
    target = 'mortos'
    
    #Separando features e target
    y = df[target]
    X = df.drop(columns=[target])

    features_numericas = ['idade', 'ano_fabricacao_veiculo']
    features_categoricas = [
        'tipo_veiculo', 'dia_semana', 'fase_dia', 'condicao_metereologica',
        'tipo_envolvido', 'uso_solo', 'sexo', 'tipo_acidente', 'uf'
    ]

    #Divisão treino/teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Preprocessamento dentro do Pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", features_numericas),
            ("cat", OneHotEncoder(handle_unknown="ignore", drop="first"), features_categoricas)
        ]
    )

    #Criação do Pipeline com SMOTE e RandomForest
    # Usando o ImbPipeline da imblearn para que o SMOTE seja aplicado apenas no treino
    model = ImbPipeline(steps=[
        ("preprocessor", preprocessor),
        ("smote", SMOTE(random_state=42)),
        ("classifier", RandomForestClassifier(random_state=42, n_jobs=-1))
    ])

    #Treinamento
    model.fit(X_train, y_train)

    return model, X_test, y_test

if __name__ == "__main__":
    df = pd.read_csv("data/processed/acidentes_prf_processed.csv")
    
    model, X_test, y_test = train_model(df)
    
    joblib.dump(model, "models/modelo_acidentes_prf.pkl")

    X_test.to_csv("data/features/X_test.csv", index=False)
    y_test.to_csv("data/features/y_test.csv", index=False)



