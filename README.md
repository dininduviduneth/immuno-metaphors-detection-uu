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

This script breaks each abstract into individual sentences and searches for any metaphorical keywords given in ```helpers.py``` and marks the sentences which contains a keyword as ```has_metaphor: 1```, if not ```has_metaphor: 0```.

The saves the sentences in a JSON document in an array of the following format.

```
{
        "sentence": "<SENTENCE>",
        "metaphors": [
            "<metaphor 1>",
            "<metaphor 2>"
        ],
        "has_metaphor": 1
}
```

## 3/4. Autogenerating spacy annotations

For our model, we require the data to be in the ```spacy annotations format```. This scripts consumes the sentences generated from the previous script and auto-annotate them based on the presence of metaphorical keywords. It also has the configurability to change the proportions of the metaphorical and non-metaphorical sentences we use for training.

An example of a generated spacy annotation is as follows:

```
[
    "the immune system is composed of organs, tissues, and cells tasked with providing protection from invading pathogens.",
    {
        "entities": [
            [
                0,
                3,
                "O"
            ],
            [
                4,
                10,
                "O"
            ],
            [
                11,
                17,
                "O"
            ],
            [
                18,
                20,
                "O"
            ],
            [
                21,
                29,
                "O"
            ],
            [
                30,
                32,
                "O"
            ],
            [
                33,
                40,
                "O"
            ],
            [
                41,
                49,
                "O"
            ],
            [
                50,
                53,
                "O"
            ],
            [
                54,
                59,
                "O"
            ],
            [
                60,
                66,
                "O"
            ],
            [
                67,
                71,
                "O"
            ],
            [
                72,
                81,
                "O"
            ],
            [
                82,
                92,
                "O"
            ],
            [
                93,
                97,
                "O"
            ],
            [
                98,
                106,
                "MET"
            ],
            [
                107,
                117,
                "O"
            ]
        ]
    }
]
```

This can be re-used to generate additional tags (or manually annotate) using the following graphical tool --> [Spacy Online NER Annotator](https://tecoholic.github.io/ner-annotator/).

## 5. Creating train, test and validation datasets

This script splits the data into train, test and validation and saves them in the required format of the model.

## 6. Training the model

This shell script will train the model from the generated datasets and save it for later use.

## 7. Use the model for performace measurement

This script will measure and provide the performance of the trained model.