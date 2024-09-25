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

# # Import the necessary libraries
# import openai
# from decouple import config
# import openpyxl




# def ReadTheInput():
    
#     wrkbk = openpyxl.load_workbook("TestSteps.xlsx")

#     sh = wrkbk.active

#     # iterate through excel and display data
#     mylist=[]
#     for i in range(1, sh.max_row + 1):
#         # print("\n")
#         # print("Row ", i, " data :")

#         for j in range(1, sh.max_column + 1):
#             cell_obj = sh.cell(row=i, column=j)
#             # print(cell_obj.value, end=" ")
#             mylist.append(cell_obj.value)
    
    
#     return mylist
    



# def chatwithme(value):

#     # Check if all required environment variables are loaded
#     if None in [AZURE_OPENAI_BASE_PATH, OPENAI_API_KEY, AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME, AZURE_OPENAI_API_VERSION]:
#         print("Error: Some environment variables are not set.")
#         return

#     # Construct the correct URL
#     url = f"{AZURE_OPENAI_BASE_PATH}/{AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME}/chat/completions?api-version={AZURE_OPENAI_API_VERSION}"
    
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": OPENAI_API_KEY
#     }
    
#     data = {
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": "Tell me a joke."}
#         ],
#         "max_tokens": 50
#     }
    
#     try:
#         response = requests.post(url, headers=headers, json=data)
#         response.raise_for_status()  # Raise an HTTPError for bad responses
#         result = response.json()
#         print("Response:", result['choices'][0]['message']['content'].strip())
#         print("\n" + "Response returned from LLM" + "\n")
    
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#     except KeyError:
#         print("Error: Response format is unexpected.")
#         print("Response content:", response.content)


# def createFile(data):
    
#     fp = open('TestCase.py', 'w')
#     fp.write(data)
#     fp.close()
    


def main():
    
    print("Testing...\n")
    
    try:
        input_value = ReadTheInput()
        print("Test Steps...\n")
        print(input_value)
        print("\nInput these test steps into LLM...\n")

        chatwithLLM("input_value")
        

        print("\n" + "createFile function called with LLM response" + "\n")
        print(createFile("chat_response"))

    except Exception as e:
        print(f"An error occurred in Main(): {e}")


if __name__ == "__main__":
    main()    