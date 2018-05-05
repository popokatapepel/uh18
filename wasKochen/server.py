#script um server requests zu handlen


from waskochen import *

from flask import Flask, jsonify, request
import requests
import urllib, json

app=Flask(__name__)

@app.route("/api")
def main():
    return jsonify(returnjsonmock())

@app.route("/api/test")
def test():
    return jsonify(getgericht())

@app.route("/api/geting/<user>")
def geting(user):
    return jsonify(getingredients(user))


@app.route("/api/possible_meals")
def getmeals():
    users=request.args.getlist('user')
    return jsonify(getpossiblemeals(users))


@app.route('/api/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.getlist('user')
    return "hallo"


@app.route("/")
def xxx():
    str_url=request.base_url+"api/possible_meals?user=janniklas"
    #return "<a href="+str_url+">xxx</a>"
    print(str_url)
    l=requests.get(str_url).json()

    print(ll)
    with urllib.request.urlopen(str_url) as url:
        json_str=url.read().decode()
        data = json.loads(url.read().decode())
    print(str(data))
    return str(data)


@app.route("/<user>")
def showing(user):
    out="<h1>hallo {0}</h1><br>".format(user)
    out+="<p> Das ist in deinem Kühlschrank</p>"
    str_url = "http://localhost:5000/api/geting/" + user
    l = requests.get(str_url).json()
    out+="<ul>"
    for ll in l:
        out+="<li>"+ll["name"]+"</li>"
    out+="</ul>"
    out+="<br><br>"
    out+="<p><a href=http://localhost:5000/possible_meals?user={1}>{0}</a>".format("Was kann ich damit kochen?", user)
    out+="<p><a href=http://localhost:5000/possible_meals?user=janniklas&user=maxim>{0}</a>".format("Was kann ich mit meinem Bruder damit kochen?")

    return out

@app.route("/possible_meals")
def showing_pos_meals():
    users = request.args.getlist('user')
    out=""
    lnk=""
    for user in users:
        out+="<h1>hallo {0}</h1><br>".format(user)
        lnk+="user="+user+"&"
    lnk=lnk[:-1]

    out+="<p> Das kannst du/ihr damit kochen</p>"
    str_url = "http://localhost:5000/api/possible_meals?" + lnk
    l = requests.get(str_url).json()
    out+="<ul>"
    for ll in l:
        out+="<li>"+ll["name"]+"</li>"
    out+="</ul>"
    out+="<br><br>"
    return out





if __name__=="__main__":
    app.run(host='0.0.0.0')