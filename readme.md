# Introduction
This project aims to classify sentences into Singlish or English using traditional machine learning and large language model approaches.

# Collaborators
The code and report sections were collaboratively completed by Pong Yi Zhen 方怡蓁 (2023级元培学院交换生 Yuanpei College Peking University Exchanger) and 游历 from (2021级外国语学院本科生 Peking University)

# Datasets
original datasets from
- Tao Chen and Min-Yen Kan (2013). Creating a Live, Public Short Message Service Corpus: The NUS SMS Corpus. Language Resources and Evaluation, 47(2)(2013), pages 299-355. URL: https://link.springer.com/article/10.1007%2Fs10579-012-9197-9
    - "https://www.kaggle.com/datasets/rtatman/the-national-university-of-singapore-sms-corpus/data?select=smsCorpus_en_2015.03.09_all.json"
    - singlish_en (used) and singlish_chi (not used)
-  Kiesel, J., Stein, B., & Lucks, S. (2017). Webis-Simple-Sentences-17 Corpus [Data set]. Network and Distributed System Security Symposium 2017 (NDSS 2017), San Diego, California. Zenodo. https://doi.org/10.5281/zenodo.205950
    - https://zenodo.org/records/205950
    - randomly selected 60,000 sets, set seed = 10

# Sampling data and Combining datasets
`data_helper.py` to clean and generate `final_dataset.txt` with sentence and corresponding labels 
- Singlish (0) English (1)

# Approach
Traditional Machine Learning methods conducted to do classification
- logistic regression
- SVM
- naive bayes 
    run `traditional_ML.ipynb`

Large Language model (LLM) methods 
- Models chosen:
    - llama2 7B model 
    - Mistral 7B model
- How to interact with the two models:
    - `open_source_llm.py` describes how we interact with the LLM
    - Structured Output is expected:
        ```json
            {"sentence": "If he wants a place, he must jostle for it.",
            "label": 1} 
        ```
    - Comment line 42 and uncomment lines 44-46 in `open_source_llm.py` to get this output:
        ``` json
            {"sentence": "Haha 6pm lo",
            "label": 0,
            "explanation": "The sentence is in Singlish format with 'lo' as a colloquial way of expressing
                                'is' or 'at', indicating a time expression. Thus, it is classified as Singlish."}
        ```

- run `get_llm_outputs_1.py` to generate the csv file in `output` folder for the first time
- run `get_llm_outputs_3.py` to update the csv file accordingly
    - note that there will be an extra label (2) for sentences that the LLM is unable to classify due to various reasons:   
        - sentences that may be disrespectful
        - sentence contains another language, eg shld be classified as German rather than Singlish or English
        - Output parser error 
- run `eval_llm_outputs` to generate the confusion matrix and accuracy score
    - edit these fields accordingly: `model_name` and `ran_until` which represents the row number

# Experiment 
Only ran rows 1-300 for llama2 7B model and rows 1-2300 for mistral 7b model
- mistral 7b took about 3.5 hours to run

# Results 
Please refer to the research paper and note that it is unfortunately written in Chinese. I have translated the abstract in English for those who would like to get a quick overview.

【摘要】目的：在自然语言处理领域，通过机器学习和大语言模型（LLM）方法鉴别“新式英语” 及我们普遍认知的“英语”。方法：采用 Logistic Regression, Support VectorMachine, Naïve Bayes 等机器学习方法，及零射击提示（Zero Shot Prompting）Llama2 7B 和 Mistral 7B 的 LLM 进行文本分类任务，标注新式英语为 0，英语为 1，LLM 特例为 2。采用的数据集包括 The National University of Singapore SMS Corpus 及经过随机筛
选 Webis-Simple-Sentences-17 Corpus 合成的数据。假设：Zero Shot Prompting LLM 的效果会比传统机器学习方式更好。结论：从准确率的角度看机器学习的方法比 LLM 的结果较好。然而，我们使用的 LLM 仅有 7B，对比而言兴起的 GPT3 推测为 175B，GPT4则是 1.76T。此外，我们仅仅采用最原始的 Zero Shot，并没有尝试其他更有效的提示方式如 Few Shot, Chain of Thought, Tree of thought，等。因此进一步探究是有必要的。

【Abstract】Purpose: Utilising traditional machine learning methods and large language model for a NLP text classification task, distinguishing "Singlish" from "English". Methods: Various machine learning methods such as Logistic Regression, Support Vector Machine, Naïve Bayes, and Zero-Shot Prompting with Llama2 7B and Mistral 7B LLMs are employed for text classification tasks. Singlish is labeled as 0, English as 1, and exceptions in LLM methods as 2. The datasets used include The National University of Singapore SMS Corpus and randomly selected sentences from Webis-Simple-Sentences-17 Corpus. Hypothesis: Our hypothesis is that Zero Shot Prompting LLM will outperform traditional machine learning methods. Conclusion: Based on accuracy scores, machine learning methods perform better than LLM. However, the LLM used in this study is only 7B parameter size, just for comparison sake, the speculated sizes of GPT3 and GPT4 (as part of the GPT family) are 175B and 1.76T, respectively. Additionally, we only employed the most basic zero shot prompting method, without exploring more effective prompting techniques such as Few Shot, Chain of Thought, Tree of Thought, etc. Hence, further investigation is necessary.




