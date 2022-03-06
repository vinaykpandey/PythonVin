class Student:
    """
    This is regarding
    student
    """
    name = 'Student'

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__avg()

    def avg(self):
        print("average")
        self.__avg()

    def __avg(self):
        """
        This will used to calculate average
        """
        print("::::: name::: ", self.name)
        self.name = "Vinay Pandey"
        # self.info()
        # self.show()
        _avg = (self.a + self.b) / 2
        print(_avg)

    @classmethod
    def info(cls):
        print("Info called")
        cls.a = 100
        cls.name = "Dev Pandey"
        # cls.show()
        return cls.name

    @staticmethod
    def show():
        """
        This will used to show info
       """
        print("show called")
        return "This is a student"


s1 = Student(10, 20)
s1.avg()
# s1.avg()
# Student.info()
# print(s1.name)
# print(Student.name)
# s_info = Student.info()
# s_info_s = s1.show()
# print(s1)
# print(s_info)
# print(s_info_s)
# print(s1.a)
# s1.avg()
