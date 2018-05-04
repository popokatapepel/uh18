#script um server requests zu handlen


from waskochen import *

from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def main():
    return returnjsonmock()

@app.route("/test")
def test():
    return getgericht()

@app.route("/geting/<user>")
def geting(user):
    return getingredients(user)


if __name__=="__main__":
    app.run(host='0.0.0.0')