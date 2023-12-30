import sys
from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')

    # Check if the user wants to quit
    if user_message.lower() == 'quit':
        bot_response = "Goodbye! Conversation ended."
        sys.exit()
    else:
        # Call your chatbot function to get a response
        bot_response = get_response(user_message)

    # Return the response as JSON
    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)
