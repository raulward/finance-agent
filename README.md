# Finance Agent 💰

Um agente de inteligência artificial especializado em análise financeira e gestão de dados financeiros. Desenvolvido com Python 3.13+, FastAPI e LangChain para oferecer análises inteligentes, recomendações em tempo real e integração com dados de mercado.

## 🚀 Demonstração em Produção

O projeto está disponível para demonstração:

- **URL**: https://finance-agent-production-3c0e.up.railway.app/
- **Disponibilidade**: Ativo por 30 dias a partir de hoje
- **Status**: ![Status](https://img.shields.io/badge/Status-Online-green)

## 📋 Sobre o Projeto

Finance Agent é um agente inteligente de análise financeira que combina:
- **IA Generativa**: Integração com OpenAI para análise conversacional
- **Orquestração de Fluxos**: LangGraph para workflows complexos
- **Dados de Mercado**: Integração com yfinance para dados em tempo real
- **API RESTful**: Endpoints bem estruturados para fácil consumo

### Características Principais

- 📊 **Análise Inteligente**: Processamento avançado de dados financeiros usando IA
- 🔗 **API RESTful**: Interface limpa e documentada automaticamente
- 🏗️ **Arquitetura Escalável**: Preparada para produção com Docker
- 📈 **Dados em Tempo Real**: Integração com APIs de mercado
- 🔒 **Seguro**: Validação de dados com Pydantic, variáveis de ambiente protegidas
- 🐳 **Containerizado**: Dockerfile incluído para deploy fácil

## 🛠️ Stack Tecnológico

| Componente | Tecnologia | Versão |
|-----------|-----------|--------|
| **Linguagem** | Python | 3.13+ |
| **Framework Web** | FastAPI | 0.128.2+ |
| **Servidor** | Uvicorn | 0.40.0+ |
| **Gerenciador de Deps** | Poetry | - |
| **Validação** | Pydantic | 2.12.5+ |
| **IA/ML** | LangChain + LangGraph | 1.2.8+, 1.0.8+ |
| **OpenAI** | OpenAI Python SDK | 2.17.0+ |
| **Dados Financeiros** | yfinance | 1.1.0+ |
| **Análise de Dados** | Pandas, NumPy | 3.0.0+, 2.4.2+ |
| **Linting** | Ruff | 0.15.0+ |

## 📦 Instalação e Execução

### Opção 1: Desenvolvimento Local com Poetry

#### Pré-requisitos
- **Python 3.13+** instalado
- **Poetry 2.0.0+** instalado
- **Git** para clonar o repositório
- Conta **OpenAI** com API key

#### Passo 1: Clonar o Repositório
```bash
git clone https://github.com/raulward/finance-agent.git
cd finance-agent
```

#### Passo 2: Instalar Dependências
```bash
poetry install
```

Para instalar apenas as dependências de produção (sem ferramentas de desenvolvimento):
```bash
poetry install --without dev
```

#### Passo 3: Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env  # se existir
```

ou crie manualmente:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
SEACH_API_KEY=your_openai_api_key_here

# Application Settings
PYTHONUNBUFFERED=1
ENV=development
```

#### Passo 4: Executar a Aplicação
```bash
poetry run uvicorn app.main:app --reload
```

**Acesso:**
- 🌐 API: http://localhost:8000
- 📖 Documentação Swagger: http://localhost:8000/docs
- 📋 Documentação ReDoc: http://localhost:8000/redoc

---

### Opção 2: Execução com Docker (Recomendado para Produção)

#### Pré-requisitos
- **Docker** instalado
- **Docker Compose** (opcional, mas recomendado)

#### Construir a Imagem
```bash
docker build -t finance-agent:latest .
```

#### Executar o Container
```bash
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_openai_api_key_here \
  finance-agent:latest
```

#### Ou usando Docker Compose (se disponível)
```bash
docker-compose up
```

**Acesso:**
- 🌐 API: http://localhost:8000
- 📖 Documentação: http://localhost:8000/docs

---

## 🔧 Configuração Avançada

### Variáveis de Ambiente

| Variável | Descrição | Exemplo | Obrigatória |
|----------|-----------|---------|------------|
| `OPENAI_API_KEY` | Chave da API OpenAI | `sk-...` | ✅ Sim |
| `PYTHONUNBUFFERED` | Output sem buffer | `1` | ❌ Não |
| `ENV` | Ambiente da aplicação | `development` ou `production` | ❌ Não |

### Desenvolvimento com Poetry

**Ativar o ambiente virtual:**
```bash
poetry shell
```

**Instalar pacote em desenvolvimento:**
```bash
poetry add novo-pacote
poetry add novo-pacote --group dev  # apenas para desenvolvimento
```

**Executar comandos dentro do ambiente Poetry:**
```bash
poetry run python seu_script.py
```

## 📡 API - Endpoints Principais

### Health Check
```bash
curl http://localhost:8000/
```

**Resposta:**
```json
{
  "message": "ok"
}
```

### Análise de Ações (Exemplo)
Consulte a documentação interativa em `/docs` para explorar todos os endpoints disponíveis.

## 📝 Estrutura do Projeto

```
finance-agent/
├── app/                           # Código-fonte principal
│   ├── main.py                   # Aplicação FastAPI
│   ├── api/
│   │   └── v1/
│   │       └── stock.py          # Endpoints de análise de ações
│   ├── ai/                        # Lógica de IA e LLM
│   │   ├── prompts/              # Prompts do sistema
│   │   └── structured_outputs/   # Definições de outputs estruturados
│   ├── services/                  # Serviços de negócio
│   │   ├── openai_service.py     # Integração com OpenAI
│   │   ├── finance.py            # Lógica financeira
│   │   └── news.py               # Serviço de notícias
│   ├── schemas/                   # Modelos Pydantic
│   │   └── stock.py
│   └── core/
│       └── config.py              # Configurações da aplicação
│
├── pyproject.toml                 # Configuração Poetry
├── poetry.lock                    # Lock file de dependências
├── Dockerfile                     # Configuração Docker
├── .env.example                   # Template de variáveis de ambiente
└── README.md                      # Este arquivo
```

## 🧪 Testes e Linting

### Executar Linting
```bash
poetry run ruff check .
poetry run ruff format .
```

### Estrutura de Linting
- **Ruff** para linting e formatação
- Configurado para padrão de linha 88 caracteres (Black)
- Verifica: PEP 8 (E), Pyflakes (F), Isort (I)

## 🚀 Deployment

### Deploy no Railway.app

O projeto está configurado para deploy automático no Railway.app com Docker.

#### Prerequisitos:
- Conta no [Railway.app](https://railway.app)
- Railway CLI instalado

#### Passos:
```bash
# Fazer login no Railway
railway login

# Inicializar projeto (se primeira vez)
railway init

# Deploy
railway up
```

#### Configuração de Variáveis de Ambiente no Railway:
1. Vá para o projeto no Railway Dashboard
2. Abra a aba "Variables"
3. Adicione: `OPENAI_API_KEY=seu_valor`


## 📚 Documentação da API

A documentação interativa está disponível em:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Explore os endpoints, veja os schemas e teste diretamente da documentação.

## 🛠️ Desenvolvimento

### Adicionar Nova Dependência
```bash
poetry add novo-pacote
```

### Remover Dependência
```bash
poetry remove pacote
```

### Atualizar Todas as Dependências
```bash
poetry update
```

### Executar Aplicação em Modo Debug
```bash
poetry run uvicorn app.main:app --reload --log-level debug
```

## 📋 Dependências Principais

- **fastapi**: Framework web moderno e rápido
- **uvicorn**: Servidor ASGI de alta performance
- **pydantic**: Validação de dados e parsing
- **langchain**: Framework para aplicações LLM
- **openai**: Cliente SDK oficial OpenAI
- **yfinance**: Dados de mercado financeiro
- **pandas**: Análise e manipulação de dados
- **numpy**: Computação numérica

## ⚠️ Notas Importantes

1. **Chave OpenAI**: Mantenha sua `OPENAI_API_KEY` segura. Use variáveis de ambiente, nunca commite no repositório.

2. **Disponibilidade de Produção**: Este projeto está em produção por tempo limitado (30 dias). Para uso prolongado, considere fazer um fork ou clonar localmente.

3. **Custos**: Tenha cuidado com custos da API OpenAI durante testes. Configure limites se necessário.

4. **Rate Limiting**: A API de dados financeiros pode ter limites de requisições. Implemente cache se necessário.

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Faça commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📧 Suporte e Contato

- **Autor**: Raul Ward
- **Email**: raulwarddev@gmail.com
- **Repository**: https://github.com/raulward/finance-agent


## 🔄 Changelog

### v0.1.0 (Atual)
- ✅ Inicialização do projeto
- ✅ Integração com OpenAI API
- ✅ Endpoints de análise de ações
- ✅ Docker e deployment no Railway
- ✅ Documentação automática com FastAPI

---

**Última atualização**: Fevereiro de 2026  
**Status da Produção**: ✅ Online  
**Python**: 3.13+  
**Gerenciador**: Poetry
