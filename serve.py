from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load pre-trained model and tokenizer from Hugging Face
model_name = "nrml34/skybound-mysteries"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prompt = data.get('prompt', '')
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=50)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
