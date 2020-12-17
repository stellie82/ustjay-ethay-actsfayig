# Stella Kim
# Assignment 5: Ustjay ethay Actsfayig

import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get('http://unkno.com')

    soup = BeautifulSoup(response.content, 'html.parser')
    facts = soup.find_all('div', id='content')

    return facts[0].getText()


def translate(fact):
    url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    response = requests.post(url, data={'input_text': fact},
                             allow_redirects=False)

    return response.headers.get('location')


@app.route('/')
def home():
    fact = get_fact().strip()
    body = translate(fact)

    template = f"""
    <h1>Pig Latin Translator</h1>
    <p><b>Random Fact</b>: {fact}</p>
    <p><b>Translation</b>: <a href={body}>{body}</a></p>
    """
    # <a href='https://hidden-journey-62459.herokuapp.com/'>Link to Translator</a>

    return Response(response=template, mimetype='text/html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6787))
    app.run(host='0.0.0.0', port=port)
