# Figurative Language Detection in the Frame of Humanities for Medicine

This project is an attempt to implement and test a language model to detect figurative language usage, such as metaphors in immunology based academic texts.

## Scripts and locations

This repository (located in ```src/production```) contains the scripts used for the following purposes.

1. Extraction of abstracts from [Semantic Scholar](https://www.semanticscholar.org/).
2. Spliting abstract texts into sentences and saving them in a JSON file.
3. Generate a feed dataset with a given ratio of sentences which contains metaphors and sentences which doesn't contain metaphors.
4. Auto-annotate sentences with NER tags for metaphors.
5. Splitting an annotated dataset into train, test and validation sets.
6. Train the RoBERTa model and save it.
7. Pull a model and run train - test validation.

The steps 1 - 5 are mainly given for the preparation of the dataset. We have given two shell scripts to run steps 1 - 5 (for the case where the data is first extracted and prepared) and to run steps 2 - 5 (for the case where the user already has a dataset and only the preparation needs to be done).

Once the datasets are prepared, training the model needs to be done using ```6_spacy_train.py```.

NOTE:
* Other scripts we used to try out different models and scenarios has been added to ```src/experiments```.
* The ```spacy``` folder consists the configurations required to train, test and validate the model.
* The ```data``` folder will hold the data being prepared.

## Scripts documentation
### 1. Semantic search API (file ```1_semantic_search_api.py```)

This script hits ```http://api.semanticscholar.org/graph/v1/paper/search/bulk?query={query}&fields={fields}&year=2022-``` URL with the parameters ```query``` and ```fields``` given by the user, extracts abstracts from papers based on the ```query``` and saves them in a JSON document in the following format.

```
{
    "paperId":"000407663906d6235e1e6a45a7bee245a0d6f3c3",
    "title": "<ABSTRACT TEXT>",
    "isOpenAccess": false
}
```

This JSON document can be used in the next script which is ```2_sentence_generator.py```.

## 2. Splitting abstract texts into sentences (file: ```2_sentence_generator.py```)