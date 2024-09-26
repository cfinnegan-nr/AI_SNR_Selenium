import requests
from openaienvvars import (AZURE_OPENAI_BASE_PATH, OPENAI_API_KEY, 
                           AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME, 
                           AZURE_OPENAI_API_VERSION)

def chatwithLLM(value):
    # Check if all required environment variables are loaded
    if None in [AZURE_OPENAI_BASE_PATH, OPENAI_API_KEY, AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME, AZURE_OPENAI_API_VERSION]:
        print("Error: Some environment variables are not set.")
        return

    # Construct the correct URL
    url = f"{AZURE_OPENAI_BASE_PATH}/{AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME}/chat/completions?api-version={AZURE_OPENAI_API_VERSION}"
    
    headers = {
        "Content-Type": "application/json",
        "api-key": OPENAI_API_KEY
    }

    # Build the prompt from the value passed and other string instructions
    initial_instruction = "Using Selenium 4.0 with Python write code for following scenario:"
    #initial_instruction = "Using Selenium 4.0 with Java write code for following scenario:"
    final_instruction = " using with dynamic wait at each step"

        
    prompt = f"{initial_instruction}\n{value}\n{final_instruction}"
    prompt1 = "Tell me a joke."
    
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1,
        "max_tokens": 1024
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.json()
        response_text = result['choices'][0]['message']['content'].strip()
        print("\n" + "Response returned from LLM is " + "\n")
        print(response_text + "\n")
        return response_text

    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("Error: Response format is unexpected.")
        print("Response content:", response.content)

    return None