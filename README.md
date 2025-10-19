# analyseur-logs-ssh

Petit projet étudiant en **cybersécurité** réalisé en **Python**.  
Le programme analyse un fichier de logs (`logs.txt`) et détecte les **tentatives de connexion échouées**.  
Les résultats sont enregistrés dans un fichier `resultat.txt`.

---

## ⚙️ Fonctionnement
1. Le script lit les lignes du fichier `logs.txt`
2. Il recherche les messages contenant “Failed password”
3. Il compte combien de fois chaque adresse IP a échoué
4. Il enregistre le rapport dans `resultat.txt`

---

##  Fichiers
- `main.py` → le programme principal  
- `logs.txt` → les logs à analyser  
- `resultat.txt` → le résultat généré  

---

##  Auteur
**Kenneth Oussou Lio**  
Étudiant en Bachelor Cybersécurité & Intelligence Artificielle – ESEO Paris-Vélizy
