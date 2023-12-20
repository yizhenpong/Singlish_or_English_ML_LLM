import json
import pandas as pd
import random
random.seed(10)

############################################################################################################################## 
'''format singlish corpus'''
# Load the JSON file
with open('original_data/smsCorpus_en_2015.03.09_all.json', 'r') as file:
    data = json.load(file)

# Extract the text from each index under the "message" key
messages = [item['text']['$'] for item in data['smsCorpus']['message']]
# print(messages[:5])

# Create a DataFrame with only the second column
singlish_text = pd.DataFrame({'Message': messages})

# Save the DataFrame to a text file (change 'singlish_eng_text.txt' to your desired file name)
singlish_text.to_csv('./data/singlish_corpus.txt', sep='\t', index=False, header=False)

############################################################################################################################## 
'''sample eng dataset'''

# Specify the path to your text file
file_path = "original_data/webis-simple-sentences-17-corpus-test.txt"

# Specify the path for the new file with the sampled lines
sampled_file_path = "data/smaller_eng_corpus.txt"

# Specify the number of lines you want to sample
sample_size = 60000

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the entire contents of the file
    all_lines = file.readlines()
    file.close()

# Randomly sample lines
sampled_lines = random.sample(all_lines, min(sample_size, len(all_lines)))

# Write the sampled lines to the new file
with open(sampled_file_path, 'w') as sampled_file:
    sampled_file.writelines(sampled_lines)
    sampled_file.close()

# Print a message indicating the process is complete
print(f"{sample_size} lines randomly sampled and written to {sampled_file_path}")

############################################################################################################################## 
''' combine datasets & add labels [Singlish (0) English (1)] '''

# Read Singlish text file
with open('data/singlish_corpus.txt', 'r', encoding='utf-8') as singlish_file:
    singlish_sentences = [line.strip() for line in singlish_file]
    singlish_file.close()

# Read English text file
with open('data/smaller_eng_corpus.txt', 'r', encoding='utf-8') as english_file:
    english_sentences = [line.strip() for line in english_file]
    english_file.close()

# Label the sentences
singlish_labels = [0] * len(singlish_sentences)
english_labels = [1] * len(english_sentences)

# Combine data into a DataFrame
data = {'Text': singlish_sentences + english_sentences,
        'Target_Label': singlish_labels + english_labels}

df_final = pd.DataFrame(data)

# Save the final dataset to a text file
df_final.to_csv('./data/final_dataset.txt', sep='\t', index=False, escapechar='\\')

