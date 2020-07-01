import unittest
from tests.home.login_tests import loginTests
from tests.courses.register_courses_tests_csv_data import registerCoursesCSVDataTests

# Get all tests from test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(loginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(registerCoursesCSVDataTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)