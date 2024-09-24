# Import OpenAI Environment Variables
from openaienvvars import OPENAI_API_KEY

# Import the necessary libraries
import openai
from decouple import config
import openpyxl

# Set up OpenAI API credentials
openai.api_key = config('OPENAI_API_KEY')

