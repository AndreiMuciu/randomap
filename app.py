import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the main page, passing the author's name from the environment.
    """
    # Fetch the author name, providing a default if it's not set.
    author_name = os.environ.get("APP_AUTHOR", "Anonymous Developer")
        
    return render_template('index.html', author=author_name)

@app.route('/andrei')
def andrei():
    """
    Custom route for Andrei
    """
    return f"<h1>Hello, this is Andrei's page!</h1><p>Welcome to my custom route.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
