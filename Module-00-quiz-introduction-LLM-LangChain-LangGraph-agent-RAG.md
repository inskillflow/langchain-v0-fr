<a id="top"></a>

# Module 0b — Quiz : 50 questions sur l'introduction à LangChain et à l'IA agentique

> Ce quiz teste ta compréhension de **[00-introduction.md](./00-introduction.md)**. Les 50 questions sont en QCM avec une seule bonne réponse. Lis chaque question, choisis ta réponse, puis déroule **« Réponse »** pour vérifier.

> [!NOTE]
> Objectif : valider la **carte mentale** avant d'attaquer le code du Module 1. Si tu obtiens moins de 35/50, relis les sections concernées de `00-introduction.md` avant de continuer.

## Table des matières

| #   | Section                                                                                  | Questions |
| --- | ---------------------------------------------------------------------------------------- | --------- |
| 1   | [Les bases du LLM](#section-1)                                                           | Q1 → Q7   |
| 2   | [Pourquoi un LLM seul ne suffit pas](#section-2)                                         | Q8 → Q13  |
| 3   | [LangChain](#section-3)                                                                  | Q14 → Q21 |
| 4   | [LangGraph](#section-4)                                                                  | Q22 → Q26 |
| 5   | [IA agentique](#section-5)                                                               | Q27 → Q32 |
| 6   | [Paysage des frameworks](#section-6)                                                     | Q33 → Q38 |
| 7   | [Concepts transverses (RAG, embeddings, retriever, etc.)](#section-7)                    | Q39 → Q46 |
| 8   | [Sans framework / Avec framework](#section-8)                                            | Q47 → Q50 |
| 9   | [Grille d'évaluation et corrigé condensé](#section-9)                                    | —         |

---

<a id="section-1"></a>

## 1. Les bases du LLM

<details>
<summary>Conseils avant de commencer</summary>

<br/>

- Réponds **sans relire** l'introduction la première fois.
- Note tes réponses sur papier ou dans un fichier à part.
- Calcule ton score à la fin : 1 point par bonne réponse, 0 sinon.
- Pour chaque erreur, retourne lire la sous-section concernée.

</details>

---

### Q1. Que veut dire LLM ?

- a) Linear Language Model
- b) Large Language Model
- c) Long Language Memory
- d) Language Learning Module

<details>
<summary>Réponse Q1</summary>

**b) Large Language Model.** Un LLM est un grand modèle de langage entraîné à prédire le prochain token.

</details>

---

### Q2. Comment un LLM génère-t-il du texte ?

- a) En cherchant la réponse dans une base de données
- b) En appelant des API externes
- c) Token par token, en prédisant statistiquement le suivant
- d) En lisant un script préprogrammé

<details>
<summary>Réponse Q2</summary>

**c) Token par token, en prédisant statistiquement le suivant.** À chaque étape, le modèle relit tout ce qui précède et calcule le token le plus probable.

</details>

---

### Q3. Quelle analogie illustre le mieux le fonctionnement d'un LLM ?

- a) Un dictionnaire numérique
- b) Un moteur de recherche
- c) Une autocomplétion entraînée sur Internet
- d) Une calculatrice scientifique

<details>
<summary>Réponse Q3</summary>

**c) Une autocomplétion entraînée sur Internet.** C'est l'analogie utilisée dans la section 2.

</details>

---

### Q4. Qu'est-ce qu'un "token" ?

- a) Une clé d'API
- b) Un fragment de mot d'environ 4 caractères
- c) Un mot complet
- d) Un identifiant utilisateur

<details>
<summary>Réponse Q4</summary>

**b) Un fragment de mot d'environ 4 caractères.** L'unité de base sur laquelle un LLM raisonne.

</details>

---

### Q5. Que signifie "cutoff date" pour un LLM ?

- a) La date d'expiration de la clé API
- b) La date jusqu'à laquelle le LLM a été entraîné
- c) La date de sortie du modèle
- d) La date limite d'utilisation

<details>
<summary>Réponse Q5</summary>

**b) La date jusqu'à laquelle le LLM a été entraîné.** Tout ce qui s'est passé après cette date n'est pas dans sa mémoire.

</details>

---

### Q6. Lequel des éléments suivants un LLM **ne peut PAS** faire seul ?

- a) Reformuler un texte
- b) Traduire une phrase
- c) Aller chercher une information en temps réel sur Internet
- d) Suivre une instruction comme "réponds en JSON"

<details>
<summary>Réponse Q6</summary>

**c) Aller chercher une information en temps réel sur Internet.** Pour ça, il faut lui brancher un outil de recherche (Tavily, etc.).

</details>

---

### Q7. Pourquoi parle-t-on d'hallucination chez les LLM ?

- a) Parce qu'ils peuvent planter
- b) Parce qu'ils peuvent générer une réponse qui sonne juste mais qui est fausse
- c) Parce qu'ils sont parfois lents
- d) Parce qu'ils consomment beaucoup d'énergie

<details>
<summary>Réponse Q7</summary>

**b) Parce qu'ils peuvent générer une réponse qui sonne juste mais qui est fausse.** C'est statistique, pas magique.

</details>

<p align="right"><a href="#top">↑ Retour en haut</a></p>

---

<a id="section-2"></a>

## 2. Pourquoi un LLM seul ne suffit pas

### Q8. Le "mur de la connaissance figée" désigne quel problème ?

- a) Le LLM ne peut pas lire de fichiers locaux
- b) Le LLM ne connaît pas les événements postérieurs à sa cutoff date
- c) Le LLM consomme trop de tokens
- d) Le LLM est trop lent

<details>
<summary>Réponse Q8</summary>

**b) Le LLM ne connaît pas les événements postérieurs à sa cutoff date.** D'où l'intérêt de la recherche web ou du RAG.

</details>

---

### Q9. Le "mur de l'action" se résout typiquement avec :

- a) Un autre LLM
- b) Des outils (tools / function calling)
- c) Une mémoire vectorielle
- d) Un fichier .env

<details>
<summary>Réponse Q9</summary>

**b) Des outils (tools / function calling).** Le LLM décide d'appeler une fonction, et un framework exécute l'action réelle.

</details>

---

### Q10. Pourquoi par défaut un LLM ne se souvient-il pas d'un message à l'autre ?

- a) Parce qu'il oublie volontairement
- b) Parce que chaque appel API est indépendant
- c) Parce que la mémoire coûte trop cher
- d) Parce que c'est une limite légale

<details>
<summary>Réponse Q10</summary>

**b) Parce que chaque appel API est indépendant.** Sans réinjection d'historique, il n'a aucun contexte conversationnel.

</details>

---

### Q11. Quelle solution traite le "mur du format" ?

- a) Un retriever
- b) Un output parser (Pydantic, JSON schema)
- c) Un vector store
- d) Un agent

<details>
<summary>Réponse Q11</summary>

**b) Un output parser (Pydantic, JSON schema).** Il transforme la sortie texte du LLM en objet typé prévisible.

</details>

---

### Q12. Quelle catégorie de problème **ne figure pas** parmi les "5 murs" ?

- a) Le mur de la connaissance figée
- b) Le mur de l'action
- c) Le mur de la traduction
- d) Le mur du format

<details>
<summary>Réponse Q12</summary>

**c) Le mur de la traduction.** Les 5 murs sont : connaissance figée, action, mémoire, format, robustesse.

</details>

---

### Q13. Quel est l'objectif principal des frameworks comme LangChain par rapport aux 5 murs ?

- a) Remplacer les LLM
- b) Apporter des briques prêtes à l'emploi pour les contourner
- c) Réduire le coût de l'API
- d) Accélérer l'inférence

<details>
<summary>Réponse Q13</summary>

**b) Apporter des briques prêtes à l'emploi pour les contourner.** Tracing, retry, parsers, retrievers, etc.

</details>

<p align="right"><a href="#top">↑ Retour en haut</a></p>

---

<a id="section-3"></a>

## 3. LangChain

### Q14. LangChain est avant tout :

- a) Un fournisseur de LLM
- b) Une boîte à outils open source pour construire des applications LLM
- c) Un service cloud payant
- d) Un modèle open source

<details>
<summary>Réponse Q14</summary>

**b) Une boîte à outils open source pour construire des applications LLM.** Disponible en Python et JavaScript.

</details>

---

### Q15. Quelle métaphore décrit bien LangChain ?

- a) Une voiture autonome
- b) Un set de Lego pour applications IA
- c) Un compilateur Python
- d) Une base de données

<details>
<summary>Réponse Q15</summary>

**b) Un set de Lego pour applications IA.** Briques standardisées que tu assembles selon ton besoin.

</details>

---

### Q16. Que signifie LCEL ?

- a) Large Coding Expression Library
- b) LangChain Expression Language
- c) Lambda Chain Execution Layer
- d) Local Compute Execution Loop

<details>
<summary>Réponse Q16</summary>

**b) LangChain Expression Language.** Le langage de composition basé sur l'opérateur `|`.

</details>

---

### Q17. Quel opérateur Python utilise LCEL pour composer des briques ?

- a) `+`
- b) `>>`
- c) `|`
- d) `&`

<details>
<summary>Réponse Q17</summary>

**c) `|`.** L'opérateur pipe : `prompt | llm | parser`.

</details>

---

### Q18. Une chaîne LCEL `prompt | llm | parser` expose automatiquement :

- a) Uniquement `.invoke()`
- b) `.invoke()`, `.stream()`, `.batch()`, `.ainvoke()`
- c) Uniquement `.run()`
- d) Uniquement la méthode HTTP POST

<details>
<summary>Réponse Q18</summary>

**b) `.invoke()`, `.stream()`, `.batch()`, `.ainvoke()`.** Tu obtiens streaming, async, batch gratuitement.

</details>

---

### Q19. Quel composant LangChain permet de transformer une fonction Python en outil utilisable par un LLM ?

- a) `@chain`
- b) `@tool`
- c) `@runnable`
- d) `@agent`

<details>
<summary>Réponse Q19</summary>

**b) `@tool`.** Le décorateur génère automatiquement le schéma JSON depuis la signature et la docstring.

</details>

---

### Q20. Que fait `init_chat_model("openai:gpt-4o")` ?

- a) Démarre un serveur OpenAI local
- b) Crée une instance de LLM via une interface uniforme
- c) Télécharge le modèle GPT-4o sur ton disque
- d) Active le mode streaming

<details>
<summary>Réponse Q20</summary>

**b) Crée une instance de LLM via une interface uniforme.** Tu peux changer de fournisseur en changeant juste la chaîne.

</details>

---

### Q21. Lequel n'est **pas** une brique standard de LangChain ?

- a) PromptTemplate
- b) ChatModel
- c) Retriever
- d) GPUManager

<details>
<summary>Réponse Q21</summary>

**d) GPUManager.** N'existe pas dans LangChain. Les autres sont des briques officielles.

</details>

<p align="right"><a href="#top">↑ Retour en haut</a></p>

---

<a id="section-4"></a>

## 4. LangGraph

### Q22. LangGraph représente une application IA comme :

- a) Une chaîne linéaire
- b) Un script bash
- c) Un graphe d'états avec nœuds et edges
- d) Une base de données

<details>
<summary>Réponse Q22</summary>

**c) Un graphe d'états avec nœuds et edges.** D'où le mot "Graph" dans LangGraph.

</details>

---

### Q23. Lequel des cas suivants justifie LangGraph plutôt que LangChain LCEL ?

- a) Un simple appel LLM
- b) Une boucle de réflexion (générer puis critiquer puis re-générer)
- c) Une seule traduction
- d) Un calcul mathématique direct

<details>
<summary>Réponse Q23</summary>

**b) Une boucle de réflexion.** LCEL gère mal les boucles ; LangGraph est conçu pour ça.

</details>

---

### Q24. Une "edge conditionnelle" dans LangGraph permet de :

- a) Connecter à Internet
- b) Choisir le prochain nœud selon l'état
- c) Activer le streaming
- d) Réduire le nombre de tokens

<details>
<summary>Réponse Q24</summary>

**b) Choisir le prochain nœud selon l'état.** Ça implémente les branches conditionnelles ("si pertinent → generate, sinon → web_search").

</details>

---

### Q25. LangChain et LangGraph sont :

- a) Deux frameworks concurrents
- b) Le même produit avec deux noms
- c) Complémentaires : on utilise souvent les deux ensemble
- d) Incompatibles

<details>
<summary>Réponse Q25</summary>

**c) Complémentaires.** Tes nœuds LangGraph contiennent souvent des chaînes LCEL LangChain.

</details>

---

### Q26. Pour un workflow multi-agent complexe, l'outil le plus adapté est :

- a) L'API OpenAI brute
- b) LangChain LCEL
- c) LangGraph
- d) `requests`

<details>
<summary>Réponse Q26</summary>

**c) LangGraph.** Conçu pour orchestrer plusieurs agents avec état partagé et boucles.

</details>

<p align="right"><a href="#top">↑ Retour en haut</a></p>

---

<a id="section-5"></a>

## 5. IA agentique

### Q27. Un "agent IA" se distingue d'un chatbot par :

- a) Sa capacité à parler plus vite
- b) Sa capacité à prendre des décisions et exécuter des actions
- c) Son interface graphique
- d) Le modèle utilisé

<details>
<summary>Réponse Q27</summary>

**b) Sa capacité à prendre des décisions et exécuter des actions.** Un agent observe, décide, agit, boucle.

</details>

---

### Q28. La boucle universelle d'un agent suit le schéma :

- a) Open → Close → Repeat
- b) Reason → Act → Observe → Repeat
- c) Read → Write → Save
- d) Train → Test → Deploy

<details>
<summary>Réponse Q28</summary>

**b) Reason → Act → Observe → Repeat.** Tous les agents respectent ce cycle, peu importe le framework.

</details>

---

### Q29. Quel pattern historique cette boucle porte-t-elle pour nom ?

- a) Map-Reduce
- b) ReAct
- c) MVC
- d) CRUD

<details>
<summary>Réponse Q29</summary>

**b) ReAct.** Pour Reasoning + Acting.

</details>

---

### Q30. Qui a publié le papier introduisant le pattern ReAct ?

- a) OpenAI
- b) Microsoft Research
- c) Yao et al. (2022)
- d) Google Research

<details>
<summary>Réponse Q30</summary>

**c) Yao et al. (2022).** Référence : arXiv:2210.03629.

</details>

---

### Q31. Lequel **n'est pas** un pattern d'IA agentique cité dans le document ?

- a) Reflection
- b) Reflexion
- c) Plan-and-Execute
- d) BatchNorm

<details>
<summary>Réponse Q31</summary>

**d) BatchNorm.** C'est une technique de réseau de neurones, sans rapport avec les agents.

</details>

---

### Q32. Quand on dit qu'un agent peut "boucler", cela signifie :

- a) Qu'il plante
- b) Qu'il appelle un outil, observe le résultat, puis raisonne à nouveau jusqu'à pouvoir répondre
- c) Qu'il refuse de répondre
- d) Qu'il consomme une mémoire infinie

<details>
<summary>Réponse Q32</summary>

**b) Qu'il appelle un outil, observe le résultat, puis raisonne à nouveau.** C'est le cœur de la boucle ReAct.

</details>

<p align="right"><a href="#top">↑ Retour en haut</a></p>

---

<a id="section-6"></a>

## 6. Paysage des frameworks

### Q33. Quel framework est spécialisé dans le RAG complexe et l'indexation hiérarchique de documents ?

- a) AutoGen
- b) CrewAI
- c) LlamaIndex
- d) Smolagents

<details>
<summary>Réponse Q33</summary>

**c) LlamaIndex.** Excellent sur les indexes complexes ; moins orienté agents que LangChain.

</details>

---

### Q34. Quel framework est connu pour les conversations entre agents (assistant ↔ critique ↔ user) ?

- a) LangGraph
- b) AutoGen
- c) Haystack
- d) DSPy

<details>
<summary>Réponse Q34</summary>

**b) AutoGen.** Édité par Microsoft, orienté multi-agent conversationnel.

</details>

---

### Q35. Quel framework est édité par Hugging Face et propose des agents minimalistes basés sur le code Python ?

- a) AutoGen
- b) Haystack
- c) Smolagents
- d) LangFlow

<details>
<summary>Réponse Q35</summary>

**c) Smolagents.** Léger, transparent, output = code Python exécutable.

</details>

---

### Q36. Quel est le principal inconvénient du SDK Agents officiel d'OpenAI ?

- a) Il est lent
- b) Il est verrouillé sur OpenAI
- c) Il ne supporte pas Python
- d) Il ne fonctionne qu'en local

<details>
<summary>Réponse Q36</summary>

**b) Il est verrouillé sur OpenAI.** Tu perds la portabilité entre fournisseurs.

</details>

---

### Q37. CrewAI est plus particulièrement utilisé pour :

- a) Créer des modèles
- b) Modéliser une équipe d'agents avec des rôles
- c) Faire du fine-tuning
- d) Faire du déploiement

<details>
<summary>Réponse Q37</summary>

**b) Modéliser une équipe d'agents avec des rôles.** Très simple à prendre en main, intuitif.

</details>

---

### Q38. D'après le document, LangChain + LangGraph couvre quel pourcentage des cas réels ?

- a) 20 %
- b) 50 %
- c) 80 %
- d) 100 %

<details>
<summary>Réponse Q38</summary>

**c) 80 %.** Les autres frameworks restent utiles dans des contextes spécifiques.

</details>

<p align="right"><a href="#top">↑ Retour en haut</a></p>

---

<a id="section-7"></a>

## 7. Concepts transverses (RAG, embeddings, retriever, etc.)

### Q39. Un "embedding" est :

- a) Un fichier vidéo
- b) Une représentation numérique d'un texte sous forme de vecteur
- c) Une clé d'API
- d) Un nœud LangGraph

<details>
<summary>Réponse Q39</summary>

**b) Une représentation numérique d'un texte sous forme de vecteur.** Deux textes proches ont des vecteurs proches.

</details>

---

### Q40. La dimension typique d'un embedding OpenAI `text-embedding-3-small` est :

- a) 256
- b) 512
- c) 1024
- d) 1536

<details>
<summary>Réponse Q40</summary>

**d) 1536.** C'est la taille de vecteur attendue côté Pinecone pour ce modèle.

</details>

---

### Q41. Que fait un "retriever" ?

- a) Génère un nouveau texte
- b) Renvoie les `k` documents les plus pertinents pour une question
- c) Compresse les images
- d) Stocke des secrets

<details>
<summary>Réponse Q41</summary>

**b) Renvoie les `k` documents les plus pertinents pour une question.** C'est l'étape "R" du RAG.

</details>

---

### Q42. RAG signifie :

- a) Random Answer Generator
- b) Retrieval-Augmented Generation
- c) Real Agent Graph
- d) Recursive Adaptive Generation

<details>
<summary>Réponse Q42</summary>

**b) Retrieval-Augmented Generation.** Génération augmentée par la recherche dans tes propres documents.

</details>

---

### Q43. Un "vector store" est utilisé pour :

- a) Sauvegarder des fichiers binaires
- b) Stocker et rechercher des embeddings
- c) Loger les utilisateurs
- d) Compiler du Python

<details>
<summary>Réponse Q43</summary>

**b) Stocker et rechercher des embeddings.** Avec recherche par similarité (cosinus, dot product, etc.).

</details>

---

### Q44. Lequel **n'est pas** un vector store cité dans le document ?

- a) Pinecone
- b) Chroma
- c) MongoDB
- d) FAISS

<details>
<summary>Réponse Q44</summary>

**c) MongoDB.** C'est une base de documents classique, pas spécifiquement un vector store dans le contexte du cours.

</details>

---

### Q45. Le "streaming" en LLM signifie :

- a) Diffuser un film
- b) Recevoir la réponse token par token au fil de la génération
- c) Utiliser plusieurs LLM en parallèle
- d) Compresser la réponse

<details>
<summary>Réponse Q45</summary>

**b) Recevoir la réponse token par token au fil de la génération.** C'est l'effet "ChatGPT qui écrit en direct".

</details>

---

### Q46. LangSmith sert principalement à :

- a) Compiler les modèles
- b) Faire le tracing et l'observabilité
- c) Héberger des modèles
- d) Gérer la facturation

<details>
<summary>Réponse Q46</summary>

**b) Faire le tracing et l'observabilité.** Enregistre prompts, réponses, durées, coûts pour chaque étape.

</details>

<p align="right"><a href="#top">↑ Retour en haut</a></p>

---

<a id="section-8"></a>

## 8. Sans framework / Avec framework

### Q47. Lequel est un avantage **concret** d'utiliser LangChain plutôt qu'un appel API direct ?

- a) Le LLM répond plus vite
- b) Le LLM coûte moins cher
- c) On peut changer de fournisseur en modifiant une seule ligne
- d) Le LLM devient plus précis

<details>
<summary>Réponse Q47</summary>

**c) On peut changer de fournisseur en modifiant une seule ligne.** `init_chat_model("openai:gpt-4o")` → `init_chat_model("anthropic:claude-...")`.

</details>

---

### Q48. Quelle phrase décrit **mal** un projet sans framework ?

- a) Le code est fortement couplé au fournisseur
- b) Pas d'observabilité par défaut
- c) Beaucoup de boilerplate
- d) Tracing automatique gratuit

<details>
<summary>Réponse Q48</summary>

**d) Tracing automatique gratuit.** Sans framework, tu dois tout instrumenter à la main.

</details>

---

### Q49. Pour faire du streaming en LangChain, il suffit d'utiliser :

- a) `chain.stream(...)`
- b) `chain.async_invoke(...)`
- c) `chain.exec(...)`
- d) `chain.flush(...)`

<details>
<summary>Réponse Q49</summary>

**a) `chain.stream(...)`.** Disponible automatiquement sur tout `Runnable`.

</details>

---

### Q50. Quelle est la "vraie valeur" d'un framework selon le document ?

- a) Écrire moins de code uniquement
- b) Garder le focus sur la logique métier au lieu de réinventer la plomberie
- c) Utiliser les meilleurs LLM
- d) Réduire le coût des API

<details>
<summary>Réponse Q50</summary>

**b) Garder le focus sur la logique métier au lieu de réinventer la plomberie.** C'est la conclusion explicite de la section 8a.

</details>

<p align="right"><a href="#top">↑ Retour en haut</a></p>

---

<a id="section-9"></a>

## 9. Grille d'évaluation et corrigé condensé

<details>
<summary>9 - Grille d'évaluation</summary>

<br/>

Calcule ton score sur 50.

| Score    | Interprétation                                                                                          | Recommandation                                                  |
| -------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| 45 → 50  | Excellent : ta carte mentale est solide.                                                                | Tu peux passer au [Module 1](./01-cours.md) directement.        |
| 35 → 44  | Bon niveau : tu as l'essentiel, quelques zones grises.                                                  | Relis les sections où tu as fait des erreurs.                   |
| 25 → 34  | Niveau partiel : la plupart des notions sont floues.                                                    | Relis [00-introduction.md](./00-introduction.md) avant le code. |
| < 25     | Tu es en train d'apprendre, c'est normal.                                                               | Reprends `00-introduction.md` section par section, puis refais le quiz. |

</details>

<details>
<summary>9 - Corrigé condensé (réponses uniquement)</summary>

<br/>

| Q | Réponse | Q  | Réponse | Q  | Réponse | Q  | Réponse | Q  | Réponse |
| - | ------- | -- | ------- | -- | ------- | -- | ------- | -- | ------- |
| 1 | b       | 11 | b       | 21 | d       | 31 | d       | 41 | b       |
| 2 | c       | 12 | c       | 22 | c       | 32 | b       | 42 | b       |
| 3 | c       | 13 | b       | 23 | b       | 33 | c       | 43 | b       |
| 4 | b       | 14 | b       | 24 | b       | 34 | b       | 44 | c       |
| 5 | b       | 15 | b       | 25 | c       | 35 | c       | 45 | b       |
| 6 | c       | 16 | b       | 26 | c       | 36 | b       | 46 | b       |
| 7 | b       | 17 | c       | 27 | b       | 37 | b       | 47 | c       |
| 8 | b       | 18 | b       | 28 | b       | 38 | c       | 48 | d       |
| 9 | b       | 19 | b       | 29 | b       | 39 | b       | 49 | a       |
| 10| b       | 20 | b       | 30 | c       | 40 | d       | 50 | b       |

</details>

<details>
<summary>9 - Mappage question → section de l'introduction</summary>

<br/>

Si tu as raté une question, retourne sur la section correspondante :

| Questions   | Section de [00-introduction.md](./00-introduction.md)                |
| ----------- | -------------------------------------------------------------------- |
| Q1 → Q7     | Section 2 — C'est quoi un LLM, vraiment ?                            |
| Q8 → Q13    | Section 3 — Pourquoi un LLM seul ne suffit pas                       |
| Q14 → Q21   | Section 4 — Qu'est-ce que LangChain ?                                |
| Q22 → Q26   | Section 4a — Qu'est-ce que LangGraph ?                               |
| Q27 → Q32   | Sections 5 et 5a — IA agentique et boucle universelle                |
| Q33 → Q38   | Sections 6 et 6a — Paysage des frameworks                            |
| Q39 → Q46   | Section 7 — Concepts clés transverses                                |
| Q47 → Q50   | Sections 8 et 8a — Scénarios sans / avec framework                   |

</details>

<p align="right"><a href="#top">↑ Retour en haut</a></p>

---

## Prochaine étape

> [!NOTE]
> Quand ton score est satisfaisant, passe au **[Module 1 — Hello World LangChain](./01-cours.md)**. Tu vas écrire ton premier code LangChain.

<p align="center">
  <strong>Fin du Module 0b — Quiz</strong><br/>
  <a href="#top">↑ Retour en haut</a>
</p>
