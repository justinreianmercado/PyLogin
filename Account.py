class Account:
    def __init__(self, firstName="", lastName="", username="", password="", phoneNumber="",
                 recoveryMethod=-1, recoveryEmail="", recoveryPhone=""):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.phoneNumber = phoneNumber
        self.recoveryMethod = recoveryMethod
        self.recoveryEmail = recoveryEmail
        self.recoveryPhone = recoveryPhone
