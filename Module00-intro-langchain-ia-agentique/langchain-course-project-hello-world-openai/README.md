# Hello World LangChain - Version OpenAI

Premier projet du cours : un appel LLM simple a travers une chaine LCEL (`PromptTemplate | ChatOpenAI`).

> [!IMPORTANT]
> Cette version utilise l'API OpenAI et necessite **5 USD minimum** de credit sur ton compte.
> Si tu prefereres une option **gratuite et 100% locale**, utilise plutot le dossier
> `langchain-course-project-hello-world-local/` (Pratique 2 - Ollama).

## Pour qui ?

Si tu debutes completement, commence par l'[introduction vulgarisee](../Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md) puis valide tes acquis avec le [quiz de 50 questions](../Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md).

Ensuite, suis la **[Pratique 1 - OpenAI cle API](../Module-00-pratique-1-OpenAI-clef-API.md)** : creation du compte, configuration billing, recuperation de la cle, execution native (`venv` + `pip` ou `uv`) et execution Docker.

Pour un memo court de toutes les commandes, ouvre le [resume des commandes](../Module-00-resume-commandes-hello-world-LangChain.md).

## Variables d'environnement

Copie `.env.example` vers `.env` puis renseigne ta cle :

```bash
OPENAI_API_KEY=ta_clef_openai
```

## Installation

```bash
uv sync
```

## Execution native

```bash
uv run python main.py
```

## Execution avec Docker

```bash
docker compose up --build
```

## Fichiers principaux

- `main.py` - point d'entree unique. Definit le prompt, le modele OpenAI, la chaine et invoque le tout sur 3 personnages historiques avec affichage des couts.
- `pyproject.toml` - dependances (`langchain`, `langchain-openai`, `python-dotenv`).
- `Dockerfile` + `docker-compose.yml` - image Python 3.12 + uv avec dependances pre-installees. Container : `langchain-hello-world-openai`.
- `.env.example` - gabarit pour ton fichier `.env` (uniquement `OPENAI_API_KEY`).
