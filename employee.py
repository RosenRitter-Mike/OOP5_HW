from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def __init__(self, id, name, address, age):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__age = age

    @abstractmethod
    def calculateSalary(self):
        pass

    def __str__(self):
        return (f"[Employee] id: {self.__id}\n"
                f"[Employee] name: {self.__name}\n"
                f"[Employee] address: {self.__address}\n"
                f"[Employee] age: {self.__age}\n")