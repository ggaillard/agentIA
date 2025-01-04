import os
import sys

def classifier(phrase):
    keywords_sisr = ["réseau", "serveur", "sécurité"]
    keywords_slam = ["application", "programmation", "base de données"]

    if any(kw in phrase for kw in keywords_sisr):
        return {"label": "SISR", "confidence": 0.95}
    elif any(kw in phrase for kw in keywords_slam):
        return {"label": "SLAM", "confidence": 0.95}
    else:
        return {"label": "Inconnu", "confidence": 0.50}

if __name__ == "__main__":
    # Mode non interactif (ligne de commande ou variable d'environnement)
    phrase = None
    if len(sys.argv) > 1:  # Vérifie si une phrase est passée en argument
        phrase = " ".join(sys.argv[1:])
    elif os.getenv("TEST_PHRASE"):  # Vérifie si une variable d'environnement est définie
        phrase = os.getenv("TEST_PHRASE")

    if not phrase:  # Mode interactif si aucune donnée n'est fournie
        phrase = input("Entrez une description : ")

    result = classifier(phrase)
    print(f"Résultat : {result['label']} (Confiance : {result['confidence']*100}%)")
