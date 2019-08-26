from flask import Flask
from redis import Redis

app = Flask(__name__)

redis = Redis(host="redis")

@app.route("/")
def index():
    cnt = redis.incr("cnt")
    return f"PV is {cnt}"