#!/usr/bin/bash
echo "Running api search"
python3 1_semantic_search_api.py
echo "Ran api search"
echo "Running sentence generator"
python3 2_sentence_generator.py
echo "Ran sentence generator"
echo "Running general sentence annotator"
python3 3_annotation_texts_gen.py
echo "Ran general sentence annotator"
echo "Running spacy annotator"
python3 4_spacy_auto_annotation.py
echo "Ran spacy annotator"
echo "Running spacy annotator"
python3 5_create_test_train_validation_data.py 
echo "Ran spacy annotator"
