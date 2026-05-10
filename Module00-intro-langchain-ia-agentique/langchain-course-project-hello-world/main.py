"""
Hello World LangChain - Premier appel LLM avec PromptTemplate + LCEL.

Ce script demontre les bases de LangChain :
  1. Construction d'un PromptTemplate reutilisable.
  2. Initialisation d'un LLM (OpenAI ou Ollama).
  3. Composition d'une chaine LCEL avec l'operateur pipe |.
  4. Invocation de la meme chaine sur PLUSIEURS entrees pour montrer la reutilisation.

Bonus pedagogique : affichage de la progression, du temps d'inference,
des tokens consommes et du cout estime en USD.
"""

import time

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Pour utiliser Ollama local (gratuit) : decommente la ligne ci-dessous,
# commente l'import ChatOpenAI et la ligne `llm = ChatOpenAI(...)` plus bas.
# from langchain_ollama import ChatOllama

load_dotenv()

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
MODEL_NAME = "gpt-4o-mini"  # alternatives : "gpt-4o", "gpt-5", ou "gemma3:270m" pour Ollama

# Tarifs OpenAI (USD pour 1 million de tokens, mai 2026)
TARIFS_OPENAI = {
    "gpt-4o-mini": (0.15, 0.60),
    "gpt-4o":      (2.50, 10.00),
    "gpt-5":       (5.00, 15.00),
}


def banner(titre: str, char: str = "=") -> None:
    """Affiche une banniere visuelle pour structurer la sortie."""
    print()
    print(char * 72)
    print(f"  {titre}")
    print(char * 72)


def cout_usd(tokens_in: int, tokens_out: int, modele: str) -> float | None:
    """Estime le cout d'un appel LLM en USD a partir des tokens."""
    if modele not in TARIFS_OPENAI:
        return None
    prix_in, prix_out = TARIFS_OPENAI[modele]
    return (tokens_in * prix_in + tokens_out * prix_out) / 1_000_000


def main() -> None:
    banner("LangChain Hello World - PromptTemplate + LCEL")

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

    print(f"\n[2/4] Initialisation du LLM '{MODEL_NAME}' (le 'cerveau')")
    llm = ChatOpenAI(temperature=0, model=MODEL_NAME)
    # Variante Ollama locale (gratuite) :
    # llm = ChatOllama(temperature=0, model="gemma3:270m")
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
    cout_total = 0.0

    for i, (nom, info) in enumerate(personnages.items(), start=1):
        banner(f"{i}/{len(personnages)} - {nom}", char="-")

        print("Appel LLM en cours (peut prendre 2-30s selon le modele)...", end=" ", flush=True)
        t0 = time.time()
        reponse = chain.invoke({"information": info})
        duree = time.time() - t0
        print(f"[OK] {duree:.1f}s\n")

        print(reponse.content)

        usage = (
            reponse.response_metadata.get("token_usage", {})
            if hasattr(reponse, "response_metadata")
            else {}
        )
        if usage:
            tokens_in = usage.get("prompt_tokens", 0)
            tokens_out = usage.get("completion_tokens", 0)
            cout = cout_usd(tokens_in, tokens_out, MODEL_NAME)
            print(
                f"\n[i] Tokens : {tokens_in} entree + {tokens_out} sortie "
                f"= {tokens_in + tokens_out} total"
            )
            if cout is not None:
                print(f"[i] Cout estime : ${cout:.5f} USD")
                cout_total += cout

    duree_globale = time.time() - t_global
    banner(f"Termine en {duree_globale:.1f}s")
    if cout_total > 0:
        print(f"  Cout total estime    : ${cout_total:.4f} USD")
        print(f"  Cout moyen par appel : ${cout_total / len(personnages):.5f} USD")
    print(f"  Modele utilise       : {MODEL_NAME}")
    print(f"  La meme chaine LCEL a ete invoquee {len(personnages)} fois sans rebuild.")
    print()


if __name__ == "__main__":
    main()
