from flask import Flask,render_template,request,redirect,url_for
import uuid
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient
import hello_db
import one
#mongodb+srv://Aditya:Aditya12345@cluster0.s8rga.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
app=Flask(__name__)
# cluster=MongoClient("mongodb+srv://Aditya:Aditya12345@cluster0.s8rga.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db=cluster["Feedbackdb"]
# collection=db["feedbacklist"]
@app.route('/')
def home_view():
    cont=hello_db.contr_list()
    cont_list=[]
    for x in cont:
        cont_list.append(x)
    print(cont_list)
    return render_template('feedbckform.html',cont_list=cont_list)

@app.route('/listview',methods=['POST','GET'])
def listview():
    if request.method=='POST':
        info={}
        cont=hello_db.contr_list()
        cont_list=[]
        for x in cont:
            cont_list.append(x)
        print(cont_list)
        code=one.uniquecode()
        fid=code[0:10]
        info["feedback_id"]=fid#=uuid.uuid4().hex
        #info["contr_id"]=uuid.uuid4().hex
        info["origin"]=request.form["origin"]
        info["status"]=request.form["status"]
        info["contr_id"]=request.form["clist"]
        info["opinion"]=request.form["opinion"]
        info["feedback"]=request.form["feedback"]
        info["time"]=request.form["time"]
        info["attention"]=""
        info["quicknote"]=""
        hello_db.save_feed(info)
        allfeed=hello_db.view_feed()
        # collection.insert_one({"feedback_id":feedback_id,"contr_id":contr_id,"origin":origin,"status":status,
        # "Contractor":clist,"opinion":opinion,
        # "time":time,"feedback":feedback})
        # list=[feedback_id,contr_id,status,opinion]
        listfeed=[]
        for x in allfeed:
            listfeed.append(x)
        return render_template('feedbacklist.html',listfeed=listfeed)
    elif request.method=='GET':
        allfeed=hello_db.view_feed()
        listfeed=[]
        for x in allfeed:
            listfeed.append(x)
        return render_template('feedbacklist.html',listfeed=listfeed)

@app.route('/details/<fid>/',methods=['POST'])
def details_feed(fid):

    # if request.method == 'POST':
        #id=request.args[id]
    print("it is fid",fid)
    data=hello_db.fulldata(fid)
    print(data)
    fid=fid
    list1=[]
    for detail in data:
        list1.append(detail)

    return render_template("fulldetails.html",list1=list1,fid=fid)


@app.route('/final_submit/<fid>/',methods=['POST'])
def final_submit(fid):
    print("my fid---->",fid)
    info={}
    info["attention"]=request.form["attention"]
    info["quicknote"]=request.form["quicknote"]
    print("this is my info")
    hello_db.fsubmit(fid,info)
    return redirect('/listview')

@app.route('/delete/<fid>/',methods=['POST'])
def delete(fid):
    print("for delete purpose fid id->>",fid)
    hello_db.deletecoll(fid)
    return redirect(url_for('listview'))


@app.route('/editupdate/<fid>/',methods=["POST"])
def editupdate(fid):
    if request.method=="POST":
        info={}
        # info["feedback_id"]=fid
        #info["contr_id"]=uuid.uuid4().hex
        info["origin"]=request.form["origin"]
        info["status"]=request.form["status"]
        info["contr_id"]=request.form["clist"]
        info["opinion"]=request.form["opinion"]
        info["feedback"]=request.form["feedback"]
        info["time"]=request.form["time"]
        info["attention"]=request.form["attention"]
        info["quicknote"]=request.form["quicknote"]
        hello_db.updatelist(fid,info)
    return redirect('/listview')
    # elif request.method=="GET":
    #     cont_list=hello_db.contr_list()
    #     data=hello_db.fulldata(fid)
    #     return render_template("updateform.html",cont_list=cont_list,data=data)

@app.route('/edit/<fid>/',methods=["POST"])
def edit(fid):
    if request.method=="POST":
        cont=hello_db.contr_list()
        datasow=hello_db.fulldata(fid)
        cont_list=[]
        for xe in cont:
            cont_list.append(xe)
        data=[]
        for x in datasow:
            data.append(x)
        print(cont_list)
        print( "thias is access___<><><>",datasow)
        return render_template("updateform.html",cont_list=cont_list,data=data)









@app.errorhandler(500)
def internalserver_error(e):
    return render_template("500.html"),500

@app.errorhandler(404)
def internalserver_error(e):
    return render_template("404.html"),404
