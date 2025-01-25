from employee import Employee


class Contractor(Employee):
    def __init__(self, id, name, address, age, number_of_projects, project_rate):
        super().__init__(id, name, address, age)
        self.__number_of_projects = number_of_projects
        self.__project_rate = project_rate

    def calculateSalary(self):
        return self.__project_rate * self.__number_of_projects

    def __str__(self):
        return (f"{super().__str__()}"
                f"[Worker] number of projects: {self.__number_of_projects}\n"
                f"[Worker] project rate: {self.__project_rate}\n"
                f"[Worker] salary: {self.calculateSalary()}\n")
