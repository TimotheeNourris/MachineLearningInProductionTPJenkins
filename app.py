
"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import os

import ast
#import numpy as np
#import pandas as pd
#import tensorflow as tf
#from tensorflow import keras

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify

##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

##########################################################################
## Routes
##########################################################################
@app.route("/classify/<path:array>", methods=['GET', 'POST'])
def classify(array):
    
    image = ast.literal_eval(array)

    # preprocess the image
    image = np.array(image, dtype=np.float32)
    image = image.reshape(1, 28, 28, 1)
    image = image.astype("float32")
    image /= 255

    # make the prediction
    prediction = model.predict(image)
    label = int(np.argmax(prediction))
    return jsonify({"prediction": label, 'label': class_labels[label]})


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/hello")
def hello():
    """
    Return a hello message
    """
    return jsonify({"hello": "world"})

@app.route("/api/hello/<name>")
def hello_name(name):
    """
    Return a hello message with name
    """
    return jsonify({"hello": name})

@app.route("/api/whoami")
def whoami():
    """
    Return a JSON object with the name, ip, and user agent
    """
    return jsonify(
        name=request.remote_addr,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )

@app.route("/api/whoami/<name>")
def whoami_name(name):
    """
    Return a JSON object with the name, ip, and user agent
    """
    return jsonify(
        name=name,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )

##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()
