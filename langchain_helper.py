from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains import SequentialChain

# Calling api key from .env
load_dotenv()
apikey = os.getenv  ('OPENAI_API_KEY')
llm = OpenAI(temperature=0.7)


def generate_restuarant_name_and_items(cuisine):

    name_prompt_template = PromptTemplate(
    input_variables= ['cuisine'],
    template = "I want to open a restuarant for {cuisine} food. Suggest a fency name for this."
    )

    name_chain = LLMChain(llm=llm,prompt=name_prompt_template,output_key="restuarant_name")

    menu_item_template = PromptTemplate(
    input_variables=['restuarant_name'],
    template = "Suggest some menu items for {restuarant_name}. Return it as a comma seperated list."
    )

    menu_chain = LLMChain(llm=llm,prompt=menu_item_template, output_key="menu_items")

    final_chain = SequentialChain(
    chains=[name_chain,menu_chain],
    input_variables=["cuisine"],
    output_variables = ["restuarant_name","menu_items"]
    )

    response = final_chain({'cuisine':cuisine})
    print(response)

    return response

if __name__=="__main__":
    result = generate_restuarant_name_and_items("Indian")
    print(result)
