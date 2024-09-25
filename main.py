# Import OpenAI Environment Variables
import requests
from openaienvvars import (AZURE_OPENAI_BASE_PATH, OPENAI_API_KEY, 
                       AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME, 
                       AZURE_OPENAI_API_INSTANCE_NAME, 
                       AZURE_OPENAI_API_VERSION)

# Import the necessary libraries
from modules.read_input_TC import ReadTheInput
from modules.chat import chatwithLLM
from modules.create_testauto_file import createFile



def main():
    
    print("Testing...\n")
    
    try:
        input_value = ReadTheInput()
        print("Test Steps...\n")
        print(input_value)
        print("\nInput these test steps into LLM...\n")

        resp = chatwithLLM(str(input_value))
        

        print("\n" + "createFile function called with LLM response" + "\n")
        createFile(resp)

    except Exception as e:
        print(f"An error occurred in Main(): {e}")


if __name__ == "__main__":
    main()    