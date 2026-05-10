# Hello World LangChain

Premier projet du cours : un appel LLM simple à travers une chaîne LCEL (`PromptTemplate | ChatOpenAI`).

Le contenu pédagogique complet se trouve dans [../01-cours.md](../01-cours.md). Toutes les commandes (natif et Docker) sont dans [../Module-01-commandes-hello-world-LangChain.md](../Module-01-commandes-hello-world-LangChain.md). Si tu débutes complètement, commence par [../Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md](../Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md) — un cours de vulgarisation sur LangChain, LangGraph et l'IA agentique. Tu peux ensuite valider ta compréhension avec le [quiz de 50 questions](../Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md) puis suivre la [pratique pas-à-pas en venv et Docker](../Module-00-pratique-introduction-LLM-LangChain-LangGraph-agent-RAG.md).

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
