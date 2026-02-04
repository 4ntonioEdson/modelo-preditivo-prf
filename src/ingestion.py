import pandas as pd
from pathlib import Path

raw_data_path = Path("data/raw")

def ingest_prf_data(file_path:str) -> pd.DataFrame:
    """
    Realiza a ingestão dos dados de acidentes da PRF.
    
    - Lê o arquivo CSV original
    - Salva uma cópia dos dados brutos em data/raw
    - Retorna o DataFrame carregado

    """

    raw_data_path.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(file_path, sep=";", encoding="latin1")

    output_path = raw_data_path / "acidentes_prf_raw.csv"
    df.to_csv(output_path, index=False)

    return df

if __name__ == "__main__":
    df_prf = ingest_prf_data("datasets/acidentes_prf.csv")
    print(f"Dados PRF ingeridos com sucesso. Total de registros: {len(df_prf)}")