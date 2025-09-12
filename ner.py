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

# Define the directory path
directory_path = 'docs'

# Get all file paths in the directory
file_paths = glob.glob(os.path.join(directory_path, '*'))

# List to store the results
results = []

# Process each file
for file_path in file_paths:
    with open(file_path, 'r') as file:
        content = file.read()
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(content)
        for ent in doc.ents:
            results.append((ent.text, ent.start_char, ent.end_char, ent.label_))

# Define the CSV file path
csv_file_path = 'entities.csv'

# Write the results to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Entity Text', 'Start Char', 'End Char', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        writer.writerow({'Entity Text': result[0], 'Start Char': result[1], 'End Char': result[2], 'Label': result[3]})

print(f"Results have been written to {csv_file_path}")


""" legend

GPE : Countries, Cities, Stats
LOC : non-GPE locations, rivers, mountains
PER : person
ORG : organization
DATE : date
NORP: Nationalities or religious or political groups