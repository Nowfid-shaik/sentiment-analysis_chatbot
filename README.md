Sentiment Analysis Chatbot

A simple Flask-based web app that performs real-time sentiment analysis using NLTK’s VADER Sentiment Analyzer.
It classifies text as Positive, Negative, or Neutral.

Features
Real-time text analysis
Web interface with Flask
Uses NLTK’s pre-trained sentiment model

Installation and SetUp
1.clone the repository
git clone https://github.com/<your-username>/sentiment-analysis-chatbot.git
cd sentiment-analysis-chatbot
2.Create and activate a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate    # For macOS/Linux
venv\Scripts\activate       # For Windows

3.Install the dependencies
pip install flask nltk

4.Download NLTK data (only once)
python
>>> import nltk
>>> nltk.download('vader_lexicon')
>>> exit()

5.Run the Flask app
python app.py

6.Open in browser
Visit http://127.0.0.1:5000

Project Structure
sentiment-analysis-chatbot/
│
├── app.py
├── templates/
│   └── index.html
├── static/              # (optional: add CSS here)
├── requirements.txt      # (optional: to list dependencies)
└── README.md

Example Output

| Input Text            | Sentiment |
| --------------------- | --------- |
| “I love this app!”    | Positive  |
| “This is terrible.”   | Negative  |
| “It’s okay, not bad.” | Neutral   |


Future Enhancements
Integrate with an actual chatbot interface (e.g., ChatGPT API or custom NLP model)
Add a stylish front-end with Bootstrap or React
Display sentiment scores (compound, pos, neg, neu)

License
This project is open source and available under the MIT License



Tech Stack
Python, Flask, NLTK, HTML/CSS
