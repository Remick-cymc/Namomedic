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
            member = cursor.fetchone()
            return jsonify(member)
        
class AddDependants(Resource):
    def post(self):
        data = request.json
        member_id = data["member_id"]
        surname = data["surname"]
        others = data["others"]
        dob = data["dob"]
        # connection to db
        connection = pymysql.connect(host='localhost',user='root',password='',database='mediic')
        cursor = connection.cursor()
        sql = "select * from members where member_id = %s"
        cursor.execute(sql, member_id)
        if cursor.rowcount == 0:
            return jsonify({"message":"member does not exist"})
        else:
            # member exist, now you can add the dependant
            # insert the data
            sql1 = "insert into dependants(member_id, surname, others, dob) values(%s, %s, %s, %s)"
            data = (member_id, surname, others, dob)

            try:
                cursor.execute(sql1, data)
                connection.commit()
                return jsonify({ "message":"Dependant added successful" })
            except:
                connection.rollback()
                return jsonify( {"message":"failed to add dependant"} )
# view dependants
class ViewDependants(Resource):
    def post(self):
        data = request.json
        member_id = data["member_id"]

        connection = pymysql.connect(host='localhost',user='root',password='',database='mediic')
        cursor = connection.cursor(  pymysql.cursors.DictCursor)
        sql = "select * from dependants where member_id = %s"
        cursor.execute(sql,member_id)
        if cursor.rowcount == 0:
            return jsonify({"message":"member does not exist"})
        else:
            dependants = cursor.fetchall()
            return jsonify(dependants)

# view lab test
class ViewLabTests(Resource):
    def get(self):
        connection = pymysql.connect(host='localhost',user='root',password='',database='mediic')
        cursor = connection.cursor(  pymysql.cursors.DictCursor)
        sql = "select * from labtests"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({"message":"no lab test found"})
        else:
            labtests = cursor.fetchall()
            return jsonify(labtests)

# bookings
class Bookings(Resource):
    def post(self):
        data = request.json
        member_id = data ["member_id"]
        booked_for = data["booked_for"]
        dependant_id = data["dependant_id"]
        test_id = data["test_id"]
        appointment_date = data["appointment_date"]
        appointment_time = data["appointment_time"]
        where_taken = data["where_taken"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        status = data["status"]
        invoice_no = data["invoice_no"]

        connection = pymysql.connect(host='localhost',user='root',password='',database='mediic')
        cursor = connection.cursor()
        
        sql = "insert into bookings (member_id,booked_for, dependant_id, test_id, appointment_date,appointment_time,where_taken,latitude,longitude,status,invoice_no) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (member_id,booked_for,dependant_id,test_id,appointment_date,appointment_time,where_taken,latitude,longitude,status,invoice_no)

        try:


            cursor.execute(sql, data)
            connection.commit()
            return jsonify({"message":"booked successful"})
        
        except:
            connection.rollback()
            return jsonify({"message":"booked failed"})

        

            