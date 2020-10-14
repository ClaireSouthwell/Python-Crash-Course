'''Write a test case for Employee. Write two test methods, test_give_default
_raise() and test_give_custom_raise(). Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.'''


import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    #our class TestEmployee inherits from the class unittest.TestCase
    
    '''Tests for the class Employee'''

    def setUp(self):
    # the setUp method allows us to create one employee used for all tests
        first_name = 'Brad'
        last_name = 'Pitt'
        salary = 5000000

        self.my_employee = Employee(first_name, last_name, salary)

    def test_give_default_raise(self):
        '''test that the default raise is given correctly'''
        self.my_employee.give_raise()
        self.assertEqual(5005000, self.my_employee.salary)

    def test_give_custom_raise(self):
        '''test that a custom raise is given correctly'''
        self.my_employee.give_raise(6)
        self.assertEqual(5000006, self.my_employee.salary)

if __name__ == '__main__':
    unittest.main()

# Note that the 2 tests are run independently
# salary value is rest to $5mil for each test
