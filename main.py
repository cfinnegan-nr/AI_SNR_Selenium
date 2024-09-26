# Import OpenAI Environment Variables
import requests
from openaienvvars import (AZURE_OPENAI_BASE_PATH, OPENAI_API_KEY, 
                       AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME, 
                       AZURE_OPENAI_API_INSTANCE_NAME, 
                       AZURE_OPENAI_API_VERSION)

# Import the necessary libraries
from modules.read_input_TC import ReadTheXLTCInput
from modules.parse_LLMPrompt import parsePrompt
from modules.chat import chatwithLLM
from modules.create_testauto_file import createFile



def main():
    # Main function to run the testing workflow
    print("Testing...\n")
    
    try:
        # Read input for XLTC (assuming it's a custom format or testing protocol)
        input_value = ReadTheXLTCInput()
        print("Test Steps...\n")
        print(input_value)
        print("\n")

        # Build prompt for submission to LLM
        prompt = ""
        prompt = parsePrompt(input_value)


        # Interact with a Language Learning Model (LLM) using the input steps
        resp = chatwithLLM(str(prompt))
        
        print("\n" + "createFile function called with LLM response" + "\n")

        # Create a file using the response from the LLM
        createFile(resp)

    except Exception as e:
        # Catch and print any exceptions that occur during the process
        print(f"An error occurred in Main(): {e}")



if __name__ == "__main__":
    main()    