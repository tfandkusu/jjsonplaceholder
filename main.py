from flask import Flask
from flask import jsonify
from flask import abort
from card import Card
import maker
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# 名刺一覧を作る
cards = maker.make()

@app.route('/')
def root():
    return "JJSONPlaceholder"

@app.route('/cards')
def list_cards():
    "名刺一覧を返却"
    ja = []
    for card in cards:
        ja.append(card.__dict__)
    return jsonify(ja)

@app.route('/cards/<int:id>')
def show_card(id):
    "名刺1枚を返却"
    if 1 <= id and id <= len(cards):
        card = cards[id - 1]
        return jsonify(card.__dict__)
    else:
        abort(404)

if __name__ == '__main__':
    # ローカルテスト環境
    app.run(host='127.0.0.1', port=8080, debug=True)
