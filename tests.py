import unittest
from oop import SignUp


class TestSignup(unittest.TestCase):

    def setUp(self):
        self.signup = SignUp('chuck', 'mark', 'chuck1@mark.com')
        self.user2 = SignUp('dude', 'mike', 'mike@dude.com')
        self.user = self.signup.submit()[0]

    def test_combined_name(self):
        self.assertEqual('chuckmark', self.signup.combined_name())

    # @unittest.expectedFailure
    def test_valid_email(self):
        self.assertFalse(self.signup.validate_email('chuck.zbxcjzhx.com'))
        self.assertFalse(self.signup.validate_email('chuck#cnjcjs.com'))
        self.assertFalse(self.signup.validate_email('chuck@.com'))
        self.assertFalse(self.signup.validate_email('chuck@.12312312'))

    def test_submit(self):
        self.assertIs(list, type(self.signup.submit()))

    def test_submit_lenght(self):
        self.assertEqual(1, len(self.signup.submit()))

    def test_submit_lenght(self):
        self.assertIs(dict, type(self.user))

    def test_submit_user_object(self):
        self.assertEqual(
            {'first_name': 'chuck', 'last_name': 'mark', 'email': 'chuck1@mark.com'}, self.user)


if __name__ == '__main__':
    unittest.main(verbosity=2)
