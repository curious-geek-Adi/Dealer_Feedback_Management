from pymongo import MongoClient
#from bson.objectid import ObjecrtId

global con
global db
global coll

def connect_db():
    global con
    global db
    global coll
    con=MongoClient("mongodb+srv://Aditya:Aditya12345@cluster0.s8rga.mongodb.net/Feedbackdb?retryWrites=true&w=majority")
    db=con.Feedbackdb
    coll=db.feedbacklist

def contr_list():
    global coll
    connect_db()
    db=con.Feedbackdb
    coll=db.conractor
    cont_listall=coll.find({})
    return cont_listall

def save_feed(feed_info):
    global coll
    connect_db()
    coll.insert(feed_info)

def view_feed():
    global coll
    connect_db()
    feedinfo=coll.find({})
    return feedinfo

def fulldata(id):
    global coll
    connect_db()
    # db=con.Feedbackdb
    # coll=db.feedbacklist
    data=coll.find({"feedback_id":id})
    return data

def fsubmit(id,info):
    global coll
    connect_db()
    coll=db.feedbacklist
    myquery={"feedback_id":id}
    updatequery={ "$set": { "attention":info["attention"]} }
    updatequery1={ "$set": { "quicknote":info["quicknote"]} }
    # temp=info["attention"]
    # temp1=info["quicknote"]
    coll.update_one(myquery,updatequery)
    coll.update_one(myquery,updatequery1)


def deletecoll(fid):
    global coll
    connect_db()
    coll=db.feedbacklist
    coll.delete_many({"feedback_id":fid})

def updatelist(id,info):
    global coll
    connect_db()
    coll=db.feedbacklist
    myquery={"feedback_id":id}
    # origin=info["origin"]
    # status=info["status"]
    # contr_id=info["contr_id"]
    # opinion=info["opinion"]
    # feedback=info["feedback"]
    # time=info["time"]
    # attention=info["attention"]
    # quicknote=info["quicknote"]
    updatequery1={ "$set": { "origin":info["origin"]} }
    updatequery2={ "$set": { "status":info["status"]} }
    updatequery3={ "$set": { "contr_id":info["contr_id"]} }
    updatequery4={ "$set": { "opinion":info["opinion"]} }
    updatequery5={ "$set": { "feedback":info["feedback"]} }
    updatequery6={ "$set": { "time":info["time"]} }
    updatequery7={ "$set": { "attention":info["attention"]} }
    updatequery8={ "$set": { "quicknote":info["quicknote"]} }
    #coll.update_one({"feedback_id":id},{"$set":{"origin":origin,"status":status,"contr_id":contr_id,"opinion":opinion,"feedback":feedback,"time":time,"attention":attention,"quicknote":quicknote}})
    coll.update_one(myquery,updatequery1)
    coll.update_one(myquery,updatequery2)
    coll.update_one(myquery,updatequery3)
    coll.update_one(myquery,updatequery4)
    coll.update_one(myquery,updatequery5)
    coll.update_one(myquery,updatequery6)
    coll.update_one(myquery,updatequery7)
    coll.update_one(myquery,updatequery8)
