from utils import *
from config import *
from pprint import pprint

import spacy
nlp = spacy.load("fr_core_news_sm")

# extract sentences from the dataset
sentences = line_to_sentences(DATA_INPUT_PATH)

#renaming the output
DATA_OUTPUT_PATH += "/out_spacy.csv"

# print the head of the output [csv ]file
print("Sentence #,Word,POS,Tag", file=open(DATA_OUTPUT_PATH, "a", encoding="utf-8"))

# looping through the sentences
for id,sentence in enumerate(sentences):

    tags = pos_tag_spacy(nlp,sentence)
    #print(tags)

    for id,word_pos_tag in enumerate(tags):
        # print the beginning part of every sentence
        if id==0:
            s = "Sentence: "+str(id)+","
        else :
            s = ","
        
        # concatenate word pos tag in s
        s += word_pos_tag[0] + "," + word_pos_tag[1] + "," + word_pos_tag[2]

        #write s to fie
        print(s, file=open(DATA_OUTPUT_PATH, "a", encoding="utf-8"))

