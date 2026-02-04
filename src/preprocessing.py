import pandas as pd
from pathlib import Path

processed_data_path = Path("data/processed")

def preprocess_prf_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza o pré-processamento dos dados de acidentes da PRF.
    
    - Trata valores ausentes
    - Converte tipos de dados
    - Salva uma cópia dos dados processados em data/processed
    - Retorna o DataFrame processado

    """

    df = df.copy()

    # Retirei colunas redundantes e/ou que eu não considero relevantes para a análise.
    df = df.drop(columns=[
        'id','horario', 'km', 'municipio', 'causa_principal','causa_acidente',
        'ordem_tipo_acidente','sentido_via','ilesos', 'tipo_pista' ,'feridos_leves',
        'feridos_graves', 'classificacao_acidente','latitude', 'longitude', 'regional',
        'delegacia', 'uop', 'id_veiculo', 'data_inversa', 'pesid' ])

    # Renomeação de colunas para facilitar o entendimento. Ajustes baseados no dicionário de dados.
    df['uso_solo'] = df['uso_solo'].replace({'Sim': 'Urbano', 'Não': 'Rural'})

    #Remover os valores nulos da coluna br
    df.dropna(subset=['br'], inplace=True)

    #Os valores nulos são preenchidos com a mediana da respectiva coluna.
    for col in ['ano_fabricacao_veiculo', 'idade']:
        df[col] = df[col].fillna(df[col].median())

    # Os valores nulos são preenchidos usando o método (forward fill)
    for col in ['tipo_veiculo', 'sexo', 'mortos', 'estado_fisico']:
        df[col] = df[col].ffill()

    # Preenche os valores vazios com a moda de cada coluna
    for col in ['tipo_envolvido']:
        # Calculate mode and fill NaN, handling potential multiple modes by taking the first one
        mode_value = df[col].mode()[0] if not df[col].mode().empty else None
        if mode_value is not None:
            df[col] = df[col].fillna(mode_value)
    # Os valores de idade e de ano-fabricação-veículo estavam com valores irreais (idade registrada 2000) ou com outliers. Criação de um filtro para contornar esse problema.
    df = df[(df['idade'] > 10) & (df['idade'] <= 70)]
    df = df[df['ano_fabricacao_veiculo'] >= 1995]

    return df

def save_processed_data(df: pd.DataFrame, filename: str = "acidentes_prf_processed.csv"):
    """
    Salva o DataFrame processado em data/processed.
    """
    processed_data_path.mkdir(parents=True, exist_ok=True)
    output_path = processed_data_path / filename
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    df = pd.read_csv("data/raw/acidentes_prf_raw.csv")
    df = preprocess_prf_data(df)
    save_processed_data(df)