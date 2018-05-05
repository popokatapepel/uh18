#script um server requests zu handlen


from waskochen import *

from flask import Flask, jsonify
app=Flask(__name__)

@app.route("/")
def main():
    return jsonify(returnjsonmock())

@app.route("/test")
def test():
    return jsonify(getgericht())

@app.route("/geting/<user>")
def geting(user):
    return jsonify(getingredients(user))


if __name__=="__main__":
    app.run(host='0.0.0.0')