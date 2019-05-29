import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('SetUp')
        self.emp_1 = Employee('Adam', 'Opalka', 50000)
        self.emp_2 = Employee('Ewa', 'Nosacz', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        # emp_1 = Employee('Adam', 'Opalka', 50000)
        # emp_2 = Employee('Ewa', 'Nosacz', 60000)

        self.assertEqual(self.emp_1.email, 'Adam.Opalka@email.com')
        self.assertEqual(self.emp_2.email, 'Ewa.Nosacz@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Opalka@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Nosacz@email.com')

    def test_fullname(self):
        print('test_fullname')
        # emp_1 = Employee('Adam', 'Opalka', 50000)
        # emp_2 = Employee('Ewa', 'Nosacz', 60000)

        self.assertEqual(self.emp_1.fullname, 'Adam Opalka')
        self.assertEqual(self.emp_2.fullname, 'Ewa Nosacz')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Opalka')
        self.assertEqual(self.emp_2.fullname, 'Jane Nosacz')

    def test_apply_raise(self):
        print('test_apply_raise')
        # emp_1 = Employee('Adam', 'Opalka', 50000)
        # emp_2 = Employee('Ewa', 'Nosacz', 60000)

        self.emp_1.apply_raise
        self.emp_2.apply_raise

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assort_called_with('http://company.com/Opalka/May')
            self.assertEqual(schedule, 'Success')

            # schedule = self.emp_2.monthly_schedule('June')
            # mocked_get.assort_called_with('http://company.com/Nosacz/June')
            # self.assertEqual(schedule, 'Bad Response')


if __name__ == '__main__':
    unittest.main()
