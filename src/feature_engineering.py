import pandas as pd
from pathlib import Path

features_data_path = Path("data/features")

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza a engenharia de features nos dados de acidentes da PRF.
    
    - Separa variáveis numéricas e categóricas
    - Aplica One-Hot Encoding nas variáveis categóricas
    - Retorna o DataFrame com as features preparadas para modelagem

    """

    df = df.copy()


    features = ['tipo_veiculo', 'dia_semana','fase_dia', 'condicao_metereologica','tipo_envolvido', 'uso_solo','sexo','idade', 'tipo_acidente','ano_fabricacao_veiculo', 'uf', 'mortos']

    return df[features] 

def save_features_data(df: pd.DataFrame, filename: str = "acidentes_prf_features.csv"):
    """
    Salva o DataFrame com features em data/features.
    """
    features_data_path.mkdir(parents=True, exist_ok=True)
    output_path = features_data_path / filename
    df.to_csv(output_path, index=False)

if __name__ == "__main__":

    df = pd.read_csv("data/processed/acidentes_prf_processed.csv")
    df_features = create_features(df)
    save_features_data(df_features)
    print(f"Features criadas e salvas com sucesso. Total de registros: {len(df_features)}")