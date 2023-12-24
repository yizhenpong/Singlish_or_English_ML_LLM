original datasets from
    - "https://www.kaggle.com/datasets/rtatman/the-national-university-of-singapore-sms-corpus/data?select=smsCorpus_en_2015.03.09_all.json"
        - singlish_en and singlish_chi (not used)
    -  https://zenodo.org/records/205950
        - randomly selected 60,000 sets

data_helper to clean and generate `final_dataset.txt` with sentence and corresponding labels - Singlish (0) English (1)

traditional ML methods conducted to do classification
    - tokenisation and cleaning of strings
    - logistic regression
    - naive bayes 
    run `traditional_ML.ipynb`

LLM
    - llama2 7B model chosen
    - mistral 7b also possible
    run `get_llm_outputs_1.py` to generate the csv file
    run `get_llm_outputs_3.py` to update the csv file accordingly
