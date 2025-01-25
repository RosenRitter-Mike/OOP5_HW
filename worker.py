from employee import Employee


class Worker(Employee):
    def __init__(self, id, name, address, age, year_of_birth, hours_per_day, hour_rate):
        super().__init__(id, name, address, age, year_of_birth)
        self.__hours_per_day = hours_per_day
        self.__hour_rate = hour_rate

    def calculateSalary(self):
        return self.__hour_rate * self.__hours_per_day

    def __str__(self):
        return (f"{super().__str__()}"
                f"[Worker] hours per day: {self.__hours_per_day}\n"
                f"[Worker] hour rate: {self.__hour_rate}\n"
                f"[Worker] salary: {self.calculateSalary()}\n")