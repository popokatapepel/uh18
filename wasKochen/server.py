#script um server requests zu handlen


from waskochen import *

from flask import Flask, jsonify, request
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


@app.route("/possible_meals/<user>")
def getmeals(user):
    return jsonify(getpossiblemeals(user))


@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.getlist('user')
    return "hallo"


if __name__=="__main__":
    app.run(host='0.0.0.0')