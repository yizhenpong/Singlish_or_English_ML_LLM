from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


model_names = ["llama2_7b", "mistral_7b"] #dont change this!
model_name = model_names[0] # change based on model
ran_until = 300 #which row number

csv_file_path=f"output/llm_output_{model_name}.csv"

df = pd.read_csv(csv_file_path, sep='\t')
df = df[:ran_until]
df['llm_labels'] = df['llm_labels'].astype('int')
y_pred = df['llm_labels']
y_true = df['Target_Label']

accuracy = accuracy_score(y_true, y_pred)
print(f"{model_name} Accuracy: {accuracy}")

conf_matrix = confusion_matrix(y_true, y_pred)
# Display the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=[0, 1,2])
disp.plot(cmap='Blues', values_format='d')

plt.title('Confusion Matrix')
plt.show()
