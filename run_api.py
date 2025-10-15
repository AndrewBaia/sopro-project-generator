#!/usr/bin/env python3
"""
Script de execução da API SOPRO
"""

import os
import sys
import uvicorn
from pathlib import Path

def main():
    """Executar API SOPRO"""

    print("🌬️ SOPRO API Backend")
    print("FastAPI server para integração com frontend Next.js")
    print("=" * 60)

    # Verificar se estamos no ambiente correto
    if not Path("src/api/main.py").exists():
        print("❌ Execute este script do diretório raiz do projeto SOPRO")
        sys.exit(1)

    # Adicionar diretório raiz ao path
    root_dir = Path(__file__).parent
    sys.path.insert(0, str(root_dir))

    print("🚀 Iniciando servidor FastAPI...")
    print("📡 API disponível em: http://localhost:8000")
    print("📖 Documentação: http://localhost:8000/docs")
    print("🔄 Health check: http://localhost:8000/health")
    print("")
    print("Para parar o servidor, pressione Ctrl+C")
    print("=" * 60)

    # Executar FastAPI
    uvicorn.run(
        "src.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()