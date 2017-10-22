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

