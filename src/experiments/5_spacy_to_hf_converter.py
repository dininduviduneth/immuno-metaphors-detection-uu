# TO CONVERT SPACY ANNOTATED DATA TO HUGGINGFACCE ANNOTATION FORMAT

import json
import nltk

nltk.download("punkt")
from nltk.tokenize import word_tokenize

with open("../data/spacy_annotations.json", "r") as file:
    spacy_annotations = json.load(file)


def convert_to_hf(spacy_ann_object):
    classes = spacy_ann_object["classes"]
    annotations = spacy_ann_object["annotations"]

    # CREATE TAG DICTIONARY
    tag_count = len(classes)
    tag_ids = []

    for i in range(tag_count):
        tag_ids.append(i)

    tag_dictionary = dict(zip(classes, tag_ids))

    # DEFINE HUGGING FACE FORMATS
    hf_sentences = []

    for annotation in annotations:
        sentence = annotation[0]
        entities = annotation[1]["entities"]

        letter_tokens = [*sentence.lower()]
        word_tokens = sentence.lower().split(" ")

        hf_sentence = {"tokens": [], "ner_tags": []}

        # for entity in entities:
        #     start_index = entity[0]
        #     end_index = entity[1]
        #     tag = entity[2]

        #     token = ''.join(letter_tokens[start_index:end_index])
        #     ner_tag = tag_dictionary.get(tag)

        #     hf_sentence['tokens'].append(token)
        #     hf_sentence['ner_tags'].append(ner_tag)

        for i in range(len(entities)):
            tag = entities[i][2]
            ner_tag = tag_dictionary.get(tag)

            token = word_tokens[i]
            hf_sentence["tokens"].append(token)
            hf_sentence["ner_tags"].append(ner_tag)

        hf_sentences.append(hf_sentence)

    return hf_sentences


hf_data = convert_to_hf(spacy_annotations)

with open("../data/hf_annotations.json", "w") as json_file:
    json.dump(hf_data, json_file)
