from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    pod_name = os.getenv('HOSTNAME', 'Lokalny-Laptop')
    return f"Gratulacje! Aplikacja dziala w kontenerze. Pod ID: {pod_name}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)