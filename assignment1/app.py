import sys
import base64
import os
import yaml 
import json
from github import Github
from flask import Flask, redirect, url_for, request

g = Github()
url_temp = sys.argv[1];   # get temp url with github
repo = g.get_repo(url_temp.split("https://github.com/")[1])  # get correct repo

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/")
def hello_v1():
    return "Hello from Dockerized Flask App Version One!!"

@app.route("/v1/<name>")
def test(name):
    
    file, file_extension = os.path.splitext(name)    # get input path extension
    content = repo.get_file_contents(file+".yml").content
    #content = repo.get_file_contents("/dev-config.yml").content
    decode_str = base64.b64decode(content) 

    if file_extension == ".yml":    
        return decode_str
    elif file_extension == ".json":
        #str_json = json.dumps(yaml.load(decode_str), indent=2)
        str_json = json.dumps(yaml.load(decode_str), indent=2)
        return str_json

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
