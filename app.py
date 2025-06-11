# app.py
from flask import Flask, render_template, request, jsonify
from Producer import send_click_event
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def handle_click():
    event_data = {
        'timestamp': datetime.datetime.now().isoformat(),
        'event': 'button_clicked'
    }
    send_click_event(event_data)
    return jsonify({"status": "sent"}), 200

if __name__ == '__main__':
    app.run(debug=True)
