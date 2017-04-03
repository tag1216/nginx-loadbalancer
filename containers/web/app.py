import os
import time

from flask import Flask

app = Flask(__name__)

wait = float(os.environ.get("WAIT", "0"))
response_text = os.environ["RESPONSE_TEXT"]


@app.route("/", methods=["GET"])
def index():
    time.sleep(wait)
    return response_text


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, processes=1)
