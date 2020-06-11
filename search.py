from flask import Flask, jsonify, Response

app = Flask(__name__)


@app.route('/search', methods=["POST"])
def search():
    return jsonify({"hello": "world"})


if __name__ == '__main__':
    app.run(debug=True)
