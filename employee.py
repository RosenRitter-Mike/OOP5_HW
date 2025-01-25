from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Employee(ABC):
    @abstractmethod
    def __init__(self, id, name, address, age, year_of_birth):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__age = age
        self.__year_of_birth = year_of_birth

    @abstractmethod
    def calculateSalary(self):
        pass

    def __str__(self):
        return (f"[Employee] id: {self.__id}\n"
                f"[Employee] name: {self.__name}\n"
                f"[Employee] address: {self.__address}\n"
                f"[Employee] declared age: {self.__age}\n"
                f"[Employee] year of birth: {self.__year_of_birth}\n"
                f"[Employee] calculated age: {self.get_age()}\n")

    def get_age(self):
        return datetime.now().year - self.__year_of_birth
