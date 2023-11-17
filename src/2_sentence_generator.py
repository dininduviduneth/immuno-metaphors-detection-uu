# TO FIND KEYWORDS WITHIN ABSTRACT SENTENCES AND GET A SENTENCE LEVEL OUTPUT

import json
import nltk
# nltk.download('punkt')  # Download the punkt tokenizer models

from nltk.tokenize import sent_tokenize

with open('../data/paper_abstracts.json', 'r') as f:
    data = json.load(f)

sentences = []

metaphors = ["invasion", "invaders", "invading", "soldier", "attack", "foreign", "battle", "weapon", "destroy"]

for paper in data:
    abstract = paper.get('abstract')
    abs_sentences = sent_tokenize(abstract)
    
    for sentence in abs_sentences:
        temp = {
                "sentence": sentence,
                "metaphors": [],
                "has_metaphor": 0
            }
        for metaphor in metaphors:
            if metaphor.lower() in sentence.lower():
                temp["has_metaphor"] = 1
                temp["metaphors"].append(metaphor)

        sentences.append(temp)
        print("Appended: " + str(paper.get('paperId')))

print("Extracted " + str(len(sentences)) + " sentences!")

with open('../data/sentences.json', 'w') as json_file:
  json.dump(sentences, json_file)