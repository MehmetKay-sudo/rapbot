import requests

def query_gpt4all(prompt: str) -> str:
    url = "http://localhost:5000/api/generate"  # replace with actual GPT4All endpoint
    response = requests.post(url, json={"prompt": prompt})
    if response.status_code == 200:
        return response.json().get("generated_text", "")
    else:
        return f"Error: {response.status_code}"

# Example usage:
if __name__ == "__main__":
    prompt = "Write an aggressive rap verse about winning."
    result = query_gpt4all(prompt)
    print("GPT4All says:", result)
