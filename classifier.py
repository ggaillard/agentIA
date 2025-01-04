from transformers import pipeline

def classifier(phrase):
    keywords_sisr = ["réseau", "serveur", "sécurité"]
    keywords_slam = ["application", "programmation", "base de données"]

    if any(kw in phrase for kw in keywords_sisr):
        return {"label": "SISR", "confidence": 0.95}
    elif any(kw in phrase for kw in keywords_slam):
        return {"label": "SLAM", "confidence": 0.95}
    else:
        return {"label": "Inconnu", "confidence": 0.50}

phrase = input("Entrez une description : ")
result = classifier(phrase)
print(f"Résultat : {result['label']} (Confiance : {result['confidence']*100}%)")