import re


class SignUp(object):
    """Sign class to handle users"""

    def __init__(self, first_name, last_name, email_address='chucky@gmail.com'):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = SignUp.validate_email(email_address)
        self.db = []

    def user():
        pass

    def combined_name(self):
        ''' Combine the first name and last name of the user '''
        self.name = self.first_name + self.last_name
        # print(self.name)
        return self.name

    def submit(self):
        self.user = {'first_name': self.first_name,
                     'last_name': self.last_name, 'email': self.email_address}
        self.db.append(self.user)
        print(self.db)

    @staticmethod
    def validate_email(email_address):
        pattern = re.compile("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$")
        if not pattern.match(email_address):
            print('Not a valid email')
            return False
        else:
            print('email is valid')
            return email_address


signup = SignUp('chuck', 'mark')
signup.combined_name()
signup.submit()
