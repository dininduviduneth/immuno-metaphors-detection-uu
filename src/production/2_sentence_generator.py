# TO FIND KEYWORDS WITHIN ABSTRACT SENTENCES AND GET A SENTENCE LEVEL OUTPUT

import json
from helpers import split_sentences, metaphors

with open("../../data/paper_abstracts.json", "r") as f:
    data = json.load(f)

sentences = []

for paper in data:
    abstract = paper.get("abstract")
    abs_sentences = split_sentences(abstract)  # sent_tokenize(abstract)
    for sentence in abs_sentences:
        temp = {"sentence": sentence, "metaphors": [], "has_metaphor": 0}
        for metaphor in metaphors:
            if metaphor.lower() in sentence.lower():
                temp["has_metaphor"] = 1
                temp["metaphors"].append(metaphor)

        sentences.append(temp)
        ##print("Appended: " + str(paper.get("paperId")))

print("Extracted " + str(len(sentences)) + " sentences!")

with open("../../data/sentences.json", "w") as json_file:
    json.dump(sentences, json_file)
