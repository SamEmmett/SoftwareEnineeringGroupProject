from flask import Flask, render_template, request
from flask_mysqldb import MySQL

main = Flask(__name__)
#This is the server connection you can change each attribute to connect to a server of your choice
main.config['MYSQL_HOST'] = 'localhost'
main.config['MYSQL_USER'] = 'root'
main.config['MYSQL_PASSWORD'] = 'dbsucks'
main.config['MYSQL_DB'] = 'groupproject'

mysql = MySQL(main)
#Our first route / 
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        userDetails = request.form
        PTID = userDetails['ptID']
        DOB = userDetails['DoB']
        SEX = request.form.getlist('radSex')
        WEIGHT = userDetails['Weight']
        RPTBY = userDetails['rptBy']
        FACNAME = userDetails['facName']
        ADDRESS = userDetails['Address']
        CITY = userDetails['City']
        FACILITYSTATE = userDetails['FacilityState']
        ZIP = userDetails['Zip']
        PHONE = userDetails['Phone']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Form(ptID, DoB, Sex, Weight, ReportedBy, FacilityName, Address, City, FacilityState, Zip, Phone) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(PTID, DOB, SEX, WEIGHT, RPTBY, FACNAME, ADDRESS, CITY, FACILITYSTATE, ZIP, PHONE))
        mysql.connection.commit()
        cur.close()
        return 'Values have been added'
    return render_template('index.html')


if __name__ == '__main__':
   main.run(debug=True)