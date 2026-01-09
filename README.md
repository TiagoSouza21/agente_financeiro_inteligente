🧠 Agente Financeiro Inteligente
================================

Aplicação de **agente financeiro inteligente** desenvolvida em Python, com **interface em Streamlit**, **análise de dados com Pandas** e **LLM local via Ollama**, focada em análise financeira e interação em linguagem natural.

> ⚠️ Projeto com finalidade educacional e de portfólio. Não constitui recomendação de investimento.

* * * * *

📌 Visão Geral
--------------

Este projeto implementa um **agente de IA aplicado ao contexto financeiro**, capaz de:

-   Analisar dados financeiros estruturados

-   Interpretar perguntas em linguagem natural

-   Gerar respostas inteligentes utilizando **LLM local**

-   Exibir resultados por meio de uma **interface web interativa**

O foco é demonstrar **integração entre dados, IA e aplicações web**, seguindo boas práticas de organização de código.

* * * * *

🏗️ Arquitetura do Projeto
--------------------------

A aplicação segue uma arquitetura simples, modular e escalável:
```mermaid
Usuário
  │
  ▼
Interface Streamlit
  │
  ▼
Camada de Processamento (Python)
  │   ├── Manipulação de dados (Pandas)
  │   ├── Regras de negócio
  │   └── Preparação de contexto
  │
  ▼
LLM Local (Ollama)
  │
  ▼
Resposta gerada em linguagem natural`
```
### 🔹 Descrição das Camadas

-   **Interface (Streamlit)**\
    Responsável pela interação com o usuário, entrada de dados e exibição dos resultados.

-   **Processamento de Dados (Python + Pandas)**\
    Realiza leitura, tratamento, análise e preparação dos dados financeiros.

-   **Camada de IA (Ollama)**\
    Executa um **modelo de linguagem local**, responsável por interpretar o contexto e gerar respostas inteligentes.

Essa separação facilita:\
✔ Manutenção\
✔ Evolução do projeto\
✔ Substituição de modelos ou interface no futuro

* * * * *

📁 Estrutura do Projeto
-----------------------
```text
agente_financeiro_inteligente/
├── data/                   # Dados utilizados na análise
├── src/                    # Código-fonte do agente
├── app.py                  # Aplicação principal (Streamlit)
└── README.md               # Documentação
``` 
* * * * *

🛠️ Tecnologias Utilizadas
--------------------------

### 🔹 Linguagem e Frameworks

-   **Python**

-   **Streamlit** -- Interface web interativa

-   **Pandas** -- Análise e manipulação de dados

### 🔹 Inteligência Artificial

-   **Ollama** -- Execução de LLM local

-   **Modelo LLM local** (ex: LLaMA 3)

* * * * *

🦙 Ollama (LLM Local)
---------------------

Este projeto utiliza **Ollama** para rodar modelos de linguagem **localmente**, sem depender de APIs externas.

### ✔ Vantagens

-   Execução offline

-   Maior privacidade dos dados

-   Redução de custos

-   Baixa latência

### 🔹 Instalação do Ollama

Download oficial:

`https://ollama.com/`

Após instalar, faça o download do modelo:

`ollama pull llama3`

Inicie o modelo:

`ollama run llama3`

> O Ollama deve estar ativo antes de executar a aplicação.

* * * * *

🛠️ Pré-requisitos
------------------

### 🔹 Ambiente

-   Python **3.8+**

-   pip

-   Ollama instalado e em execução

### 🔹 Bibliotecas Python
```
pandas        # Análise de dados
streamlit     # Interface web
requests      # Requisições HTTP
``` 

* * * * *

📦 Instalação
-------------

1.  Clone o repositório:

`git clone https://github.com/TiagoSouza21/agente_financeiro_inteligente.git
cd agente_financeiro_inteligente`

1.  Crie e ative um ambiente virtual:

`python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows`

1.  Instale as dependências:

`pip install pandas streamlit requests`

* * * * *

▶️ Execução
-----------

Certifique-se de que o **Ollama está rodando**, depois execute:

`streamlit run app.py`

A aplicação será aberta automaticamente no navegador.

* * * * *

🎯 Objetivos do Projeto
-----------------------

-   Demonstrar integração entre **IA + Dados + Interface Web**

-   Aplicar conceitos de **agentes inteligentes**

-   Servir como **projeto de portfólio** para vagas de:

    -   Estágio em Dados

    -   Ciência de Dados Jr

    -   IA / Machine Learning

    -   Engenharia de Software

* * * * *

📈 Possíveis Evoluções
----------------------

-   Integração com APIs financeiras (ex: Yahoo Finance)

-   Memória de conversas do agente

-   Avaliação de múltiplos ativos

-   Deploy em nuvem

-   Substituição do Streamlit por FastAPI + Frontend

* * * * *

👤 Autor
--------

**Tiago Souza**\
Estudante de Análise e Desenvolvimento de Sistemas\
Estudante de Engenharia de Controle e Automação\
Foco em **Ciência de Dados, IA e Análise de Dados**

🔗 LinkedIn: *www.linkedin.com/in/tiagosouzasantos21*

* * * * *

📄 Licença
----------

Projeto de uso educacional e livre para estudos.
