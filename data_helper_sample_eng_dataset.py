import random

random.seed(10)

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

# Randomly sample lines
sampled_lines = random.sample(all_lines, min(sample_size, len(all_lines)))

# Write the sampled lines to the new file
with open(sampled_file_path, 'w') as sampled_file:
    sampled_file.writelines(sampled_lines)

# Print a message indicating the process is complete
print(f"{sample_size} lines randomly sampled and written to {sampled_file_path}")

