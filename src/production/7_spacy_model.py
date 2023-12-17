import spacy
from spacy import displacy
import pandas as pd
import pickle
import random

def main():
    file = open("../../data/test_pickle", "rb")
    test = pickle.load(file)
    file.close()
    nlp = spacy.load("../../spacy/output/model-best")
    tp = 0 
    fp = 0
    tn = 0
    fn = 0
    num_samples = random.randint(10,30)
    total = len(test)
    sample_index = random.randint(num_samples,total)
    sample_range = (sample_index, sample_index + num_samples)
    print(sample_range)
    print(f"Will iterate over {total} items")
    for idx, item in enumerate(test):
        sentence = item[0]
        ents = item[1]
        ents = ents['entities']

        doc = nlp(sentence)
        ent_set_pred = []
        ent_set_true = []
        for ent in doc.ents:
            ent_set_pred.append((ent.text, ent.label_))
        for ent in ents:
            start, end, label = ent
            ent_set_true.append((sentence[start:end], label))
        if sample_range[0] < idx < sample_range[1]:
            print(f"{sentence} - (pred: {ent_set_pred}, true: {ent_set_true})")
        if ent_set_true == ent_set_pred:
            if len(ent_set_pred) == 0:
                tn += 1
            else:
                tp += 1
        else: 
            if len(ent_set_pred) == 0:
                fn += 1
            else:
                fp += 1
    p = tp + fp  
    n = tn + fn
    print(f"Does the predictions of true and negative match the total of items?: {'Yes' if total == p + n else 'No'}")
    print(f"Precision is {tp / (tp + fp):.2f}")
    print(f"Recall is {tp / (tp + fn):.2f}")
    print(f"F1-Score is {2*tp / (2*tp + fp + fn):.2f}")
    return

if __name__ == "__main__":
    main()
