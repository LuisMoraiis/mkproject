# mkproject 🚀

Ferramenta CLI para criar estrutura base de projetos Data Science.

## Instalação

```bash
pip install -e .

## Instalação

```bash
mkproject nome-do-projeto

## Estrutura

meu_projeto/
├── app.py                            # Interface principal com Streamlit
├── requirements.txt                  # Dependências
│
├── data/
│   ├── raw/                          # 📥 Dados brutos (originais, sem tratamento)
│   └── processed/                    # 📊 Dados prontos para análise/modelagem
│
├── analysis/
│   ├── __init__.py
│   ├── pre_processamento.py         # Limpeza e transformação de dados
│   └── estatisticas.py              # Estatísticas descritivas e sumarizações
│
├── models/
│   └── __init__.py                  # Diretório pronto para receber modelos
│
├── utils/
│   └── helpers.py                   # Funções auxiliares (ex: formatação, gráficos)
│
└── pages/
    ├── 1_Exploracao.py              # Página de análise exploratória
    └── 2_Modelagem.py               # Página de visualização/modelagem
