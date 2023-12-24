from get_llm_outputs_1 import get_rows, llm_outputs
from open_source_llm import get_output_dict_llama, get_output_dict_mistral

"""
to clear all previous outputs in csv file, run `get_llm_outputs_1.py`
run this command in your terminal: 
    -`ollama pull llama2` or `ollama pull mistral`
    - if you have not downloaded ollama, please refer to instructions in `open_source_llm.py`
update the llm_output.csv file by using the `llm_outputs` function 
"""
model_names = ["llama2_7b", "mistral_7b"] #dont change this!

model_name = model_names[1]
start_index = 0
end_index = 10

if model_name == model_names[0]:
    print(get_rows(model_name))
    print(llm_outputs(start_index,end_index,get_output_dict_llama,model_names[0]))
elif model_name == model_names[1]:
    print(get_rows(model_name))
    print(llm_outputs(start_index,end_index,get_output_dict_mistral,model_names[1]))
else:
    print("model is not available for use")

# print(llm_outputs(242,245))


