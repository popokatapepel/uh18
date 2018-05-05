import api

a = api.ChefkochApi()

s = a.search_recipe("zigeuner")

for r in s["results"]:
    id = r["recipe"]["id"]
    s = a.get_recipe(id)
    file = open("data/"+id+".txt", "w+")
    file.write(str(s))
    file.close()