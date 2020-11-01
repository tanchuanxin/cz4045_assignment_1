# CZ4045 Natural Language Processing Assignment 1
Members: Chua Peng Shaun, Ding Si Han, Gabriel Sze Whye Han, John Lim Jin, Tan Chuan Xin

# Introduction
This repository contains our groups' work for Assignment 1. The data folders are Q1_folder, Q2_folder, Q3_folder

Our source code comprises python scripts for Q1 and for Q3's application, and Colab notebooks for Q2 and Q3.

# Q1 Instructions - run in terminal
<b>Data</b><br>
The necessary datasets can already be found in the Q1_folder. The evaluation figures are also stored there. 

<b>Packages and Setup</b><br>
Only conventional python packages were used for this question. For NLP packages, we used NLTK.

<b>Run the script</b><br>
* In the main directory of the folder, activate the necessary environment that contains all the required packages for Q1. 
* Run the command `python 1_domain_specific_dataset_analysis.py` 
* Print statements for each of the three domains, containing <i>distinct tokens, stemmed tokens, number of sentences</i> will be printed
* The rest of the information can be found in Q1_folder under subdirectories of `domain_figs, domain_Outputs, domain_POS`


# Q2 Instructions - run in colab
<b>Data</b><br>
The necessary dataset can already be found in the Q2_folder as `data_airpods_reviews.csv`. It contains 30 handpicked reviews on Amazon for Apple Airpods, which can be found here: https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=cm_cr_srp_d_product_top?ie=UTF8

The reviews have been annotated 

<b>Packages and Setup</b><br>
<b>Colab Setup + Run the Notebook</b>
1. Copy this entire repository into Google Drive
2. Open the file `2_noun_adjective_pair_ranker.ipynb`
3. Scroll down to the markdown cell with message **Please input your own directory path towards the root location where this file is**
4. Replace the line with `%cd "path"` with your own path towards this repository folder 
5. Scroll back up to the top and run the cell with `!python -m spacy download en_core_web_lg`
6. Try and run the file with `Runtime > Run All`
7. If you receive an error like `[E050] Can't find model 'en_core_web_lg'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.`, this means the instance needs to be restarted to register that it has downloaded the `en_core_web_lg` module
    * <b>simply go to `Runtime > Restart and Run All` to fix this</b>
7. Colab will then prompt you for an authorization key in the cell with `drive.mount`. Click on the provided URL and copy the code, paste it back in the box
8. The rest of the code should run 
9. The outputs are in the notebook cells

<b>Other packages</b><br>
Conventional python packages were used for this question. For NLP packages, we used NLTK and Spacy (https://spacy.io/)



# Q3 Instructions - run in colab
> Try not to run this unless you really have to. It takes a long time to complete due to the training process

<b>Data</b><br>
The necessary dataset can already be found in the Q2_folder as `data_airpods_reviews.csv`. It contains 30 handpicked reviews on Amazon for Apple Airpods, which can be found here: https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=cm_cr_srp_d_product_top?ie=UTF8

The reviews have been annotated 

<b>Training Data</b><br>
For sentiment analysis, we made use of an external dataset. It can be found from the following:

Amazon reviews for "Cell Phones and Accessories" dataset
1. Visit https://nijianmo.github.io/amazon/index.html#subsets
2. Scroll down until you find ""Small" subsets for experimentation"
3. Click on "Cell Phones and Accessories"  >  "5-core (1,443,755 reviews)"
4. A message might pop up that says the dataset is dangerous, but it is not. Click on it to proceed with the download
5. Use and zip manager like 7zip, winzip to unzip the data into its raw .json file `Cell_Phones_and_Accessories_5.json`
6. Upload it into the `Q3_folder` directory under this repository


<b>Packages and Setup</b><br>
<b>Colab Setup + Run the Notebook</b>
1. Copy this entire repository into Google Drive
2. Open the file `3_sentiment_analysis_application.ipynb`
3-9. The rest follows as per Q2

<b>Other packages</b><br>
Conventional python packages were used for this question. For NLP packages, we used NLTK and Spacy (https://spacy.io/)




# Q3 Application Instruction - run in terminal
<b>Data</b><br>
The necessary dataset can already be found in the Q2_folder as `data_airpods_reviews.csv`. It contains 30 handpicked reviews on Amazon for Apple Airpods, which can be found here: https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=cm_cr_srp_d_product_top?ie=UTF8

The reviews have been annotated 

<b>Training Data</b><br>
The same `Cell_Phones_and_Accessories_5.json` should be uploaded in the local `Q3_folder` directory as well

<b>Run the script</b><br>
* In the main directory of the folder, activate the necessary environment that contains all the required packages for Q3. 
* Run the command `python 3_app.py` 
* Follow the terminal prompts to run the application 


<b>Other packages</b><br>
Conventional python packages were used for this question. For NLP packages, we used NLTK and Spacy (https://spacy.io/)
