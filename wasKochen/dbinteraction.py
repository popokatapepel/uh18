from sqlalchemy import create_engine
import copy


'''
returns all mealt als a list of dictionaries that are in the database
'''
def getallmeals():
    return getmeals()

'''
returns all meals mit id in liste als a list of dictionaries that are in the database
'''
def getmeals(id=None):
    if id==[]:
        return []
    eng = create_engine("sqlite:///main.db")
    conn = eng.connect()
    sqlcmd="select * from t_meal_dat tmd"
    if not id==None:
        sqlcmd+=" where "
        for i in id:
            sqlcmd+="tmd.id={0} or ".format(str(i))

        sqlcmd=sqlcmd[:-4]
    print(sqlcmd)
    meals = conn.execute(sqlcmd)


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


'''
returns a list of dictionaries which are in the users fridge
'''
def getingredientsforuser(username):
    eng = create_engine("sqlite:///main.db")
    conn = eng.connect()
    ing = conn.execute("select * from t_usr_ingredient tui, t_ingredients_dat tid where user='{0}' and tui.id_ingridient=tid.id".format(username))
    l=[]
    for i in ing:
        ing_dict={}
        for (k,v,) in i.items():
            ing_dict[k]=v
        l.append(copy.deepcopy(ing_dict))
    conn.close()
    return l


def getingredientsetforuser(user):
    eng = create_engine("sqlite:///main.db")
    conn = eng.connect()
    ing = conn.execute(
        "select * from t_usr_ingredient tui, t_ingredients_dat tid where user='{0}' and tui.id_ingridient=tid.id".format(
            username))
    l = []
    for i in ing:
        ing_dict = {}
        for (k, v,) in i.items():
            ing_dict[k] = v
        l.append(copy.deepcopy(ing_dict))
    conn.close()
    return l