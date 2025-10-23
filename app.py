from flask import Flask, request, render_template
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the Flask app
app = Flask(__name__)

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to analyze sentiment
@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['text']
    sentiment = sia.polarity_scores(user_input)

    # Determine sentiment
    if sentiment['compound'] >= 0.05:
        result = 'Positive'
    elif sentiment['compound'] <= -0.05:
        result = 'Negative'
    else:
        result = 'Neutral'

    return render_template('index.html', sentiment=result, user_input=user_input)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
