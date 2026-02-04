# Modelo Preditivo de Acidentes – PRF

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-green)
![Pipeline](https://img.shields.io/badge/Data%20Pipeline-Orchestrated-brightgreen)

## Visão Geral

Este projeto tem como objetivo desenvolver um pipeline de Machine Learning ponta a ponta para previsão de acidentes a partir de dados públicos da Polícia Rodoviária Federal (PRF).

O foco do projeto não é apenas o modelo, mas a arquitetura do pipeline, contemplando ingestão, processamento, feature engineering, treinamento, avaliação e orquestração — seguindo boas práticas utilizadas no mercado.

## Objetivo

Construir um pipeline modular e reprodutível que permita:

* Processar dados brutos de acidentes

* Criar features relevantes

* Treinar e avaliar modelos preditivos

* Facilitar futuras evoluções (cloud, Spark, Airflow, etc.)

## Diagrama do Pipeline

flowchart TD
    A[Dados Brutos PRF 2023] --> B[Ingestão<br/>src/ingestion.py]

    B --> C[Pré-processamento<br/>src/preprocessing.py]
    C --> D[Feature Engineering<br/>src/feature_engineering.py]

    D --> E[Treinamento<br/>src/train.py]
    E --> F[Avaliação<br/>src/evaluate.py]

    F --> G[Modelo Persistido<br/>models/modelo_acidentes_prf.pkl]

    subgraph Orquestração
        H[pipelines/pipeline.py]
    end

    H --> B
    H --> C
    H --> D
    H --> E
    H --> F

## Tecnologias Utilizadas

* Python

* Pandas

* Scikit-learn

* Imbalanced-learn

* Joblib

## Análise Exploratória

A análise exploratória dos dados (EDA) está disponível na pasta notebooks/.

Observação:
Os notebooks têm caráter exploratório e analítico.
O pipeline produtivo do projeto está implementado nos módulos em src/ e pipelines/.

## Modelagem

* Modelo: Random Forest Classifier

* Problema: classificação binária

* Base desbalanceada

* Oversampling aplicado somente no conjunto de treino

* Métricas avaliadas:

    * Precision

    * Recall

    * F1-score

    * Confusion Matrix


```
Accuracy: 0.98

Classe 1 (minoritária):
Precision: 0.92
Recall:    0.78
F1-score:  0.84

```

## Como Executar o Pipeline

1️⃣ Criar ambiente virtual
```
python -m venv venv

```

2️⃣ Ativar o ambiente

Windows:
```
venv\Scripts\activate

```
Linux/Mac:
```
source venv/bin/activate

```
3️⃣ Instalar dependências
```
pip install -r requirements.txt

```
4️⃣ Executar o pipeline completo
```
python -m pipelines.pipeline

```

## Possíveis Evoluções

* Inclusão de dados de múltiplos anos (Data Lake)

* Processamento distribuído com Spark

* Execução em cloud (AWS / GCP / Azure)

* Orquestração com Airflow ou Prefect

* Rastreamento de experimentos com MLflow

## Observação Final

Este projeto foi originalmente iniciado em notebook e evoluído para uma arquitetura modular e orquestrada, refletindo um fluxo de trabalho mais próximo do ambiente profissional.