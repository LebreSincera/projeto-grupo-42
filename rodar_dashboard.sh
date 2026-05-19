#!/bin/bash
echo "============================================"
echo "  BMW Sales Dashboard - Grupo 42"
echo "============================================"
echo ""

# Verifica se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python nao encontrado. Instale em https://www.python.org"
    exit 1
fi

# Cria o ambiente virtual se não existir
if [ ! -d ".venv" ]; then
    echo "[1/3] Criando ambiente virtual..."
    python3 -m venv .venv
else
    echo "[1/3] Ambiente virtual ja existe."
fi

# Ativa o ambiente virtual
echo "[2/3] Ativando ambiente virtual..."
source .venv/bin/activate

# Instala as dependências
echo "[3/3] Instalando dependencias..."
pip install -r Project_Files/requirements.txt --quiet

# Roda o dashboard
echo ""
echo "Abrindo o dashboard no navegador..."
echo "Para encerrar, pressione CTRL+C"
echo ""
streamlit run Project_Files/app/dashboard.py
