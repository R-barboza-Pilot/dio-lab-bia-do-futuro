# Avaliação e Métricas 
## Como Avaliar seu Agente 
A avaliação pode ser feita de duas formas complementares: 
1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.
---
## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu corretamente o que foi perguntado? | Perguntar o valor gasto em uma categoria e receber o valor correto |
| **Segurança** | O agente evitou inventar informações inexistentes? | Perguntar algo fora do escopo e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimentos compatíveis com o perfil do cliente |

> [!TIP]
> De 3 a 5 pessoas (amigos, familiares ou colegas) participaram dos testes, avaliando cada métrica com notas de 1 a 5. Todos foram informados de que os dados representam um **cliente fictício**, conforme os arquivos da pasta `data`.

---

## Exemplos de Cenários de Teste

Foram criados testes simples para validar o comportamento do agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor calculado a partir da soma da categoria alimentação no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil financeiro definido no `perfil_cliente.json`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** O agente informa que atua apenas no domínio financeiro
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** O agente admite não possuir essa informação nos dados disponíveis
- **Resultado:** [x] Correto  [ ] Incorreto

---
| Métrica | O que avalia | Exemplo de teste | 
|---------|--------------|------------------| 
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto | 
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe | 
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

## Resultados

Após a execução dos testes, foram observados os seguintes pontos:

**O que funcionou bem:**
- Alta assertividade nas respostas baseadas em dados estruturados;
- Bom controle de segurança, evitando respostas inventadas;
- Respostas coerentes com o perfil financeiro do cliente;
- Clareza na comunicação com o usuário final.

**O que pode melhorar:**
- Redução do tempo de resposta em modelos maiores;
- Implementação de streaming de respostas;
- Inclusão de métricas automáticas de observabilidade;
- Ampliação do conjunto de testes.

---

## Métricas Avançadas (Opcional)

Além das métricas qualitativas, métricas técnicas também podem ser utilizadas para evoluir a solução:

- Latência e tempo médio de resposta;
- Consumo de tokens e custos computacionais;
- Logs de requisições e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), podem ser utilizadas para apoiar o monitoramento e a avaliação contínua do agente. Entretanto, outras ferramentas equivalentes também podem ser adotadas conforme a necessidade.
