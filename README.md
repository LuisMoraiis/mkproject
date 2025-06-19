# mkproject 📁🧪

Ferramenta CLI para criar estrutura base de projetos Data Science.

## Instalação

### Recomendado instalar atravez do pipx:

```bash
brew install pipx
pipx ensurepath
# Reinicie seu terminal após esse comando
pipx install ~/path/mkproject
```

## Uso

```bash
mkproject nome-do-projeto
```

## Estrutura

```bash
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
    ├── exploracao.py              # Página de análise exploratória
    └── modelagem.py               # Página de visualização/modelagem
```
