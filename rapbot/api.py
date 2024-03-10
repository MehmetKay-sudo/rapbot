import requests

# code for binding API keys to the language model f.e. Chatgpt 
# aim is to connect bot to an LLM 
# this is an example / pseudocode here 
#BASE_URL = "https://api.languagemodel.com" 


def generate_text(prompt, temperature=0.7, max_tokens=100):
    #url = f"{BASE_URL}"/generate"
    params = { 
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    } 
    response = requests.post(url, json=params)
    response.raise_for_status()
    return response.json()["text"]

prompt = "Write a poem about a cat"
generated_text = generate_text(prompt)
print(generated_text)