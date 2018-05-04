#script um server requests zu handlen


from waskochen import *

from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def main():
    return returnjsonmock()


if __name__=="__main__":
    app.run(host='0.0.0.0')