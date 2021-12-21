import unittest
from UserRegistration import UserRegistration
from UserRegistrationException import UserRegistrationException


class TestUserRegistration(unittest.TestCase):
    def test_first_name_valid(self):
        expected = 'Shreesh'
        object_user = UserRegistration()
        object_user.setter_first_name(expected)
        self.assertEqual(expected, object_user.getter_first_name())

    def test_first_name_invalid(self):
        expected = 'shreesh'
        object_user = UserRegistration()
        try:
            object_user.setter_first_name(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid", exception.__str__())

    def test_first_name_empty(self):
        expected = ''
        object_user = UserRegistration()
        try:
            object_user.setter_first_name(expected)
        except UserRegistrationException as exception:
            self.assertEqual("First Name Empty", exception.__str__())

    def test_last_name_is_valid(self):
        expected = 'Pandey'
        object_user = UserRegistration()
        object_user.setter_last_name(expected)
        self.assertEqual(expected, object_user.getter_last_name())

    def test_last_name_is_invalid(self):
        expected = 'pandey'
        object_user = UserRegistration()
        try:
            object_user.setter_last_name(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid", exception.__str__())

    def test_last_name_is_empty(self):
        expected = ''
        object_user = UserRegistration()
        try:
            object_user.setter_last_name(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Last name empty", exception.__str__())

    def test_mobile_no_is_valid(self):
        expected = "91 9454977489"
        object_user = UserRegistration()
        object_user.setter_mobile_no(expected)
        self.assertEqual(expected, object_user.getter_mobile_no())

    def test_mobile_no_is_invalid(self):
        expected = "247963247921488"
        object_user = UserRegistration()
        try:
            object_user.setter_mobile_no(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid", exception.__str__())

    def test_mobile_no_is_empty(self):
        expected = ""
        object_user = UserRegistration()
        try:
            object_user.setter_mobile_no(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid", exception.__str__())


if __name__ == '__main__':
    unittest.main()

