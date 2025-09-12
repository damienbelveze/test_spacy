"""
import spacy
import glob
import os
file_paths = glob.glob(os.path.join("docs", '*'))
# uploaded_files = []
for file_path in file_paths:
    with open(file_path, 'r') as file:
        content = file.read()
#        uploaded_files.append((file_path, content))
nlp = spacy.load('en_core_web_sm')
doc = nlp(content)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
"""

import spacy
import glob
import os
import csv

# Definit le dossier source
directory_path = 'docs'

# récupère tous les chemins de fichiers dans le dossier source
file_paths = glob.glob(os.path.join(directory_path, '*'))

# crée une liste vide 'results'
results = []

# pour chaque fichier dans 'docs"
for file_path in file_paths:
    with open(file_path, 'r') as file: # ouvre le fichier en lecture
        content = file.read() # lit le contenu du fichier et l'envoie dans la variable 'content'
        nlp = spacy.load('en_core_web_sm') # exécute la fonction nlp de SpaCy à partir du modèle EN (anglais) préalablement téléchargé dans l'environnement virtuel 
        doc = nlp(content) # crée une variable doc qui comporte le contenu de la variable contents après traitement par la fonction nlp de SpaCy
        for ent in doc.ents:
            results.append((ent.text, ent.start_char, ent.end_char, ent.label_)) # extrait les entités nommées de 'doc' en 4 valeurs (envoie le tout dans la variable 'results') : le texte de l'entité nommée, le numéro du premier caractère, le numéro du dernier caractère, le type d'entité nommée

# définit un chemin et un nom pour le fichier CSV de sortie
csv_file_path = 'entities.csv'

# envoie le résultat du traitement vers le fichier CSV de sortie
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile: # ouvre un fichier CSV formaté en écriture et formaté en utf-8
    fieldnames = ['Entity Text', 'Start Char', 'End Char', 'Label'] # crée les entêtes de colonnes du CSV d'après les 4 valeurs de 'results'

    writer.writeheader()
    for result in results: 
        writer.writerow({'Entity Text': result[0], 'Start Char': result[1], 'End Char': result[2], 'Label': result[3]}) #remplit les colonnes du CSV avec les valeurs issues de results, pour Python le premier nombre d'une énumération est 0

print(f"les résultats sont disponibles sur {csv_file_path}") #imprime un message indiquant que le traitement s'est bien déroulé


""" legend

GPE : Countries, Cities, Stats
LOC : non-GPE locations, rivers, mountains
PER : person
ORG : organization
DATE : date
NORP: Nationalities or religious or political groups