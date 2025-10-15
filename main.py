"""
SOPRO - Sistema de Projetos
Agente especialista em geração de projetos para democratizar ideias e potencializar impacto
"""

import os
import sys
from pathlib import Path

# Adicionar diretório raiz ao path
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

def main():
    """Função principal da aplicação SOPRO"""

    print("🌬️ SOPRO - Sistema de Projetos")
    print("Democratizar o processo, multiplicar as ideias, potencializar o impacto")
    print("=" * 70)

    # Verificar se estamos no ambiente correto
    try:
        # Importar e executar a interface principal
        from src.ui.main_interface import main as run_interface

        print("🚀 Iniciando interface web...")
        run_interface()

    except ImportError as e:
        print(f"❌ Erro ao importar módulos: {e}")
        print("Verifique se todas as dependências foram instaladas:")
        print("pip install -r requirements.txt")
        return

    except Exception as e:
        print(f"❌ Erro ao executar aplicação: {e}")
        return

def setup_environment():
    """Configurar ambiente da aplicação"""

    # Carregar variáveis de ambiente
    from dotenv import load_dotenv
    load_dotenv()

    # Verificar dependências críticas
    required_env_vars = ['OPENAI_API_KEY']
    missing_vars = []

    for var in required_env_vars:
        if not os.getenv(var):
            missing_vars.append(var)

    if missing_vars:
        print("⚠️ Variáveis de ambiente necessárias não encontradas:")
        for var in missing_vars:
            print(f"   - {var}")
        print("Configure essas variáveis no arquivo .env")
        return False

    # Verificar arquivos necessários
    required_files = [
        'Perguntas direcionadoras - SOPRO.pdf',
        'tap-modelo.pdf',
        'sopro-redondo.png',
        'logo_mt.jpg'
    ]

    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)

    if missing_files:
        print("⚠️ Arquivos necessários não encontrados:")
        for file in missing_files:
            print(f"   - {file}")
        print("Verifique se todos os arquivos estão no diretório raiz")
        return False

    return True

if __name__ == "__main__":
    # Configurar ambiente
    if not setup_environment():
        print("❌ Configuração incompleta. Abortando execução.")
        sys.exit(1)

    # Executar aplicação
    main()