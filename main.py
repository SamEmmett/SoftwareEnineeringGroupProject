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
        ADVERSEEVENT = None
        PRODUCTPROBLEM = None
        for i in range(len(DESCRIBEEVENTORPROBLEM)):
            if (DESCRIBEEVENTORPROBLEM[i] == a):
                 ADVERSEEVENT = DESCRIBEEVENTORPROBLEM[i]
            if (DESCRIBEEVENTORPROBLEM[i] == a1):
                PRODUCTPROBLEM = DESCRIBEEVENTORPROBLEM[i]

        #print(DESCRIBEEVENTORPROBLEM)
        OUTCOME = request.form.getlist('outcome')
        b  = 'death'
        b1 = 'Intervention'
        b2 = 'LifeThreatening'
        b3 = 'Disability'
        b4 = 'Hospitalized'
        b5 = 'CongenitalAnomaly'
        b6 = 'Other'
        DATEOFDEATH = None
        INTERVENTION = None
        LIFETHREATENING = None
        DISABILITY = None
        HOSPITALIZED = None
        CONGETITALANOMALY = None
        OTHER = None

      
        for i in range(len(OUTCOME)): #Sam no longer wrote this ¯\_(ツ)_/¯
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
                OTHER = userDetails['OtherText1']


        print(OUTCOME)
        OPERATOR = request.form.getlist('operator')
        c = 'HealthProfessional'
        c1 = 'User/Patient'
        c2 = 'Other2'
        HEALTHPROFESSIONAL = None
        LAYUSERPATIENT = None
        OTHER2 = None
        for i in range(len(OPERATOR)):
            if(OPERATOR[i] == c):
               HEALTHPROFESSIONAL = OPERATOR[i]
            if(OPERATOR[i] == c1):
                LAYUSERPATIENT = OPERATOR[i]
            if(OPERATOR[i] == c2):
                OTHER2 = userDetails['OtherText2']



        DATEOFEVENT = None
        DATEOFREPORT = None
        DATEREPORTCLOSED = None
        DATEOFEVENT = userDetails['DateOfEvent']
        DATEOFREPORT = userDetails['DateOfReport']
        DATEREPORTCLOSED = userDetails['DateClosed']
        DESCRIBE = userDetails['Description']
        FINDINGS = userDetails['Findings']
        cur = mysql.connection.cursor()
        ID = session['id']
        
        SIGNATURE = None
        DATECOMP = "1900-01-01"
        SIGNATURE = userDetails['Signature']
        DATECOMP = userDetails['SignatureDate']
        if DATECOMP == "":
            DATECOMP = None
        BRANDNAME = userDetails['BrandName']
        MODELNUMBER = userDetails['ModelNum']
        if MODELNUMBER == "":
            MODELNUMBER = None
        DEVICETYPE = userDetails['DeviceType']
        SERIALNUMBER = userDetails['SerialNum']
        MANUNAME = userDetails['ManuName']
        MANUCITY = userDetails['ManuCity']
        MANUSTATE = userDetails['ManuState']
        REPCOMPANY = userDetails['RepComp']
        REPADDRESS = userDetails['RepAddress']
        REPNAME = userDetails['RepName']
        REPCITY = userDetails['RepCity']
        REPSTATE = userDetails['RepState']
        REPPHONE = userDetails['RepPhone']
        MANUFACTURER = userDetails['RepManuName']
        USERFACILITY = userDetails['RepUserFac']
        DISTRIBUTORIMPORTER = userDetails['RepDisImp']
      

        cur.execute("INSERT INTO patientinfo(ptID, DoB, Sex, Weight)VALUES(%s, %s, %s, %s)",(PTID, DOB, SEX, WEIGHT))
        
        cur.execute("INSERT INTO reportingfacilityinfo(ReportedBy, FacilityName, Address, City, FacilityState, Zip, Phone)VALUES(%s, %s, %s, %s, %s, %s, %s)",(RPTBY, FACNAME, ADDRESS, CITY, FACILITYSTATE, ZIP, PHONE))
        
        cur.execute("INSERT INTO susmedicaldevice(BrandName, ModelNumber, TOD, SerialNumber, ManufacturerName, MCity, MState, HealthProfessional, LayUserPatient, Other2)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s , %s)",(BRANDNAME, MODELNUMBER, DEVICETYPE, SERIALNUMBER, MANUNAME, MANUCITY, MANUSTATE,HEALTHPROFESSIONAL, LAYUSERPATIENT, OTHER2))

        cur.execute("INSERT INTO adverseeventorproductproblem(AdverseEvent, ProductProblem, DoD, Intervention, LifeThreatening, Disability, Hospitalized, CongenitalAnomaly, Other, DateOfEvent, DateOfReport, DateReportClosed)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(ADVERSEEVENT, PRODUCTPROBLEM, DATEOFDEATH, INTERVENTION, LIFETHREATENING, DISABILITY, HOSPITALIZED, CONGETITALANOMALY,OTHER, DATEOFEVENT, DATEOFREPORT, DATEREPORTCLOSED))
        
        cur.execute("INSERT INTO reportcompletedby(RepCompany, RepName, RepAddress, RepCity, RepState, RepPhone)Values(%s,%s,%s,%s,%s,%s)",(REPCOMPANY, REPNAME, REPADDRESS, REPCITY , REPSTATE, REPPHONE))
        
        cur.execute("INSERT INTO EventInformation(DescribeEoP, Findings )VALUES(%s, %s)",(DESCRIBE,FINDINGS))
        
        cur.execute("INSERT INTO AlsoReportedTo(MANUFACTURER, USERFACILITY, DISTRIBUTORIMPORTER)VALUES(%s, %s, %s)",(MANUFACTURER, USERFACILITY, DISTRIBUTORIMPORTER))
        
        cur.execute("INSERT INTO SignOff(Signature, DateCompleted)VALUES(%s, %s)",(SIGNATURE, DATECOMP))
        
        mysql.connection.commit()
      
        form = cur.execute("select formID from form order by formid asc;")
       
        if form == None:
            form=0
        form=form+1
        
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
        UID = UIDVAL[0][0] #Evan wrote this ¯\_(ツ)_/¯
        PIID = PIIDVAL[0][0]
        RFIID = RFIIDVAL[0][0]
        SMDID = SMDIDVAL[0][0]
        AEOPPID = AEOPPIDVAL[0][0]
        RCBID = RCBIDVAL[0][0]
        SOID = SOIDVAL[0][0]
        EVENTID = EVENTIDVAL[0][0]
        ARTID = ARTIDVAL[0][0]
        cur.execute("INSERT INTO Form (UserID, piID, rfiID, smdID, aeoppID, rcbID, soID, EventID, artID) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (UID,PIID,RFIID,SMDID,AEOPPID,RCBID,SOID,EVENTID,ARTID,))
        mysql.connection.commit()
       
        cur.close()
        
        return redirect(url_for('home')) 
        
    if request.method == 'GET':  
        adminitem = session['admincheck']
        return render_template("index.html",adminitem  = adminitem )

@main.route('/logout')      
def logout():
    session['loggedin']=False
    session['id'] = None
    session['username'] = None
    session['first'] = None
    session['last'] = None
    session['admin'] = None
    session['admincheck'] = 0
    return redirect(url_for('login'))



@main.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method =='POST':
        loginCreds = request.form
        Username = loginCreds['username']
        Password = loginCreds['password']
        cur =mysql.connection.cursor()
        cur.execute("Select userID, Uname, FirstName, LastName, IsAdmin from users WHERE UName = %s and Pword = %s", (Username, Password))
        account = cur.fetchone()
        #print(account)
        if account:
            session['loggedin']=True
            session['id'] = account[0]
            session['username'] = account[1]
            session['first'] = account[2]
            session['last'] = account[3]
            session['admin'] = "Standard User"
            session['admincheck'] = account[4]
            if account[4]==1:
                session['admin']="Administrator"
            # this is the redirect to the page after login
            return redirect(url_for('home'))
        else:
            #account doesn't exist or incorrect info entered
            msg = "Incorrect credentials"
           
    return render_template('login.html', msg=msg)
    
#Route for our homepage
@main.route('/homepage', methods=['GET', 'POST'])
def home():
    adminitem = session['admincheck']
    page = 'login'
    usermsg = 'Log In'
    print(adminitem)
    if 'loggedin' in session:
        usermsg ='Hello, '+ session['first'] +" "+session['last']
        page = 'profile'
        print(adminitem)
        if request.method =='GET':
            alist = []
            cur = mysql.connection.cursor()
            ID = session['id']
            cur.execute("SELECT isAdmin FROM Users WHERE UserID = %s",(ID,))
            admincheck = cur.fetchall()
        
        for item in admincheck:
            alist.append(item)
            session['admincheck'] = alist[0]
        
        #print(admincheck)
        adminitem = session['admincheck']
        return render_template("Homepage.html", page=page, usermsg=usermsg, adminitem = adminitem )
    return render_template("Homepage.html" , page=page, usermsg=usermsg, adminitem = adminitem)
   
    
@main.route('/viewform', methods=['GET', 'POST'])
def viewform():
    if request.method =='GET':
            ID = session['id'] 
            
            cur = mysql.connection.cursor()
            if ID != 1:
                cur.execute("SELECT FormID FROM Form as f JOIN adverseeventorproductproblem as a ON a.aeoppID = f.aeoppID WHERE UserID = %s ORDER BY DateOfReport ASC",(ID,))
            else: 
                cur.execute("SELECT FormID FROM Form as f JOIN adverseeventorproductproblem as a ON a.aeoppID = f.aeoppID ORDER BY DateOfReport ASC")
            
            #cur.execute("SELECT FormID, %s , piID, EventID, DateOfReport FROM Form as f JOIN adverseeventorproductproblem as a ON a.aeoppID = f.aeoppID",(ID,))
            myresult = cur.fetchall()
            new_list = []
            formID = ["         "]
            Date=[" "]
            CompletedBy =[" "]
            Facility = [" "]
            Brand = [" "]

            i=0
            for item in myresult:
                formInfo =[]
                #print("\n\n\n\n\n\n\n\n\n\n"+item)
                #print(i+"\n\n\n\n\n\n\n\n\n\n\n\n\n")
                new_list.append(item[0])
                cur.execute("SELECT form.formID, adverseeventorproductproblem.DateOfEvent, reportcompletedby.RepName, reportingfacilityinfo.facilityName, susmedicaldevice.BrandName FROM form INNER JOIN adverseeventorproductproblem ON form.aeoppID = adverseeventorproductproblem.aeoppID INNER JOIN reportingfacilityinfo ON form.rfiID = reportingfacilityinfo.rfiID INNER JOIN susmedicaldevice ON form.smdID = susmedicaldevice.smdID INNER JOIN reportcompletedby ON form.rcbID = reportcompletedby.rcbID WHERE form.formID = %s;",(i,))
                formInfo = cur.fetchone()
                if i !=0:
                    formID.append(formInfo[0])
                    Date.append(formInfo[1])
                    CompletedBy.append(formInfo[2])
                    Facility.append(formInfo[3])
                    Brand.append(formInfo[4])
                i=i+1
                
           
            cur.execute("SELECT form.formID, adverseeventorproductproblem.DateOfEvent, reportcompletedby.RepName, reportingfacilityinfo.facilityName, susmedicaldevice.BrandName FROM form INNER JOIN adverseeventorproductproblem ON form.aeoppID = adverseeventorproductproblem.aeoppID INNER JOIN reportingfacilityinfo ON form.rfiID = reportingfacilityinfo.rfiID INNER JOIN susmedicaldevice ON form.smdID = susmedicaldevice.smdID INNER JOIN reportcompletedby ON form.rcbID = reportcompletedby.rcbID WHERE form.formID = %s;",(i,))
            formInfo = []
            formInfo = cur.fetchone()
            formID.append(formInfo[0])
            Date.append(formInfo[1])
            CompletedBy.append(formInfo[2])
            Facility.append(formInfo[3])
            Brand.append(formInfo[4])
            cur.close()
            adminitem = session['admincheck']
            return render_template("ViewForm.html" , formID=formID, Date=Date, CompletedBy=CompletedBy, Facility=Facility, Brand=Brand, adminitem = adminitem )
    #If a post request is made on the viewform it grabs all data from forms from the logged in ID from the current session then it stores the data in a list
    # called seshlist and passes that in the session to the getform route
    if request.method == 'POST':
        
        formnum = request.form['formnum']
        cur = mysql.connection.cursor()    
        formnumlist = formnum.split()
        print(formnumlist[0])
        cur.execute("SELECT * FROM Form JOIN USERS on users.USERID = form.USERID JOIN PATIENTINFO ON patientinfo.PIID = form.PIID JOIN EventInformation ON EventInformation.EVENTID = form.EVENTID JOIN reportingfacilityinfo ON reportingfacilityinfo.RFIID = form.RFIID JOIN susmedicaldevice ON susmedicaldevice.SMDID = form.SMDID JOIN adverseeventorproductproblem ON adverseeventorproductproblem.aeoppID = form.aeoppID JOIN reportcompletedby ON reportcompletedby.rcbID = form.soID JOIN AlsoReportedTo ON AlsoReportedTo.artID = form.rcbID JOIN signoff ON signoff.soID = form.artID WHERE FormID = %s ORDER BY DateOfReport ASC",(formnumlist[0],))
        getformData = cur.fetchall()  
        #print("this is before") 
        #print(getformData)
        new_list1 = []
        for item in getformData:
            for j in item:
                new_list1.append(j)
        #print("this is after")
        #print(new_list1)
        session['ses_list'] = new_list1
        cur.close()
        return redirect(url_for('getform')) 

@main.route('/getform', methods=['GET', 'POST'])
def getform():
    seshlist = session['ses_list'] 
    if request.method =='GET':
        adminitem = session['admincheck']
        return render_template("Viewingindex.html", seshlist = seshlist, adminitem = adminitem)
        
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
        adminitem = session['admincheck']
        return render_template("profile.html", page=page, usermsg=usermsg, username=session['username'], adminitem = adminitem, email = info[0], FirstName = info[1], lastname = info[2], Company = info[3], Address=info[4], City=info[5], State=info[6], Phone=info[7], Admin = session['admin'])
    return render_template("profile.html" , page=page, usermsg=usermsg)

@main.route('/edit', methods=['GET', 'POST'])
def edit():

    #Lists of forms based off of user ID 
    if request.method =='GET':
            ID = session['id'] 
            cur = mysql.connection.cursor()
            if ID != 1:
                cur.execute("SELECT FormID FROM Form as f JOIN adverseeventorproductproblem as a ON a.aeoppID = f.aeoppID WHERE UserID = %s ORDER BY DateOfReport ASC",(ID,))
            else: 
                cur.execute("SELECT FormID FROM Form as f JOIN adverseeventorproductproblem as a ON a.aeoppID = f.aeoppID ORDER BY DateOfReport ASC")
            
            #cur.execute("SELECT FormID, %s , piID, EventID, DateOfReport FROM Form as f JOIN adverseeventorproductproblem as a ON a.aeoppID = f.aeoppID",(ID,))
            myresult = cur.fetchall()
            new_list = []
            formID = ["         "]
            Date=[" "]
            CompletedBy =[" "]
            Facility = [" "]
            Brand = [" "]

            i=0
            for item in myresult:
                formInfo =[]
                #print("\n\n\n\n\n\n\n\n\n\n"+item)
                #print(i+"\n\n\n\n\n\n\n\n\n\n\n\n\n")
                new_list.append(item[0])
                cur.execute("SELECT form.formID, adverseeventorproductproblem.DateOfEvent, reportcompletedby.RepName, reportingfacilityinfo.facilityName, susmedicaldevice.BrandName FROM form INNER JOIN adverseeventorproductproblem ON form.aeoppID = adverseeventorproductproblem.aeoppID INNER JOIN reportingfacilityinfo ON form.rfiID = reportingfacilityinfo.rfiID INNER JOIN susmedicaldevice ON form.smdID = susmedicaldevice.smdID INNER JOIN reportcompletedby ON form.rcbID = reportcompletedby.rcbID WHERE form.formID = %s;",(i,))
                formInfo = cur.fetchone()
                if i !=0:
                    formID.append(formInfo[0])
                    Date.append(formInfo[1])
                    CompletedBy.append(formInfo[2])
                    Facility.append(formInfo[3])
                    Brand.append(formInfo[4])
                i=i+1
                
           
            cur.execute("SELECT form.formID, adverseeventorproductproblem.DateOfEvent, reportcompletedby.RepName, reportingfacilityinfo.facilityName, susmedicaldevice.BrandName FROM form INNER JOIN adverseeventorproductproblem ON form.aeoppID = adverseeventorproductproblem.aeoppID INNER JOIN reportingfacilityinfo ON form.rfiID = reportingfacilityinfo.rfiID INNER JOIN susmedicaldevice ON form.smdID = susmedicaldevice.smdID INNER JOIN reportcompletedby ON form.rcbID = reportcompletedby.rcbID WHERE form.formID = %s;",(i,))
            formInfo = []
            formInfo = cur.fetchone()
            formID.append(formInfo[0])
            Date.append(formInfo[1])
            CompletedBy.append(formInfo[2])
            Facility.append(formInfo[3])
            Brand.append(formInfo[4])
            cur.close()
            adminitem = session['admincheck']
            return render_template("EditForm.html" , formID=formID, Date=Date, CompletedBy=CompletedBy, Facility=Facility, Brand=Brand, adminitem = adminitem)
    # when update is pressed it takes value submitted into the edit form page and passes them into the database the db used an update statement depending on FormID to update each table
    if request.method == 'POST':
       
        formnumedit = request.form['formnumedit']
        session['formnumedit'] = formnumedit
        cur = mysql.connection.cursor()                                                                                     
        cur.execute("SELECT * FROM Form JOIN USERS on users.USERID = form.USERID JOIN PATIENTINFO ON patientinfo.PIID = form.PIID JOIN EventInformation ON EventInformation.EVENTID = form.EVENTID JOIN reportingfacilityinfo ON reportingfacilityinfo.RFIID = form.RFIID JOIN susmedicaldevice ON susmedicaldevice.SMDID = form.SMDID JOIN adverseeventorproductproblem ON adverseeventorproductproblem.aeoppID = form.aeoppID JOIN reportcompletedby ON reportcompletedby.rcbID = form.soID JOIN AlsoReportedTo ON AlsoReportedTo.artID = form.rcbID JOIN signoff ON signoff.soID = form.artID WHERE FormID = %s ORDER BY DateOfReport ASC",(formnumedit,))
        getformData = cur.fetchall()  
        #print("this is before") 
        #print(getformData)
        new_list1 = []
        for item in getformData:
            for j in item:
                new_list1.append(j)
        #print("this is after")
        #print(new_list1)
        session['ses_list'] = new_list1
        cur.close()
        return redirect(url_for('getform2')) 

@main.route('/getform2', methods=['GET', 'POST'])

def getform2():
    
    seshlist = session['ses_list'] 
    
    if request.method =='GET':

        adminitem = session['admincheck']
        return render_template("Editindexing.html", seshlist = seshlist, adminitem = adminitem)
    if request.method == 'POST' :
        adminitem = session['admincheck']
        editForm = request.form
        editformselect = session['formnumedit']
        formnumlistedit = editformselect.split()
        
        print(formnumlistedit[0])
        PTID = editForm['ptID']
        DOB = editForm['DoB']
        SEX = request.form.getlist('radSex')
        WEIGHT = editForm['Weight']
        RPTBY = editForm['rptBy']
        FACNAME = editForm['facName']
        ADDRESS = editForm['Address']
        CITY = editForm['City']
        FACILITYSTATE = editForm['FacilityState']
        ZIP = editForm['Zip']
        PHONE = editForm['Phone']
        

        DESCRIBEEVENTORPROBLEM = request.form.getlist('EventOrProblem')
        a = 'AdverseEvent'
        a1 = 'ProductProblem'
        ADVERSEEVENT = None
        PRODUCTPROBLEM = None
        for i in range(len(DESCRIBEEVENTORPROBLEM)):
            if (DESCRIBEEVENTORPROBLEM[i] == a):
                 ADVERSEEVENT = DESCRIBEEVENTORPROBLEM[i]
            if (DESCRIBEEVENTORPROBLEM[i] == a1):
                PRODUCTPROBLEM = DESCRIBEEVENTORPROBLEM[i]

        #print(DESCRIBEEVENTORPROBLEM)
        OUTCOME = request.form.getlist('outcome')
        b  = 'death'
        b1 = 'Intervention'
        b2 = 'LifeThreatening'
        b3 = 'Disability'
        b4 = 'Hospitalized'
        b5 = 'CongenitalAnomaly'
        b6 = 'Other'
        DATEOFDEATH = None
        INTERVENTION = None
        LIFETHREATENING = None
        DISABILITY = None
        HOSPITALIZED = None
        CONGETITALANOMALY = None
        OTHER = None

      
        for i in range(len(OUTCOME)): #Sam no longer wrote this ¯\_(ツ)_/¯
            if(OUTCOME[i] == b):
                DATEOFDEATH = editForm['DoD']
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
                OTHER = editForm['OtherText1']


        print(OUTCOME)
        OPERATOR = request.form.getlist('operator')
        c = 'HealthProfessional'
        c1 = 'User/Patient'
        c2 = 'Other2'
        HEALTHPROFESSIONAL = None
        LAYUSERPATIENT = None
        OTHER2 = None
        for i in range(len(OPERATOR)):
            if(OPERATOR[i] == c):
               HEALTHPROFESSIONAL = OPERATOR[i]
            if(OPERATOR[i] == c1):
                LAYUSERPATIENT = OPERATOR[i]
            if(OPERATOR[i] == c2):
                OTHER2 = editForm['OtherText2']



        DATEOFEVENT = None
        DATEOFREPORT = None
        DATEREPORTCLOSED = None
        DATEOFEVENT = editForm['DateOfEvent']
        DATEOFREPORT = editForm['DateOfReport']
        DATEREPORTCLOSED = editForm['DateClosed']
        DESCRIBE = editForm['Description']
        FINDINGS = editForm['Findings']
        cur = mysql.connection.cursor()
        ID = session['id']
        SIGNATURE = None
        DATECOMP = None
        SIGNATURE = editForm['Signature']
        DATECOMP = editForm['SignatureDate']
        if DATECOMP == "":
            DATECOMP = None
        BRANDNAME = editForm['BrandName']
        MODELNUMBER = editForm['ModelNum']
        if MODELNUMBER == "":
            MODELNUMBER = None
        DEVICETYPE = editForm['DeviceType']
        SERIALNUMBER = editForm['SerialNum']
        MANUNAME = editForm['ManuName']
        MANUCITY = editForm['ManuCity']
        MANUSTATE = editForm['ManuState']
        REPCOMPANY = editForm['RepComp']
        REPADDRESS = editForm['RepAddress']
        REPNAME = editForm['RepName']
        REPCITY = editForm['RepCity']
        REPSTATE = editForm['RepState']
        REPPHONE = editForm['RepPhone']
        MANUFACTURER = editForm['RepManuName']
        USERFACILITY = editForm['RepUserFac']
        DISTRIBUTORIMPORTER = editForm['RepDisImp']
        PIID = formnumlistedit[0]
        RFIID = formnumlistedit[0]
        SMDID = formnumlistedit[0]
        AEOPPID = formnumlistedit[0]
        RCBID = formnumlistedit[0]
        SOID = formnumlistedit[0]
        EVENTID = formnumlistedit[0]
        ARTID = formnumlistedit[0]
        cur.execute("UPDATE patientinfo SET ptID = %s, DoB = %s, Sex = %s, Weight = %s WHERE piID = %s", (PTID, DOB, SEX, WEIGHT, PIID,))
        
        cur.execute("UPDATE reportingfacilityinfo SET ReportedBy = %s, FacilityName = %s, Address = %s, City = %s, FacilityState = %s, Zip = %s, Phone = %s WHERE RfiID = %s",(RPTBY, FACNAME, ADDRESS, CITY, FACILITYSTATE, ZIP, PHONE, RFIID,))
    
        cur.execute("UPDATE susmedicaldevice SET BrandName = %s, ModelNumber = %s, TOD = %s, SerialNumber = %s, ManufacturerName = %s, MCity = %s, MState = %s, HealthProfessional = %s, LayUserPatient = %s, Other2 = %s WHERE SmDID = %s",(BRANDNAME, MODELNUMBER, DEVICETYPE, SERIALNUMBER, MANUNAME, MANUCITY, MANUSTATE,HEALTHPROFESSIONAL, LAYUSERPATIENT, OTHER2, SMDID,))
        
        cur.execute("UPDATE adverseeventorproductproblem SET AdverseEvent = %s, ProductProblem = %s, DoD = %s, Intervention = %s, LifeThreatening = %s, Disability = %s, Hospitalized = %s, CongenitalAnomaly = %s, Other = %s, DateOfEvent= %s, DateOfReport = %s, DateReportClosed = %s WHERE AeOPPID = %s",(ADVERSEEVENT, PRODUCTPROBLEM, DATEOFDEATH, INTERVENTION, LIFETHREATENING, DISABILITY, HOSPITALIZED, CONGETITALANOMALY,OTHER, DATEOFEVENT, DATEOFREPORT, DATEREPORTCLOSED, AEOPPID,))
        
        cur.execute("UPDATE reportcompletedby SET RepCompany = %s, RepName = %s, RepAddress = %s, RepCity = %s, RepState = %s, RepPhone = %s WHERE RcBID = %s",(REPCOMPANY, REPNAME, REPADDRESS, REPCITY , REPSTATE, REPPHONE, RCBID,))
        
        cur.execute("UPDATE EventInformation SET DescribeEoP = %s, Findings= %s WHERE EvENTID = %s",(DESCRIBE,FINDINGS, EVENTID,))
        
        cur.execute("UPDATE AlsoReportedTo SET Manufacturer =  %s, UserFacility = %s, DistributorImporter = %s WHERE artID = %s",(MANUFACTURER, USERFACILITY, DISTRIBUTORIMPORTER, ARTID))
        
        cur.execute("UPDATE SignOff SET Signature = %s, DateCompleted = %s WHERE soID = %s",(SIGNATURE, DATECOMP,SOID))

        mysql.connection.commit()
        cur.close() 
        return render_template("Homepage.html", adminitem=adminitem)
    return render_template("Homepage.html", adminitem=adminitem)  

if __name__ == '__main__':
    main.run(debug=True)