from flask import Flask, request, jsonify
import gpt4all

app = Flask(__name__)

# Initialize the GPT4All model (replace with your actual model path)
model = gpt4all.GPT4All("path/to/your/model.bin")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Generate a response; adjust parameters according to the GPT4All API
    response = model.generate(prompt)
    return jsonify({"generated_text": response})

if __name__ == "__main__":
    app.run(port=5000)
