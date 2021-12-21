from UserRegistrationException import UserRegistrationException
import re


class UserRegistration:
    '''Here We are performing a user registration
        program in which exception and regex is used.
        For the following the test case is bieng created'''

    def getter_first_name(self):
        return self.first_name

    def setter_first_name(self, first_name):
        if first_name == "":
            raise UserRegistrationException("First name empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", first_name):
            self.first_name = first_name
        else:
            raise UserRegistrationException('Invalid ')

    def getter_last_name(self):
        return self.last_name

    def setter_last_name(self, last_name):
        if last_name == "":
            raise UserRegistrationException("Last name empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", last_name):
            self.last_name = last_name
        else:
            raise UserRegistrationException('Invalid')

    def getter_mobile_no(self):
        return self.mobile_no

    def setter_mobile_no(self, mobile_no):
        if mobile_no == "":
            raise UserRegistrationException("Mobile Number empty")
        if re.fullmatch("^([91]{2}[ ])?[0-9]{10}$", mobile_no):
            self.mobile_no = mobile_no
        else:
            raise UserRegistrationException('Invalid')

