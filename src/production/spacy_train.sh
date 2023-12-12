# -g flags specifies ID for your device to use for computations, in our case 0 indicates we should use a GPU
python3 -m spacy train ../spacy/config_gpu.cfg --output ../spacy/output --paths.train ../spacy/train.spacy --paths.dev ../spacy/test.spacy -g 0
