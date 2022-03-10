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
        DESCRIBEEVENTORPROBLEM = request.form.getlist('EventOrProblem')
    
        a = 'AdverseEvent'
        a1 = 'ProductProblem'
        for i in range(len(DESCRIBEEVENTORPROBLEM)):
            if(DESCRIBEEVENTORPROBLEM[i] == a):
                ADVERSEEVENT = DESCRIBEEVENTORPROBLEM[i]
            if(DESCRIBEEVENTORPROBLEM[i] == a1):
                PRODUCTPROBLEM = DESCRIBEEVENTORPROBLEM[i]
        OUTCOME = request.form.getlist('outcome')
        b = 'death'
        b1 = 'Intervention'
        b2 = 'LifeThreatening'
        b3 = 'Disability'
        b4 = 'Hospitalized'
        b5 = 'CongenitalAnomaly'
        b6 = 'Other'
        for i in range(len(OUTCOME)):
            if(OUTCOME[i] == b):
                DATEOFDEATH = userDetails['DoD']
            if(OUTCOME[i] == b1):
                INTERVENTION = OUTCOME[i]
            if(OUTCOME[i] == b2):
                LIFETHREATENING = OUTCOME[i]
            if(OUTCOME[i] == b3):
                DISABILITY = OUTCOME[i]
            if(OUTCOME[i] == b4):
                HOSPITALIZED = OUTCOME[i]
            if(OUTCOME[i] == b5):
                CONGETITALANOMALY = OUTCOME[i]
            if(OUTCOME[i] == b6):
                OTHER = OUTCOME[i]
        DATEOFEVENT = userDetails['DateOfEvent']
        DATEOFREPORT = userDetails['DateOfReport']
        DATEREPORTCLOSED = userDetails['DateClosed']
        FINDINGS = userDetails['Findings']
        BRANDNAME = userDetails['BrandName']
        MODELNUMBER = userDetails['ModelNum']
        DEVICETYPE = userDetails['DeviceType']
        SERIALNUMBER = userDetails['SerialNum']
        MANUFACTURERNAME = userDetails['ManuName']
        OPERATOR = request.form.getlist('operator')
        REPCOMPANY = userDetails['RepComp']
        REPNAME = userDetails['RepName']
        REPADDRESS = userDetails['RepAddress']
        REPCITY = userDetails['RepCity']
        REPSTATE = userDetails['RepState']
        REPPHONE = userDetails['RepPhone']
        MANUFACTURER = userDetails['RepManuName']
        USERFACILITY = userDetails['RepUserFac']
        DISTRIBUTORIMPORTER = userDetails['RepDisImp']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Form(ptID, DoB, Sex, Weight, ReportedBy, FacilityName, Address, City, FacilityState, Zip, Phone, AdverseEvent, ProductProblem, DoD, Intervention, LifeThreatening, Disability, Hospitalized, CongenitalAnomaly, Other, DateOfEvent, DateOfReport, DateReportClosed, Findings, BrandName, ModelNumber, TOD, SerialNumber, ManufacturerNameManufacturerName, OperatorofDevice, RepCompany, RepName, RepAddress, RepCity, RepState, RepPhone, Manufacturer, UserFacility, DistributorImporter) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(PTID, DOB, SEX, WEIGHT, RPTBY, FACNAME, ADDRESS, CITY, FACILITYSTATE, ZIP, PHONE, ADVERSEEVENT, PRODUCTPROBLEM, DATEOFDEATH, INTERVENTION, LIFETHREATENING, DISABILITY, HOSPITALIZED, CONGETITALANOMALY, OTHER, DATEOFEVENT, DATEOFREPORT, DATEREPORTCLOSED, DESCRIBEEVENTORPROBLEM, FINDINGS, BRANDNAME, MODELNUMBER, DEVICETYPE, SERIALNUMBER, MANUFACTURERNAME, OPERATOR, REPCOMPANY, REPNAME, REPADDRESS, REPCITY, REPSTATE, REPPHONE, MANUFACTURER, USERFACILITY, DISTRIBUTORIMPORTER))
        mysql.connection.commit()
        cur.close()
        return 'Values have been added'
    return render_template('index.html')


if __name__ == '__main__':
   main.run(debug=True)