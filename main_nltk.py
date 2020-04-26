from nltk.tag.stanford import StanfordPOSTagger
from utils import *
from config import *
import os

# download maxent_ne_chunker if it's not already up to date in the nltk data
import nltk
nltk.download('maxent_ne_chunker')

# get the current absolute path
CURRENT_ABSOLUTE_PATH = os.path.abspath(os.getcwd())

# instantiate the StanfordPOSTagger(main,model) class with config parameter
pos_tagger = StanfordPOSTagger(CURRENT_ABSOLUTE_PATH + "/" + STANFORD_POSTAGGER_JAR_PATH,CURRENT_ABSOLUTE_PATH + "/" + STANFORD_POSTAGGER_MODEL_PATH)

#renaming the output
DATA_OUTPUT_PATH += "/out_nltk.csv"

# extract sentences from the dataset
sentences = line_to_sentences(DATA_INPUT_PATH)

# print the head of the output [csv ]file
print("Sentence #,Word,POS,Tag", file=open(DATA_OUTPUT_PATH, "a", encoding="utf-8"))

# looping through the sentences
for id,sentence in enumerate(sentences):

    tags = pos_tag_nltk(pos_tagger,sentence)
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