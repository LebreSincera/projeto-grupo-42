@echo off
echo ============================================
echo   BMW Sales Dashboard - Grupo 42
echo ============================================
echo.

:: Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado. Instale em https://www.python.org
    pause
    exit /b
)

:: Cria o ambiente virtual se não existir
if not exist ".venv" (
    echo [1/3] Criando ambiente virtual...
    python -m venv .venv
) else (
    echo [1/3] Ambiente virtual ja existe.
)

:: Ativa o ambiente virtual
echo [2/3] Ativando ambiente virtual...
call .venv\Scripts\activate.bat

:: Instala as dependências
echo [3/3] Instalando dependencias...
pip install -r Project_Files\requirements.txt --quiet

:: Roda o dashboard
echo.
echo Abrindo o dashboard no navegador...
echo Para encerrar, feche esta janela ou pressione CTRL+C
echo.
streamlit run Project_Files\app\dashboard.py

pause
