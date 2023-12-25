# Introduction
The aim of this project is to classify sentences into Singlish or English using traditional machine learning and large language model approaches.

# Datasets
original datasets from
    - "https://www.kaggle.com/datasets/rtatman/the-national-university-of-singapore-sms-corpus/data?select=smsCorpus_en_2015.03.09_all.json"
        - singlish_en and singlish_chi (not used)
    -  https://zenodo.org/records/205950
        - randomly selected 60,000 sets

# Sampling data and Combining datasets
data_helper to clean and generate `final_dataset.txt` with sentence and corresponding labels 
    - Singlish (0) English (1)

# Approach
Traditional Machine Learning methods conducted to do classification
    - tokenisation and cleaning of strings
    - logistic regression
    - naive bayes 
    run `traditional_ML.ipynb`

Large Language model (LLM) methods 
    Models chosen:
        - llama2 7B model 
        - Mistral 7b model
    How to interact with the two models:
        - `open_source_llm.py` describes how we interact with the LLM
        - Structured Output is expected:
             ```json{"sentence": "If he wants a place, he must jostle for it.",
                    "label": 1} ```
        - Comment line 42 and uncomment lines 44-46 in `open_source_llm.py` to get this output:
            ```json{"sentence": "Haha 6pm lo",
                    "label": 0,
                    "explanation": "The sentence is in Singlish format with 'lo' as a colloquial way of expressing
                                     'is' or 'at', indicating a time expression. Thus, it is classified as Singlish."}```
    run `get_llm_outputs_1.py` to generate the csv file in `output` folder for the first time
    run `get_llm_outputs_3.py` to update the csv file accordingly
        - note that there will be an extra label (2) for sentences that the LLM is unable to classify due to various reasons:   
            - sentences that may be disrespectful
            - sentence contains another language, eg shld be classified as German rather than Singlish or English
            - Output parser error 
    run `eval_llm_outputs` to generate the confusion matrix and accuracy score
        - edit these fields accordingly: `model_name` and `ran_until` which represents the row number

# Experiment 
Only ran rows 1-300 for llama2 7B model and rows 1-2300 for mistral 7b model
    - mistral 7b took about 3.5 hours to run

# Results 
Please see the research paper uploaded.
