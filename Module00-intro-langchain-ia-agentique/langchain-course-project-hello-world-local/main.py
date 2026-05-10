"""
Hello World LangChain - Version Ollama locale.

Ce script demontre les bases de LangChain :
  1. Construction d'un PromptTemplate reutilisable.
  2. Initialisation d'un LLM Ollama 100% local.
  3. Composition d'une chaine LCEL avec l'operateur pipe |.
  4. Invocation de la meme chaine sur PLUSIEURS entrees pour montrer la reutilisation.

Pas de cle API, pas de cout : tout tourne sur ton ordinateur via Ollama.
Voir Module-00-pratique-2-Ollama-local.md pour l'installation d'Ollama
et le telechargement du modele (`ollama pull gemma3:270m`).

Pour la version OpenAI (qualite superieure mais payante), voir le dossier
langchain-course-project-hello-world-openai/ (Pratique 1).
"""

import os
import time

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()

MODEL_NAME = "gemma3:270m"

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")


def banner(titre: str, char: str = "=") -> None:
    """Affiche une banniere visuelle pour structurer la sortie."""
    print()
    print(char * 72)
    print(f"  {titre}")
    print(char * 72)


def main() -> None:
    banner("LangChain Hello World - Ollama local - PromptTemplate + LCEL")

    print("\n[1/4] Construction du PromptTemplate (le 'formulaire' reutilisable)")
    template = """
A partir de l'information suivante :

{information}

Donne, en francais et en Markdown court :
1. Un resume en une seule phrase.
2. Deux faits interessants peu connus.
3. Une question ouverte a creuser.
"""
    prompt = PromptTemplate(input_variables=["information"], template=template)
    print(f"      [OK] Variables du template : {prompt.input_variables}")

    print(f"\n[2/4] Initialisation du LLM Ollama '{MODEL_NAME}' (le 'cerveau')")
    print(f"      Endpoint : {OLLAMA_BASE_URL}")
    llm = ChatOllama(
        temperature=0,
        model=MODEL_NAME,
        base_url=OLLAMA_BASE_URL,
    )
    print(f"      [OK] {type(llm).__name__} pret")

    print("\n[3/4] Composition de la chaine LCEL : prompt | llm  (le 'tuyau')")
    chain = prompt | llm
    print("      [OK] Chaine construite. Reutilisable a l'infini.")

    personnages = {
        "Elon Musk": (
            "Elon Reeve Musk (born 1971) is a businessman known for leading Tesla, "
            "SpaceX, X (Twitter), and DOGE. Born in Pretoria, South Africa, he "
            "co-founded PayPal, founded SpaceX in 2002, and made Tesla the leader "
            "in electric vehicles. He acquired Twitter in 2022 and renamed it X."
        ),
        "Marie Curie": (
            "Maria Sklodowska-Curie (1867-1934), Polish-French physicist and "
            "chemist, conducted pioneering research on radioactivity. First woman "
            "to win a Nobel Prize, only person to win Nobels in two different "
            "scientific fields (Physics 1903, Chemistry 1911)."
        ),
        "Albert Einstein": (
            "Albert Einstein (1879-1955), German-born theoretical physicist, "
            "developed the theory of relativity. Won the 1921 Nobel Prize in "
            "Physics for the photoelectric effect, considered the most influential "
            "physicist of the 20th century."
        ),
    }
    print(f"\n[4/4] Invocation de la chaine sur {len(personnages)} personnages historiques")

    t_global = time.time()
    succes = 0

    for i, (nom, info) in enumerate(personnages.items(), start=1):
        banner(f"{i}/{len(personnages)} - {nom}", char="-")

        print("Appel LLM en cours (peut prendre 5-60s selon la machine)...", end=" ", flush=True)
        t0 = time.time()
        try:
            reponse = chain.invoke({"information": info})
        except Exception as e:
            print(f"\n[ERREUR] {type(e).__name__}: {e}")
            print(
                "[i] Verifie qu'Ollama tourne (`ollama serve`) et que le modele "
                f"'{MODEL_NAME}' est disponible (`ollama pull {MODEL_NAME}`)."
            )
            print("[i] On continue avec le prochain personnage.\n")
            continue
        duree = time.time() - t0
        print(f"[OK] {duree:.1f}s\n")
        succes += 1

        print(reponse.content)

    duree_globale = time.time() - t_global
    banner(f"Termine en {duree_globale:.1f}s ({succes}/{len(personnages)} reussis)")
    print(f"  Modele utilise       : {MODEL_NAME} (Ollama, 100% local)")
    print(f"  Endpoint Ollama      : {OLLAMA_BASE_URL}")
    print(f"  Cout                 : 0.00 USD (gratuit, tout tourne sur ta machine)")
    print(f"  La meme chaine LCEL a ete invoquee {len(personnages)} fois sans rebuild.")
    print()


if __name__ == "__main__":
    main()
