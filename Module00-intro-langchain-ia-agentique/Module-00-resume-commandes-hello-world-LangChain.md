# Module 1 — Commandes (Hello World LangChain)

Mémo rapide pour faire tourner le projet Hello World en **trois méthodes** : `uv` (rapide), `venv + pip` (classique), `Docker` (isolé). Le tutoriel pédagogique complet est dans [Module-00-pratique-introduction-LLM-LangChain-LangGraph-agent-RAG.md](Module-00-pratique-introduction-LLM-LangChain-LangGraph-agent-RAG.md). Le cours théorique est dans [01-cours.md](01-cours.md).

> [!TIP]
> Si tu débutes complètement, ouvre plutôt la **[pratique pas-à-pas](Module-00-pratique-introduction-LLM-LangChain-LangGraph-agent-RAG.md)**. Ce fichier-ci suppose que tu connais déjà Python, le terminal et `git`.

---

## Table de référence rapide

| Méthode | Outil | Vitesse install | Isolation | Quand l'utiliser |
|---|---|---|---|---|
| **uv** | `uv sync` puis `uv run` | Très rapide | venv automatique | Recommandée (moderne, gère tout) |
| **venv + pip** | `python -m venv` puis `pip install` | Lente | venv manuel | Si tu n'as pas `uv` installé |
| **Docker** | `docker compose up --build` | Moyenne (1ère fois) | Conteneur complet | Reproductibilité, pas besoin de Python local |

---

## 0. Prérequis

| Outil | Version | Vérifier | Nécessaire pour |
|---|---|---|---|
| Python | 3.12+ | `python --version` | uv et venv |
| `uv` (optionnel) | dernier | `uv --version` | Méthode uv |
| Docker Desktop | dernier | `docker --version` | Méthode Docker |
| Ollama (optionnel) | dernier | `ollama --version` | LLM local sans clé OpenAI |

Installer `uv` (Windows PowerShell) :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Installer `uv` (macOS / Linux) :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 1. Aller dans le dossier du code

```bash
cd repositories/01-langchain-course-project-hello-world/langchain-course-project-hello-world
```

> [!IMPORTANT]
> Toutes les commandes ci-dessous se lancent **depuis ce dossier intérieur**, pas depuis la racine du cours.

---

## 2. Préparer le fichier `.env`

```bash
cp .env.example .env
```

Puis ouvre `.env` et renseigne :

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxx
```

Récupère ta clé sur https://platform.openai.com/api-keys (cliquer « Create new secret key »).

---

## 3. Méthode A — `uv` (recommandée)

```bash
uv sync
uv run python main.py
```

- `uv sync` lit `pyproject.toml` et `uv.lock`, crée `.venv/` et installe tout en une fois.
- `uv run` lance Python dans cet environnement sans avoir besoin d'activer manuellement.

Pour ajouter une dépendance plus tard :

```bash
uv add nom-du-package
```

---

## 4. Méthode B — `venv + pip` (classique)

Création et activation de l'environnement virtuel :

```bash
python -m venv .venv
```

Activation **Windows PowerShell** :

```powershell
.\.venv\Scripts\Activate.ps1
```

Activation **macOS / Linux** :

```bash
source .venv/bin/activate
```

Installation des dépendances et exécution :

```bash
pip install --upgrade pip
pip install langchain langchain-openai langchain-ollama python-dotenv
python main.py
```

Désactivation quand tu as fini :

```bash
deactivate
```

---

## 5. Méthode C — Docker

Build + run en une commande (utilise le `.env` que tu viens de créer) :

```bash
docker compose up --build
```

Pour relancer sans rebuild (plus rapide) :

```bash
docker compose up
```

Pour exécuter en mode détaché (en arrière-plan) :

```bash
docker compose up -d
docker compose logs -f
```

Pour arrêter et tout nettoyer :

```bash
docker compose down
```

Pour rebuild proprement après changement de dépendances :

```bash
docker compose build --no-cache
docker compose up
```

---

## 6. Variante — Ollama (LLM local, sans clé OpenAI)

Démarre Ollama et tire un petit modèle :

```bash
ollama serve
ollama pull gemma3:270m
```

Dans `main.py`, commente la ligne `ChatOpenAI(...)` et décommente la ligne `ChatOllama(model="gemma3:270m")`. Puis relance avec n'importe laquelle des trois méthodes ci-dessus.

> [!NOTE]
> Avec Docker, il faut une configuration supplémentaire pour atteindre Ollama depuis le conteneur (variable `OLLAMA_BASE_URL=http://host.docker.internal:11434` dans `.env`).

---

## 7. Sortie attendue

```
Hello from langchain-course!
content='1. Short summary: ...
2. Two interesting facts: ...' additional_kwargs={...} response_metadata={...}
```

Le contenu varie à chaque exécution (le LLM est non-déterministe), mais tu dois voir au minimum un résumé court et deux faits.

---

## 8. Pièges courants

| Symptôme | Cause | Solution |
|---|---|---|
| `ModuleNotFoundError: langchain` | venv pas activé ou `uv sync` non lancé | Refais l'étape 3 ou 4 |
| `openai.AuthenticationError` | `OPENAI_API_KEY` manquante / invalide | Vérifie `.env`, relance le terminal |
| `model 'gpt-5' does not exist` | Modèle non disponible sur ton compte | Remplace par `gpt-4o-mini` dans `main.py` ligne ~12 |
| `connection refused` (Ollama) | `ollama serve` pas lancé | Démarre Ollama dans un autre terminal |
| Docker : `port already in use` | Un autre conteneur tourne | `docker compose down` puis relance |
| `.env` ignoré | Mauvais dossier | `.env` doit être dans le **dossier intérieur**, pas à la racine du cours |

---

## 9. Aller plus loin

- Tutoriel pas-à-pas avec captures et explications : [Module-00-pratique-introduction-LLM-LangChain-LangGraph-agent-RAG.md](Module-00-pratique-introduction-LLM-LangChain-LangGraph-agent-RAG.md)
- Quiz de validation 50 questions : [Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md](Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md)
- Cours théorique du module : [01-cours.md](01-cours.md)
- Module suivant : [Module 2 — Search Agent](../02-langchain-course-project-search-agent/01-cours.md)
