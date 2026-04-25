# 📊 Dashboard Logístico de Notas Fiscais | SaborTech Alimentos

![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)

---

## 🚀 Sobre o Projeto

Este projeto consiste em um **Dashboard Logístico interativo** desenvolvido para monitorar e analisar **Notas Fiscais (NFe)** em uma indústria do setor alimentício.

A aplicação transforma dados operacionais (vindos de um ERP) em **informações estratégicas**, permitindo uma visão clara sobre compras, fornecedores e volume financeiro.

💡 **Objetivo:** Demonstrar na prática habilidades em:
- Engenharia de Dados
- Análise de Dados
- Integração Banco + Aplicação
- Visualização de KPIs

> ⚠️ Os dados e o nome da empresa (**SaborTech Alimentos**) são fictícios.

---

## 🧠 Problema de Negócio

Em muitos ambientes logísticos, o lançamento de notas fiscais é feito de forma operacional, sem geração de insights.

Este projeto resolve isso ao:
- Centralizar os dados em um banco relacional
- Estruturar consultas eficientes
- Exibir indicadores em tempo real

---

## 🛠️ Tecnologias Utilizadas

| Categoria              | Tecnologia           |
|----------------------|----------------------|
| Linguagem            | Python               |
| Banco de Dados       | MySQL                |
| Visualização         | Streamlit            |
| Manipulação de Dados | Pandas               |
| Conexão DB           | SQLAlchemy + PyMySQL |
| Variáveis de Ambiente| python-dotenv        |

---

## 📊 Funcionalidades

### 📌 KPIs em Tempo Real
- Total de notas fiscais processadas
- Volume financeiro acumulado
- Ticket médio por nota

### 📦 Análise de Fornecedores
- Ranking dos fornecedores com maior volume de compras
- Visualização em gráfico de barras

### 📋 Relatório de Lançamentos
- Tabela interativa com:
  - Número da nota
  - Valor
  - Data de emissão

### 🔄 Integração com Banco de Dados
- Atualização automática ao alterar dados no MySQL

---

## 📁 Estrutura do Projeto

```
📂 dashboard-logistico
│
├── app.py              # Aplicação principal (dashboard)
├── sql_queries.py      # Queries SQL reutilizáveis
├── setup_banco.sql     # Script para criar o banco de dados
├── requirements.txt    # Dependências do projeto
├── .env.example        # Modelo de configuração das credenciais
└── README.md           # Documentação
```

---

## ⚙️ Como Executar — Passo a Passo Completo

Siga os passos abaixo **na ordem indicada**. Mesmo que você nunca tenha rodado um projeto assim antes, conseguirá executar sem problemas.

---

### ✅ Pré-requisitos

Antes de começar, certifique-se de que você tem instalado na sua máquina:

| Ferramenta | Para que serve | Como verificar se já tem |
|---|---|---|
| Python 3.x | Rodar o código | `python --version` no terminal |
| MySQL Server | Banco de dados | Abrir o MySQL Workbench |
| pip | Instalar bibliotecas Python | `pip --version` no terminal |

> 💡 Caso não tenha o Python, baixe em: https://www.python.org/downloads/  
> 💡 Caso não tenha o MySQL, baixe em: https://dev.mysql.com/downloads/installer/

---

### 📥 Passo 1 — Baixar o Projeto

Clone o repositório ou baixe os arquivos manualmente:

```bash
git clone https://github.com/seu-usuario/dashboard-logistico.git
```

Depois, entre na pasta do projeto:

```bash
cd dashboard-logistico
```

> 💡 Se você baixou o ZIP pelo GitHub, apenas extraia a pasta e abra o terminal dentro dela.

---

### 🗄️ Passo 2 — Criar o Banco de Dados no MySQL

1. Abra o **MySQL Workbench**
2. Conecte-se ao seu servidor local
3. Abra o arquivo `setup_banco.sql` (vá em `File > Open SQL Script`)
4. Clique em **Execute** (ícone de raio ⚡) para rodar o script

Isso vai criar automaticamente:
- O banco de dados `logistica_alimentar`
- As tabelas `fornecedores` e `notas_fiscais`
- Dados de exemplo para visualizar o dashboard imediatamente

> ⚠️ **Atenção:** Guarde a sua senha do MySQL — você vai precisar dela no próximo passo.

---

### 🔑 Passo 3 — Configurar as Credenciais do Banco

O projeto usa um arquivo `.env` para guardar as credenciais com segurança. **A senha nunca fica exposta no código.**

1. Renomeie o arquivo `.env.example` para `.env`:

```bash
# Linux / Mac
cp .env.example .env

# Windows
copy .env.example .env
```

2. Abra o arquivo `.env` e preencha com os seus dados:

```
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_HOST=localhost
DB_PORT=3306
DB_NAME=logistica_alimentar
```

> 💡 Se você não alterou o usuário e a porta durante a instalação do MySQL, apenas mude o campo `DB_PASSWORD`.

> 🔒 **Importante:** O arquivo `.env` já está no `.gitignore`. Ele **nunca será enviado ao GitHub**, mantendo suas credenciais seguras.

---

### 📦 Passo 4 — Instalar as Dependências Python

No terminal, dentro da pasta do projeto, rode:

```bash
pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias: Streamlit, Pandas, SQLAlchemy, PyMySQL e python-dotenv.

Aguarde a instalação terminar. Você verá mensagens de `Successfully installed` ao final.

> 💡 Se aparecer um erro de permissão, tente: `pip install -r requirements.txt --user`

---

### 🚀 Passo 5 — Rodar o Dashboard

Com tudo configurado, execute o comando abaixo no terminal:

```bash
python -m streamlit run app.py
```

O terminal exibirá uma mensagem parecida com esta:

```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

O dashboard abrirá **automaticamente no seu navegador**. Se não abrir, acesse manualmente:  
👉 http://localhost:8501

---

### 🎉 Resultado Esperado

Ao abrir o navegador, você verá:

- **3 KPIs** no topo: total de notas, volume financeiro e ticket médio
- **Gráfico de barras** com volume por fornecedor
- **Tabela** com os últimos lançamentos

---

## 🐛 Solução de Problemas Comuns

| Erro | Causa provável | Solução |
|---|---|---|
| `Access denied for user 'root'` | Senha incorreta no `.env` | Reveja o Passo 3 e corrija o campo `DB_PASSWORD` |
| `ModuleNotFoundError` | Bibliotecas não instaladas | Rode novamente o Passo 4 |
| `Unknown database 'logistica_alimentar'` | Banco não foi criado | Repita o Passo 2 no MySQL Workbench |
| Dashboard abre em branco | Tabelas vazias no banco | Verifique se o `setup_banco.sql` inseriu os dados de exemplo |
| Porta 8501 em uso | Outro processo usando a porta | Rode com `streamlit run app.py --server.port 8502` |

---

## 📈 Possíveis Melhorias Futuras

- Sistema de login de usuários
- Deploy na nuvem
- Novos KPIs
- Integração com API
- Formulário para cadastro de notas diretamente no dashboard

---

## 🧑‍💻 Autor

Vinícius Teodoro de Freitas  
Estudante de Ciência da Computação

🔗 Conecte-se comigo no LinkedIn:  
[Vinícius T. Freitas](https://linkedin.com/in/vinícius-teodoro-de-freitas)
