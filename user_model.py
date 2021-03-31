class User:
    def __init__(self, name=None, username=None, password=None, phone_number=None, email_id=None):
        self._name = name
        self._username = username
        self._password = password
        self._phone_number = phone_number
        self._email_id = email_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name= name


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,username):
        self._username= username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password= password

    @property
    def phone_number(self):
        return self._phone_number    

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number= phone_number

    @property
    def email_id(self):
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        self._email_id= email_id


