
# JARVIS Acadêmico


### Autor: Daniel Garcia Amaral

Assistente inteligente para estudantes utilizando:

- RAG (Retrieval-Augmented Generation)
- Tool Calling
- LLM Gemma 3 12B Instruct
- Active Recall
- Geração de Exercícios
- Interface Gráfica com Gradio

---
# Sumário

- [Objetivo do Projeto](#objetivo-do-projeto)
- [Funcionalidades](#funcionalidades)
  - [1. Consulta a Materiais Acadêmicos (RAG)](#1-consulta-a-materiais-acadêmicos-rag)
  - [2. Agenda Acadêmica](#2-agenda-acadêmica)
  - [3. Lista de Tarefas](#3-lista-de-tarefas)
  - [4. Geração de Exercícios](#4-geração-de-exercícios)
  - [5. Active Recall (Interativo)](#5-active-recall-interativo)
  - [6. Identificação de Dificuldades](#6-identificação-de-dificuldades)
  - [7. Recomendação de Revisão](#7-recomendação-de-revisão)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
    - [Interface Gráfica com Gradio](#interface-gráfica-com-gradio)
- [Engenharia de Software](#engenharia-de-software)
  - [Organização modular](#organização-modular)
  - [Separação de responsabilidades](#separação-de-responsabilidades)
  - [Persistência](#persistência)
  - [Logs](#logs)
  - [Testes](#testes)
- [Conceitos utilizados](#conceitos-utilizados)
  - [RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation)
  - [Embeddings](#embeddings)
  - [Chunking](#chunking)
  - [Tool Calling](#tool-calling)
  - [Active Recall](#active-recall)
- [Dataset](#dataset)
  - [Origem dos Dados](#origem-dos-dados)
  - [Limitações](#limitações)
  - [Estratégia de Chunking](#estratégia-de-chunking)
- [Ferramentas Implementadas](#ferramentas-implementadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
  - [1. Clonar Repositório](#1-clonar-repositório)
  - [2. Entrar na Pasta](#2-entrar-na-pasta)
  - [3. Criar Ambiente Virtual](#3-criar-ambiente-virtual)
  - [4. Ativar Ambiente Virtual](#4-ativar-ambiente-virtual)
  - [5. Instalar Dependências](#5-instalar-dependências)
  - [6. Configurar Variáveis de Ambiente](#6-configurar-variáveis-de-ambiente)
  - [7. Indexar pdfs](#7-indexar-pdfs)
- [Executar o sistema](#executar-o-sistema)
  - [1. Executar no terminal](#1-executar-no-terminal)
  - [2. Interface](#2-interface)
- [Como Executar os Testes](#como-executar-os-testes)
- [Logs](#logs-1)
- [Estrutura dos bancos](#estrutura-dos-bancos)
  - [agenda.db](#agendadb)
  - [tasks.db](#tasksdb)
  - [performance.db](#performancedb)
- [Melhorias Futuras](#melhorias-futuras)
- [IAs Utilizadas no Desenvolvimento](#ias-utilizadas-no-desenvolvimento)
---

# Objetivo do Projeto

O objetivo deste projeto é desenvolver um assistente acadêmico inteligente capaz de auxiliar estudantes em:

- consulta a materiais de estudo;
- organização acadêmica;
- gerenciamento de tarefas;
- reforço do aprendizado;
- revisão ativa de conteúdos.

O sistema integra:
- recuperação de informações via RAG;
- chamadas de ferramentas (tool calling);
- modelo de linguagem Gemma 3 12B Instruct;
- mecanismos educacionais interativos.

---

# Funcionalidades

## 1. Consulta a Materiais Acadêmicos (RAG)

O usuário pode realizar perguntas sobre PDFs e materiais acadêmicos.

Exemplos:

- "Explique regressão logística"
- "O que são embeddings?"
- "O que é RAG?"

O sistema:
- carrega PDFs;
- realiza chunking;
- gera embeddings;
- armazena vetores no ChromaDB;
- recupera trechos relevantes;
- envia contexto para a LLM.

---

## 2. Agenda Acadêmica

Permite:
- adicionar eventos;
- listar compromissos;
- organizar atividades acadêmicas.

Exemplos:
- provas;
- aulas;
- seminários;
- apresentações.

---

## 3. Lista de Tarefas

Permite:
- adicionar tarefas;
- listar tarefas;
- concluir tarefas.

Exemplos:
- estudar conteúdo;
- fazer lista;
- revisar conteúdo.

---

## 4. Geração de Exercícios

O sistema consegue gerar exercícios automaticamente a partir do conteúdo armazenado no RAG.

Exemplo:

```text
Gere exercícios sobre embeddings
```

---

## 5. Active Recall (Interativo)

O sistema:

- gera perguntas;
- avalia respostas do usuário;
- identifica dificuldades.

Fluxo:

1. sistema faz pergunta;
2. usuário responde;
3. sistema avalia;
4. sistema registra desempenho.

---

## 6. Identificação de Dificuldades

O sistema analisa:

- notas;
- desempenho por tema.

E identifica:

- conteúdos com baixo desempenho;
- tópicos que precisam de revisão.

---

## 7. Recomendação de Revisão

Com base no desempenho do usuário, o sistema recomenda:

- temas para revisar;
- conteúdos prioritários.

---

# Arquitetura do Sistema

```
Usuário (Gradio)
        │
        ▼
Agent Controller
        │
 ┌──────┼──────────────┬───────────────┐
 ▼      ▼              ▼               ▼
RAG   Agenda       Tarefas       Aprendizado
 │       │              │               │
 ▼       ▼              ▼               ▼
Chroma SQLite       SQLite        SQLite
 │
 ▼
Embeddings
 │
 ▼
Gemma 3 12B Instruct
```

---

# Estrutura do Projeto
```
jarvis-academico/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   ├── pdfs/
│   ├── chroma/
│   ├── agenda.db
│   ├── tasks.db
│   └── performance.db
│
├── logs/
│   └── jarvis.log
│
├── src/
│   ├── llm/
│   │   └── client.py
│   │
│   ├── rag/
│   │   ├── chunking.py
│   │   ├── ingest.py
│   │   └── retriever.py
│   │
│   ├── database/
│   │   ├── agenda_db.py
│   │   ├── tasks_db.py
│   │   └── performance_db.py
│   │
│   ├── tools/
│   │   ├── rag_tools.py
│   │   ├── agenda_tools.py
│   │   ├── task_tools.py
│   │   ├── learning_tools.py
│   │   ├── active_recall.py
│   │   └── difficulty_tools.py
│   │
│   ├── agent/
│   │   ├── prompts.py
│   │   └── controller.py
│   │
│   └── utils/
│       ├── config.py
│       └── logger.py
│
└── tests/
    ├── test_rag.py
    ├── test_tasks.py
    ├── test_learning.py
    └── test_active_recall.py

```

---
# Tecnologias Utilizadas

| Tecnologia           | Função               |
| -------------------- | -------------------- |
| Python               | linguagem principal  |
| Gradio               | interface gráfica    |
| OpenAI SDK           | integração com Gemma |
| ChromaDB             | banco vetorial       |
| SentenceTransformers | embeddings           |
| SQLite               | persistência local   |
| PyPDF                | leitura de PDFs      |
| Pytest               | testes               |
| Logging              | rastreamento e debug |


## Interface Gráfica com Gradio

O sistema utiliza o framework Gradio para construção da interface gráfica web interativa.

O Gradio foi escolhido por:

- simplicidade de integração com modelos de IA;
- rápida prototipação;
- suporte nativo para aplicações com LLM;
- integração facilitada com Python;
- interface amigável para demonstração acadêmica.

A interface permite:

- interação com o assistente acadêmico;
- geração de perguntas de active recall;
- avaliação de respostas;
- visualização de dificuldades;
- recomendação de revisão.

Componentes principais utilizados:

| Componente Gradio | Função |
| ----------------- | ------ |
| Blocks            | estrutura principal da interface |
| Tab               | separação das funcionalidades |
| Chatbot           | chat principal do sistema |
| Textbox           | entrada e saída de texto |
| Button            | execução de ações |
| Markdown          | títulos e descrições |

Fluxo da interface:

1. usuário envia mensagem;
2. controller interpreta intenção;
3. ferramenta é acionada;
4. resultado retorna para interface.


# Engenharia de Software

O projeto foi estruturado seguindo princípios de organização e separação de responsabilidades.

## Organização modular

O sistema foi dividido em módulos independentes:
| Módulo   | Responsabilidade           |
| -------- | -------------------------- |
| rag      | recuperação de informações |
| llm      | comunicação com Gemma      |
| tools    | ferramentas do agente      |
| database | persistência               |
| agent    | controle do agente         |
| utils    | utilitários e logs         |

## Separação de responsabilidades

Cada camada possui responsabilidade específica:

- recuperação;
- geração;
- persistência;
- interface;
- controle do agente.

## Persistência

O sistema utiliza:

- SQLite para agenda, tarefas e desempenho;
- ChromaDB para embeddings.

## Logs

O sistema registra:

- chamadas de ferramentas;
- entradas;
- saídas;
- eventos importantes.

Logs ficam em:

```
logs/jarvis.log
```

## Testes

O sistema possui testes básicos utilizando Pytest.

Testes:

- chunking;
- tarefas;
- geração de exercícios;
- active recall.

---

# Conceitos utilizados

## RAG (Retrieval-Augmented Generation)

RAG combina:

- recuperação de documentos;
- geração de texto com LLM.

Fluxo:

- usuário faz pergunta;
- sistema recupera chunks relevantes;
- contexto é enviado para a LLM;
- resposta é gerada baseada no contexto.

## Embeddings

Embeddings são representações vetoriais de texto.

Eles permitem:

- busca semântica;
- comparação de similaridade;
- recuperação inteligente de conteúdo.

Modelo utilizado:
```
sentence-transformers/all-MiniLM-L6-v2
```

## Chunking

Os documentos são divididos em pequenos trechos chamados chunks.

Configuração utilizada:

```
chunk_size = 500
overlap = 100
```

O overlap foi utilizado para preservar continuidade semântica.

## Tool Calling

O agente utiliza tool calling para decidir qual ferramenta executar.

Exemplos:

- buscar material;
- listar tarefas;
- gerar exercícios.

A decisão é feita pela LLM.

## Active Recall

Técnica de aprendizado baseada em:

- recuperação ativa da memória;
- perguntas e respostas;
- avaliação contínua.

O sistema:

- gera perguntas;
- avalia respostas;
- identifica dificuldades.

---

# Dataset
## Origem dos Dados

O dataset foi composto por materiais acadêmicos **em pdf** relacionados a:

Inteligência Artificial;
Deep Learning;
Recuperação de Informação;
Ciência de Dados;
Sistemas Operacionais.


Fontes utilizadas:

- materiais de disciplinas (extraídos do AVA);
- artigos e PDFs acadêmicos (extraídos do scielo e google acadêmico).

## Limitações

Exemplo de limitações:

- PDFs com tabelas podem perder formatação;
- imagens não são interpretadas;
- documentos muito pequenos reduzem qualidade do RAG;
- OCR não foi implementado.

## Estratégia de Chunking

Configuração:
```
chunk_size = 500
overlap = 100
```
Impacto:

- melhora continuidade semântica;
- evita perda de contexto;
- aumenta qualidade da recuperação.

---

# Ferramentas Implementadas

O sistema implementa as seguintes ferramentas:
| Ferramenta          | Descrição                     |
| ------------------- | ----------------------------- |
| buscar_material_rag | consulta materiais acadêmicos |
| listar_tarefas      | lista tarefas                 |
| adicionar_tarefa    | adiciona tarefas              |
| concluir_tarefa     | conclui tarefas               |
| listar_eventos      | lista eventos da agenda                  |
| adicionar_evento | adiciona evento na agenda |
| gerar_exercicios    | cria exercícios               |
| gerar_pergunta      | active recall                 |
| avaliar_resposta    | avalia aluno                  |


--- 

# Como Executar o Projeto
## 1. Clonar Repositório
```
git clone URL_DO_REPOSITORIO
```

## 2. Entrar na Pasta
```
cd jarvis-academico
```

## 3. Criar Ambiente Virtual
- Windows
```
python -m venv venv
```

- Linux/Mac
```
python3 -m venv venv
```

## 4. Ativar Ambiente Virtual
- Windows
```
venv\Scripts\activate
```
- Linux/Mac
```
source venv/bin/activate
```

## 5. Instalar Dependências
```
pip install -r requirements.txt
```

## 6. Configurar Variáveis de Ambiente

Criar arquivo .env
```
OPENAI_API_KEY=SUA_CHAVE
OPENAI_BASE_URL=SUA_URL
MODEL_NAME=google/gemma-3-12b-it
```

## 7. Indexar pdfs
Execute:
```
python -m src.rag.index_all
```

---

# Executar o sistema

## 1. Executar no terminal
Execute: 
```
python app.py
```

## 2. Interface
Após executar:
```
python app.py
````
O Gradio abrirá um link local semelhante a:
```
http://127.0.0.1:7860
```
Abrir no navegador.

---

# Como Executar os Testes

Execute:
```
pytest
```

---

# Logs 
Os logs são registrados em:
```
logs/jarvis.log
```

---

# Estrutura dos bancos

## agenda.db

Tabela:

- agenda

Campos:

- id
- titulo
- data
- horario

## tasks.db

Tabela:

- tasks

Campos:

- id
- tarefa
- concluida

## performance.db

Tabela:

- performance

Campos:

Campos:

- id
- topic
- score

---

# Melhorias Futuras

Possíveis melhorias:

- memória conversacional;
- busca híbrida;
- reranking;
- OCR;
- upload de PDFs pela interface;
- dashboards;
- histórico de aprendizado;
- analytics de desempenho.

--- 

# IAs Utilizadas no Desenvolvimento

Ferramentas utilizadas:

- ChatGPT
- Claude
- Copilot

Utilização:

- revisão de código;
- auxílio em debugging;
- identificação de bugs;
- melhorias de organização;
- auxílio na documentação,