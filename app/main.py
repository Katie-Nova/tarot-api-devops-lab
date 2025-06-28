from flask import Flask, jsonify
import random

app = Flask(__name__)

tarot_deck = [
    {"card": "The Fool", "meaning": "New beginnings, spontaneity"},
    {"card": "The Magician", "meaning": "Manifestation, personal power"},
    {"card": "The High Priestess", "meaning": "Intuition, divine knowledge"},
    {"card": "The Empress", "meaning": "Creativity, abundance"},
    {"card": "The Tower", "meaning": "Sudden change, awakening"},
    {"card": "The Devil", "meaning": "Temptation, shadow self"},
    {"card": "The Star", "meaning": "Hope, divine clarity"},
    {"card": "Death", "meaning": "Transformation, cycles closing"},
    {"card": "The Moon", "meaning": "Illusion, hidden truth"},
    {"card": "The Sun", "meaning": "Vitality, joy"}
]

@app.route('/pull')
def pull_card():
    card = random.choice(tarot_deck)
    return jsonify(card)

if __name__ == '__main__':
    app.run(debug=True)
