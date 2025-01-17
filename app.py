import os
from flask import Flask, render_template, request, jsonify
from chatbot.retriever import DocumentRetriever
from chatbot.generator import ResponseGenerator

# Set environment variable to avoid OpenMP issue
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

app = Flask(__name__)

# Initialize retriever and generator
retriever = DocumentRetriever()
generator = ResponseGenerator()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.form['query']

    # Retrieve documents related to the user's query using DuckDuckGo API
    documents = retriever.retrieve_documents(user_query)

    # Generate a response based on retrieved documents using GPT-2
    response = generator.generate_response(user_query, documents)

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
