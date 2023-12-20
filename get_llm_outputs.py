from open_source_llm import get_output_dict
import pandas as pd

'''
read test.txt file
input the sentences into the function `get_output_label`
output the labels
create the dataframe for the llm output
'''

# Path to the test.txt file
test_file_path = 'data/test.txt'
data = pd.read_table(test_file_path)
# print(data)

llm_labels = []
# explanation = []

for sentence in data['Text'].values:
    x = get_output_dict(sentence=sentence)
    llm_labels.append(x['label'])
    # explanation.append(x['explanation'])

data['llm_label'] = llm_labels
# data['reasoning'] = explanation

print(data)

# # Process sentences and get labels
# sentences, labels = process_sentences(test_file_path)

# # Create a DataFrame
# df_llm_output = pd.DataFrame({'Sentence': sentences, 'Label': labels})

# # Print the DataFrame
# print(df_llm_output)


'''how test.txt will look roughly:
Text	Target_Label
I LOVE YOU TOO	0
C-YA	0
:-)	0
BE MY GUEST	0
MANY MANY MANY PEOPLE	0
I already have a host and blogger.	1
Thank you for shopping	1
We next see FiB dancing the night away at the Bronze, having quite a good time with the guys there.	1
There may have been as many as ten stories in the book.	1
(2:25) Now both of them were naked, the man and his wife, but they felt no shame in front of each other.	1
GRAMM FELLOWSHIP Reagan Errera (OCNG) and Eugene Farrell (GEOG) received the 2011 U.S.	1
'''