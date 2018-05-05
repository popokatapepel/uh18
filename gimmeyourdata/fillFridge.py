from sqlalchemy import create_engine
from pathlib import Path
import json

eng = create_engine("sqlite:///../wasKochen/main.db")

for i in range(215,233):
    conn = eng.connect()
    #try:
    conn.execute("insert into t_usr_ingredient (id_ingridient,user,amount) VALUES ('"+str(i)+"','"+"maxim"+"','"+str(1)+"')")
    #except:
    #    pass

    conn.close()
    #break
#conn.close()

for i in [229,234,234,232,236,219]:
    conn = eng.connect()
    #try:
    conn.execute("insert into t_usr_ingredient (id_ingridient,user,amount) VALUES ('"+str(i)+"','"+"janniklas"+"','"+str(1)+"')")
    #except:
     #   pass

    conn.close()