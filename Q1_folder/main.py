# Import modules
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string
import glob
import os
import random
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

# Initialize an array of all 3 datasets
folder_names = ['Legal Documents','Instruction Manuals','Biomedical Journals']

totalsentences = []                         # list to contain variables to be plotted for sentence tokenization comparison

# Looks into all .txt files in each dataset 
for folder in folder_names:
    file_list = glob.glob(os.path.join(os.getcwd(),"Q1_folder/"+folder,"*.txt"))

    print("==========================="+folder+" dataset==============================")
    # List to store all txt entries
    corpus = []
    
    # Append the contents of each .txt file into empty list
    for file_path in file_list:
        with open(file_path) as f_input:
            corpus.append(f_input.read())

    #=======================================================TOKENIZATION=======================================================================

    # List to store all tokens
    tokens = []
    # Iterate through all text entries, tokenize and add to list, remove punctuation and turn all words to lowercase
    for story in corpus:
        tokens.extend(word_tokenize(story.lower()))                                                 # all words lowercase

    tokens = list(filter(lambda token: token not in string.punctuation, tokens))                    # remove punctuations
    tokens = list(filter(lambda token: token not in stopwords.words('english'), tokens))            # remove stop words
    tokens = list(filter(lambda token: token if not token.isdigit() else "", tokens))               # remove numbers 


    # Create collection counter (dictionary) with key: token and value: num occurences of token
    tokenDict = Counter(tokens)
    print("Number of distinct tokens for "+folder+" dataset: " ,len(tokenDict))

    # Write to outputs a text file that prints collection counter (dictionary) with key: token and value: num occurences of token
    with open("Q1_folder/"+folder+"_Outputs/tokens.txt", "w") as f:
        print(tokenDict, file=f)

    # Create list of length of each token
    tokenLengths = []
    for length in tokens:
        tokenLengths.append(len(length))

    # Create collection counter (dictionary) with key: length of token and value: num occurences of length of token
    uniqLengths = Counter(tokenLengths)
    
    # Create new dict where keys of collection counter are sorted
    sorted_uniqLengths = {}
    for i in sorted (uniqLengths) : 
        sorted_uniqLengths[i] = uniqLengths[i]

    # Plot length distribution: x-axis is the length of a token in number of characters, and the y-axis is the number of tokens of each length. 
    barwidth = 0.4                                      # Set bar width of graph to 0.4
    x = np.arange(len(sorted_uniqLengths.keys()))       # Arrange keys of sorted dict in ascending order
    plt.bar(x+1,sorted_uniqLengths.values(),width = barwidth,label = 'tokenization')                # +1 to arranged x-axis to adjust 0 to 1
    plt.title('Length distribution for tokens in '+folder+' dataset')
    plt.xlim(0,20)
    plt.xlabel('Length of tokens in number of characters')
    plt.ylabel('Number of tokens of each length')
    plt.legend()
    plt.savefig("Q1_folder/"+folder+'_figs/tokens.png')              # save plot distribution
    # plt.show()

    #===========================================================STEMMING==========================================================================

    # Use snowball stemmer toolkit
    snowball = SnowballStemmer(language = 'english')
    def stemming(words):
        new = []
        stem_words = [snowball.stem(x) for x in (words[:])]
        new.append(stem_words)
        return new


    stemmedTokens = stemming(tokens)
    # Create collection counter (dictionary) with key: stemmed token and value: num occurences of stemmed token
    stemmedDict = Counter(stemmedTokens[0])
    print("Number of distinct tokens after stemming for "+folder+" dataset: " ,len(stemmedDict))

    # Write to outputs a text file that prints collection counter (dictionary) with key: stemmed token and value: num occurences of stemmed token
    with open("Q1_folder/"+folder+"_Outputs/stemmedWords.txt", "w") as f:
        print(stemmedDict, file=f)

    # Create list of length of each stemmed token
    stemmedLengths = []
    for length in stemmedTokens[0]:
        stemmedLengths.append(len(length))

    # Create collection counter (dictionary) with key: length of token and value: num occurences of length of token
    uniqStemmed = Counter(stemmedLengths)

    # Create new dict where keys of collection counter are sorted
    sorted_uniqStemmed = {}
    for i in sorted (uniqStemmed) :
        sorted_uniqStemmed[i] = uniqStemmed[i] 

    # Plot length distribution: x-axis is the length of a token in number of characters, and the y-axis is the number of tokens of each length. 
    # Plot length distribution for stemming in comparison to pre-stemming
    x = np.arange(len(sorted_uniqStemmed.keys()))               # Arrange keys of sorted dict in ascending order
    y = x+1                                                     # +1 to arranged x-axis to adjust 0 to 1
    plt.bar(y+barwidth,sorted_uniqStemmed.values(),width = barwidth, label = 'stemmed') # Add barwidth to x-axis so that stemmed bargraph appears beside tokenized bar graph
    plt.title('Comparison of length distribution \nfor tokens in '+folder+' dataset after stemming')
    plt.xlim(0,20)
    plt.xlabel('Length of tokens in number of characters')
    plt.ylabel('Number of tokens of each length')
    plt.legend()
    plt.savefig("Q1_folder/"+folder+'_figs/stemmed.png')                # save plot distribution
    # plt.show()

    #=======================================================SENTENCE TOKENIZATION=======================================================================

    # List to store all sentence tokens
    sentence_tokens = []

    # Iterate through all text entries, tokenize by sentence and add to list
    for story in corpus:
        sentence_tokens.extend(sent_tokenize(story))

    # To get a dictionary where key is sentence and value is the number of words/ tokens in the sentence
    lengths =[]
    for i in sentence_tokens:
        lengths.append(len(i.split()))
    sentences = dict(zip(sentence_tokens,lengths))

    # Write to outputs a text file that prints dictionary where key is sentence and value is the number of words/ tokens in the sentence
    with open("Q1_folder/"+folder+"_Outputs/sentences.txt", "w") as f:
        print(sentences, file=f)

    # Create collection counter (dictionary) with key: sentences and value: num occurences of sentences
    sentenceDict = Counter(sentence_tokens)
    print("Number of distinct sentences for "+folder+" dataset: ",len(sentenceDict),'\n')

    # Create list of length of each sentence
    sentenceLengths = []
    for length in sentence_tokens:
        sentenceLengths.append(len(length.split()))

    # Create collection counter (dictionary) with key: length of sentence and value: num occurences of length of sentence 
    uniqSentences = Counter(sentenceLengths)

    # Create new dict where keys of collection counter are sorted
    sorted_uniqSentences= {}
    for i in sorted(uniqSentences) :                        # variables must be sorted so that line graph plots doesn't jump everywhere
        sorted_uniqSentences[i] = uniqSentences[i] 

    # Plot length distribution: x-axis is the length of a sentence in number of words/tokens, and the y-axis is the number of sentences of each length. 
    plt.clf()                                               # Clear the graph plot of previous graphs
    x = sorted_uniqSentences.keys()                         # store as variables and append to list for plotting of all sentences for comparison
    y = sorted_uniqSentences.values()
    totalsentences.append(x)
    totalsentences.append(y)
    plt.bar(uniqSentences.keys(),uniqSentences.values())
    plt.title('Length distribution for sentences in '+folder+' dataset')
    plt.xlim(0,100)
    plt.xlabel('Length of sentence in number of words/tokens')
    plt.ylabel('Number of sentences of each length')
    plt.savefig("Q1_folder/"+folder+'_figs/sentence.png')                # save plot distribution
    # plt.show()
    plt.clf()

    #==========================================================POS TAGGING==========================================================================

    # Tokenizing function 
    def tokenizing(sentence):
        new = []
        new.extend(word_tokenize(sentence))
        new = list(filter(lambda token: token not in string.punctuation, new))
        return new

    # Set random.seed() to fix random selection of 3 sentences and select 3 random sentences
    # Tokenize each sentence
    random.seed(13)
    randomSentences = random.sample(sentence_tokens,3)
    sentence1 = tokenizing(randomSentences[0])
    sentence2 = tokenizing(randomSentences[1])
    sentence3 = tokenizing(randomSentences[2])

    # Write to outputs a text file that prints the 3 random selected sentences in the dataset and run POS Tagging on the tokens
    with open("Q1_folder/"+folder+"_POS/pos_tag.txt", "w") as f:
        print("3 random sentences : ",randomSentences,'\n',file=f)
        print("Parts of Speech for sentence 1: ",pos_tag(sentence1),'\n', file=f)
        print("Parts of Speech for sentence 2: ",pos_tag(sentence2),'\n',file=f)
        print("Parts of Speech for sentence 3: ",pos_tag(sentence3),'\n',file=f)

#=======================================================SENTENCE TOKENIZATION=======================================================================
plt.clf()
plt.title('Length distribution for sentences in all datasets')
plt.plot(totalsentences[0],totalsentences[1],label = 'Legal Documents')             # line plots to plot all 3 sentence tokenization graphs for comparison
plt.plot(totalsentences[2],totalsentences[3],label = 'Instruction Manuals')
plt.plot(totalsentences[4],totalsentences[5],label = 'Biomedical Journals')
plt.xlim(0,100)
plt.xlabel('Length of sentence in number of words/tokens')
plt.ylabel('Number of sentences of each length')
plt.legend()
plt.savefig("Q1_folder/"+'figs/sentences.png')                # save plot distribution
# plt.show()
