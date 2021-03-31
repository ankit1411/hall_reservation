class users:
    def __init__(self):
        self.name=0
        self.username = 0
        self.pword = 0
        self.ph_num = 0
        self.email = 0

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name

    def set_uname(self,uname):
        self.username=uname

    def get_uname(self):
        return self.username

    def set_pass(self,passw):
        self.pword=passw

    def get_pass(self):
        return self.pword

    def set_ph_num(self,phone):
        self.ph_num=phone

    def get_ph_num(self):
        return self.ph_num

    def set_email(self,mail):
        self.email=mail

    def get_email(self):
        return self.email

    def printg(self):
        print("hello")



