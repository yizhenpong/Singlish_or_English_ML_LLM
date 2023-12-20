"""
instructions:
- download ollama `https://ollama.ai/download`
    - ollama pull llama2
- pip install langchain
"""

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

'''
Run llama2 and get outputs for this large language model
'''

############################################################################################################################## 

'''loading the model'''

llm = Ollama(model='llama2',
                callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))


'''building schemas'''
sentence_schema = ResponseSchema(name="sentence", description="This is the input sentence")
label_schema = ResponseSchema(name="label", 
    description="""Integer type is expected, do not put any comments beside it. 
                    This label must be strictly an integer label of 0 or 1""")
explanation_schema = ResponseSchema(name="explanation", description="This is the reasoning for why the sentence was classified as the label")
response_schemas = [sentence_schema, label_schema, explanation_schema]

'''getting structured output'''
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()
template_string = """
    Given this sentence: '{sentence}', classify if it is Singlish (0) or English (1), 
        the label you provide must be strictly an integer output of either 0 or 1 with no comments like '//' or '#' beside it,
        {format_instructions}"""
prompt = PromptTemplate(
    template=template_string,
    input_variables=["sentence"],
    partial_variables={"format_instructions": format_instructions},
)
# print(prompt.messages)
chain = LLMChain(llm=llm, 
                 prompt=prompt)

def get_output_dict(sentence):
   answer=chain.run(sentence)
   """ to resolve this error:
        langchain.schema.output_parser.OutputParserException: Got invalid JSON object.
        https://stackoverflow.com/questions/77396803/langchain-schema-output-parser-outputparserexception-got-invalid-json-object-e
   """
   if answer.find("\`\`\`\n\`\`\`") != -1:
     answer = answer.replace("\`\`\`\n\`\`\`", "\`\`\`")
     #print("Found and replaced")
   output_dict = output_parser.parse(answer)
   return output_dict

def get_output_label(sentence):
   return get_output_dict(sentence)['label']

############################################################################################################################## 
"""test case"""

# sentence1 = "I already have a host and blogger"
# sentence2 = "Meet after lunch la..."

# # print(get_output_dict(sentence1))
# x = get_output_label(sentence1)
# print(x)
# print(type(x))

