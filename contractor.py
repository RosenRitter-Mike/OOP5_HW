from employee import Employee


class Contractor(Employee):
    def __init__(self, id, name, address, age, year_of_birth,number_of_projects, project_rate):
        super().__init__(id, name, address, age, year_of_birth)
        self.__number_of_projects = number_of_projects
        self.__project_rate = project_rate

    def calculateSalary(self):
        return self.__project_rate * self.__number_of_projects

    def __str__(self):
        return (f"{super().__str__()}"
                f"[Contractor] number of projects: {self.__number_of_projects}\n"
                f"[Contractor] project rate: {self.__project_rate}\n"
                f"[Contractor] salary: {self.calculateSalary()}\n")
