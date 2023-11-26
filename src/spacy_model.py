import spacy
from spacy import displacy
import pandas as pd

def main():
    df = pd.read_csv("../data/spacy_test.csv")

    sentences = df["str"]
    ent_strs = df["ents"]
    nlp = spacy.load("../spacy/output/model-best")
    for idx, item in enumerate(sentences):
        doc = nlp(item)
        ent_set = []
        for ent in doc.ents:
            ent_set.append((ent.text,ent.label_))
        real_ent_set = ent_strs.iloc[idx].split("/")
        tokens = item.split()
        for idx, ent in enumerate(ent_set):
            print(f"{ent} == {tokens[idx],real_ent_set[idx]}")
    return

if __name__ == "__main__":
    main()
