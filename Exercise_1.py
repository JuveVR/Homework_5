#1.1
class Person:
    """ Class handle with instances that includes personal data of persons """
    def __init__(self, full_name = "", birth_year = None):
        """
        Defines two parameters for Person class instances. Validate parameters value.
        :param full_name: Full Name of the Person should consists of 2 words
        :param birth_year: When the person was born
        """
        self.full_name = full_name
        self.birth_year = birth_year
        if type(self.full_name) != str or self.full_name.count(" ") == 0:
            raise Exception("There value is not string or string consists of 1 word")
        else:
            pass
        if 1900 < self.birth_year < 2019:
            pass
        else:
            raise ValueError("Year value is out of allowed range")


    def name(self):
        """
        :return: Persons name
        """
        return self.full_name[0:self.full_name.index(" ")]
    def surname(self):
        """
        :return: Persons surname
        """
        return self.full_name[self.full_name.index(" ")+1:]
    def years_old(self, year = 2019):
        """
        Calculate persons age in the certain year
        :param year: certain year when you check persons age
        :return: persons age
        """
        return year - self.birth_year


#1.2
class Employee(Person):
    """Class add Employee parameters to Persons class instances"""
    def __init__(self, full_name = "", birth_year = 0, position = "", experience = 0, salary = 0):
        """
        Defines additional parameters for Employee class instances.
        :param full_name: inherits from class Person
        :param birth_year: inherits from class Person
        :param position: position of the Employee
        :param experience: Employee experience
        :param salary: Employee salary
        """
        Person.__init__(self, full_name, birth_year)
        self.position = position
        self.experience = experience
        self.salary = salary
        if self.experience < 0 or self.salary < 0:
            raise ValueError("Salary or Experience value cannot be negative")
        else:
            pass

    def position_level(self):
        """
        :return: position level based on Employee experience
        """
        b = None
        if self.experience < 3:
            b = "Junior {}".format(self.position)
        elif 3 <= self.experience <= 6:
            b = "Middle {}".format(self.position)
        else:
            b = "Senior {}".format(self.position)
        return b

    def salary_raise(self, amount):
        """
        Calculates salary after raise
        :param amount: amount of raise
        :return: salary after raise
        """
        return self.salary + amount




#1.3

class ITEmployee(Employee):
    """Class add ITEmployee parameters to Employee class instances """
    def __init__(self, *args, **kwargs):
        """
        Add possibility to add skills to ITEmployee
        :param args: inherits from Employee
        :param kwargs: inherits from Employee
        """
        Employee.__init__(self, *args, **kwargs)
        self.skills = []
    def add_skill(self, new_skill):
        """ Adds one value mentioned in arg to objects property skills"""
        self.skills.append(new_skill)
    def add_skills(self, *args ):
        """ Adds all values mentioned in args to objects property skills"""
        for skill in args:
            self.skills.append(skill)







if __name__ == "__main__":
    p1 = Person("Artur Pirozkov", 2000)
    print(p1.name())
    print(p1.surname())
    print(p1.years_old(2020))
    e1 = Employee("Gogi Suhishvili", 1992, "cleaner", 2, 14878)
    print("*" * 30)
    print(e1.position_level())
    print(e1.salary_raise(1488))
    it1 = ITEmployee(full_name="Valera Leontiev", experience=3, position="plotnik", birth_year=1950)
    print("*" * 30)
    print(it1.name())
    print(it1.position_level())
    it1.add_skill("QA Automation")
    it1.add_skill("lazy_ass")
    print(it1.skills)
    it1.add_skills("Selenium", "Python", "Mentoring")
    print(it1.skills)