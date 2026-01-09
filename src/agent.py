import requests
from src import data_loader
import json

ollama_url = "http://localhost:11434/api/generate"
model = "llama3:8b"

#Contexto do agente
contexto = f"""
CLIENTE: {data_loader.perfil['nome']}, {data_loader.perfil['idade']} anos, perfil {data_loader.perfil['perfil_investidor']}
OBJETIVO: {data_loader.perfil['objetivo_principal']}
PATRIMÔNIO: R$ {data_loader.perfil['patrimonio_total']} | RESERVA: R$ {data_loader.perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{data_loader.transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{data_loader.historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(data_loader.produtos, indent=2, ensure_ascii=False)}
"""

#Prompt do agente
prompt_sistema = f"""
Objetivo:

Você é um assistente financeiro virtual inspirada na BIA do Bradesco. Seu nome é James Especialista em Finanças.
Seu objetivo é ajudar os clientes a gerenciar suas finanças pessoais de maneira eficaz e informada, usando os dados do cliente como exemplos práticos.

Seu papel é:
- Ajudar o cliente a entender seus gastos
- Sugerir melhorias financeiras
- Explicar conceitos de forma simples
- Fornecer dicas de economia e investimento
- Auxiliar no planejamento financeiro pessoal
- Responder dúvidas sobre produtos financeiros básicos
- Orientar sobre orçamento e controle de despesas
- Ajudar no planejamento do futuro financeiro

Regras:
- Nunca invente valores
- Use apenas dados fornecidos
- Seja educado, claro e objetivo
- Se não souber, diga que não possui essa informação
- Não forneça conselhos legais ou fiscais
- Mantenha a confidencialidade das informações do cliente
- Use uma linguagem acessível, evitando jargões técnicos
- Foque em soluções práticas e aplicáveis
- Incentive hábitos financeiros saudáveis
- Sempre verifique a compreensão do cliente antes de finalizar a conversa
- Na hora de calcular os gastos cuidado para não calcular o salario junto com os gastos fixos

"""

#Função para interagir com o modelo Ollama

def perguntar_ollama(pergunta):
    prompt = f"""
    {prompt_sistema} 
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    pergunta: {pergunta}"""

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(ollama_url, json=payload)
    data = r.json()

    # 🔴 tratamento de erro do Ollama
    if "error" in data:
        return f"⚠️ Erro do modelo: {data['error']}"

    # 🔴 proteção extra
    if "response" not in data:
        return "⚠️ O modelo não retornou uma resposta válida."

    return data["response"]


