import configparser
import requests
from flask import Flask, request

config: configparser.ConfigParser = configparser.ConfigParser()
config.read("./config.ini")

POST_URL = config["constants"]["discord_webhook_url"]

app = Flask(__name__)


@app.route("/", methods=["post", "get"])
def requestHandler():
    if request.method == "POST":
        recieved_data = request.get_json()
        if recieved_data.get("ref") != None:
            request_body = {
                "content": "New commit added!\r"+ recieved_data["repository"]["html_url"] + "/commit/" + recieved_data["after"]
            }
            requests.post(POST_URL, json=request_body)
            return ("OK!", 200)
        if recieved_data.get("issue") != None and recieved_data.get("action") == "opened":
            request_body = {
                "content": "New issue opened!\r"+ recieved_data["issue"]["html_url"]
            }
            requests.post(POST_URL, json=request_body)
            return ("OK!", 200)
    else:
        return ("<p>Only POST requests accepted!</p>", 405)


app.run(host="0.0.0.0", port=config["constants"]["flask_port"])