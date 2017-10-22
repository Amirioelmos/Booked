#!/usr/bin/python
import psycopg2
import string
import random
from random import randint



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


class DataBase():
    def __init__(self):
        print "\n DB "
        self.hostname = 'localhost'
        self.username = 'booked'
        self.password = 'booked'
        self.database = 'booked'
        self.myConnection = psycopg2.connect(host=self.hostname, user=self.username, password=self.password, dbname=self.database)
        self.connection = self.myConnection.cursor()
    def select(self,query):
        self.connection.execute(query)
        return self.connection
    def insert(self):
        for i in range (0,100):
            print i
            randomString = id_generator()
            self.query = "insert INTO test (name,id) values ('{0}',{1});".format(randomString,randint(0,1000))
            self.connection.execute(self.query)

    def userDefined(self,email,passwd):
        self.email = email
        self.passwd = passwd
        query = "select * from users where email='{0}' and password='{1}';".format(self.email,self.passwd)
        self.connection.execute(query)
        if self.connection.fetchone() != None:
            return True
        else:
            return False




class login:
    def __init__(self):
        print("\n Login")
        # self.email = email
        # self.passwd = passwd

    def enterEmail(self, email):
        self.email = email
        check = clientLoginValidation()
        checkEmail = check.checkEmailValid(self.email)
        if checkEmail:
            print ("\nEmail Ascepted")
        else:
            print ("inValid Eamil")

    def enterPasswd(self,passwd):
        self.passwd = passwd
        check = clientLoginValidation()
        checkPass = check.checkPassValid(self.passwd)
        if checkPass:
            print ("\nPassword Ascepted")
        else:
            print ("inValid Pass")

    def submit(self):
        serverSubmit = serverLoginValidation(self.email, self.passwd)
        validUser = serverSubmit.validateUser()
        if validUser:
            print("\n Show Home User Page")
        else:
            print("\n Error in Validation of User In server")



import re

class clientLoginValidation:
    def __init__(self):
        print ("clientLoginValidation")

    def checkEmailValid(self,email):
        self.email = email
        self.matchMail = re.match(r'(.*)@(.*).iust.ac.ir', self.email, re.M|re.I)
        if self.matchMail:
            return True
        else:
            return False

    def checkPassValid(self,passwd):
        self.passwd = passwd
        self.matchPass = re.match(r'([a-zA-Z0-9].+)', self.passwd, re.M|re.I)
        if self.matchPass:
            return True
        else:
            return False


class serverLoginValidation():
    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd

    def validateUser(self):
        self.db = DataBase()
        self.userdata = self.db.userDefined(self.email, self.passwd)
        if self.userdata:
            return True
        else:
            return False



mylogin = login()
mylogin.enterEmail("am_zare@comp.iust.ac.ir")
mylogin.enterPasswd("amirio")
mylogin.submit()
