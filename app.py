from flask import Flask, render_template,jsonify
import pymongo
import json

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.police

police_db = db["police"]
contracts_db = db["contracts"]
equipment_db = db["equipment"]
city_db = db["city"]
state_db = db["state"]



@app.route("/", methods=['GET','POST'])
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    return render_template("index.html")

@app.route("/api/v1.0/contracts", methods=['GET','POST'])
def contracts():
    # write a statement that finds all the items in the db and sets it to a variable
    from bson.json_util import loads
    contracts = contracts_db.find()
    # print(loads("'"+str(contracts[0])+"'"))
    # print(jsondumps(contracts[0], indent=3))
    lst = []
    for x in contracts:
        dct = {}
        for y in x:
            if y != "_id":
                dct[y]=x[y]
        lst.append(dct)
    print(lst[0])

    return jsonify(lst)

    # render an index.html template and pass it the data you retrieved from the database
@app.route("/api/v1.0/police", methods=['GET','POST'])
def police():
    # write a statement that finds all the items in the db and sets it to a variable
    from bson.json_util import loads
    police_killings = police_db.find()
    # print(loads("'"+str(contracts[0])+"'"))
    # print(jsondumps(contracts[0], indent=3))
    police_lst = []
    for x in police_killings:
        dct = {}
        for y in x:
            if y != "_id":
                dct[y]=x[y]
        police_lst.append(dct)
    print(police_lst[0])

    return jsonify(police_lst)    

@app.route("/api/v1.0/equipment", methods=['GET','POST'])
def equipment():
    # write a statement that finds all the items in the db and sets it to a variable
    from bson.json_util import loads
    dod_equipment = equipment_db.find()
    # print(loads("'"+str(contracts[0])+"'"))
    # print(jsondumps(contracts[0], indent=3))
    equipment_lst = []
    for x in dod_equipment:
        dct = {}
        for y in x:
            if y != "_id":
                dct[y]=x[y]
        equipment_lst.append(dct)
    print(equipment_lst[0])

    return jsonify(equipment_lst)    

@app.route("/api/v1.0/city", methods=['GET','POST'])
def city():
    # write a statement that finds all the items in the db and sets it to a variable
    from bson.json_util import loads
    dod_city = city_db.find()
    # print(loads("'"+str(contracts[0])+"'"))
    # print(jsondumps(contracts[0], indent=3))
    city_lst = []
    for x in dod_city:
        dct = {}
        for y in x:
            if y != "_id":
                dct[y]=x[y]
        city_lst.append(dct)
    print(city_lst[0])

    return jsonify(city_lst)    

@app.route("/api/v1.0/state", methods=['GET','POST'])
def state():
    # write a statement that finds all the items in the db and sets it to a variable
    from bson.json_util import loads
    dod_state = state_db.find()
    # print(loads("'"+str(contracts[0])+"'"))
    # print(jsondumps(contracts[0], indent=3))
    state_lst = []
    for x in dod_state:
        dct = {}
        for y in x:
            if y != "_id":
                dct[y]=x[y]
        state_lst.append(dct)
    print(state_lst[0])

    return jsonify(state_lst)    


if __name__ == "__main__":
    app.run(debug=True)
