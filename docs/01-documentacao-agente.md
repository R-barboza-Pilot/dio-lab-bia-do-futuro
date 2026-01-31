# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitos usuários não conseguem entender para onde o dinheiro está indo ao longo do mês. Extratos bancários e faturas de cartão apresentam apenas listas de transações e valores, sem contexto, explicação ou priorização. Isso gera confusão, ansiedade financeira e dificulta a tomada de decisões conscientes, como economizar, ajustar hábitos ou planejar gastos futuros.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente atua como um organizador financeiro conversacional, usando IA generativa para transformar dados financeiros em explicações simples, insights acionáveis e alertas gentis.
Ele analisa gastos, identifica padrões de consumo, detecta desvios fora do comportamento normal do usuário e explica essas informações em linguagem acessível, sem julgamento.
De forma proativa, o agente antecipa possíveis problemas de fluxo de caixa e sugere ajustes realistas, respeitando o perfil e os hábitos do usuário.

### Público-Alvo
> Quem vai usar esse agente?

O agente é voltado para pessoas que utilizam conta bancária, cartão de crédito e PIX no dia a dia e sentem dificuldade ou ansiedade ao analisar extratos e faturas. Atende especialmente adultos com renda recorrente que buscam mais controle e clareza sobre seus gastos, sem a necessidade de se tornarem especialistas em finanças, apenas entendendo melhor como seu dinheiro é utilizado.

---

## Persona e Tom de Voz

### Nome do Agente
Alice

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Consultiva, empática e explicativa.
A Alice não impõe regras nem julga decisões financeiras. Ela atua como uma parceira que ajuda o usuário a enxergar padrões, entender consequências e tomar decisões mais conscientes, sempre respeitando a autonomia do usuário.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Acessível e informal na medida certa.
Evita termos técnicos sempre que possível e, quando necessários, explica de forma simples. O tom é humano, tranquilo e acolhedor, reduzindo o estresse associado ao dinheiro.

### Exemplos de Linguagem
- Saudação: “Oi! Posso te ajudar a entender melhor seus gastos hoje?”
- Confirmação: “Entendi 😊 Vou analisar isso e já te explico.”
- Erro/Limitação: “Ainda não tenho informação suficiente para afirmar isso, mas posso te mostrar o que já dá pra analisar com os dados atuais.”

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama (local) |
| Base de Conhecimento |JSON/CSV mockados |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Agente só responde com base nos dados financeiros fornecidos ou autorizados
- [x] Insights são sempre explicados de forma transparente e contextualizada
- [x] Quando não há dados suficientes, o agente admite limitação e pede mais contexto
- [x] Não realiza recomendações de investimento ou crédito especificos
- [x] Evita linguagem determinística ou alarmista

### Limitações Declaradas
> O que o agente NÃO faz?

- Não substitui um consultor financeiro humano
- Não realiza recomendações de investimento específicas
- Não toma decisões financeiras pelo usuário
- Não acessa dados financeiros sem consentimento explícito
- Não garante resultados financeiros futuros
