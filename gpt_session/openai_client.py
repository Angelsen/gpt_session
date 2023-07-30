import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key

class OpenAIClient:
    def ask(self, question, last_command=None, last_output=None, conversation=None):
        if last_command and last_output:
            system_message = f"You are a helpful assistant with expertise in terminal commands. The user just ran the command `{last_command}` and received the following output: `{last_output}`. Please consider this when answering the following question."
        else:
            system_message = "You are a helpful assistant that provides guidance, examples, and explanations for terminal commands. The user has a question."
        
        if conversation:
            conversation.append({"role": "user", "content": question})
        else:
            conversation = [{"role": "system", "content": system_message}, {"role": "user", "content": question}]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        
        conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        
        return response['choices'][0]['message']['content']
