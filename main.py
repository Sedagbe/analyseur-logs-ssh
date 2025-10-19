# main.py
# Auteur : Kenneth
# Projet : Détection de tentatives de connexion échouées

# On ouvre le fichier des logs
with open("logs.txt", "r") as fichier:
    lignes = fichier.readlines()

# Dictionnaire pour compter les erreurs par IP
erreurs = {}

# On parcourt chaque ligne
for ligne in lignes:
    if "Failed password" in ligne:
        # On récupère l’adresse IP
        mots = ligne.split()
        ip = mots[-4]  # Exemple : 192.168.1.15
        erreurs[ip] = erreurs.get(ip, 0) + 1

# On écrit le résultat dans un autre fichier
with open("resultat.txt", "w") as res:
    for ip, nombre in erreurs.items():
        res.write(f"{ip} : {nombre} tentatives echouees\n")

print(" Analyse terminée ! Résultats enregistrés dans resultat.txt")
