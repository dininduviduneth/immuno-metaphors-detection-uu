import json
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

with open('../data/sentences.json', 'r') as file:
    lines = json.load(file)

def generate_annotations(lines):
    metaphors = ["invasion", "invaders", "invading", "soldier", "attack", "foreign", "battle", "weapon", "destroy"]

    met_annotations = []
    non_met_annotations = []

    for line in lines:
        sentence = line['sentence']
        
        cursor = 0

        annotation = [
            sentence.lower(),
            {
                'entities': []
            }
        ]

        # tokens = [token.lower() for token in word_tokenize(sentence)]
        tokens = sentence.lower().split(' ')

        for token in tokens:
            if token in metaphors:
                entity = [
                    cursor,
                    cursor + len(token),
                    "MET"
                ]
            else:
                entity = [
                    cursor,
                    cursor + len(token),
                    "O"
                ]

            cursor += (len(token) + 1)

            annotation[1]['entities'].append(entity)

        if line['has_metaphor'] == 1:
            met_annotations.append(annotation)
        else:
            non_met_annotations.append(annotation)
    
    return met_annotations, non_met_annotations

met_annotations, non_met_annotations = generate_annotations(lines)

combined_annotations = []

for i in range(250):
    if i % 3 == 0:
        combined_annotations.append(met_annotations[i])
    else:
        combined_annotations.append(non_met_annotations[i])

classes = ["O", "MET"]
spacy_annotations = {
    'classes': classes,
    'annotations': combined_annotations
}

to_text_file = []

for annotation in combined_annotations:
    to_text_file.append(annotation[0])

with open('../data/spacy_annotations.json', 'w') as json_file:
    json.dump(spacy_annotations, json_file)

with open('../data/spacy_feed.txt', 'w') as f:
    for text in to_text_file:
        f.write(text)
        f.write('\n')