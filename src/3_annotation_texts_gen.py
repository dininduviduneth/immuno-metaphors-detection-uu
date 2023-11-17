# TO GENERATE A TEXT FILE WITH MET 1:3 NON-MET SENTENCES

import json

with open('../data/sentences.json', 'r') as file:
    data = json.load(file)

to_text_file = []

group_of_four = []

BREAK_POINT = 0

for item in data:
    if BREAK_POINT <= 2500:
        if item['has_metaphor'] == 1:
            if len(group_of_four) == 0:
                group_of_four.append(item['sentence'])
        else:
            if len(group_of_four) >= 1:
                group_of_four.append(item['sentence'])

        if len(group_of_four) == 4:
            for sentence in group_of_four:
                to_text_file.append(sentence)
                group_of_four = []

        BREAK_POINT += 1
    else:
        break

with open('../data/spacy_feed.txt', 'w') as f:
    for text in to_text_file:
        f.write(text)
        f.write('\n')