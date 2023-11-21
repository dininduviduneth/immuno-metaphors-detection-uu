import json
import re
from helpers import metaphors
with open("../data/sentences.json", "r") as file:
    lines = json.load(file)


def generate_annotations(lines):
    met_annotations = []
    non_met_annotations = []
    pattern = re.compile('[\W_]+', re.UNICODE)
    for line in lines:
        sentence = line["sentence"].lower()
        sentence = re.sub('\s+',' ',sentence)

        cursor = 0

        annotation = [sentence, {"entities": []}]
        tokens = sentence.split(" ")
        tokens = [token.strip() for token in tokens]
        # print(tokens)
        for token in tokens:
            if token in metaphors:
                entity = [cursor, cursor + len(token), "MET"]
            else:
                entity = [cursor, cursor + len(token), "O"]

            cursor += len(token) + 1
            annotation[1]["entities"].append(entity)
                
        if line["has_metaphor"] == 1:
            met_annotations.append(annotation)
        else:
            non_met_annotations.append(annotation)
    
    return met_annotations, non_met_annotations


met_annotations, non_met_annotations = generate_annotations(lines)

combined_annotations = []

#TODO Incerase range to be dynamics based on size of document
for i in range(25000):
    if i % 3 == 0:
        combined_annotations.append(met_annotations[i])
    else:
        combined_annotations.append(non_met_annotations[i])

print(combined_annotations[0])
classes = ["O", "MET"]
spacy_annotations = {"classes": classes, "annotations": combined_annotations}

to_text_file = []

for annotation in combined_annotations:
    to_text_file.append(annotation[0])

with open("../data/spacy_annotations.json", "w") as json_file:
    json.dump(spacy_annotations, json_file)

with open("../data/spacy_feed.txt", "w") as f:
    for text in to_text_file:
        f.write(text)
        f.write("\n")
