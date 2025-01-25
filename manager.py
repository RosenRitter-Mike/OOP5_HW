from employee import Employee


class Manager(Employee):
    def __init__(self, id, name, address, age, number_of_employees, employee_rate):
        super().__init__(id, name, address, age)
        self.__number_of_employees = number_of_employees
        self.__employee_rate = employee_rate

    def calculateSalary(self):
        return self.__number_of_employees * self.__employee_rate

    def __str__(self):
        return (f"{super().__str__()}"
                f"[Manager] number of employees: {self.__number_of_employees}\n"
                f"[Manager] employee rate: {self.__employee_rate}\n"
                f"[Manager] salary: {self.calculateSalary()}\n")
