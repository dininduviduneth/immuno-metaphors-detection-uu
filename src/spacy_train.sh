rm -rfv ../data/output
python3 -m spacy train ../spacy/config_gpu.cfg --output ../spacy/output --paths.train ../spacy/train.spacy --paths.dev ../spacy/test.spacy
