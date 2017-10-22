
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
