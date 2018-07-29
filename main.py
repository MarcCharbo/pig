import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    pig_latin_form_data = get_fact()
    pig_latin_form_data = pig_latin_form_data.strip()
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    body = {'input_text': pig_latin_form_data}
    response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", headers = headers, data=body)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    print(soup.prettify())
    body = soup.find_all("body")

    return str(body[0])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

