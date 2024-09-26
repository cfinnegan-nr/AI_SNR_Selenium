import os

def parsePrompt(input_value):
    """
    Function to parse and build a prompt from the input value.
    Modify this function based on the specific requirements needed to 
    create a useful prompt from the input_value.
    """
        

    # Get the current working directory
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")

    # Read contents of the 'initial_instructions.txt' file
    try:
        # Construct the path to the file in the current working directory
        file_path1 = os.path.join(current_directory, 'initial_instructions.txt')
        print(f"Attempting to open file at: {file_path1}")
        
        with open(file_path1, 'r') as file:
            prompt_initial_instructions = file.read()
        print("Initial Instructionns File read successfully.")
    except FileNotFoundError:
        # Handle the case where the file is not found
        prompt_initial_instructions = "No Initial instructions. \n"
        print("Initial Instructionns File not found.")


    # Read contents of the 'final_instructions.txt' file
    try:
        # Construct the path to the file in the current working directory
        file_path2 = os.path.join(current_directory, 'final_instructions.txt')
        print(f"Attempting to open file at: {file_path2}")
        
        with open(file_path2, 'r') as file:
            prompt_final_instructions = file.read()
        print("Final Instructionns File read successfully.")
    except FileNotFoundError:
        # Handle the case where the file is not found
        prompt_final_instructions = "No Final instructions. \n"
        print("Final Instructionns File not found.")    


    prompt_instructions = f"{prompt_initial_instructions}\n{input_value}\n{prompt_final_instructions}"
    print("\nFile read prompt..\n")
    print(prompt_instructions)
    print("\n\n")
    
    # Example: Simply concatenate instructions if input_value is a list of steps
    # prompt_instructions = prompt_initial_instructions + "\n"
    # prompt_instructions += "\n".join(input_value)
    # prompt_instructions += "\n" + prompt_final_instructions

    return prompt_instructions
