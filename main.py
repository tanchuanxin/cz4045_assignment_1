# Import modules
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.stem.snowball import SnowballStemmer
import string
import glob
import os
import random
from collections import Counter
import matplotlib.pyplot as plt


folder_names = ['Fairy Tales','Legal Documents']

# Looks into all .txt files in each dataset 
for folder in folder_names:
    file_list = glob.glob(os.path.join(os.getcwd(),folder,"*.txt"))

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
        tokens.extend(word_tokenize(story.lower()))
        tokens = list(filter(lambda token: token not in string.punctuation, tokens))

    # Create collection counter (dictionary) with key: token and value: num occurences of token
    tokenDict = Counter(tokens)
    print("Number of distinct tokens for "+folder+" dataset: " ,len(tokenDict))
    with open(folder+"_Outputs/tokens.txt", "w") as f:
        print(tokenDict, file=f)

    # Create list of length of each token
    tokenLengths = []
    for length in tokens:
        tokenLengths.append(len(length))

    # Create collection counter (dictionary) with key: length of token and value: num occurences of length of token
    uniqLengths = Counter(tokenLengths)

    # Plot length distribution: x-axis is the length of a token in number of characters, and the y-axis is the number of tokens of each length. 
    plt.bar(uniqLengths.keys(),uniqLengths.values())
    plt.title('Length distribution for tokens in '+folder+' dataset')
    plt.xlabel('Length of tokens in number of characters')
    plt.ylabel('Number of tokens of each length')
    plt.savefig(folder+'_figs/tokens.png')              # save plot distribution
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

    with open(folder+"_Outputs/stemmedWords.txt", "w") as f:
        print(stemmedDict, file=f)

    # Create list of length of each stemmed token
    stemmedLengths = []
    for length in stemmedTokens[0]:
        stemmedLengths.append(len(length))

    # Create collection counter (dictionary) with key: length of token and value: num occurences of length of token
    uniqStemmed = Counter(stemmedLengths)

    # Plot length distribution: x-axis is the length of a token in number of characters, and the y-axis is the number of tokens of each length. 
    plt.bar(uniqStemmed.keys(),uniqStemmed.values())
    plt.title('Length distribution for tokens in '+folder+' dataset after stemming')
    plt.xlabel('Length of stemmed tokens in number of characters')
    plt.ylabel('Number of stemmed tokens of each length')
    plt.savefig(folder+'_figs/stemmed.png')                # save plot distribution
    # plt.show()

    #=======================================================SENTENCE TOKENIZATION=======================================================================

    # List to store all sentence tokens
    sentence_tokens = []

    # Iterate through all text entries, tokenize by sentence and add to list
    for story in corpus:
        sentence_tokens.extend(sent_tokenize(story))

    # To get a dict where key is sentence and value is the number of words/ tokens in the sentence
    lengths =[]
    for i in sentence_tokens:
        lengths.append(len(i.split()))
    sentences = dict(zip(sentence_tokens,lengths))
    with open(folder+"_Outputs/sentences.txt", "w") as f:
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


    # Plot length distribution: x-axis is the length of a sentence in number of words/tokens, and the y-axis is the number of sentences of each length. 
    plt.clf()
    plt.bar(uniqSentences.keys(),uniqSentences.values())
    plt.title('Length distribution for sentences in '+folder+' dataset')
    plt.xlabel('Length of sentence in number of words/tokens')
    plt.ylabel('Number of sentences of each length')
    plt.savefig(folder+'_figs/sentence.png')                # save plot distribution
    # plt.show()

    #==========================================================POS TAGGING==========================================================================


    # Tokenizing function 
    def tokenizing(sentence):
        new = []
        new.extend(word_tokenize(sentence))
        new = list(filter(lambda token: token not in string.punctuation, new))
        return new

    # Current random selection of 3 sentences 
    random.seed(10)
    randomSentences = random.sample(sentence_tokens,3)
    sentence1 = tokenizing(randomSentences[0])
    sentence2 = tokenizing(randomSentences[1])
    sentence3 = tokenizing(randomSentences[2])
    with open(folder+"_POS/pos_tag.txt", "w") as f:
        print("3 random sentences : ",randomSentences,'\n',file=f)
        print("Parts of Speech for sentence 1: ",pos_tag(sentence1),'\n', file=f)
        print("Parts of Speech for sentence 2: ",pos_tag(sentence2),'\n',file=f)
        print("Parts of Speech for sentence 3: ",pos_tag(sentence3),'\n',file=f)

