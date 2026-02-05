import streamlit as st
import pandas as pd
import json
import requests

# ==============================
# Configuração OLLAMA
# ==============================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"
timeout=600


# ==============================
# Configuração Streamlit
# ==============================
st.set_page_config(
    page_title="Alice - Agente de Organização Financeira",
    page_icon="💰",
    layout="centered"
)

# ==============================
# Carregamento dos arquivos CSV
# ==============================
transacoes = pd.read_csv("./data/transacoes.csv")
historico_interacoes = pd.read_csv("./data/historico_interacoes.csv")

# ==============================
# Carregamento dos arquivos JSON
# ==============================
with open("./data/perfil_cliente.json", "r", encoding="utf-8") as f:
    perfil_cliente = json.load(f)

with open("./data/contas.json", "r", encoding="utf-8") as f:
    contas = json.load(f)

with open("./data/cartoes.json", "r", encoding="utf-8") as f:
    cartoes = json.load(f)

with open("./data/categorias.json", "r", encoding="utf-8") as f:
    categorias = json.load(f)

with open("./data/assinaturas.json", "r", encoding="utf-8") as f:
    assinaturas = json.load(f)

# ==============================
# Montagem do CONTEXTO
# ==============================
contexto = f"""
CLIENTE:
Nome: {perfil_cliente.get('nome', 'Não informado')}
Idade: {perfil_cliente.get('idade', 'Não informado')} anos
Perfil Financeiro: {perfil_cliente.get('perfil_investidor', 'Não informado')}
Objetivo Principal: {perfil_cliente.get('objetivo_principal', 'Não informado')}

SITUAÇÃO FINANCEIRA:
Renda Mensal: R$ {perfil_cliente.get('renda_mensal', 0)}
Renda Extra: R$ {perfil_cliente.get('renda_extra', 0)}
Reserva de Emergência Atual: R$ {perfil_cliente.get('reserva_emergencia', 0)}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico_interacoes.to_string(index=False)}

CATEGORIAS DISPONÍVEIS:
{json.dumps(categorias, indent=2, ensure_ascii=False)}
"""

# ==============================
# SYSTEM PROMPT
# ==============================
SYSTEM_PROMPT = """
Você é a Alice, um Agente de Organização Financeira pessoal, inteligente e confiável.

OBJETIVO:
Ajudar o usuário a entender seus gastos, organizar sua vida financeira,
reduzir ansiedade com dinheiro e tomar decisões conscientes no dia a dia.

LIMITAÇÕES IMPORTANTES:
- Você NÃO é consultor de investimentos.
- Não forneça recomendações financeiras sem dados suficientes.
- Nunca invente valores ou informações.
- Nunca solicite senhas ou dados sensíveis.

REGRAS:
- Utilize somente os dados fornecidos no contexto.
- Seja clara, empática e didática.
- Se algo não puder ser respondido, admita e explique.
- Priorize clareza em vez de jargões técnicos.
"""

# ==============================
# Função para chamar o OLLAMA
# ==============================
def perguntar(msg: str) -> str:
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta do usuário:
{msg}
"""

    try:
        r = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            },
            timeout=600
        )

        data = r.json()

        # Tratamento robusto da resposta
        if isinstance(data, dict):
            if "response" in data:
                return data["response"]

            if "message" in data and "content" in data["message"]:
                return data["message"]["content"]

            if "error" in data:
                return f"⚠️ Erro do modelo: {data['error']}"

        return "⚠️ Não consegui interpretar a resposta do modelo."

    except Exception as e:
        return f"❌ Erro ao consultar o modelo: {str(e)}"

# ==============================
# INTERFACE
# ==============================
st.title("💰 Alice — Agente de Organização Financeira")

st.markdown(
    "Converse comigo para entender melhor seus gastos, hábitos financeiros e organização do seu dinheiro."
)

if pergunta := st.chat_input("Faça sua pergunta sobre sua vida financeira..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("Analisando sua situação financeira..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)

