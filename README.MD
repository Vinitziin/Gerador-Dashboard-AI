📊 Gerador de Dashboards via Prompt

Um aplicativo Streamlit que permite gerar visualizações de dados automaticamente usando IA. Os usuários podem fazer upload de arquivos CSV e descrever em linguagem natural o tipo de visualização que desejam, e o sistema gera e executa código Python automaticamente.

## 🎯 Funcionalidades

- **Upload de CSV**: Interface simples para carregar arquivos de dados
- **Geração de código via IA**: Usa Azure OpenAI para gerar código Python baseado em prompts em linguagem natural
- **Execução segura**: Executa o código gerado em ambiente controlado
- **Visualizações automáticas**: Gera gráficos usando Matplotlib
- **Interface amigável**: Interface web intuitiva com Streamlit

## 🏗️ Estrutura do Projeto

```
Gerador de Dashboard/
├── .env                     # Variáveis de ambiente (Azure OpenAI)
├── .gitignore              # Arquivos ignorados pelo Git
├── README.MD               # Documentação
├── app/                    # Aplicação principal
│   ├── __init__.py
│   └── main.py            # Interface Streamlit
├── assets/                # Recursos estáticos
├── data/                  # Dados de teste
│   └── teste.csv         # Arquivo CSV de exemplo
├── services/              # Serviços externos
│   └── llm_handler.py    # Integração com Azure OpenAI
└── utils/                 # Utilitários
    └── safe_exec.py      # Execução segura de código
```

## 🔧 Configuração

### Pré-requisitos

- Python 3.11+
- Conta Azure OpenAI configurada

### Instalação

1. Clone o repositório
2. Instale as dependências:

```bash
pip install streamlit pandas matplotlib numpy openai python-dotenv
```

3. Configure as variáveis de ambiente no arquivo .env:

```env
AZURE_OPENAI_API_KEY=sua_api_key
AZURE_OPENAI_API_VERSION=sua_versao_api
AZURE_OPENAI_ENDPOINT=seu_endpoint
AZURE_OPENAI_DEPLOYMENT=seu_deployment
```

### Execução

```bash
streamlit run app/main.py
```

## 📁 Módulos

### main.py

Interface principal do Streamlit que:

- Gerencia upload de arquivos CSV
- Coleta prompts do usuário
- Exibe código gerado e visualizações
- Coordena o fluxo entre os módulos

### llm_handler.py

Responsável pela integração com Azure OpenAI:

- **`gerar_codigo(prompt)`**: Envia prompts para o modelo e retorna código Python

### safe_exec.py

Execução segura de código Python:

- **[`executar_codigo(codigo, df)`](utils/safe_exec.py)**: Executa código em ambiente controlado
- Remove acesso a built-ins perigosos
- Captura saída e erros

## 🎮 Como Usar

1. **Execute o aplicativo**: `streamlit run app/main.py`
2. **Faça upload do CSV**: Use o botão de upload na interface
3. **Descreva a visualização**: Digite o que deseja ver (ex: "gráfico de barras das vendas")
4. **Veja o resultado**: O código será gerado e executado automaticamente

### Exemplo de Prompts

- "Quero ver um gráfico de linhas das vendas ao longo do tempo"
- "Crie um gráfico de barras mostrando a média por categoria"
- "Mostre um histograma dos valores"

## 🔒 Segurança

O sistema implementa várias camadas de segurança:

- **Namespace restrito**: Remove acesso a funções built-in perigosas
- **Ambiente controlado**: Código executa em contexto isolado
- **Bibliotecas limitadas**: Apenas pandas, matplotlib e numpy disponíveis
- **Captura de saída**: Toda saída é capturada e controlada

## 📊 Dados de Teste

O arquivo teste.csv contém dados de exemplo:

```csv
data,vendas
2024-01-01,100
2024-01-02,150
2024-01-03,200
```

## 🛠️ Tecnologias

- **Streamlit**: Interface web
- **Azure OpenAI**: Geração de código via IA
- **Pandas**: Manipulação de dados
- **Matplotlib**: Visualizações
- **Python**: Linguagem principal

## ⚠️ Limitações

- **Segurança**: Embora implementada, a execução de código dinâmico sempre apresenta riscos
- **Bibliotecas**: Limitado a pandas, matplotlib e numpy
- **Complexidade**: Funciona melhor com visualizações simples a moderadas
- **Dependência de IA**: Qualidade dos resultados depende do modelo Azure OpenAI

## 🔮 Melhorias Futuras

- Suporte a mais bibliotecas de visualização (Plotly, Seaborn)
- Cache de resultados
- Histórico de visualizações
- Templates de visualização
- Validação mais robusta de código
- Suporte a múltiplos formatos de arquivo

## 📝 Contribuição

1. Faça fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request
