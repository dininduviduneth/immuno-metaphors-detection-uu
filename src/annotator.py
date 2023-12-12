import numpy as np 
import pandas as pd 
import json 
import csv


def main():
    df = pd.read_csv("../data/abstracts.csv", quoting=csv.QUOTE_ALL)
    print(df)
    pass



if __name__ == "__main__":
    main()
