from turtle import pos
from flask import Flask, jsonify, request
from logging import getLogger
from dotenv import load_dotenv
import os

from .tools import tools

load_dotenv(verbose=True)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

logger = getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/payback', methods=['POST'])
def return_payback():
    posted_json = request.get_json()
    is_correct_response = tools.check_json_type(posted_json)
    if is_correct_response:
        pay_back_json = tools.calk_payback(posted_json)
        return jsonify(pay_back_json), 200
    else:
        return jsonify({"error":"Contains indexes that cannot be processed."}), 400