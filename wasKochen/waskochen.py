#modul waskochen ist für die logik gedacht
import json
from dbinteraction import *

def first():
    return "janniklas"


def returnjsonmock():
    d={"gerichte": [{"name": "rührei", "url":"www.ruehrei.com", "bewertung": 1, "zutaten": [(5, "Eier"),(0.3, "Milch")]},
                   {"name": "müsli", "url":"www.muesli.com", "bewertung": 0.5, "zutaten": [(200, "Müsli"), (0.3, "Milch"), (1, "Banane")]},
                   {"name": "schnitzel","url":"www.schnitzel.com", "bewertung": 2, "zutaten": [(100, "Fleich"), (0.3, "Semmelbrösel"), (2, "Pommes")]}]}
    return json.dumps(d)


def getgericht():
    return json.dumps({"meals": getallmeals()})


def getingredients(username):
    return json.dumps(getingredientsforuser(username))




