from functions import *
import pymysql
from flask import*
from flask_restful import Resource

# Member signup/regestration
class MemberSignup(Resource):
    def post(self):
        data = request.json
        sur_name = data["sur_name"]
        email = data["email"]
        others = data["others"]
        gender = data ["gender"]
        phone = data["phone"]
        DOB = data["DOB"]
        status = data["status"]
        password = data["password"]
        location_id = data["location_id"]
        # conect to db
        connection = pymysql.connect(host='localhost',user='root',password='',database='mediic')
        cursor = connection.cursor()

        response = checkpassword(password)
        if response == True:
            # it means the password is too strong
            sql = "insert into members (email,sur_name,others,gender,phone, DOB, status, password, location_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            data = (email,sur_name, others, gender, encrypt(phone), DOB, status, hash_password(password), location_id) 
            # try:
            cursor.execute(sql, data)
            connection.commit()
            return jsonify({ "message" : "Registration Successfuly" })

            # except:
            #     # incase of an error 
            #     connection.rollback()
            #     return jsonify({"message" : "Registration Failed"})
        else:
            return jsonify({  'message'  : response  })
        
class MembersSignin(Resource):
    def post(self):
        data = request.json
        email = data["email"]
        password = data["password"]

        # connect to db
        connection = pymysql.connect(host='localhost',user='root',password='',database='mediic')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        # check if user exist
        sql = "select * from members where email = %s"
        cursor.execute(sql, email)

        # check the row count to see if email exists 
        if cursor.rowcount == 0:
            return jsonify({ "message":"user does not exist" })
        else: 
            # user exist
            member = cursor.fetchone()
            hashedpassword = member["password"]
            if hash_verify(password, hashedpassword):
                # login successful
                return jsonify({ "message":"Login successful" })
            else:
                return jsonify({ "message":"Login failed" })

class memberprofile(Resource):
    def post(self):
        data = request.json
        member_id = data["member_id"]
        
        

        connection = pymysql.connect(host='localhost',user='root',password='',database='mediic')
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        sql = "SELECT * FROM members WHERE member_id = %s"

        cursor.execute(sql,member_id)

        if cursor.rowcount == 0:
            return jsonify({"message":"user does not exist"})
        else:
            return jsonify({"message":"member found"})
           

            