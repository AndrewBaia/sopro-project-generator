# 🌬️ SOPRO - Sistema de Projetos

**Democratizar o processo, multiplicar as ideias, potencializar o impacto**

SOPRO é um agente especialista em IA que ajuda pessoas leigas a transformarem suas ideias em projetos estruturados e profissionais. Utilizando tecnologia avançada de processamento de linguagem natural e um sistema de Retrieval-Augmented Generation (RAG), o SOPRO guia usuários através de um processo intuitivo de 8 etapas para criar projetos de impacto social.

## ✨ Características Principais

- 🤖 **Agente Especialista**: IA treinada especificamente para criação de projetos
- 📋 **Formulário Intuitivo**: Interface moderna com 8 etapas claras
- 💬 **Chatbot Integrado**: Assistente disponível a partir da segunda etapa
- 📄 **Geração de PDF**: Documentos profissionais baseados em modelos oficiais
- 🎨 **Design Moderno**: Tema em azul celeste e ciano para leveza
- 🔍 **Sistema RAG**: Baseado em documentação especializada em elaboração de projetos

## 🚀 Instalação e Execução

### Pré-requisitos

- **Backend**: Python 3.12+
- **Frontend**: Node.js 18+ e npm
- **APIs**: Conta OpenAI (para funcionalidades de IA), Conta Tavily (opcional, para pesquisa web)

### Instalação Completa

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd sopro-app
   ```

2. **Instale as dependências do backend**:
   ```bash
   pip install -e .
   ```

3. **Configure as variáveis de ambiente**:
   ```bash
   cp .env .env.local
   ```
   Edite o `.env.local`:
   ```env
   OPENAI_API_KEY=sua-chave-openai-aqui
   TAVILY_API_KEY=sua-chave-tavily-aqui
   ```

4. **Instale as dependências do frontend**:
   ```bash
   cd frontend
   npm install
   cd ..
   ```

### Execução da Aplicação

#### 🚀 Modo Fácil (Recomendado)

Execute o sistema completo automaticamente:

```bash
python start_sopro.py
```

Este comando irá:
- ✅ Verificar todos os requisitos
- ✅ Instalar dependências automaticamente
- ✅ Iniciar backend e frontend simultaneamente
- ✅ Aguardar serviços ficarem prontos
- ✅ Mostrar links de acesso

#### Modo Manual (Desenvolvimento Avançado)

Execute o backend e frontend separadamente:

**Terminal 1 - Backend API (Python/FastAPI):**
```bash
python run_api.py
```
- API disponível em: http://localhost:8000
- Documentação: http://localhost:8000/docs
- Health check: http://localhost:8000/health

**Terminal 2 - Frontend Next.js:**
```bash
cd frontend
npm run dev
```
- Aplicação disponível em: http://localhost:3000

#### Modo Produção

**Backend:**
```bash
python run_api.py
```

**Frontend:**
```bash
cd frontend
npm run build
npm start
```

### Scripts Disponíveis

- `python start_sopro.py` - **🏆 Sistema completo automático**
- `python run_api.py` - API FastAPI apenas
- `cd frontend && npm run dev` - Frontend Next.js apenas
- `cd frontend && npm run build` - Build de produção frontend
- `cd frontend && npm start` - Servidor produção frontend

### Verificação do Sistema

- ✅ **API Backend**: http://localhost:8000/health
- ✅ **API Docs**: http://localhost:8000/docs
- ✅ **Frontend**: http://localhost:3000
- ✅ **Build Status**: `cd frontend && npm run build`

## 📋 Estrutura do Formulário (8 Etapas)

### 1. Identificação
- Nome do Projeto
- Instituição/Entidade Responsável
- Local da Execução
- Período de Execução

### 2. Justificativa ⭐
**Etapa mais importante** - A IA armazena todas as informações para gerar respostas contextuais
- Qual problema o projeto busca resolver?
- O que tem causado esse problema?
- Há evidências desse problema?
- Quem são as pessoas/áreas atingidas?
- Por que é importante para a comunidade?
- Que impactos positivos são esperados?
- Relação com direitos difusos/coletivos?
- Conexão com ODS (Objetivos de Desenvolvimento Sustentável)

### 3. Objetivo Geral
- Descrição clara e objetiva do que o projeto busca alcançar
- **Botão IA**: Gera objetivo baseado na justificativa

### 4. Objetivos Específicos
- Metas mensuráveis e alcançáveis
- **Botão IA**: Gera objetivos específicos baseados no objetivo geral

### 5. Metodologia
- Estratégias e ações a serem desenvolvidas
- Cronograma de atividades
- Recursos necessários (Materiais, Humanos, Financeiros)
- **Botões IA**: Geração automática para cada seção

### 6. Resultados Esperados
- Resultados esperados a partir do contexto anterior
- Indicadores de sucesso
- **Botão IA**: Geração baseada em toda a metodologia

### 7. Orçamento
- Detalhamento dos custos
- Fontes de financiamento
- **Botões IA**: Sugestões automáticas

### 8. Fiscalização e Prestação de Contas
- Procedimentos para monitoramento e avaliação
- Cronograma de prestação de contas
- Indicadores de transparência e eficiência
- **Botões IA**: Geração baseada no projeto completo

## 💬 Chatbot Especialista

A partir da **segunda etapa**, um chatbot aparece no canto inferior direito da tela:

- 🎯 **Especialista Contextual**: Respostas baseadas no progresso do projeto
- 📚 **Baseado em RAG**: Utiliza documentação especializada
- 🤖 **IA Avançada**: Respostas inteligentes e personalizadas
- 💡 **Sugestões Automáticas**: Orientações específicas para cada etapa

## 🎨 Interface e Design

- **Tema**: Azul celeste (#00BFFF) e ciano (#00FFFF)
- **Animações**: Logo SOPRO animada na abertura
- **Header Fixo**: Logo permanece no canto superior esquerdo
- **Responsivo**: Funciona em desktop e mobile
- **Intuitivo**: Fluxo linear e claro para usuários leigos

## 📄 Geração de PDF

- **Modelo Baseado**: Utiliza `tap-modelo.pdf` como referência
- **Formatação Profissional**: Estrutura oficial de projetos
- **Dados Persistentes**: Mantém formatação adequada mesmo com texto informal
- **Download Automático**: Geração one-click

## 🛠️ Arquitetura Técnica

```
sopro-app/
├── src/                          # Backend Python
│   ├── agents/                   # Agentes especializados (AGNO)
│   │   └── project_consultant.py
│   ├── rag/                     # Sistema RAG
│   │   └── rag_processor.py
│   ├── api/                     # API FastAPI
│   │   └── main.py
│   └── utils/                   # Utilitários
│       └── pdf_generator.py
├── frontend/                     # Frontend Next.js
│   ├── src/
│   │   ├── app/                 # Next.js App Router
│   │   │   ├── layout.tsx       # Layout principal
│   │   │   ├── page.tsx         # Página principal
│   │   │   └── globals.css      # Estilos globais
│   │   ├── components/          # Componentes React
│   │   │   ├── Header.tsx       # Cabeçalho animado
│   │   │   ├── Footer.tsx       # Rodapé
│   │   │   ├── ProgressBar.tsx  # Barra de progresso
│   │   │   ├── StepCard.tsx     # Cards das etapas
│   │   │   └── Chatbot.tsx      # Chatbot popup
│   │   ├── lib/                 # Utilitários
│   │   │   └── api.ts           # Cliente API
│   │   └── types/               # TypeScript types
│   │       └── project.ts
│   ├── public/images/           # Imagens estáticas
│   ├── tailwind.config.ts       # Configuração Tailwind
│   └── package.json             # Dependências Node.js
├── main.py                      # Ponto de entrada (Streamlit - legado)
├── run_api.py                   # Script API FastAPI
├── run.py                       # Script Streamlit (legado)
├── pyproject.toml               # Dependências Python
├── .env                         # Configurações
└── README.md
```

## 🔧 Tecnologias Utilizadas

### Backend
- **Framework IA**: [Agno](https://github.com/agno-agi/agno)
- **API**: FastAPI (Python)
- **LLM**: OpenAI GPT-4 Turbo
- **RAG**: ChromaDB + Sentence Transformers
- **PDF**: ReportLab
- **Pesquisa**: Tavily API

### Frontend
- **Framework**: Next.js 15 (App Router)
- **Linguagem**: TypeScript
- **Styling**: Tailwind CSS
- **Animações**: Framer Motion
- **UI/UX**: Componentes React modernos
- **Tema**: Azul celeste (#00BFFF) e ciano (#00FFFF)

## 🚀 Executando em Produção

### Docker (Recomendado)

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install -e .
EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.address", "0.0.0.0"]
```

### Deploy na Nuvem

- **Streamlit Cloud**: Deploy direto do GitHub
- **Heroku**: Usar buildpack Python
- **Vercel**: Para versão web otimizada
- **Railway**: Deploy automático

## 📚 Documentação Técnica

### Configuração do Agente

O agente especialista utiliza múltiplos "sub-agentes" especializados:

- **Justification Agent**: Análise de problemas e justificativas
- **Objectives Agent**: Definição de objetivos claros
- **Methodology Agent**: Planejamento estratégico
- **Results Agent**: Avaliação de impacto
- **Budget Agent**: Planejamento financeiro
- **Monitoring Agent**: Transparência e accountability

### Sistema RAG

- **Fonte**: `Perguntas direcionadoras - SOPRO.pdf`
- **Vector DB**: ChromaDB
- **Embeddings**: OpenAI ou Sentence Transformers
- **Busca**: Similaridade semântica

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Equipe

- **Desenvolvimento**: SOPRO Team
- **Design**: Interface moderna e intuitiva
- **IA**: Agentes especializados treinados

## 📞 Suporte

Para dúvidas ou suporte:
- 📧 Email: suporte@sopro.com.br
- 💬 Chatbot integrado na aplicação
- 📖 Documentação: [Link da documentação]

---

**SOPRO** - Transformando ideias em projetos que transformam vidas! 🌟