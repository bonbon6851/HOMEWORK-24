import os

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from models import RequestSchema
from builder import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():

    data_request = request.json

    try:
        RequestSchema().load(data_request)
    except ValidationError as error:
        return jsonify(error.messages), 400

    file_name = data_request.get("file_name")
    path = os.path.join(DATA_DIR, file_name)

    first_result = build_query(
        cmd=data_request["cmd1"],
        value=data_request["value1"],
        file_name=path,
        data=None
    )

    second_result = build_query(
        cmd=data_request["cmd2"],
        value=data_request["value2"],
        file_name=path,
        data=first_result
    )

    return jsonify(second_result)


if __name__ == "__main__":
    app.run()
