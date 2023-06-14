from flask import Flask, render_template
import requests
import json
import os

app = Flask(__name__)

board_id = os.environ.get('BOARD_ID')
api_key = os.environ.get('API_KEY')
api_token = os.environ.get('API_TOKEN')

def get_trello_cards():
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    params = {
        'key': api_key,
        'token': api_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        cards = response.json()
        return cards
    else:
        raise Exception(f"Request returned an error: {response.status_code}")

@app.route('/')
def index():
    cards = get_trello_cards()
    return render_template('cards.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
