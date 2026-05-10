<a id="top"></a>

# Module 0 — Pratique 2 : Hello World avec Ollama local (100% gratuit)

> [!IMPORTANT]
> **Cette voie est gratuite et fonctionne hors ligne** une fois le modèle téléchargé. Pas de carte bancaire, pas de quota, pas de coût par appel. En contrepartie, tu fais tourner le LLM **sur ton propre ordinateur** : c'est plus lent qu'OpenAI, et la qualité du modèle dépend de ton matériel.
>
> Si tu préfères la **qualité maximale** (et payer), va plutôt voir la **[Pratique 1 — Hello World avec OpenAI (clé API + crédit)](./Module-00-pratique-1-OpenAI-clef-API.md)**.

---

## Table des matières

| # | Section |
|---|---------|
| 1 | [Objectifs](#section-1) |
| 2 | [Prérequis matériels](#section-2) |
| 3 | [Étape 1 — Installer Ollama](#section-3) |
| 4 | [Étape 2 — Télécharger un modèle (`gemma3:270m`)](#section-4) |
| 5 | [Étape 3 — Vérifier qu'Ollama tourne](#section-5) |
| 6 | [Étape 4 — Aller dans le projet](#section-6) |
| 7 | [Étape 5 — Modifier `main.py` pour pointer sur Ollama](#section-7) |
| 8 | [Étape 6 — Configurer le `.env` (minimal)](#section-8) |
| 9 | [Méthode A — Exécution avec `venv + pip`](#section-9) |
| 10 | [Méthode B — Exécution avec `uv`](#section-10) |
| 11 | [Méthode C — Exécution avec Docker](#section-11) |
| 11b | [Méthode D — Mode interactif : entrer dans le conteneur](#section-11b) |
| 12 | [Sortie attendue](#section-12) |
| 13 | [Choix du modèle Ollama (`gemma3:270m`, `qwen3:1.7b`, etc.)](#section-13) |
| 14 | [Pièges spécifiques à Ollama](#section-14) |
| 15 | [Combien ça consomme (RAM, disque, CPU/GPU)](#section-15) |
| 16 | [Toutes les commandes — cheat-sheet par méthode](#section-16) |
| 17 | [Conclusion et étapes suivantes](#section-17) |

---

<a id="section-1"></a>

## 1. Objectifs

À la fin de cette pratique, tu sauras :

- Installer Ollama sur ton ordinateur (Windows / macOS / Linux).
- Télécharger un modèle local (`gemma3:270m`, ~290 Mo).
- Modifier `main.py` pour utiliser **Ollama** au lieu d'OpenAI.
- Lancer le projet en `venv + pip`, `uv`, ou Docker.
- Diagnostiquer les erreurs Ollama courantes (`connection refused`, `model not found`).
- Choisir le bon modèle selon la mémoire de ta machine.

[↑ retour en haut](#top)

---

<a id="section-2"></a>

## 2. Prérequis matériels

| Prérequis | Minimum | Recommandé |
|---|---|---|
| RAM | 4 Go (pour `gemma3:270m`) | 8 Go ou plus pour modèles plus gros |
| Disque | 1 Go libre | 10 Go si tu veux essayer plusieurs modèles |
| OS | Windows 10+, macOS 12+, Linux | Idem |
| GPU | Aucun obligatoire | NVIDIA ou Apple Silicon accélère beaucoup |
| Internet | Requis pour le `pull` initial | Plus requis ensuite |
| Carte bancaire | **Aucune** | — |

> [!TIP]
> Sur Windows, Ollama utilise CUDA si tu as une carte NVIDIA, sinon il tourne sur CPU. Sur Apple Silicon (M1/M2/M3/M4), Ollama exploite le Neural Engine automatiquement.

[↑ retour en haut](#top)

---

<a id="section-3"></a>

## 3. Étape 1 — Installer Ollama

### Windows

1. Va sur https://ollama.com/download/windows
2. Télécharge `OllamaSetup.exe`.
3. Double-clique pour installer (~200 Mo).
4. Une fois installé, Ollama démarre automatiquement en arrière-plan (icône dans la barre des tâches).

### macOS

1. Va sur https://ollama.com/download/mac
2. Télécharge `Ollama.dmg`, ouvre, glisse `Ollama` dans `/Applications`.
3. Lance Ollama depuis le Launchpad.

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Vérifier l'installation

```bash
ollama --version
```

Tu dois voir quelque chose comme `ollama version is 0.x.y`.

[↑ retour en haut](#top)

---

<a id="section-4"></a>

## 4. Étape 2 — Télécharger un modèle (`gemma3:270m`)

```bash
ollama pull gemma3:270m
```

C'est un petit modèle de **270 millions de paramètres** (~290 Mo). Il télécharge en quelques secondes / minutes selon ta connexion.

Pour vérifier qu'il est bien là :

```bash
ollama list
```

Tu dois voir :

```
NAME            ID              SIZE      MODIFIED
gemma3:270m     abc123def456    290 MB    a minute ago
```

> [!NOTE]
> `gemma3:270m` est volontairement **petit** pour démarrer vite, même sur un ordinateur modeste. La qualité est limitée mais largement suffisante pour ce Hello World. Pour la suite du cours, vois la [section 13](#section-13) pour des modèles plus gros.

[↑ retour en haut](#top)

---

<a id="section-5"></a>

## 5. Étape 3 — Vérifier qu'Ollama tourne

Ollama expose une API HTTP sur `http://localhost:11434`. Vérifie :

```bash
curl http://localhost:11434/api/tags
```

Réponse attendue :

```json
{"models":[{"name":"gemma3:270m",...}]}
```

> [!TIP]
> Si Ollama ne tourne pas (cas Linux ou si tu as fermé la barre des tâches sur Windows / macOS), démarre-le manuellement :
> ```bash
> ollama serve
> ```
> Laisse ce terminal ouvert. Ouvre-en un nouveau pour la suite des commandes.

[↑ retour en haut](#top)

---

<a id="section-6"></a>

## 6. Étape 4 — Être dans le dossier du projet

> [!IMPORTANT]
> Toutes les commandes de ce guide se lancent depuis le **dossier du projet** (celui qui contient `main.py`, `Dockerfile`, `pyproject.toml`, `.env.example`, etc.). Si tu as cloné le cours complet, c'est `repositories/Module00-intro-langchain-ia-agentique/langchain-course-project-hello-world/`. Si tu as juste reçu le dossier `langchain-course-project-hello-world/` zippé, **tu es déjà dedans** dès que tu l'ouvres.

Vérifie en listant les fichiers :

```bash
ls
# main.py, pyproject.toml, uv.lock, Dockerfile, docker-compose.yml, .env.example...
```

[↑ retour en haut](#top)

---

<a id="section-7"></a>

## 7. Étape 5 — Modifier `main.py` pour pointer sur Ollama

Ouvre `main.py`. Tu vois, autour de la ligne 33-34 :

```python
# llm = ChatOllama(temperature=0, model="gemma3:270m")
llm = ChatOpenAI(temperature=0, model="gpt-5")
```

**Inverse les commentaires** : commente la ligne `ChatOpenAI`, décommente la ligne `ChatOllama` :

```python
llm = ChatOllama(temperature=0, model="gemma3:270m")
# llm = ChatOpenAI(temperature=0, model="gpt-5")
```

> [!IMPORTANT]
> Si tu prévois d'exécuter avec **Docker**, il faut en plus pointer sur l'hôte. Remplace par :
> ```python
> llm = ChatOllama(temperature=0, model="gemma3:270m", base_url="http://host.docker.internal:11434")
> ```
> Pour `venv` ou `uv` (méthodes A et B), pas besoin du `base_url`, le défaut `http://localhost:11434` marche directement.

Sauvegarde le fichier.

[↑ retour en haut](#top)

---

<a id="section-8"></a>

## 8. Étape 6 — Configurer le `.env` (minimal)

Avec Ollama, **aucune clé API n'est requise**. Mais le projet utilise `python-dotenv` qui s'attend à un `.env`. Crée-en un vide ou avec une variable factice :

```bash
cp .env.example .env
```

Puis dans `.env`, tu peux laisser ainsi (Ollama ne lit aucune clé) :

```
OPENAI_API_KEY=not_needed_for_ollama
```

> [!NOTE]
> `python-dotenv` n'échoue pas si `.env` est absent ou vide, mais avoir le fichier évite les warnings.

[↑ retour en haut](#top)

---

<a id="section-9"></a>

## 9. Méthode A — Exécution avec `venv + pip` (classique)

```bash
python -m venv .venv
```

Active l'environnement :

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Installe et lance :

```bash
pip install --upgrade pip
pip install langchain langchain-openai langchain-ollama python-dotenv
python main.py
```

Pour désactiver :

```bash
deactivate
```

[↑ retour en haut](#top)

---

<a id="section-10"></a>

## 10. Méthode B — Exécution avec `uv` (recommandée)

`uv` est un gestionnaire Python ultra-rapide, ~10-100× plus rapide que `pip`. Il remplace `pip`, `pip-tools`, `pyenv` et `virtualenv` en un seul outil.

### 10.1 Installer `uv`

```powershell
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 10.2 Setup et lancement

```bash
uv sync
uv run python main.py
```

| Commande | Rôle |
|---|---|
| `uv sync` | Crée `.venv/` et installe les deps depuis `uv.lock` |
| `uv run python main.py` | Lance Python dans le venv (sans avoir à l'activer) |

### 10.3 Toutes les commandes `uv` utiles

| Commande | Rôle |
|---|---|
| `uv sync` | Premier setup ou après un changement de deps |
| `uv sync --frozen` | Idem mais sans modifier `uv.lock` |
| `uv run python main.py` | Lancer un script |
| `uv run python` | REPL interactif (utile pour tester `ChatOllama` manuellement) |
| `uv run python -c "import langchain_ollama; print('OK')"` | Test d'import rapide |
| `uv add nom-package` | Ajouter une dépendance |
| `uv remove nom-package` | Supprimer |
| `uv lock` | Re-générer `uv.lock` |
| `uv lock --upgrade` | Mettre à jour toutes les deps |
| `uv tree` | Arbre des dépendances |
| `uv pip list` | Lister les packages installés |
| `uv cache clean` | Nettoyer le cache |

[↑ retour en haut](#top)

---

<a id="section-11"></a>

## 11. Méthode C — Exécution avec Docker

> [!IMPORTANT]
> Ollama tourne sur ton **hôte** (Windows / macOS / Linux), pas dans le conteneur. Le conteneur doit donc atteindre l'hôte. Sur **Windows et macOS**, Docker Desktop fournit `host.docker.internal` automatiquement. Sur **Linux**, il faut l'ajouter manuellement.

### 11.1 Vérifie que `main.py` a bien le `base_url`

Dans la [section 7](#section-7), tu as déjà mis `base_url="http://host.docker.internal:11434"`. C'est crucial.

### 11.2 (Linux uniquement) Ajoute `extra_hosts` au `docker-compose.yml`

Le `docker-compose.yml` du projet contient déjà cette config par sécurité :

```yaml
services:
  app:
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

Si elle n'y est pas, ajoute-la sous `app:`.

### 11.3 Mode foreground (par défaut)

```bash
docker compose up --build
```

| Comportement | Détail |
|---|---|
| Logs | S'affichent en **direct dans ton terminal** |
| `Ctrl+C` | Stoppe le conteneur |
| Ton terminal | **Bloqué** tant que le conteneur tourne |
| Idéal pour | Voir la sortie une fois, débugger |

### 11.4 Mode détaché (`-d`)

```bash
docker compose up --build -d
```

| Comportement | Détail |
|---|---|
| Logs | **Pas affichés** (utilise `docker compose logs`) |
| `Ctrl+C` | Ne fait rien |
| Ton terminal | **Libéré immédiatement** |
| Idéal pour | Services longs (ex : Ollama lui-même si tu le mettais dans le compose) |

> [!IMPORTANT]
> Pour ce projet, `main.py` se termine en quelques secondes. `-d` est donc surtout utile si tu veux tester puis basculer en mode interactif via `docker compose exec`.

### 11.5 Différence `--build` vs sans `--build`

| Commande | Action |
|---|---|
| `docker compose up --build` | Reconstruit l'image avant lancement (utile quand `Dockerfile` ou `pyproject.toml` changent) |
| `docker compose up` | Réutilise l'image (bind mount permet de modifier `main.py` sans rebuild) |
| `docker compose build --no-cache` | Reconstruction complète sans cache |

### 11.6 Toutes les commandes Docker utiles

| Commande | Rôle |
|---|---|
| `docker compose up --build` | Build + run foreground |
| `docker compose up --build -d` | Build + run détaché |
| `docker compose up` | Run sans rebuild (foreground) |
| `docker compose up -d` | Run sans rebuild (détaché) |
| `docker compose logs -f` | Suivre les logs en direct |
| `docker compose logs --tail=50` | 50 dernières lignes |
| `docker compose ps` | Voir les conteneurs |
| `docker compose stop` / `start` / `restart` | Cycle de vie |
| `docker compose down` | Stop + supprime |
| `docker compose down -v` | + supprime les volumes |
| `docker compose run --rm -it app bash` | Shell interactif (voir [§ 11b](#section-11b)) |
| `docker compose exec app bash` | Shell dans un conteneur déjà en marche |

> [!TIP]
> Vérifie qu'Ollama tourne **sur l'hôte** AVANT de lancer Docker (`ollama serve` doit être actif). Tu peux tester depuis l'hôte avec `curl http://localhost:11434/api/tags` et depuis l'intérieur du conteneur avec `curl http://host.docker.internal:11434/api/tags` (cf [§ 11b.3](#section-11b)).

[↑ retour en haut](#top)

---

<a id="section-11b"></a>

## 11b. Méthode D — Mode interactif : entrer dans le conteneur et lancer `main.py` à la main

> [!TIP]
> **Pourquoi faire ça ?** Avec `docker compose up`, le conteneur démarre, exécute `python main.py`, puis **s'arrête**. Tu vois la sortie une fois et c'est fini. Le mode interactif te laisse **rester dans le conteneur** : tu peux relancer `main.py` autant de fois que tu veux (gratuit avec Ollama !), tester la connexion à Ollama avec `curl`, vérifier l'environnement, débugger.

### 11b.1 Pourquoi `docker exec` ne marche pas directement

Le réflexe Google c'est :

```bash
docker compose up -d                        # demarrer en arriere-plan
docker exec -it langchain-hello-world bash  # entrer dans le conteneur
```

Mais ça **échoue** : `docker compose up` lance `python main.py` (le `CMD` du `Dockerfile`), `main.py` se termine, le conteneur **s'arrête**. Donc `docker exec` ne trouve plus rien à entrer dedans.

```bash
docker ps        # le conteneur n'est plus la
docker ps -a     # status "Exited (0)"
```

> [!NOTE]
> `docker exec` fonctionne **uniquement** sur un conteneur en cours d'exécution.

### 11b.2 Solution recommandée : `docker compose run` (override du CMD)

```bash
docker compose run --rm -it app bash
```

Décortiquons :

| Argument | Rôle |
|---|---|
| `run` | Lance le service en mode one-shot |
| `--rm` | Supprime le conteneur quand tu en sors |
| `-it` | `-i` interactif + `-t` TTY = vrai terminal |
| `app` | Nom du **service** dans `docker-compose.yml` (PAS le `container_name`) |
| `bash` | Commande exécutée à la place de `python main.py` |

Après cette commande, tu es dans le conteneur :

```
root@a1b2c3d4e5f6:/app#
```

### 11b.3 Vérifier qu'Ollama est joignable depuis le conteneur

C'est la **chose la plus utile** quand on débugge la voie Ollama : confirmer que le conteneur arrive bien à parler à Ollama qui tourne sur l'hôte.

```bash
# 1. Verifier que la machine hote est joignable
ping -c 2 host.docker.internal
# Reponse : 64 bytes from host.docker.internal ...

# 2. Verifier que le port 11434 d'Ollama repond
curl http://host.docker.internal:11434/api/tags
# Reponse JSON : {"models":[{"name":"gemma3:270m",...}]}
```

Si `curl` retourne `Connection refused`, c'est qu'Ollama n'est pas démarré sur ton hôte (`ollama serve`) ou que le pare-feu Windows bloque la connexion entrante du conteneur Docker (rare mais possible).

```bash
# 3. Verifier les autres infos pratiques
pwd                                                # /app
ls -la                                             # main.py, pyproject.toml, .env...
python --version                                   # Python 3.12.13
python -c "import langchain_ollama; print('OK')"   # OK
```

### 11b.4 Lancer `main.py` manuellement

```bash
python main.py
```

Tu vois le Hello World + le résumé d'Elon Musk généré par Ollama. **Aucun coût** (le LLM tourne sur ton hôte).

### 11b.5 Relancer plusieurs fois

```bash
python main.py     # appel 1 (gratuit)
python main.py     # appel 2 (gratuit)
python main.py     # appel 3 (gratuit)
```

Avec Ollama, tu peux relancer **autant de fois que tu veux** sans aucune facturation. Idéal pour tester rapidement des modifs de prompt.

### 11b.6 Modifier `main.py` depuis l'intérieur

Le volume `volumes: .:/app` dans le compose monte ton dossier hôte sur `/app`. Donc toute modification de `main.py` sur ton ordinateur est **immédiatement visible** dans le conteneur, sans rebuild.

```bash
# Sur ton hote (autre terminal), edite main.py.
# Puis dans le conteneur :
python main.py     # voit la nouvelle version
```

### 11b.7 Tester un autre modèle Ollama sans modifier main.py

```bash
# Dans le conteneur, en Python interactif :
python
```

```python
>>> from langchain_ollama import ChatOllama
>>> llm = ChatOllama(model="qwen3:1.7b", base_url="http://host.docker.internal:11434")
>>> print(llm.invoke("Resume Elon Musk en 2 phrases.").content)
>>> exit()
```

> [!IMPORTANT]
> Le modèle (`qwen3:1.7b` ici) doit avoir été préalablement téléchargé sur l'hôte avec `ollama pull qwen3:1.7b`.

### 11b.8 Sortir du conteneur

```bash
exit
```

`--rm` supprime automatiquement le conteneur.

### 11b.9 Mémo : tableau récapitulatif

| Commande | Quand l'utiliser | Résultat |
|---|---|---|
| `docker compose up --build` | Voir la sortie de `main.py` une fois | Build, run, exit |
| `docker compose up` | Idem sans rebuild | Run, exit |
| `docker compose run --rm -it app bash` | **Explorer / relancer / tester** | Shell interactif, gratuit avec Ollama |
| `curl http://host.docker.internal:11434/api/tags` | Tester la connexion Ollama depuis le conteneur | Liste des modèles dispo |
| `docker compose down` | Tout nettoyer | Stop + supprime |

[↑ retour en haut](#top)

---

<a id="section-12"></a>

## 12. Sortie attendue

```
Hello from langchain-course!
content='1. Short summary: Elon Musk is a businessman known for leading Tesla, SpaceX...
2. Two interesting facts:
   - He was born in Pretoria, South Africa in 1971...
   - He co-founded PayPal which was acquired by eBay in 2002...' additional_kwargs={} response_metadata={'model': 'gemma3:270m', ...}
```

> [!NOTE]
> Avec un petit modèle comme `gemma3:270m`, la qualité est notablement inférieure à `gpt-4o-mini`. Tu peux observer des incohérences, des fautes ou des réponses incomplètes. Pour une qualité supérieure, voir la [section 13](#section-13).

[↑ retour en haut](#top)

---

<a id="section-13"></a>

## 13. Choix du modèle Ollama (`gemma3:270m`, `qwen3:1.7b`, etc.)

| Modèle | Taille | RAM minimum | Qualité | Vitesse CPU | Quand l'utiliser |
|---|---|---|---|---|---|
| `gemma3:270m` | 290 Mo | 1 Go | Basique | Très rapide | Démos, démarrage rapide |
| `qwen3:1.7b` | 1,4 Go | 4 Go | Bonne pour la taille | Rapide | Tests réalistes, agents simples |
| `llama3.2:3b` | 2 Go | 6 Go | Très correcte | Modéré | Cours, prototypes |
| `qwen3:8b` | 5 Go | 10 Go | Excellente | Lent sans GPU | Tâches plus complexes |
| `mistral:7b` | 4 Go | 8 Go | Excellente, polyvalent | Lent sans GPU | Polyvalent |
| `qwen3:14b` | 8 Go | 16 Go | Quasi GPT-4o | Très lent sans GPU | Si tu as une grosse machine |

Pour télécharger un autre modèle :

```bash
ollama pull qwen3:1.7b
```

Puis dans `main.py`, change la ligne :

```python
llm = ChatOllama(temperature=0, model="qwen3:1.7b")
```

> [!TIP]
> Tu peux garder plusieurs modèles installés en parallèle. `ollama list` te montre tout ce que tu as. `ollama rm <modèle>` supprime ceux dont tu n'as plus besoin pour libérer du disque.

[↑ retour en haut](#top)

---

<a id="section-14"></a>

## 14. Pièges spécifiques à Ollama

| Erreur | Diagnostic | Solution |
|---|---|---|
| `Connection refused: localhost:11434` | Ollama n'est pas démarré | Lance `ollama serve` (ou ouvre l'app sur Win/Mac) |
| `model 'gemma3:270m' not found` | Modèle pas téléchargé | `ollama pull gemma3:270m` |
| Docker : `Connection refused: host.docker.internal:11434` | Le conteneur n'atteint pas l'hôte | Vérifier `extra_hosts` dans `docker-compose.yml` (Linux) ou redémarrer Docker Desktop (Windows/Mac) |
| Réponse extrêmement lente | Modèle trop gros pour ton CPU/RAM | Prendre un modèle plus petit (voir section 13) |
| `out of memory` | Pas assez de RAM | Modèle plus petit, fermer d'autres applications |
| Réponse incohérente / hallucinations massives | Limite du petit modèle | Essayer `qwen3:1.7b` ou `llama3.2:3b` |
| `main.py` utilise toujours OpenAI | Tu n'as pas commenté `ChatOpenAI` ligne 34 | Re-vérifier la [section 7](#section-7) |

[↑ retour en haut](#top)

---

<a id="section-15"></a>

## 15. Combien ça consomme (RAM, disque, CPU/GPU)

Pour `gemma3:270m` qui tourne sur ce projet :

| Ressource | Au repos | Pendant l'inférence |
|---|---|---|
| Disque | 290 Mo (modèle) | idem |
| RAM | ~50 Mo (Ollama daemon) | ~500 Mo - 1 Go (chargement modèle + contexte) |
| CPU | <5 % | 50-100 % pendant 1-3 secondes |
| GPU (si NVIDIA / Apple) | 0 % | 30-80 % pendant <1 seconde |

> [!NOTE]
> Une fois l'inférence finie, le modèle reste chargé en RAM ~5 minutes par défaut puis est déchargé. Tu peux ajuster avec `OLLAMA_KEEP_ALIVE=1h` (variable d'environnement) ou `keep_alive` dans l'appel API.

[↑ retour en haut](#top)

---

<a id="section-16"></a>

## 16. Toutes les commandes — cheat-sheet par méthode

Récap exhaustif des commandes pour faire tourner ce projet en mode Ollama. Copie-colle.

### 16.1 Setup commun (à faire une fois)

```bash
# Installer Ollama (voir section 3 pour Windows/macOS/Linux)
# Puis :
ollama --version                          # verifier l'installation

# Tirer le modele
ollama pull gemma3:270m
ollama list                               # confirmer

# Verifier qu'Ollama repond sur localhost
curl http://localhost:11434/api/tags      # liste des modeles

# Aller dans le dossier du code
# Verifier que tu es bien dans le bon dossier (celui qui contient main.py)
ls
# main.py, pyproject.toml, uv.lock, Dockerfile, docker-compose.yml, .env.example...

# Creer le .env (meme avec Ollama, python-dotenv le veut)
cp .env.example .env

# Modifier main.py ligne 33-34 :
#   - commenter ChatOpenAI
#   - decommenter ChatOllama
# Pour Docker, ajouter base_url="http://host.docker.internal:11434"
```

### 16.2 Méthode A — `venv + pip` (toutes les commandes)

```bash
python -m venv .venv

# Activation Windows
.\.venv\Scripts\Activate.ps1
# Activation macOS/Linux
source .venv/bin/activate

# Install et run
pip install --upgrade pip
pip install langchain langchain-openai langchain-ollama python-dotenv
python main.py

# Relancer autant de fois que tu veux (gratuit avec Ollama !)
python main.py
python main.py
python main.py

# Sortir
deactivate
```

### 16.3 Méthode B — `uv` (toutes les commandes)

```bash
# Installer uv (une fois)
# Windows :
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# macOS/Linux :
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup
uv sync
uv sync --frozen

# Lancement
uv run python main.py

# Relancer (gratuit)
uv run python main.py

# REPL interactif Python (pour tester un autre modele Ollama)
uv run python
# >>> from langchain_ollama import ChatOllama
# >>> llm = ChatOllama(model="qwen3:1.7b")
# >>> print(llm.invoke("Hello").content)
# >>> exit()

# Test d'import
uv run python -c "import langchain_ollama; print('OK')"

# Gestion des deps
uv add nom-package
uv remove nom-package
uv lock --upgrade
uv tree
uv pip list
```

### 16.4 Méthode C — Docker foreground (toutes les commandes)

```bash
# Verifier qu'Ollama tourne sur l'hote AVANT
ollama serve                              # si pas deja lance (autre terminal)

# Build + run en foreground
docker compose up --build

# Run sans rebuild
docker compose up

# Sortir : Ctrl+C
# Nettoyage
docker compose down
```

### 16.5 Méthode C bis — Docker détaché (`-d`)

```bash
# Build + run en arriere-plan
docker compose up --build -d

# Run sans rebuild
docker compose up -d

# Voir les logs
docker compose logs
docker compose logs -f                    # suivre
docker compose logs --tail=50

# Etat des conteneurs
docker compose ps

# Cycle de vie
docker compose stop
docker compose start
docker compose restart

# Nettoyage
docker compose down
docker compose down -v                    # + volumes
docker compose down --rmi all             # + images
```

### 16.6 Méthode D — Mode interactif Docker

```bash
# Entrer dans un shell bash du conteneur
docker compose run --rm -it app bash

# A l'interieur :
pwd
ls -la
ping -c 2 host.docker.internal            # verifier que l'hote est joignable
curl http://host.docker.internal:11434/api/tags  # verifier qu'Ollama repond
python --version
python -c "import langchain_ollama; print('OK')"
python main.py                            # relance manuelle 1 (gratuit)
python main.py                            # relance 2 (gratuit)
python main.py                            # relance 3 (gratuit)
exit

# Variante : si conteneur deja en marche (apres docker compose up -d)
docker compose exec app bash
```

### 16.7 Méthode D bis — `docker exec` (cas avancé)

```bash
# Demarrer un conteneur en sleep infinity
docker compose run -d --name hello-shell --entrypoint sleep app infinity

# Entrer
docker exec -it hello-shell bash
python main.py
exit                                      # le conteneur continue de tourner

# Stopper et supprimer manuellement
docker stop hello-shell
docker rm hello-shell
```

### 16.8 Gestion des modèles Ollama

```bash
# Lister les modeles installes
ollama list

# Telecharger un modele
ollama pull gemma3:270m
ollama pull qwen3:1.7b
ollama pull llama3.2:3b

# Tester un modele en CLI directement
ollama run gemma3:270m "Hello"
ollama run gemma3:270m                    # mode interactif

# Supprimer un modele pour liberer du disque
ollama rm gemma3:270m

# Voir les details d'un modele
ollama show gemma3:270m

# Demarrer / stopper le serveur Ollama
ollama serve                              # foreground
# Sur Windows/macOS, l'app demarre Ollama automatiquement
```

### 16.9 Diagnostic rapide

```bash
# Versions
python --version
uv --version
ollama --version
docker --version
docker compose version

# Test connexion Ollama (depuis l'hote)
curl http://localhost:11434/api/tags

# Test connexion Ollama (depuis le conteneur)
docker compose run --rm -it app bash -c "curl -s http://host.docker.internal:11434/api/tags"

# Espace disque Docker
docker system df

# Conteneurs (running + stopped)
docker ps -a
```

[↑ retour en haut](#top)

---

<a id="section-17"></a>

## 17. Conclusion et étapes suivantes

Tu sais maintenant :

- Installer Ollama et télécharger un modèle local.
- Faire tourner LangChain **sans clé API et sans coût**.
- Choisir un modèle adapté à ta machine.
- Diagnostiquer les pannes Ollama.

**Avantages d'Ollama** :
- Gratuit, illimité, hors ligne après le pull.
- Confidentialité : aucune donnée ne sort de ton ordinateur.
- Idéal pour expérimenter, prototyper, apprendre.

**Limites** :
- Qualité moindre vs GPT-5 (sauf modèles 14B+ avec GPU).
- Lent sur CPU pur.
- Certains modules avancés (Module 4 RAG, Module 8 Agentic RAG) supposent un LLM puissant ; Ollama peut donner des résultats décevants.

**Ressources de ce module** :
- [Module 0 — Introduction vulgarisée à LangChain et l'IA agentique](./Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md)
- [Module 0 — Quiz de validation (50 questions)](./Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md)
- [Module 0 — Pratique 1 : Hello World avec OpenAI (avec crédit)](./Module-00-pratique-1-OpenAI-clef-API.md) ← si tu veux tester avec un meilleur modèle
- [Module 0 — Résumé des commandes](./Module-00-resume-commandes-hello-world-LangChain.md)

**Module suivant** : [Module 2 — Search Agent](../02-langchain-course-project-search-agent/01-cours.md) — passe d'un simple appel LLM à un agent capable d'utiliser des outils externes.

[↑ retour en haut](#top)
