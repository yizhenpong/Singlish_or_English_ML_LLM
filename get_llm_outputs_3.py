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

model_name = model_names[1] # change based on the model you would like
start = 15
end = 100

'''
run in cycles of 100 and save continuously to csv
'''


if model_name == model_names[0]:
    x = get_rows(model_name)
    # print(x)
    fn = get_output_dict_llama
    while start < x:
        end = min(end,x)
        print(llm_outputs(start,end,fn,model_name))
        start, end = start + 100, end +100
elif model_name == model_names[1]:
    x = get_rows(model_name)
    # print(x)
    fn = get_output_dict_mistral
    while start < x:
        end = min(end,x)
        print(llm_outputs(start,end,fn,model_name))
        start, end = start + 100, end +100

else:
    print("model is not available for use")

# print(llm_outputs(242,245))


