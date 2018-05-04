#script um server requests zu handlen


from waskochen import *

from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def main():
    return first()


if __name__=="__main__":
    app.run()