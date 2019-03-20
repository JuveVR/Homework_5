import unittest
from Homework_5.Exercise_1 import ITEmployee

class TestInitExceptions(unittest.TestCase):
    def test_birth_year_exp(self):
        with self.assertRaises(ValueError):
            self.slave = ITEmployee(full_name="Vadym Rovenko", birth_year = 1800)
    def test_space(self):
        with self.assertRaises(Exception) as ex:
            self.slave = ITEmployee(full_name="VadymRovenko", birth_year = 1990)
        self.assertEqual("There value is not string or string consists of 1 word", str(ex.exception))
    def test_experience_exep(self):
        with self.assertRaises(ValueError) as ve:
            self.slave = ITEmployee(full_name="Vadym Rovenko", experience=-5, birth_year = 1990)
        self.assertEqual("Salary or Experience value cannot be negative", str(ve.exception))
    def test_salary_exep(self):
        with self.assertRaises(ValueError) as ve:
            self.slave = ITEmployee(full_name="Vadym Rovenko", salary = -1000, birth_year = 1990)
        self.assertEqual("Salary or Experience value cannot be negative", str(ve.exception))

class TestItEmployeeName(unittest.TestCase):
    def setUp(self):
        self.slave = ITEmployee(full_name="Vadym Rovenko", birth_year = 1990)
    def test_name_return(self):
        self.assertEqual(self.slave.name(), "Vadym")
    def test_surname_return(self):
        self.assertEqual(self.slave.surname(), "Rovenko")
    def test_years_old(self):
        self.assertEqual(self.slave.years_old(), 29)

class TestItEmployeeSkills(unittest.TestCase):
    def setUp(self):
        self.slave = ITEmployee(full_name="Vadym Rovenko", birth_year=1990)
    def test_no_skills(self):
        self.assertEqual(len(self.slave.skills), 0)
    def test_skill_addition(self):
        self.slave.add_skill("python")
        self.assertIn("python", self.slave.skills)
        self.assertEqual(len(self.slave.skills), 1)

class TestPosition(unittest.TestCase):
    def test_jun(self):
        slave = ITEmployee(full_name="Vadym Rovenko", birth_year=1990, position="QA", experience=0)
        self.assertEqual(slave.position_level(), "Junior QA")
    def test_mid(self):
        slave = ITEmployee(full_name="Vadym Rovenko", birth_year=1990, position="QA", experience=3)
        self.assertEqual(slave.position_level(), "Middle QA")
    def test_sen(self):
        slave = ITEmployee(full_name="Vadym Rovenko", birth_year=1990, position="QA", experience=29)
        self.assertEqual(slave.position_level(), "Senior QA")

    def test_salary_raise(self):
        slave = ITEmployee(full_name="Vadym Rovenko", birth_year=1990, salary=2000)
        self.assertEqual(slave.salary_raise(1000), 3000)


