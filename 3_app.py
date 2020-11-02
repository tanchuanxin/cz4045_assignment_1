# Import necessary libraries
import numpy as np
import pandas as pd
import json
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.linear_model import SGDClassifier

# Load airpods Reviews and Rotten Tomatoes Dataset
airpods_df = pd.read_csv('Q3_folder/data_airpods_reviews.csv')

# Load amazon reviews into dataframe
print("loading training data... this will take some time...")
amazon_json_list = []
with open('Q3_folder/Cell_Phones_and_Accessories_5.json', 'r') as file:
    for line in tqdm(file):
        amazon_json_list.append(json.loads(line))

# some entries have missing values, clean them out
print("cleaning training data...")
amazon_json_list_clean = []
for amazon_json in tqdm(amazon_json_list, total=len(amazon_json_list), position=0, leave=True):
  try:
    amazon_json_list_clean.append({'Reviews': amazon_json['reviewText'], 'Stars': int(amazon_json['overall'])})
  except:
    pass

amazon_df = pd.DataFrame(amazon_json_list_clean)               
amazon_df.head()

# We will truncate this dataset because it is so huge - len(amazon_df) = 1 127 672
# We use less than our experiment cos the app should be snappier
amazon_df = amazon_df[:50000]

print("Data prepared")


token = RegexpTokenizer(r'[a-zA-Z0-9]+')


# Helper function to categorize sentiment to negative, neutral, positive based on star rating
def categorize_sentiment(value):
  value = int(value)
  if value >= 4:
    return 2
  if value == 3: 
    return 1
  else:
    return 0

# Apply helper function to amazon and airpods dataframes
amazon_df['Sentiment_Category'] = amazon_df['Stars'].apply(categorize_sentiment)
airpods_df['Sentiment_Category'] = airpods_df['Stars'].apply(categorize_sentiment)



# Define sentiment labels
sentiment_labels = ['negative', 'neutral', 'positive']


# Function to anylse sentiment of input string
def sentiment_analysis(input_string):
    cv = CountVectorizer(stop_words='english', ngram_range=(1,1), tokenizer = token.tokenize)
    # text_counts = cv.fit_transform(amazon_df.Reviews.tolist() + airpods_df.Reviews.tolist() + [input_string])
    # amazon_text_counts = text_counts[:-(len(airpods_df)+1)]
    # airpods_text_counts = text_counts[-(len(airpods_df)+1):-1]
    # input_string_counts = text_counts[-1]

    text_counts = cv.fit_transform(amazon_df.Reviews.tolist() + airpods_df.Reviews.tolist() + [input_string])
    amazon_text_counts = text_counts[:-(len(airpods_df)+1)]
    airpods_text_counts = text_counts[-(len(airpods_df)+1):-1]
    input_string_counts = text_counts[-1]
  
    X_train = amazon_text_counts
    y_train = amazon_df.Sentiment_Category

    # SGD Classifier
    SGDC = SGDClassifier()
    SGDC.fit(X_train, y_train)
    return SGDC.predict(input_string_counts)

# Function to take user input and return sentiment results
def analyze_sentence():
    input_string = str(input("\n\nWhat sentence do you want to analyze?  "))
    print("=" * 50)
    print("Thank you for inputting your sentence, the sentence we received is:", input_string)
    print("=" * 50)
    print("Analyzing your sentence ...")
    print("=" * 50)
    print("Analysis completed! Your sentence is classified to have a", sentiment_labels[sentiment_analysis(input_string)[0]], "sentiment")
    print("=" * 50)

def main():
    input_name = str(input("Welcome to Sentiment Analyzer! How should I address you? "))
    print("=" * 50)    
    print("Hello %s!" % input_name, end=' ')

    print("\nPress 1 to see our sentiment analysis of 30 Airpod reviews!")
    print("Press 2 to analyze your own sentence!")
    choice = str(input("What will it be? "))

    if choice == '1':
      print("Here is our sentiment analysis of some Airpod reviews.")

      exit = False
      
      for index, review in enumerate(airpods_df.Reviews.tolist()):
        if exit:
          break
        while not exit:
          print("\n\nReview", index + 1, ":", review)
          print("\nThinking.... please press <ENTER> in case the print outputs do not refresh after some time")
          print("\nWe predict this Airpod review to have a ", sentiment_labels[sentiment_analysis(review)[0]], "sentiment")
          print("-" * 50)

          next = str(input("To see another Airpod review prediction, input 1. Else press any key. "))
          if next != '1':
            exit = True
          break

        print("We are all done analyzing our Airpod reviews! Now you can have a go too")
    
    
    analyze_sentence()

    while True:
        input_request = str(input("To enter another sentence, enter 1. To exit, enter another other characters: "))
        print("=" * 50)
        if input_request == '1':
            analyze_sentence()
        else:
            print("Thanks for being part of our NLP Application, see you soon!")
            break 



if __name__ == "__main__":
    main()