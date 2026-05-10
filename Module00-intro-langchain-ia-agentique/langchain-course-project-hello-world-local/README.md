# Hello World LangChain - Version Ollama locale

Premier projet du cours : un appel LLM simple a travers une chaine LCEL (`PromptTemplate | ChatOllama`).

> [!TIP]
> Cette version est **100% gratuite et locale** : aucune cle API, aucun cout, ton ordinateur fait tout le travail via Ollama.
> Si tu veux la qualite des modeles d'OpenAI (mais avec un compte payant), utilise plutot le dossier
> `langchain-course-project-hello-world-openai/` (Pratique 1).

## Pour qui ?

Si tu debutes completement, commence par l'[introduction vulgarisee](../Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md) puis valide tes acquis avec le [quiz de 50 questions](../Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md).

Ensuite, suis la **[Pratique 2 - Ollama local](../Module-00-pratique-2-Ollama-local.md)** : installation d'Ollama, telechargement du modele (`ollama pull gemma3:270m`), execution native (`venv` + `pip` ou `uv`) et execution Docker.

Pour un memo court de toutes les commandes, ouvre le [resume des commandes](../Module-00-resume-commandes-hello-world-LangChain.md).

## Variables d'environnement

Aucune cle requise. Copie `.env.example` vers `.env` :
- en **natif**, tu peux laisser le fichier vide (le code utilise `http://localhost:11434` par defaut),
- en **Docker**, decommente `OLLAMA_BASE_URL=http://host.docker.internal:11434` pour que le conteneur atteigne Ollama qui tourne sur l'hote.

## Pre-requis : Ollama installe et le modele present

```bash
ollama serve         # demarre le serveur Ollama (port 11434)
ollama pull gemma3:270m
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

- `main.py` - point d'entree unique. Definit le prompt, le modele Ollama, la chaine et invoque le tout sur 3 personnages historiques.
- `pyproject.toml` - dependances (`langchain`, `langchain-ollama`, `python-dotenv`).
- `Dockerfile` + `docker-compose.yml` - image Python 3.12 + uv avec dependances pre-installees. Container : `langchain-hello-world-local`. `extra_hosts` configure pour atteindre Ollama sur l'hote.
- `.env.example` - gabarit pour ton fichier `.env` (uniquement `OLLAMA_BASE_URL` optionnel).
