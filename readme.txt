original datasets from
    - "https://www.kaggle.com/datasets/rtatman/the-national-university-of-singapore-sms-corpus/data?select=smsCorpus_en_2015.03.09_all.json"
        - singlish_en and singlish_chi (not used)
    -  https://zenodo.org/records/205950
        - randomly selected 60,000 sets

data_helper to clean and generate `final_dataset.txt` with sentence and corresponding labels 
    - Singlish (0) English (1)

traditional ML methods conducted to do classification
    - tokenisation and cleaning of strings
    - logistic regression
    - naive bayes 
    run `traditional_ML.ipynb`

Large Language model (LLM)
    - llama2 7B model chosen
    - mistral 7b also possible
    `open_source_llm.py describes how we interact with the LLM
        - Structured Output
        - Currently expected output:
             ```json{"sentence": "If he wants a place, he must jostle for it.",
                    "label": 1} ```
        - Comment line 42 and uncomment lines 44-46 to get this output:
            ```json{"sentence": "Haha 6pm lo",
                    "label": 0,
                    "explanation": "The sentence is in Singlish format with 'lo' as a colloquial way of expressing
                                     'is' or 'at', indicating a time expression. Thus, it is classified as Singlish."}```
    run `get_llm_outputs_1.py` to generate the csv file for the first time
    run `get_llm_outputs_3.py` to update the csv file accordingly
        - note that there will be an extra label (2) for sentences that the LLM is unable to classify due to various reasons:   
            - sentences that may be disrespectful
            - sentence contains another language, eg shld be classified as German rather than Singlish or English
            - Output parser error 
    run `eval_llm_outputs` to generate the confusion matrix and accuracy score
