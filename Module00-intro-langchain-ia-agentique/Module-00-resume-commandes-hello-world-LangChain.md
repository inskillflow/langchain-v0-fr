# Module 0 — Résumé des commandes (Hello World LangChain)

Mémo rapide pour faire tourner le projet Hello World en **trois méthodes** : `uv` (rapide), `venv + pip` (classique), `Docker` (isolé). Pour un tutoriel pas-à-pas, choisis selon ton fournisseur LLM :

- **[Pratique 1 — OpenAI clé API](Module-00-pratique-1-OpenAI-clef-API.md)** (qualité max, 5 USD minimum requis sur le compte OpenAI)
- **[Pratique 2 — Ollama local](Module-00-pratique-2-Ollama-local.md)** (gratuit, le LLM tourne sur ton ordinateur)

L'introduction théorique vulgarisée est dans [Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md](Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md).

> [!TIP]
> Si tu débutes complètement, ouvre plutôt l'une des 2 pratiques pas-à-pas : **[Pratique 1 — OpenAI](Module-00-pratique-1-OpenAI-clef-API.md)** (payant) ou **[Pratique 2 — Ollama](Module-00-pratique-2-Ollama-local.md)** (gratuit). Ce fichier-ci suppose que tu connais déjà Python, le terminal et `git`.

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

## 1. Être dans le dossier du projet

> [!IMPORTANT]
> Toutes les commandes ci-dessous se lancent depuis le **dossier du projet** (celui qui contient `main.py`, `Dockerfile`, `pyproject.toml`...). Si tu as cloné le cours complet, c'est `repositories/Module00-intro-langchain-ia-agentique/langchain-course-project-hello-world/`. Si tu as reçu le dossier zippé, **tu es déjà dedans**.

```bash
# Verifier rapidement
ls
# main.py, pyproject.toml, uv.lock, Dockerfile, docker-compose.yml, .env.example...
```

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

## 5b. Méthode D — Mode interactif (entrer dans le conteneur)

> [!TIP]
> Avec `docker compose up`, le conteneur lance `main.py` puis s'arrête. `docker exec` ne marche donc pas. La méthode propre c'est `docker compose run` qui override la commande de démarrage.

Entrer dans un shell bash du conteneur :

```bash
docker compose run --rm -it app bash
```

Une fois à l'intérieur (le prompt devient `root@xxx:/app#`) :

```bash
pwd                                       # /app
ls -la                                    # voir les fichiers du projet
env | grep OPENAI                         # verifier la cle (voie OpenAI)
curl http://host.docker.internal:11434/api/tags  # tester Ollama (voie Ollama)
python --version
python main.py                            # relance manuelle
python main.py                            # relance 2
python main.py                            # relance 3 ...
exit                                      # sortir, --rm nettoie le conteneur
```

Détails des arguments : `run` = one-shot, `--rm` = auto-suppression à la sortie, `-it` = interactif + TTY, `app` = nom du service (PAS le `container_name`), `bash` = override de `python main.py`.

> [!IMPORTANT]
> **Avec OpenAI** : chaque `python main.py` consomme du crédit (~0.0005 USD avec `gpt-4o-mini`). **Avec Ollama** : 100 % gratuit.

Pour vraiment utiliser `docker exec` (cas rare), il faut d'abord garder le conteneur vivant :

```bash
docker compose run -d --name hello-shell --entrypoint sleep app infinity
docker exec -it hello-shell bash
# ... tes commandes ...
exit
docker stop hello-shell ; docker rm hello-shell
```

Voir la section détaillée dans [Module-00-pratique-1-OpenAI-clef-API.md § 10b](Module-00-pratique-1-OpenAI-clef-API.md#section-10b) ou [Module-00-pratique-2-Ollama-local.md § 11b](Module-00-pratique-2-Ollama-local.md#section-11b).

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
| Docker : `env file ... .env not found` | Tu n'as pas créé `.env` | `cp .env.example .env` puis renseigne `OPENAI_API_KEY` |
| Docker : `No interpreter found for Python 3.11` | `.python-version` du projet ne correspond pas au Python du conteneur | Vérifie que `.python-version` contient `3.12` (alignement avec `python:3.12-slim` dans le `Dockerfile`) |
| `.env` ignoré | Mauvais dossier | `.env` doit être dans le **dossier intérieur** (`langchain-course-project-hello-world/`), pas à la racine du cours |

---

## 9. Aller plus loin

- Pratique 1 (OpenAI, payant) : [Module-00-pratique-1-OpenAI-clef-API.md](Module-00-pratique-1-OpenAI-clef-API.md)
- Pratique 2 (Ollama, gratuit) : [Module-00-pratique-2-Ollama-local.md](Module-00-pratique-2-Ollama-local.md)
- Introduction théorique vulgarisée : [Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md](Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md)
- Quiz de validation 50 questions : [Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md](Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md)
- Module suivant : [Module 2 — Search Agent](../02-langchain-course-project-search-agent/01-cours.md)
