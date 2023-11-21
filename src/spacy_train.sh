rm -rfv ../data/output
python3 -m spacy train ../spacy/config.cfg --output ../spacy/output --paths.train ../spacy/train.spacy --paths.dev ../spacy/test.spacy
