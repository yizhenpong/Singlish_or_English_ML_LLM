from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


model_names = ["llama2_7b", "mistral_7b"] #dont change this!
model_name = model_names[1]
csv_file_path=f"data/llm_output_{model_name}.csv"
df = pd.read_csv(csv_file_path, sep='\t')
df = df[:10]
df['llm_labels'] = df['llm_labels'].astype('int')
y_pred = df['llm_labels']
y_true = df['Target_Label']

conf_matrix = confusion_matrix(y_true, y_pred)

# Display the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=[0, 1])
disp.plot(cmap='Blues', values_format='d')

plt.title('Confusion Matrix')
plt.show()

# # Plot the confusion matrix using seaborn
# plt.figure(figsize=(8, 6))
# sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', annot_kws={"size": 16})
# plt.xlabel('Predicted Labels')
# plt.ylabel('True Labels')
# plt.title('Confusion Matrix')
# plt.show()