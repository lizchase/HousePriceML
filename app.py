from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask (__name__)
model = pickle.load(open(model.pkl, 'rb'))

@app.route('/')
def home():
    return 'hi there'

if __name__ == '__main__':
    app.run(debug=True)