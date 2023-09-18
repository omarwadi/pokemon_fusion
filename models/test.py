import os
import requests
import openai
from langchain.prompts import PromptTemplate

openai.api_key = "99f9798553104ac48834669eab284e5a"
openai.api_base = "https://pokemonopenai.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future
deployment_name='pokemon_gpt_new' # This will correspond to the custom name you chose for your deployment when you deployed a model.

def get_completion(prompt, model="gpt-3.5-turbo-0301", engine=deployment_name):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7,
        engine=engine
    )
    return response.choices[0].message["content"]
