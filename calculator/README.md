*** Basic Setup:
    
** Create a `.env` file with the following variable:
- GEMINI_API_KEY="your_api_key_here"

** How to generate a Goolge Gemini API Key:
1. Create an account on Google AI Studio if you don't already have one ( https://aistudio.google.com/ )
2. Click the "Create API Key" button. Here are the docs if you get lost: ( https://ai.google.dev/gemini-api/docs/api-key )
3. Copy the API key, then paste it into a new .env file in your project directory. The file should look like this:
   - GEMINI_API_KEY="your_api_key_here"
4. Add the .env file to your .gitignore