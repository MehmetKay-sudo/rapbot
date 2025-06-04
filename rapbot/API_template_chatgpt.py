import openai

# Set your OpenAI API Key here
openai.api_key = "YOUR_API_KEY_HERE"

def get_chatgpt_response(prompt):
    """
    Sends a prompt to the ChatGPT API (using model gpt-3.5-turbo) and returns the result.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative rap battle assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
