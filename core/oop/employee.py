class Employee:
    __count_obj = 0
    emp_id = None

    def __init__(self, empid):
        self.emp_id = empid
        Employee.__count_obj += 1


# obj = Employee(1001)
# obj2 = Employee(23)
Employee.__count_obj = 10
print(Employee.__count_obj)
