from flask import Flask
from redis import Redis

app = Flask(__name__)

redis = Redis(host="redis")

@app.route("/")
def index():
    cnt = redis.incr("cnt")
    return "PV is %d"%cnt

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)