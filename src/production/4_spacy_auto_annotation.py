import json
import re
from helpers import metaphors
with open("../../data/sentences.json", "r") as file:
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

                annotation[1]["entities"].append(entity)
                
            cursor += len(token) + 1
        if line["has_metaphor"] == 1:
            met_annotations.append(annotation)
        else:
            non_met_annotations.append(annotation)
    
    return met_annotations, non_met_annotations


met_annotations, non_met_annotations = generate_annotations(lines)

combined_annotations = []

combined_annotations = []
for i in range(len(met_annotations)):
    start, stop = i*3, (i+1)*3
    combined_annotations.append(met_annotations[i])
    combined_annotations.extend(non_met_annotations[start:stop])

classes = ["MET"]
spacy_annotations = {"classes": classes, "annotations": combined_annotations}

to_text_file = []

for annotation in combined_annotations:
    to_text_file.append(annotation[0])

with open("../../data/spacy_annotations.json", "w") as json_file:
    json.dump(spacy_annotations, json_file)

with open("../../data/spacy_feed.txt", "w") as f:
    for text in to_text_file:
        f.write(text)
        f.write("\n")
