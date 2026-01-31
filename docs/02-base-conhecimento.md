# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_interacoes.csv` | CSV | Contextualizar interações anteriores |
| `assinaturas.json` | JSON | Detectar gastos recorrentes e assinaturas esquecidas |
| `contas.json` | JSON | Informar contas ativas, saldos e tipos de conta |
| `cartoes.json` | JSON | Identificar limites, faturas e comportamento de uso do cartãoa |
| `categorias.json` | JSON | Classificar automaticamente as transações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram adaptados para representar comportamentos financeiros comuns, como gastos recorrentes, variação mensal de despesas, picos de consumo e categorias genéricas (alimentação, transporte, lazer, moradia).
Também foram incluídos campos adicionais, como categoria da despesa, tipo de transação (PIX, débito, crédito) e recorrência, para facilitar a geração de insights pelo agente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (ctrl + c, ctrl + v) ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json

# ==============================
# Carregamento dos arquivos CSV
# ==============================

transacoes = pd.read_csv('data/transacoes.csv')
historico_interacoes = pd.read_csv('data/historico_interacoes.csv')

# ==============================
# Carregamento dos arquivos JSON
# ==============================

with open('data/perfil_cliente.json', 'r', encoding='utf-8') as f:
    perfil_cliente = json.load(f)

with open('data/contas.json', 'r', encoding='utf-8') as f:
    contas = json.load(f)

with open('data/cartoes.json', 'r', encoding='utf-8') as f:
    cartoes = json.load(f)

with open('data/categorias.json', 'r', encoding='utf-8') as f:
    categorias = json.load(f)

with open('data/assinaturas.json', 'r', encoding='utf-8') as f:
    assinaturas = json.load(f)

# ==============================
# Exemplo de uso no agente
# ==============================

# Esses dados podem ser utilizados para:
# - Montar o contexto do prompt
# - Analisar padrões de gastos
# - Gerar insights explicativos
# - Manter histórico de interações

```
## Exemplo de Contexto Montado
> Mostre um exemplo de como os dados são formatados para o agente.

O Exemplo de contexto montado abaixo, se baseia nos dados originais da base de conhecimento, mas os sintetiza deixando as informações mais relevantes, otimizando assim o consumo de tokens. entretanto, vale lembrar que o mais importante do que economizar tokens, é ter todas as informações relevantes disponiveis em seu contexto.

Dados do Cliente:
- Nome: Carlos Andrade
- Perfil Financeiro: Conservador
- Preferência de Comunicação: Explicações simples e objetivas
- Renda mensal estimada: R$ 6.500

Resumo do Mês Atual:
- Total gasto até o momento: R$ 4.820
- Categoria com maior gasto: Alimentação
- Variação em relação ao mês anterior: +18%

Últimas transações relevantes:
- 02/11: Supermercado - R$ 480 (Crédito)
- 05/11: Restaurante - R$ 210 (PIX)
- 08/11: Streaming - R$ 55 (Débito)
- 10/11: Transporte por aplicativo - R$ 190 (Crédito)

Padrões Identificados:
- Gastos com alimentação acima da média histórica
- Assinatura ativa há mais de 12 meses sem uso frequente
...
```
