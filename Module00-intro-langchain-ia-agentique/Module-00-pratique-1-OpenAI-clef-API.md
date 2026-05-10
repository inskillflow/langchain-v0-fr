<a id="top"></a>

# Module 0 — Pratique 1 : Hello World avec OpenAI (clé API + crédit requis)

> [!IMPORTANT]
> **Cette voie coûte de l'argent.** OpenAI facture chaque appel à un modèle (par exemple `gpt-4o-mini` ≈ 0,15 $ par million de tokens en entrée). Tu dois **créer un compte OpenAI**, **ajouter une carte bancaire** et **mettre au minimum 5 $ de crédit** pour que le moindre appel fonctionne. Sans crédit, tu obtiens l'erreur `429 insufficient_quota` et **rien ne marchera**, même avec une clé valide.
>
> Si tu ne veux **pas** payer, va plutôt voir la **[Pratique 2 — Hello World avec Ollama local (gratuit)](./Module-00-pratique-2-Ollama-local.md)**.

---

## Table des matières

| # | Section |
|---|---------|
| 1 | [Objectifs](#section-1) |
| 2 | [Prérequis matériels et financiers](#section-2) |
| 3 | [Étape 1 — Créer un compte OpenAI](#section-3) |
| 4 | [Étape 2 — Ajouter du crédit (le passage obligé)](#section-4) |
| 5 | [Étape 3 — Récupérer ta clé API](#section-5) |
| 6 | [Étape 4 — Cloner / aller dans le projet](#section-6) |
| 7 | [Étape 5 — Configurer le `.env`](#section-7) |
| 8 | [Méthode A — Exécution avec `venv + pip`](#section-8) |
| 9 | [Méthode B — Exécution avec `uv`](#section-9) |
| 10 | [Méthode C — Exécution avec Docker](#section-10) |
| 10b | [Méthode D — Mode interactif : entrer dans le conteneur](#section-10b) |
| 11 | [Sortie attendue](#section-11) |
| 12 | [Choix du modèle (`gpt-4o-mini` vs `gpt-5`)](#section-12) |
| 13 | [Pièges spécifiques à OpenAI](#section-13) |
| 14 | [Combien ça coûte vraiment ?](#section-14) |
| 15 | [Toutes les commandes — cheat-sheet par méthode](#section-15) |
| 16 | [Conclusion et étapes suivantes](#section-16) |

---

<a id="section-1"></a>

## 1. Objectifs

À la fin de cette pratique, tu sauras :

- Créer un compte OpenAI et y mettre du crédit.
- Récupérer une clé API et la stocker proprement dans un `.env`.
- Lancer le projet `langchain-course-project-hello-world` en **3 méthodes distinctes** : `venv + pip` (classique), `uv` (moderne), Docker (isolé).
- Diagnostiquer les erreurs OpenAI courantes (`insufficient_quota`, `model not found`, `AuthenticationError`).
- Comprendre combien tu dépenses par appel.

[↑ retour en haut](#top)

---

<a id="section-2"></a>

## 2. Prérequis matériels et financiers

| Prérequis | Commentaire |
|---|---|
| Un ordinateur (Windows, macOS, Linux) | RAM 4 Go suffisant, l'inférence se fait chez OpenAI |
| Python 3.11 ou 3.12 | `python --version` |
| `git` | Pour cloner si tu n'as pas le projet |
| Une **carte bancaire** | Obligatoire pour OpenAI |
| **5 USD de crédit minimum** | Ajouter sur https://platform.openai.com/settings/organization/billing |
| Docker Desktop (optionnel) | Pour la méthode C |

> [!WARNING]
> OpenAI **n'offre plus** de crédit gratuit en 2026 pour les nouveaux comptes (l'ancienne offre de 5 $ a disparu). Si tu n'as **jamais** payé chez OpenAI, tu dois ajouter une carte et acheter du crédit. La plus petite recharge possible est généralement de **5 $**.

[↑ retour en haut](#top)

---

<a id="section-3"></a>

## 3. Étape 1 — Créer un compte OpenAI

1. Va sur https://platform.openai.com/signup
2. Inscris-toi avec un email + mot de passe (ou via Google / Microsoft / Apple).
3. Vérifie ton email (lien de confirmation).
4. Connecte-toi sur https://platform.openai.com/

> [!NOTE]
> Le compte ChatGPT (chat.openai.com) et le compte API (platform.openai.com) **partagent ton login** mais sont **deux services facturés séparément**. L'abonnement ChatGPT Plus à 20 $/mois **ne te donne aucun crédit API**.

[↑ retour en haut](#top)

---

<a id="section-4"></a>

## 4. Étape 2 — Ajouter du crédit (le passage obligé)

C'est l'étape qui bloque tout le monde. Voici la procédure exacte :

1. Ouvre https://platform.openai.com/settings/organization/billing/overview
2. Clique sur **"Add payment details"** ou **"Add to credit balance"**.
3. Renseigne ta carte bancaire (Visa / Mastercard / Amex acceptées, certaines cartes prépayées peuvent être refusées).
4. Choisis un montant : **5 USD minimum**, recommandé pour ce cours : **10 USD** (te durera très longtemps avec `gpt-4o-mini`).
5. Confirme l'achat.

> [!IMPORTANT]
> **Décoche** l'option **"Auto recharge"** sauf si tu veux que ton compte se recharge automatiquement. Pour un cours, manuel suffit largement.

> [!TIP]
> Définis aussi une **limite mensuelle** (Usage limits → Set monthly budget) à 5 USD pour t'éviter de mauvaises surprises. Ça coupe l'accès si tu dépasses.

### Vérifier que le crédit est bien là

Sur https://platform.openai.com/settings/organization/billing/overview, tu dois voir **"Credit balance: $X.XX"** avec un montant **> 0**.

Tant que ça affiche `$0.00`, **tous tes appels API échoueront** avec :

```
openai.RateLimitError: Error code: 429 - 'insufficient_quota'
```

[↑ retour en haut](#top)

---

<a id="section-5"></a>

## 5. Étape 3 — Récupérer ta clé API

1. Va sur https://platform.openai.com/api-keys
2. Clique **"Create new secret key"**.
3. Donne-lui un nom mémorable (ex : `langchain-course-hello-world`).
4. **Copie immédiatement** la clé (commence par `sk-proj-...`). Elle ne sera **plus jamais réaffichée**.
5. Si tu la perds, supprime-la et recrée-en une.

> [!WARNING]
> **Ne commit jamais** une clé API dans Git. Le fichier `.env` doit être dans `.gitignore` (c'est déjà le cas dans ce projet). Si tu pushes une clé par erreur, OpenAI la **détecte automatiquement** dans les minutes qui suivent et la révoque (et tu reçois un email).

[↑ retour en haut](#top)

---

<a id="section-6"></a>

## 6. Étape 4 — Aller dans le projet

```bash
cd repositories/Module00-intro-langchain-ia-agentique/langchain-course-project-hello-world
```

Vérifie que tu vois ces fichiers :

```bash
ls
# main.py, pyproject.toml, uv.lock, Dockerfile, docker-compose.yml,
# .env.example, .python-version, README.md
```

[↑ retour en haut](#top)

---

<a id="section-7"></a>

## 7. Étape 5 — Configurer le `.env`

Copie le gabarit :

```bash
cp .env.example .env
```

Ouvre `.env` et colle ta clé API :

```
OPENAI_API_KEY=sk-proj-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

> [!NOTE]
> Le `.env` doit être dans le **dossier intérieur** (`langchain-course-project-hello-world/`), **pas** à la racine du cours. C'est l'emplacement où `main.py` cherche les variables d'environnement.

[↑ retour en haut](#top)

---

<a id="section-8"></a>

## 8. Méthode A — Exécution avec `venv + pip` (classique)

```bash
python -m venv .venv
```

Active l'environnement virtuel :

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Installe les dépendances et lance :

```bash
pip install --upgrade pip
pip install langchain langchain-openai langchain-ollama python-dotenv
python main.py
```

Pour désactiver à la fin :

```bash
deactivate
```

[↑ retour en haut](#top)

---

<a id="section-9"></a>

## 9. Méthode B — Exécution avec `uv` (recommandée)

`uv` est un gestionnaire Python ultra-rapide qui remplace `pip`, `pip-tools`, `pyenv` et `virtualenv` en un seul outil. Il est ~10-100× plus rapide que `pip`.

### 9.1 Installer `uv`

```powershell
# Windows PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Vérifier l'installation :

```bash
uv --version
# uv 0.5.x ou plus recent
```

### 9.2 Installer les dépendances + lancer

```bash
uv sync
uv run python main.py
```

| Commande | Rôle |
|---|---|
| `uv sync` | Lit `pyproject.toml` + `uv.lock`, crée `.venv/` automatiquement, installe toutes les deps |
| `uv run python main.py` | Lance Python dans le venv créé (sans avoir à l'activer manuellement) |

### 9.3 Toutes les commandes `uv` utiles pour ce projet

| Commande | Quand l'utiliser |
|---|---|
| `uv sync` | Premier setup ou après pull d'un changement de deps |
| `uv sync --frozen` | Comme `uv sync` mais sans recréer le `uv.lock` (= équivalent du Docker) |
| `uv run python main.py` | Lancer un script en respectant `.venv/` |
| `uv run python` | Ouvrir un REPL Python interactif dans le venv |
| `uv run python -c "import langchain; print(langchain.__version__)"` | Tester un import rapide |
| `uv add nom-package` | Ajouter une nouvelle dépendance (modifie `pyproject.toml` + `uv.lock`) |
| `uv add --dev pytest` | Ajouter une dép de dev (groupe `dev`) |
| `uv remove nom-package` | Supprimer une dépendance |
| `uv lock` | Re-générer `uv.lock` à partir de `pyproject.toml` |
| `uv lock --upgrade` | Mettre à jour toutes les deps vers leur dernière version compatible |
| `uv tree` | Voir l'arbre des dépendances |
| `uv pip list` | Lister les packages installés (compatible `pip list`) |
| `uv venv` | Créer un venv vide (sans installer) — rarement nécessaire car `uv sync` le fait tout seul |
| `uv cache clean` | Nettoyer le cache de packages téléchargés |

### 9.4 Activer le venv créé par `uv` (optionnel)

Pas obligatoire si tu utilises `uv run`, mais pratique pour des sessions longues :

```powershell
# Windows
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Une fois activé, tu peux lancer `python main.py` directement sans `uv run`.

[↑ retour en haut](#top)

---

<a id="section-10"></a>

## 10. Méthode C — Exécution avec Docker

> [!NOTE]
> Le `Dockerfile` télécharge Python 3.12-slim, installe `uv`, copie `pyproject.toml` + `uv.lock`, fait `uv sync --frozen`, puis lance `python main.py`. Le `.env` est passé via `env_file:` dans `docker-compose.yml`.

### 10.1 Mode foreground (attaché) — par défaut

```bash
docker compose up --build
```

| Comportement | Détail |
|---|---|
| Logs | S'affichent en **direct dans ton terminal** |
| `Ctrl+C` | Stoppe le conteneur |
| Ton terminal | **Bloqué** tant que le conteneur tourne |
| Idéal pour | Voir la sortie une fois, débugger |

### 10.2 Mode détaché (background) — `-d`

```bash
docker compose up --build -d
```

| Comportement | Détail |
|---|---|
| Logs | **Pas affichés** automatiquement (utilise `docker compose logs`) |
| `Ctrl+C` | Ne fait rien (le conteneur tourne en arrière-plan) |
| Ton terminal | **Libéré immédiatement** |
| Idéal pour | Services longs (web app, API), CI, scripts |

> [!IMPORTANT]
> **Pour le projet Hello World, `-d` n'est PAS l'idéal** car `main.py` se termine en quelques secondes. Tu verrais juste « démarré, exit code 0 » sans le contenu. Utilise `-d` plutôt avec des serveurs (Module 4 RAG avec Pinecone, Module 8 Agentic RAG, etc.).

### 10.3 Différence `--build` vs sans `--build`

| Commande | Action |
|---|---|
| `docker compose up --build` | Reconstruit l'image **avant** de lancer (à utiliser quand `Dockerfile`, `pyproject.toml` ou `uv.lock` changent) |
| `docker compose up` | Réutilise l'image existante (plus rapide, à utiliser quand seul le code Python change — le bind mount `volumes: .:/app` rend `--build` inutile dans ce cas) |
| `docker compose build --no-cache` | Force une reconstruction complète sans cache (à utiliser si le cache est corrompu ou pour rebuild propre) |

### 10.4 Toutes les commandes Docker utiles pour ce projet

| Commande | Rôle |
|---|---|
| `docker compose up --build` | Build + run en foreground |
| `docker compose up --build -d` | Build + run en arrière-plan |
| `docker compose up` | Run sans rebuild (foreground) |
| `docker compose up -d` | Run sans rebuild (arrière-plan) |
| `docker compose logs` | Voir les logs (mode détaché) |
| `docker compose logs -f` | Suivre les logs en direct (`-f` = follow, comme `tail -f`) |
| `docker compose logs --tail=50` | Voir les 50 dernières lignes |
| `docker compose ps` | Voir les conteneurs du projet (running ou stopped) |
| `docker compose stop` | Arrête les conteneurs sans les supprimer |
| `docker compose start` | Redémarre les conteneurs déjà créés |
| `docker compose restart` | Stop + start |
| `docker compose down` | Stop + supprime conteneurs, réseau, volumes anonymes |
| `docker compose down -v` | Idem + supprime aussi les volumes nommés (efface les données) |
| `docker compose down --rmi all` | Idem + supprime les images |
| `docker compose build` | Build l'image sans la lancer |
| `docker compose build --no-cache` | Build sans utiliser le cache (rebuild complet) |
| `docker compose pull` | Re-télécharger les images de base |
| `docker compose run --rm -it app bash` | Shell interactif (voir [§ 10b](#section-10b)) |
| `docker compose exec app bash` | Shell dans un conteneur **déjà en marche** (ex : après `up -d`) |

### 10.5 Workflow typique avec `-d` (cas avancé)

Si tu veux quand même tester `-d` avec ce projet, voici un workflow utile :

```bash
# 1. Lancer en arriere-plan (le conteneur s'arrete tout de suite car main.py se termine)
docker compose up --build -d

# 2. Voir ce qui s'est passe
docker compose logs

# 3. Voir si le conteneur tourne encore (probablement non)
docker compose ps

# 4. Pour relancer sans rebuild
docker compose up -d

# 5. Pour tout nettoyer
docker compose down
```

Pour des services qui doivent rester actifs (ex : Ollama, Postgres, Redis), `-d` est la norme. Pour un script one-shot comme `main.py`, le foreground est plus pédagogique.

[↑ retour en haut](#top)

---

<a id="section-10b"></a>

## 10b. Méthode D — Mode interactif : entrer dans le conteneur et lancer `main.py` à la main

> [!TIP]
> **Pourquoi faire ça ?** Avec `docker compose up`, le conteneur démarre, exécute `python main.py`, puis **s'arrête**. Tu vois la sortie une fois et c'est fini. Le mode interactif te laisse **rester dans le conteneur** : tu peux relancer `main.py` autant de fois que tu veux, inspecter les variables d'environnement, vérifier que tes packages sont bien installés, débugger. C'est exactement comme une session SSH dans un mini-Linux jetable.

### 10b.1 Pourquoi `docker exec` ne marche pas directement avec ce projet

Le réflexe Google c'est :

```bash
docker compose up -d                        # demarrer en arriere-plan
docker exec -it langchain-hello-world bash  # entrer dans le conteneur
```

Mais ça **échoue** : `docker compose up` lance `python main.py` (le `CMD` du `Dockerfile`), `main.py` se termine, le conteneur **s'arrête**. Donc `docker exec` ne trouve plus rien à entrer dedans.

```bash
docker ps        # le conteneur n'est plus la
docker ps -a     # il est en status "Exited (0)"
```

> [!NOTE]
> `docker exec` fonctionne **uniquement sur un conteneur en cours d'exécution**. Pour un conteneur arrêté, c'est `docker start` qu'il faut.

### 10b.2 Solution recommandée : `docker compose run` (override du CMD)

`docker compose run` lance le service en remplaçant la commande par défaut. Tu remplaces `python main.py` par `bash` pour avoir un shell.

```bash
docker compose run --rm -it app bash
```

Décortiquons :

| Argument | Rôle |
|---|---|
| `run` | Lance le service en mode one-shot (au lieu de `up` qui orchestre tout) |
| `--rm` | Supprime le conteneur quand tu en sors (sinon il s'accumule) |
| `-it` | `-i` = interactif (stdin ouvert), `-t` = TTY (un vrai terminal). À combiner. |
| `app` | Le **nom du service** dans `docker-compose.yml` (PAS le `container_name`) |
| `bash` | La commande à exécuter dans le conteneur, à la place de `python main.py` |

> [!IMPORTANT]
> `app` est le nom du service défini dans `docker-compose.yml` (`services: app:`). `langchain-hello-world` c'est le `container_name` qui s'applique seulement avec `docker compose up`. Avec `docker compose run`, Docker crée un conteneur jetable nommé automatiquement.

Après cette commande, ton prompt change et tu es **à l'intérieur** du conteneur Linux :

```
root@a1b2c3d4e5f6:/app#
```

### 10b.3 Que faire une fois à l'intérieur

```bash
# 1. Verifier ou tu es
pwd
# /app

# 2. Lister les fichiers du projet
ls -la
# main.py, pyproject.toml, uv.lock, Dockerfile, docker-compose.yml, .env, .venv...

# 3. Verifier que la cle OpenAI est bien chargee depuis .env
env | grep OPENAI
# OPENAI_API_KEY=sk-proj-xxxxx

# 4. Verifier la version de Python utilisee
python --version
# Python 3.12.13

# 5. Verifier que langchain est bien installe
python -c "import langchain; print(langchain.__version__)"
# 1.2.7 (ou plus recent)

# 6. ENFIN : lancer main.py manuellement
python main.py
```

Tu vois la sortie de `main.py` (le Hello World + le résumé d'Elon Musk). Et **tu restes dans le conteneur**, prêt à le relancer.

### 10b.4 Relancer plusieurs fois sans recompiler

```bash
python main.py     # appel 1
python main.py     # appel 2 (chaque appel coute un peu d'argent OpenAI)
python main.py     # appel 3
```

> [!WARNING]
> **Chaque** `python main.py` consomme du crédit OpenAI (~0.0005 USD avec `gpt-4o-mini`, ~0.015 USD avec `gpt-5`). Évite les boucles infinies par accident.

### 10b.5 Modifier `main.py` depuis l'intérieur

Le `docker-compose.yml` monte ton dossier hôte sur `/app` (`volumes: .:/app`). Donc toute modification de `main.py` sur ton ordinateur est **immédiatement visible** dans le conteneur, sans rebuild.

```bash
# Sur ton hote (autre terminal), edite main.py avec ton editeur favori.
# Puis dans le conteneur :
python main.py     # voit la nouvelle version directement
```

### 10b.6 Sortir du conteneur

```bash
exit
```

Comme on a passé `--rm`, le conteneur est automatiquement supprimé. Pour vérifier :

```bash
docker ps -a | grep hello-world   # plus rien (ou alors le conteneur de docker compose up s'il existe)
```

### 10b.7 Alternative : garder le conteneur vivant pour `docker exec`

Si tu **insistes** pour utiliser `docker exec`, tu dois lancer le conteneur avec une commande qui ne se termine jamais. Méthode propre :

```bash
# Demarrer le conteneur avec sleep infinity (override du CMD)
docker compose run -d --name hello-shell --entrypoint sleep app infinity

# Maintenant le conteneur tourne indefiniment, tu peux exec dedans
docker exec -it hello-shell bash

# A l'interieur, lance main.py
python main.py

# Sortir (le conteneur continue de tourner !)
exit

# Stopper et supprimer manuellement
docker stop hello-shell
docker rm hello-shell
```

Décomposition des arguments :

| Argument | Rôle |
|---|---|
| `-d` | Mode détaché (lance en arrière-plan) |
| `--name hello-shell` | Nom fixe pour pouvoir le retrouver |
| `--entrypoint sleep` | Remplace l'entrypoint par `sleep` |
| `infinity` | Argument passé à `sleep` : dort à l'infini |

> [!TIP]
> Dans 90 % des cas, `docker compose run --rm -it app bash` (méthode 10b.2) est plus simple et plus propre. Utilise `docker exec` si tu veux **plusieurs shells simultanés** dans le même conteneur ou si un service tourne déjà via `docker compose up -d` (cas plus avancé que ce projet ne couvre pas).

### 10b.8 Mémo : tableau récapitulatif

| Commande | Quand l'utiliser | Ce qui se passe |
|---|---|---|
| `docker compose up --build` | Tu veux juste voir la sortie de `main.py` une fois | Build l'image, run, `python main.py`, exit |
| `docker compose up` | Idem mais sans rebuild | Run, `python main.py`, exit |
| `docker compose run --rm -it app bash` | Tu veux explorer / relancer plusieurs fois | Shell interactif dans le conteneur, `--rm` nettoie en sortant |
| `docker exec -it <name> bash` | Tu as déjà un conteneur qui tourne (méthode 10b.7) | Ouvre un nouveau shell dans un conteneur existant |
| `docker compose down` | Tu veux tout nettoyer | Stop + supprime conteneur, réseau, volumes anonymes |

[↑ retour en haut](#top)

---

<a id="section-11"></a>

## 11. Sortie attendue

```
Hello from langchain-course!
content='1. **Short summary**: Elon Musk is a businessman known for leading Tesla, SpaceX, X (Twitter), and DOGE...
2. **Two interesting facts**:
   - He emigrated from South Africa to Canada in 1989...
   - He was the largest donor in the 2024 U.S. presidential election...' additional_kwargs={...} response_metadata={'token_usage': {'completion_tokens': ..., 'prompt_tokens': ..., 'total_tokens': ...}, 'model_name': 'gpt-4o-mini', ...}
```

Le contenu varie à chaque appel (LLM non-déterministe sauf si `temperature=0`, ce qui est notre cas).

[↑ retour en haut](#top)

---

<a id="section-12"></a>

## 12. Choix du modèle (`gpt-4o-mini` vs `gpt-5`)

Le code par défaut utilise `gpt-5` (ligne 34 de `main.py`) :

```python
llm = ChatOpenAI(temperature=0, model="gpt-5")
```

**Recommandation pour débuter** : remplace par `gpt-4o-mini`, qui est **~30× moins cher** et largement suffisant pour ce projet.

```python
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
```

| Modèle | Prix entrée (1M tokens) | Prix sortie (1M tokens) | Quand l'utiliser |
|---|---|---|---|
| `gpt-4o-mini` | ~0,15 USD | ~0,60 USD | Tout ce qui n'exige pas du raisonnement profond. **Choix par défaut.** |
| `gpt-4o` | ~2,50 USD | ~10,00 USD | Tâches qui demandent de la qualité |
| `gpt-5` | ~5,00 USD | ~15,00 USD | Raisonnement avancé, agents complexes |

> [!TIP]
> Le projet Hello World consomme environ **800 tokens par appel** (prompt + réponse). Avec `gpt-4o-mini`, ça fait ≈ **0,0005 USD par exécution**. Tu peux relancer le projet **20 000 fois** avec 10 USD.

[↑ retour en haut](#top)

---

<a id="section-13"></a>

## 13. Pièges spécifiques à OpenAI

| Erreur | Diagnostic | Solution |
|---|---|---|
| `openai.RateLimitError 429 'insufficient_quota'` | **Pas de crédit** dans le compte | Recharger sur https://platform.openai.com/settings/organization/billing |
| `openai.AuthenticationError 401` | Clé invalide, expirée, ou révoquée | Recréer une clé sur https://platform.openai.com/api-keys et la remettre dans `.env` |
| `openai.NotFoundError: model 'gpt-5' does not exist` | Ton compte n'a pas accès à ce modèle | Remplacer par `gpt-4o-mini` dans `main.py` |
| `openai.APIConnectionError` | Pas d'internet ou pare-feu | Vérifier ta connexion, désactiver temporairement VPN/proxy |
| `openai.BadRequestError 'context_length_exceeded'` | Prompt trop long pour le modèle | Raccourcir le texte d'entrée ou changer de modèle |
| `openai.PermissionDeniedError 403` | Compte vérifié mais accès au modèle bloqué (région, organisation) | Vérifier les paramètres d'organisation, contacter OpenAI |

[↑ retour en haut](#top)

---

<a id="section-14"></a>

## 14. Combien ça coûte vraiment ?

Pour ce projet Hello World **avec `gpt-4o-mini`** :

- 1 exécution ≈ **0,0005 USD** (un demi-millième de dollar)
- 100 exécutions ≈ **0,05 USD** (5 cents)
- 10 USD de crédit ≈ **20 000 exécutions**

Avec `gpt-5` (modèle par défaut du code) :
- 1 exécution ≈ **0,015 USD**
- 10 USD ≈ **~660 exécutions**

> [!NOTE]
> Pour suivre tout le cours (8 modules avec plusieurs appels chacun), **10 USD avec `gpt-4o-mini` suffisent largement**. Garde `gpt-5` pour les modules qui exigent du raisonnement (Module 6 Reflection, Module 7 Reflexion, Module 8 Agentic RAG).

[↑ retour en haut](#top)

---

<a id="section-15"></a>

## 15. Toutes les commandes — cheat-sheet par méthode

Récap exhaustif des commandes pour faire tourner ce projet, regroupées par méthode. Copie-colle.

### 15.1 Setup commun (à faire une fois)

```bash
# Aller dans le dossier du code
cd repositories/Module00-intro-langchain-ia-agentique/langchain-course-project-hello-world

# Creer le .env a partir du gabarit
cp .env.example .env

# Ouvrir .env et coller : OPENAI_API_KEY=sk-proj-XXXXXXXXXXXX
```

### 15.2 Méthode A — `venv + pip` (toutes les commandes)

```bash
# Creation du venv
python -m venv .venv

# Activation Windows PowerShell
.\.venv\Scripts\Activate.ps1
# OU activation macOS/Linux
source .venv/bin/activate

# Installation des deps
pip install --upgrade pip
pip install langchain langchain-openai langchain-ollama python-dotenv

# Lancement
python main.py

# Relance manuelle (autant de fois que tu veux)
python main.py

# Lister les packages installes
pip list

# Sortir du venv
deactivate
```

### 15.3 Méthode B — `uv` (toutes les commandes)

```bash
# Installation de uv (une fois)
# Windows :
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# macOS/Linux :
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup du projet
uv sync                        # cree .venv et installe tout
uv sync --frozen               # idem mais sans modifier uv.lock

# Lancement
uv run python main.py
uv run python main.py          # relance (n fois, chaque appel coute du credit)

# REPL interactif
uv run python

# Test d'import
uv run python -c "import langchain; print(langchain.__version__)"

# Gestion des dependances
uv add nom-package             # ajouter
uv add --dev pytest            # ajouter en dev
uv remove nom-package          # supprimer
uv lock                        # regenerer uv.lock
uv lock --upgrade              # mettre a jour vers les dernieres versions
uv tree                        # arbre des deps
uv pip list                    # lister
uv cache clean                 # nettoyer le cache
```

### 15.4 Méthode C — Docker foreground (toutes les commandes)

```bash
# Build et run en foreground (logs en direct, Ctrl+C arrete tout)
docker compose up --build

# Run sans rebuild (apres le premier --build)
docker compose up

# Sortir : Ctrl+C dans le terminal
# Nettoyage
docker compose down
```

### 15.5 Méthode C bis — Docker détaché (`-d`)

```bash
# Build et run en arriere-plan
docker compose up --build -d

# Run sans rebuild en arriere-plan
docker compose up -d

# Voir les logs apres coup
docker compose logs
docker compose logs -f                    # suivre en direct (Ctrl+C pour quitter)
docker compose logs --tail=50             # 50 dernieres lignes

# Voir les conteneurs du projet
docker compose ps

# Stopper sans supprimer
docker compose stop

# Redemarrer
docker compose start
docker compose restart                    # stop + start

# Tout nettoyer (conteneur + reseau)
docker compose down

# Nettoyer en supprimant aussi les volumes
docker compose down -v

# Nettoyer en supprimant aussi les images
docker compose down --rmi all
```

### 15.6 Méthode D — Mode interactif Docker (`docker compose run`)

```bash
# Entrer dans un shell bash du conteneur (override le CMD)
docker compose run --rm -it app bash

# A l'interieur du conteneur :
pwd                                       # /app
ls -la                                    # voir les fichiers
env | grep OPENAI                         # verifier la cle API
python --version                          # 3.12.13
python -c "import langchain; print(langchain.__version__)"
python main.py                            # relance manuelle 1
python main.py                            # relance 2
python main.py                            # relance 3
exit                                      # sortir, --rm nettoie

# Variante : si un conteneur tourne deja (apres docker compose up -d)
docker compose exec app bash
# ... tes commandes ...
exit
```

### 15.7 Méthode D bis — `docker exec` (cas avancé, conteneur long-running)

```bash
# 1. Demarrer un conteneur qui ne s'arrete jamais
docker compose run -d --name hello-shell --entrypoint sleep app infinity

# 2. Entrer dedans avec docker exec
docker exec -it hello-shell bash
python main.py
exit                                      # sort du shell, conteneur continue

# 3. Pour ouvrir un autre shell dans le meme conteneur (terminal 2)
docker exec -it hello-shell bash

# 4. Stopper et supprimer
docker stop hello-shell
docker rm hello-shell
```

### 15.8 Diagnostic rapide (toutes méthodes)

```bash
# Versions
python --version
uv --version
docker --version
docker compose version

# Variables d'environnement
echo $OPENAI_API_KEY                      # bash/zsh
echo $env:OPENAI_API_KEY                  # PowerShell

# Tester ta cle OpenAI sans LangChain
curl https://api.openai.com/v1/models -H "Authorization: Bearer $OPENAI_API_KEY"

# Voir tous les conteneurs Docker (running + stopped)
docker ps -a

# Voir toutes les images Docker
docker images

# Espace disque utilise par Docker
docker system df
```

[↑ retour en haut](#top)

---

<a id="section-16"></a>

## 16. Conclusion et étapes suivantes

Tu sais maintenant :

- Configurer un compte OpenAI avec crédit.
- Lancer un projet LangChain en `venv`, `uv` ou Docker.
- Choisir le bon modèle selon ton budget.
- Diagnostiquer les erreurs OpenAI les plus fréquentes.

**Ressources de ce module** :
- [Module 0 — Introduction vulgarisée à LangChain et l'IA agentique](./Module-00-introduction-LLM-LangChain-LangGraph-agent-RAG.md)
- [Module 0 — Quiz de validation (50 questions)](./Module-00-quiz-introduction-LLM-LangChain-LangGraph-agent-RAG.md)
- [Module 0 — Pratique 2 : Hello World avec Ollama (gratuit)](./Module-00-pratique-2-Ollama-local.md) ← si tu veux tester sans payer
- [Module 0 — Résumé des commandes](./Module-00-resume-commandes-hello-world-LangChain.md)

**Module suivant** : [Module 2 — Search Agent](../02-langchain-course-project-search-agent/01-cours.md) — passe d'un simple appel LLM à un agent capable d'utiliser des outils externes (recherche web).

[↑ retour en haut](#top)
