import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

#Carregando dados e salvando em variaveis
perfil = json.loads((DATA_DIR / "perfil_investidor.json").read_text(encoding="utf-8"))
produtos = json.loads((DATA_DIR / "produtos_financeiros.json").read_text(encoding="utf-8"))
transacoes = pd.read_csv(DATA_DIR / "transacoes.csv")
historico = pd.read_csv(DATA_DIR / "historico_atendimento.csv")

