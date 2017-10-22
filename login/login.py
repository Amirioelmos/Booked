
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

