# Hello World LangChain

Premier projet du cours : un appel LLM simple à travers une chaîne LCEL (`PromptTemplate | ChatOpenAI`).

Si tu débutes complètement, commence par l'[introduction vulgarisée](../Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md) — un cours de vocabulaire sur LangChain, LangGraph et l'IA agentique. Valide avec le [quiz de 50 questions](../Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md). Ensuite, choisis ta voie :

- **[Pratique 1 — OpenAI clé API](../Module-00-pratique-1-OpenAI-clef-API.md)** : qualité maximale, mais nécessite **5 USD minimum** de crédit sur ton compte OpenAI.
- **[Pratique 2 — Ollama local](../Module-00-pratique-2-Ollama-local.md)** : gratuit, hors ligne, le LLM tourne sur ton ordinateur.

Pour un mémo court de toutes les commandes, ouvre le [résumé des commandes](../Module-00-resume-commandes-hello-world-LangChain.md).

## Variables d'environnement

Crée un fichier `.env` dans ce dossier :

```bash
OPENAI_API_KEY=ta_clef_openai
```

## Installation

```bash
uv sync
```

## Exécution

```bash
uv run python main.py
```

## Exécution avec Docker

Copie `.env.example` vers `.env`, renseigne ta clé OpenAI, puis :

```bash
docker compose up --build
```

## Fichiers principaux

- `main.py` — point d'entrée unique. Définit le prompt, le modèle, la chaîne et invoque le tout.
- `pyproject.toml` — dépendances (`langchain`, `langchain-openai`, `langchain-ollama`, `python-dotenv`).
- `Dockerfile` + `docker-compose.yml` — image Python 3.12 + uv avec dépendances pré-installées.
- `.env.example` — gabarit pour ton fichier `.env`.
