from flask import Flask, redirect, render_template, flash, url_for
from flask import request, session
from flask_session import Session
import mysql.connector as mysql
from sql_connection import get_sql_connection

app1 = Flask(__name__)
app1.secret_key = "super secret key"

@app1.route('/',methods=['GET'])
def MyhomeRoot():
    return render_template('login.html')

@app1.route("/My_Login_Process", methods=['POST'])
def My_Login_Process():
    uid = request.form["username"]
    pwd = request.form["password"]
    print(uid)
    print(pwd)
    try:
        db_connect = mysql.connect(
            host="localhost", database="warehousedb", user="root", passwd="Enfield@2021",auth_plugin='mysql_native_password', use_pure=True)
        sql = "Select Username, password From login where Username = " + "'" + uid + "'"
        print(sql)
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        cno = mycursor.fetchall()
        res = [tuple(str(item) for item in t) for t in cno]
        #print(res)
    except Exception as err:
        print(err)
        return render_template('MyError.html')
    if len(res) == 0:
        status = 0
        return render_template('MyError.html')
    else:
        usrid  = res[0][0]
        passwd = res[0][1]
        if (usrid == uid and pwd == passwd):
            return render_template('home.html', usrid=usrid)
        else:
            """status = 0"""
            return render_template('MyError.html')
            

@app1.route("/ViewProducts")            
def ViewProducts():
    try:
        db_connect = mysql.connect(
            host="localhost", database="warehousedb", user="root", passwd="Enfield@2021", auth_plugin='mysql_native_password',use_pure=True)
        sql = "Select PID,productName,CID,SID,brandname,quantity from products"
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        cdata = mycursor.fetchall()
        return render_template("viewproducts.html", cdata=cdata)
    except Exception as err:
        print(err)
        return render_template('MyError.html')
        
@app1.route("/AddProducts", methods=['POST'])
def AddProducts():
    PID  = request.form["PID"]
    ProductName  = request.form["ProductName"]
    CID = request.form["CID"]
    SID = request.form["SID"]
    Quantity=request.form["Quantity"]
    BrandName=request.form["BrandName"]
    # print(PID)
    # print(ProductName)
    # print(CID)
    # print(SID)
    # print(Quantity)
    # print(BrandName)
   

    try:
        db_connect = mysql.connect(
            host="localhost", database="warehousedb", user="root", passwd="Enfield@2021", auth_plugin='mysql_native_password',use_pure=True)
        sql = "INSERT INTO products(PID,productname,brandname,quantity,CID,SID) VALUES (" + "'" + PID + "'" + "," + "'" + ProductName +"'" + "," + "'" + BrandName + "'" + "," + "'" +Quantity + "'" + "," + "'" + CID + "'" + "," + "'" + SID+ "'" + ")" 
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        db_connect.commit()
        return render_template("addproducts.html")
    except Exception as err:
        print(err)
        return render_template('MyError.html')

@app1.route("/Deleteproducts", methods=['POST'])
def Deleteproducts():
    product_id = request.form["product_id"]
    try:
        print(product_id)
        db_connect = mysql.connect(
            host="localhost", database="warehousedb", user="root", passwd="Enfield@2021",auth_plugin='mysql_native_password', use_pure=True)
        sql_std = "DELETE FROM products WHERE PID = " + "'" + product_id + "'"
        print(sql_std)
        mycursor = db_connect.cursor()
        mycursor.execute(sql_std)
        db_connect.commit()
        return render_template('Deleteproduct.html')
    except Exception as err:
        print(err)
        return render_template('MyError.html')

@app1.route("/ViewCategories")            
def ViewCategories():
    try:
        db_connect = mysql.connect(
            host="localhost", database="warehousedb", user="root", passwd="Enfield@2021", auth_plugin='mysql_native_password',use_pure=True)
        sql = "Select CID,categoryname From category"
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        cdata = mycursor.fetchall()
        return render_template("viewcat.html", cdata=cdata)
    except Exception as err:
        print(err)
        return render_template('MyError.html')

@app1.route("/ViewSubCategories")            
def ViewSubCategories():
    try:
        db_connect = mysql.connect(
            host="localhost", database="warehousedb", user="root", passwd="Enfield@2021", auth_plugin='mysql_native_password',use_pure=True)
        sql = "Select SID,subcategoryname From subcategory"
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        cdata = mycursor.fetchall()
        return render_template("viewsubcat.html", cdata=cdata)
    except Exception as err:
        print(err)
        return render_template('MyError.html')











@app1.route('/')
def error():
    return render_template("login.html")




@app1.route("/MyHome")
def MyHome():
    return render_template("home.html")

@app1.route("/addProducts")
def addProducts():
    return render_template("addproducts.html")


@app1.route("/deleteproduct")
def deleteproduct():
    return render_template("Deleteproduct.html")

@app1.route("/getproduct")
def getproduct():
    return render_template("viewproducts.html")

@app1.route("/getcategory")
def getcategory():
    return render_template("viewcat.html")

@app1.route("/getsubcategory")
def getsubcategory():
    return render_template("viewsubcat.html")

if __name__== '__main__':
    app1.run()



