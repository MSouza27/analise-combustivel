# ⛽ Análise de Preços de Combustíveis — Dados ANP

Este projeto é uma aplicação **interativa em Streamlit** que permite analisar a **evolução dos preços médios de revenda de combustíveis no Brasil** com base nos dados públicos da **Agência Nacional do Petróleo (ANP)**.

A ferramenta lê uma planilha Excel (`database_anp.xlsx`), permite ao usuário filtrar **produto, estado e ano**, e exibe um **gráfico de linha interativo** mostrando a variação de preços ao longo dos meses.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **Pandas** — manipulação e limpeza de dados
* **OpenPyXL** — leitura de arquivos Excel (.xlsx)
* **Streamlit** — interface web interativa
* **Altair** — visualização de dados (gráficos interativos)
* **Pillow (PIL)** — manipulação de imagens (para logotipos ou ícones opcionais)

---

## 📊 Funcionalidades

* Leitura automática da base de dados da ANP (`database_anp.xlsx`)
* Filtros interativos na barra lateral:

  * Combustível (ex: Gasolina, Etanol, Diesel etc.)
  * Estado
  * Ano (seleção múltipla)
* Gráfico dinâmico com:

  * Evolução mensal do preço médio
  * Comparação entre diferentes anos
  * Tooltip com informações detalhadas (mês, ano e preço)

---

## 🧩 Estrutura do Código

```python
@st.cache_data
def gerar_data():
    # Lê os dados do Excel e retorna um DataFrame
```

A função `gerar_data()` é cacheada pelo Streamlit para evitar recarregar o arquivo a cada atualização.

Os dados são filtrados pelas colunas úteis:

```python
colunas_uteis = ['MÊS', 'PRODUTO', 'REGIÃO', 'ESTADO', 'PRECO MÉDIO REVENDA']
```

A aplicação usa a barra lateral (`st.sidebar`) para coletar as seleções do usuário e filtrar o DataFrame conforme:

* Produto
* Estado
* Ano(s)

O gráfico principal é gerado com **Altair**, exibindo a evolução dos preços médios ao longo dos meses:

```python
alt.Chart(dados_usuario).mark_line(point=True)
```

---

## 🖼️ Exemplo de Uso

1. Ao rodar o app, selecione na barra lateral:

   * O **combustível** (ex: Gasolina)
   * O **estado** (ex: Pernambuco)
   * Um ou mais **anos** (ex: 2022, 2023)
2. O gráfico exibirá a evolução dos preços médios mensais para as seleções feitas.
3. Passe o mouse sobre os pontos do gráfico para ver os valores detalhados.

---

## ⚙️ Como Executar Localmente

### 1️⃣ Instale as dependências

```bash
pip install pandas openpyxl streamlit altair pillow
```

### 2️⃣ Coloque o arquivo `database_anp.xlsx` na mesma pasta do código

> Dica: você pode baixar a base de dados diretamente do site da ANP (Série Histórica de Preços de Combustíveis).

### 3️⃣ Execute o aplicativo Streamlit

```bash
streamlit run app.py
```

(Onde `app.py` é o nome do arquivo com o código acima)

### 4️⃣ Acesse o app no navegador

```
http://localhost:8501
```

---

## 📁 Estrutura de Diretórios

```
📦 analise-combustiveis-anp
 ┣ 📜 app.py
 ┣ 📊 database_anp.xlsx
 ┣ 🖼️ logo.png               # (opcional)
 ┣ 📄 README.md
 ┗ 📁 venv/                  # (opcional, ambiente virtual)
```

---

## 📈 Exemplo de Gráfico

A aplicação gera um gráfico como este:

**Evolução anual do preço médio — Gasolina (PE)**
📅 Eixo X: Mês
💰 Eixo Y: Preço médio de revenda (R$/L)

---

## 💡 Ideias Futuras

* Adicionar filtro por **região**
* Incluir **média nacional** para comparação
* Permitir **download do gráfico ou dataset filtrado**
* Exibir **variação percentual mensal**

---

## 👨‍💻 Autor

**Magno Souza**
📍 Recife - PE
💼 Desenvolvedor Backend | Especialista em Análise e Engenharia de Dados
🔗 [LinkedIn](www.linkedin.com/in/magno-souza-dos-santos)
