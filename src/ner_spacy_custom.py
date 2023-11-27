import spacy
import json
from spacy.tokens import DocBin
from sklearn.model_selection import train_test_split
import pickle

def main():
    annotations = json.load(open("../data/spacy_annotations.json", "r"))
    annotations = annotations["annotations"]
    train, test = train_test_split(annotations, test_size=0.33)
    with open("../data/test_pickle", "wb") as file:
        pickle.dump(test,file=file)
    train, dev = train_test_split(train, test_size=0.2)
    print(len(train), len(dev))
    # print(train, test)
    nlp = spacy.blank("en")
    db = DocBin()
    for text, data in train:
        entity_indices = []
        ents = []
        doc = nlp.make_doc(text)
        annot = data["entities"]
        for start, end, label in annot:
            skip_entity = False
            for idx in range(start, end):
                if idx in entity_indices:
                    skip_entity = True
                    break
            if start == end:
                skip_entity = True
            if skip_entity:
                continue

            entity_indices = entity_indices + list(range(start, end))
            try:
                # print("creating span, or trying to")
                # print(text[start:end])
                span = doc.char_span(start, end, label=label, alignment_mode="strict")
            except:
                continue

            if span is None:
                # Log errors for annotations that couldn't be processed
                err_data = f"[{start, end}, ({text[start:end]})]\t{text}\n"
                print(err_data)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk("../spacy/train.spacy")
    nlp = spacy.blank("en")
    db = DocBin()
    for text, data in dev:
        entity_indices = []
        ents = []
        doc = nlp.make_doc(text)
        annot = data["entities"]
        for start, end, label in annot:
            skip_entity = False
            for idx in range(start, end):
                if idx in entity_indices:
                    skip_entity = True
                    break
            if start == end:
                skip_entity = True

            if skip_entity:
                continue

            entity_indices = entity_indices + list(range(start, end))
            try:
                # print("creating span, or trying to")
                # print(text[start:end])
                span = doc.char_span(start, end, label=label, alignment_mode="strict")
            except:
                continue

            if span is None:
                # Log errors for annotations that couldn't be processed
                err_data = f"[{start, end}, ({text[start:end]})]\t{text}\n"
                print(err_data)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk("../spacy/test.spacy")
    nlp = spacy.blank("en")
    db = DocBin()
    for text, data in test:
        entity_indices = []
        ents = []
        doc = nlp.make_doc(text)
        annot = data["entities"]
        for start, end, label in annot:
            skip_entity = False
            for idx in range(start, end):
                if idx in entity_indices:
                    skip_entity = True
                    break
            if start == end:
                skip_entity = True
            if skip_entity:
                continue

            entity_indices = entity_indices + list(range(start, end))
            try:
                span = doc.char_span(start, end, label=label, alignment_mode="strict")
            except:
                continue

            if span is None:
                # print("creating span, or trying to")
                # print(text[start:end])
                # Log errors for annotations that couldn't be processed
                err_data = f"[{start, end}, ({text[start:end]})]\t{text}\n"
                print(err_data)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk("../spacy/validation.spacy")


if __name__ == "__main__":
    main()
