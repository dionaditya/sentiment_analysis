from flask import Flask, request, jsonify
import pickle
import torch

app = Flask(__name__)

# Save the tokenizer and model using pickle
with open('models/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)
    
with open('models/best_model.pkl', 'rb') as f:
    model = pickle.load(f)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Function to predict the rating of a new text input
def predict_rating(text):
    encoding = tokenizer.encode_plus(text, padding=True, truncation=True, max_length=128, return_tensors='pt')
    input_ids = encoding['input_ids']
    attention_mask = encoding['attention_mask']

    with torch.no_grad():
        outputs = model(input_ids=input_ids.to(device), attention_mask=attention_mask.to(device))
        logits = outputs.logits
        predicted_rating = torch.argmax(logits, dim=1)

    return predicted_rating.item()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text')
    
    if text:
        # Perform prediction
        predicted_rating = predict_rating(text)
        
        if predicted_rating ==4:
            sentiment = "Really positive review"
        if predicted_rating ==3:
            sentiment = "Positive review"
        if predicted_rating ==2:
            sentiment = "Neutral review"
        if predicted_rating ==1:
            sentiment = "Bad review"
        if predicted_rating ==0:
            sentiment = "Really Bad review"
        return jsonify({'sentiment': sentiment})
    else:
        return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)