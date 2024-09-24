# Import OpenAI Environment Variables
from openaienvvars import OPENAI_API_KEY

# Import the necessary libraries
import openai
from decouple import config
import openpyxl




def ReadTheInput():
    return "ReadTheInput function called"


def chatwithme(value):

    # Set up OpenAI API credentials
    API_KEY = config('OPENAI_API_KEY')
    openai.api_key = API_KEY


    return "chatwithme function called with value: " + value


def createFile(data):
    return "createFile function called with data: " + data


def main():
    
    print("Testing...")
    
    try:
        input_value = ReadTheInput()
        print(input_value)

        chat_response = chatwithme("input_value")
        print(chat_response)

        print(createFile(chat_response))
    except Exception as e:
        print(f"An error occurred: {e}")

    