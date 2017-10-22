
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
