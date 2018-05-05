from sqlalchemy import create_engine
from pathlib import Path
import json

eng = create_engine("sqlite:///../wasKochen/main.db")


#conn.execute("insert into t_meal_dat (name,url,rating,chefkochId) VALUES ('1','2',3.0,4)")
#conn.close()
p = Path("data")
for f in p.iterdir():
    conn = eng.connect()
    try:
        #print(f)
        json_data = open(str(f)).read().strip("'<>() ").replace("False", "\"False\"").replace("True", "\"True\"").replace("None", "\"None\"").replace("\'","\"")
        #print(json_data)
        j = json.loads(json_data)
        print(j.keys())
        mealRes = conn.execute("insert into t_meal_dat (name,url,rating,chefkochId) VALUES('"+j["title"]+"','"+j["siteUrl"]+"','"+str(j["rating"]["rating"])+"','"+j["id"]+"')")
        mealId = mealRes.lastrowid
        print(len(str(j["ingredientGroups"][0]["ingredients"])))
        for i in j["ingredientGroups"][0]["ingredients"]:
            print (i["name"])
            ingRes = conn.execute("select id from t_ingredients_dat where name='"+i["name"]+"'").fetchone()
            ingId = None
            if ingRes == None:
                ingRes = conn.execute("insert into t_ingredients_dat (name) VALUES ('"+i["name"]+"')")
                ingId = ingRes.lastrowid
            else:
                ingId = ingRes[0]
            conn.execute("insert into t_meal_ingredient (id_meal,id_ingredient,amount) VALUES ('"+str(mealId)+"','"+str(ingId)+"','"+str(1)+"')")
        #print(j["id"] + " " + j["title"] + " " + str(j["rating"]["rating"]) + j["siteUrl"])
        #print(str(conn.lastrowid))
    except:
        pass

    conn.close()
    #break
#conn.close()