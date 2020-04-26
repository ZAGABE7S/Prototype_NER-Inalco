from nltk import tokenize, word_tokenize, ne_chunk, tree2conlltags
import spacy

def line_to_sentences(file_path):

    # empty for lines
    tab = []
    
    # opening file in read mode
    f = open(file_path, "r")

    # loop through the file lines
    for line in f:

        #if the line is empty we skip it; by taking the length after removing blank spaces
        if len(line.strip()) > 0 :

            #segmenting line to sentence list by tokenizing lines
            cur_line = tokenize.sent_tokenize(line)

            # add the current line to the list tab by concatenating them
            tab  = tab + cur_line
    
    # returning the cleaned lines list
    return tab




#postagging function with nltk
def pos_tag_nltk(pos_tagger,sentence):

    tokens = word_tokenize(sentence) # tokenization 

    # pos_tagging | this gives us the (WORD,POS) 
    pos_tags = pos_tagger.tag(tokens)

    # create the tree, the tree is necessary to do IOB tagging with tree2conlltags
    # so we need to convert post_tags to tree with ne_chunk
    tree = ne_chunk(pos_tags)

    # IOB tagging | this gives us (WORD,POS,TAG) with tree2conlltags
    iob_tags = tree2conlltags(tree)

    return iob_tags



#postagging function with spacy
def pos_tag_spacy(nlp,sentence):
    pos = nlp(sentence)
    tags  = []
    for X in pos:
        if  X.ent_type_ == '':
            tags.append([str(X),str(X.pos_), str(X.ent_iob_)])
        else:
            tags.append([str(X),str(X.pos_), str(X.ent_iob_)+"-"+str(X.ent_type_)])
    return tags