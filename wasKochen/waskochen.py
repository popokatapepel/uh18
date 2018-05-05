#modul waskochen ist für die logik gedacht
import json
from dbinteraction import *

def first():
    return "janniklas"


def returnjsonmock():
    d={"gerichte": [{"name": "rührei", "url":"www.ruehrei.com", "bewertung": 1, "zutaten": [(5, "Eier"),(0.3, "Milch")]},
                   {"name": "müsli", "url":"www.muesli.com", "bewertung": 0.5, "zutaten": [(200, "Müsli"), (0.3, "Milch"), (1, "Banane")]},
                   {"name": "schnitzel","url":"www.schnitzel.com", "bewertung": 2, "zutaten": [(100, "Fleich"), (0.3, "Semmelbrösel"), (2, "Pommes")]}]}
    return d


def getgericht():
    return {"meals": getallmeals()}


def getingredients(username):
    return getingredientsforuser(username)


def getingredientsetforuser(user):
    l=getingredientsforuser(user)
    s=set()
    for ll in l:
        s.add((ll["id"],ll["name"]))
    return s

def getingsetsformeals():
    x=getallmeals()
    l=[]
    for xx in x:
        s=set()
        for i in xx["ingredients"]:
            s.add((i["id"],i["name"]))
        l.append((xx["id"],xx["name"],s))
    return l

def getsetpossiblemealsforuser(users):
    fridgeset=set()
    for u in users:
        fridgeset=fridgeset.union(getingredientsetforuser(u))
    meals=getingsetsformeals()
    s=set()
    for m in meals:
        if m[2].issubset(fridgeset):
            s.add((m[0],m[1]))
    return s

'''
gibt eine liste von dicts von möglichen gerichten für einen oder mehere user a
'''
def getpossiblemeals(users):
    s=getsetpossiblemealsforuser(users)
    ids=[ss[0] for ss in s]
    meals=getmeals(ids)
    return meals





