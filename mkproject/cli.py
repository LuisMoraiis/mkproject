import os
import subprocess
import sys
import click

@click.command()
@click.argument('nome_do_projeto')
def cli(nome_do_projeto):
    """Cria estrutura base de um projeto Streamlit com ambiente virtual .env"""
    estrutura = [
        f"{nome_do_projeto}/data/raw",
        f"{nome_do_projeto}/data/processed",
        f"{nome_do_projeto}/analysis",
        f"{nome_do_projeto}/models",
        f"{nome_do_projeto}/utils",
        f"{nome_do_projeto}/pages",
    ]

    arquivos = {
        f"{nome_do_projeto}/app.py": 'import streamlit as st\n\nst.title("Meu Projeto Streamlit 🎯")',
        f"{nome_do_projeto}/requirements.txt": "streamlit\npandas\nmatplotlib\nscikit-learn",
        f"{nome_do_projeto}/analysis/__init__.py": "",
        f"{nome_do_projeto}/analysis/pre_processamento.py": "# Funções de pré-processamento de dados\n",
        f"{nome_do_projeto}/analysis/estatisticas.py": "# Estatísticas descritivas\n",
        f"{nome_do_projeto}/models/__init__.py": "# Inicializador de modelos\n",
        f"{nome_do_projeto}/utils/helpers.py": "# Funções auxiliares\n",
        f"{nome_do_projeto}/pages/1_Exploracao.py": 'import streamlit as st\n\nst.title("🔍 Análise Exploratória")',
        f"{nome_do_projeto}/pages/2_Modelagem.py": 'import streamlit as st\n\nst.title("🤖 Modelagem de Dados")',
    }

    for path in estrutura:
        os.makedirs(path, exist_ok=True)

    for path, content in arquivos.items():
        with open(path, "w") as f:
            f.write(content)

    # Criação do ambiente virtual como .env
    env_path = os.path.join(nome_do_projeto, ".env")
    click.echo(f"🔧 Criando ambiente virtual em '{env_path}'...")
    subprocess.run([sys.executable, "-m", "venv", env_path])

    click.echo(f"\n✅ Projeto '{nome_do_projeto}' criado com sucesso!")
