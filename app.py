from flask import Flask
import redis
import os

app = Flask(__name__)

# Pobieramy nazwę hosta Redisa ze zmiennych środowiskowych (Standard Kubernetes!)
redis_host = os.getenv("REDIS_HOST", "localhost")
cache = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    pod_id = os.getenv('HOSTNAME')
    return f"Gratulacje! Odwiedziny nr: {count}. Pod ID: {pod_id}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)