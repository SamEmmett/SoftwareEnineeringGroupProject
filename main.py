#Right Main File
from lib2to3.pgen2.token import OP
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

main = Flask(__name__)
main.secret_key = '0'
#This is the server connection you can change each attribute to connect to a server of your choice
main.config['MYSQL_HOST'] = 'localhost'
main.config['MYSQL_USER'] = 'root'
main.config['MYSQL_PASSWORD'] = 'dbsucks'
main.config['MYSQL_DB'] = 'groupproject'

mysql = MySQL(main)
#Our first route /
@main.route('/form', methods=['GET', 'POST'])
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

        achk = False
        a1chk= False

        for i in range(len(DESCRIBEEVENTORPROBLEM)):

            if (DESCRIBEEVENTORPROBLEM[i] == a):
                achk = True
            if (DESCRIBEEVENTORPROBLEM[i] == a1):
                a1chk = True


        if (achk == True):
            ADVERSEEVENT = DESCRIBEEVENTORPROBLEM[i]
        else:
            ADVERSEEVENT = None

        if (a1chk == True):
            PRODUCTPROBLEM = DESCRIBEEVENTORPROBLEM[i]
        else:
            PRODUCTPROBLEM = None

        print(DESCRIBEEVENTORPROBLEM)
        OUTCOME = request.form.getlist('outcome')
        b = 'death'
        b1 = 'Intervention'
        b2 = 'LifeThreatening'
        b3 = 'Disability'
        b4 = 'Hospitalized'
        b5 = 'CongenitalAnomaly'
        b6 = 'Other'

        bchk = False
        b1chk = False
        b2chk = False
        b3chk = False
        b4chk = False
        b5chk = False
        b6chk = False

        for i in range(len(OUTCOME)):
            if(OUTCOME[i] == b):
                bchk = True
            if(OUTCOME[i] == b1):
                b1chk = True
            if(OUTCOME[i] == b2):
                b2chk = True
            if(OUTCOME[i] == b3):
                b3chk = True
            if(OUTCOME[i] == b4):
                b4chk = True
            if(OUTCOME[i] == b5):
                b5chk = True
            if(OUTCOME[i] == b6):
                b6chk = True

        if (bchk == True):
            DATEOFDEATH = userDetails['DoD']
        else:
            DATEOFDEATH = None

        if (b1chk == True):
            INTERVENTION = OUTCOME[i]
        else:
            INTERVENTION = None

        if (b2chk == True):
            LIFETHREATENING = OUTCOME[i]
        else:
            LIFETHREATENING = None

        if (b3chk == True):
            DISABILITY = OUTCOME[i]
        else:
            DISABILITY = None

        if (b4chk == True):
            HOSPITALIZED = OUTCOME[i]
        else:
            HOSPITALIZED = None

        if (b5chk == True):
            CONGETITALANOMALY = OUTCOME[i]
        else:
            CONGETITALANOMALY = None

        if (b6chk == True):
            OTHER = OUTCOME[i]
        else:
            OTHER = None

        print(OUTCOME)
        OPERATOR = request.form.getlist('operator')
        c = 'HealthProfessional'
        c1 = 'User/Patient'
        c2 = 'Other2'

        cchk = False
        c1chk = False
        c2chk = False


        for i in range(len(OPERATOR)):
            if(OPERATOR[i] == c):
              cchk = True
            if(OPERATOR[i] == c1):
               c1chk = True
            if(OPERATOR[i] == c2):
                c2chk = True

        if (cchk == True):
            HEALTHPROFESSIONAL = OPERATOR[i]
        else:
            HEALTHPROFESSIONAL = None

        if (c1chk == True):
            LAYUSERPATIENT = OPERATOR[i]
        else:
            LAYUSERPATIENT = None

        if (c2chk == True):   
            OTHER2 = userDetails['OtherText2']
        else:
            OTHER2 = None

        DATEOFEVENT = None
        DATEOFREPORT = None
        DATEREPORTCLOSED = None
        DATEOFEVENT = userDetails['DateOfEvent']
        DATEOFREPORT = userDetails['DateOfReport']
        DATEREPORTCLOSED = userDetails['DateClosed']
        DESCRIBE = userDetails['Description']
        FINDINGS = userDetails['Findings']
        SIGNATURE = userDetails['Signature']
        DATECOMP = userDetails['SignatureDate']
        BRANDNAME = userDetails['BrandName']
        MODELNUMBER = userDetails['ModelNum']
        DEVICETYPE = userDetails['DeviceType']
        SERIALNUMBER = userDetails['SerialNum']
        MANUNAME = userDetails['ManuName']
        MANUCITY = userDetails['ManuCity']
        MANUSTATE = userDetails['ManuState']
        REPADDRESS = userDetails['RepAddress']
        REPCITY = userDetails['RepCity']
        REPSTATE = userDetails['RepState']
        REPPHONE = userDetails['RepPhone']
        MANUFACTURER = userDetails['RepManuName']
        USERFACILITY = userDetails['RepUserFac']
        DISTRIBUTORIMPORTER = userDetails['RepDisImp']
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO patientinfo(ptID, DoB, Sex, Weight)VALUES(%s, %s, %s, %s)",(PTID, DOB, SEX, WEIGHT))
        cur.execute("INSERT INTO reportingfacilityinfo(ReportedBy, FacilityName, Address, City, FacilityState, Zip, Phone)VALUES(%s, %s, %s, %s, %s, %s, %s)",(RPTBY, FACNAME, ADDRESS, CITY, FACILITYSTATE, ZIP, PHONE))
        cur.execute("INSERT INTO susmedicaldevice(BrandName, ModelNumber, TOD, SerialNumber, ManufacturerName, MCity, MState, HealthProfessional, LayUserPatient, Other2)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s , %s)",(BRANDNAME, MODELNUMBER, DEVICETYPE, SERIALNUMBER, MANUNAME, MANUCITY, MANUSTATE,HEALTHPROFESSIONAL, LAYUSERPATIENT, OTHER2))
        cur.execute("INSERT INTO adverseeventorproductproblem(AdverseEvent, ProductProblem, DoD, Intervention, LifeThreatening, Disability, Hospitalized, CongenitalAnomaly, Other, DateOfEvent, DateOfReport, DateReportClosed)VALUES(%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)",(ADVERSEEVENT, PRODUCTPROBLEM, DATEOFDEATH, INTERVENTION, LIFETHREATENING, DISABILITY, HOSPITALIZED, CONGETITALANOMALY,OTHER, DATEOFEVENT, DATEOFREPORT, DATEREPORTCLOSED))
        cur.execute("INSERT INTO reportcompletedby(RepCompany, RepName, RepAddress, RepCity, RepState, RepPhone)Values(%s,%s,%s,%s,%s,%s)",(REPADDRESS, REPCITY, REPADDRESS,REPCITY, REPSTATE, REPPHONE))
        cur.execute("INSERT INTO SignOff(Signature, DateCompleted)VALUES(%s, %s)",(SIGNATURE, DATECOMP))
        cur.execute("INSERT INTO EventInformation(DescribeEoP, Findings )VALUES(%s, %s)",(DESCRIBE,FINDINGS))
        cur.execute("INSERT INTO AlsoReportedTo(MANUFACTURER, USERFACILITY, DISTRIBUTORIMPORTER)VALUES(%s, %s, %s)",(MANUFACTURER, USERFACILITY, DISTRIBUTORIMPORTER))
        mysql.connection.commit()
        form = 0
        form += 1
        ID = session['id']
        form = 1
        cur = mysql.connection.cursor()
        cur.execute("SELECT UserID FROM Users WHERE UserID  = %s ", (ID,))
        UIDVAL = cur.fetchall()
        cur.execute("SELECT piID FROM patientinfo WHERE piID = %s ", (form,))
        PIIDVAL = cur.fetchall()
        cur.execute("SELECT rfiID FROM reportingfacilityinfo WHERE rfiID  = %s ", (form,))
        RFIIDVAL = cur.fetchall()
        cur.execute("SELECT smdID FROM susmedicaldevice WHERE smdID  = %s ", (form,))
        SMDIDVAL = cur.fetchall()
        cur.execute("SELECT aeoppID FROM adverseeventorproductproblem WHERE aeoppID  = %s ", (form,))
        AEOPPIDVAL = cur.fetchall()
        cur.execute("SELECT rcbID FROM reportcompletedby WHERE rcbID  = %s ", (form,))
        RCBIDVAL = cur.fetchall()
        cur.execute("SELECT soID FROM signoff WHERE soID = %s ", (form,))
        SOIDVAL = cur.fetchall()
        cur.execute("SELECT EventID FROM EventInformation WHERE EventID = %s ", (form,))
        EVENTIDVAL = cur.fetchall()
        cur.execute("SELECT artID FROM AlsoReportedTo WHERE artID = %s ", (form,))
        ARTIDVAL = cur.fetchall()
        UID = UIDVAL[0][0]
        PIID = PIIDVAL[0][0]
        RFIID = RFIIDVAL[0][0]
        SMDID = SMDIDVAL[0][0]
        AEOPPID = AEOPPIDVAL[0][0]
        RCBID = RCBIDVAL[0][0]
        SOID = SOIDVAL[0][0]
        EVENTID = EVENTIDVAL[0][0]
        ARTID = ARTIDVAL[0][0]
        cur.execute("INSERT INTO Form (UserID, piID, rfiID, smdID, aeoppID, rcbID, soID, EventID, artID) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (UID,PIID,RFIID,SMDID,AEOPPID,RCBID,SOID,EVENTID,ARTID))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('home')) 
    return render_template('index.html')


@main.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method =='POST':
        loginCreds = request.form
        Username = loginCreds['username']
        Password = loginCreds['password']
        cur =mysql.connection.cursor()
        cur.execute("Select userID, Uname, FirstName, LastName from users WHERE UName = %s and Pword = %s", (Username, Password))
        account = cur.fetchone()
        print(account)
        if account:
            session['loggedin']=True
            session['id'] = account[0]
            session['username'] = account[1]
            session['first'] = account[2]
            session['last'] = account[3]
            # this is the redirect to the page after login
            return redirect(url_for('home'))
        else:
            #account doesn't exist or incorrect info entered
            msg = "Incorrect credentials"
    return render_template('login.html', msg=msg)

@main.route('/homepage', methods=['GET', 'POST'])
def home():
    page = 'login'
    usermsg = 'Log In'
    if 'loggedin' in session:
        usermsg ='Hello, '+ session['first']+" "+session['last']
        page = 'profile'
       
        return render_template("Homepage.html", page=page, usermsg=usermsg)
    return render_template("Homepage.html" , page=page, usermsg=usermsg)
    

@main.route('/viewform', methods=['GET', 'POST'])
def viewform():
    
    if request.method =='GET':
            ID = session['id'] 
            cur = mysql.connection.cursor()
            cur.execute("SELECT FormID FROM Form as f JOIN adverseeventorproductproblem as a ON a.aeoppID = f.aeoppID WHERE UserID = %s ORDER BY DateOfReport ASC",(ID,))
            
            #cur.execute("SELECT FormID, %s , piID, EventID, DateOfReport FROM Form as f JOIN adverseeventorproductproblem as a ON a.aeoppID = f.aeoppID",(ID,))
            myresult = cur.fetchall()
            new_list = []
            for item in myresult:
                new_list.append(item[0])
            cur.close()
    
            return render_template("ViewForm.html" , new_list = new_list )
    if request.method == 'POST':
        formnum = request.form
        FORMNUML = formnum['formnumlist']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Form JOIN USERS on users.USERID = form.USERID JOIN PATIENTINFO ON patientinfo.PIID = form.PIID JOIN EventInformation ON EventInformation.EVENTID = form.EVENTID JOIN reportingfacilityinfo ON reportingfacilityinfo.RFIID = form.RFIID JOIN susmedicaldevice ON susmedicaldevice.SMDID = form.SMDID JOIN adverseeventorproductproblem ON adverseeventorproductproblem.aeoppID = form.aeoppID JOIN reportcompletedby ON reportcompletedby.rcbID = form.rcbID JOIN signoff ON signoff.soID = form.soID JOIN AlsoReportedTo ON AlsoReportedTo.artID = form.artID WHERE FormID = %s ORDER BY DateOfReport ASC", (FORMNUML,))
        getformData = cur.fetchall()   
        print(getformData)
        new_list1 = []
        for item in getformData:
            for j in item:
                new_list1.append(j)
        print(new_list1)
        session['ses_list'] = new_list1
        cur.close()
        return redirect(url_for('getform')) 

@main.route('/getform', methods=['GET', 'POST'])
def getform():
    seshlist = session['ses_list'] 
    print(seshlist)
    if request.method =='GET':
        return render_template("Viewingindex.html", seshlist = seshlist)

@main.route('/profile', methods=['GET', 'POST'])
def profile(): 
    page = 'login' 
    usermsg = 'Log In' 
    if 'loggedin' in session: 
        usermsg ='Hello, '+ session['first']+" "+session['last'] 
        page = 'profile' 
        cur=mysql.connection.cursor()
        cur.execute("Select email, FirstName, LastName, Company, Address, City, State, Phone from users WHERE UName = '{0}'".format(session['username']))
        info = cur.fetchone()
        ###print("\n\n\n\n\n\n\n"+info[2]+"\n\n\n\n\n\n\n\n")
        return render_template("profile.html", page=page, usermsg=usermsg, username=session['username'], email = info[0], FirstName = info[1], lastname = info[2], Company = info[3], Address=info[4], City=info[5], State=info[6], Phone=info[7])
    return render_template("profile.html" , page=page, usermsg=usermsg)
    
if __name__ == '__main__':
   main.run(debug=True)