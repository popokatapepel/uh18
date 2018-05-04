from sqlalchemy import create_engine
import copy

def getallmeals():
    eng = create_engine("sqlite:///main.db")
    conn = eng.connect()
    meals = conn.execute("select * from t_meal_dat tmd")
    l=[]
    for m in meals:
        d = {}
        for (k,v) in m.items():
            d[k]=v
        d["ingredients"]=[]
        ing=conn.execute("select * from t_meal_ingredient tmi, t_ingredients_dat tid "+
                         "where tmi.id_ingredient=tid.id and " +
                         "tmi.id_meal=" + str(d["id"]))
        ing_dict={}
        for i in ing:
            for (k,v) in i.items():
                ing_dict[k]=v
            d["ingredients"].append(copy.deepcopy(ing_dict))

        l.append(copy.deepcopy(d))
    conn.close()
    return l