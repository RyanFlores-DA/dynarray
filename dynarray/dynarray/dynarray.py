from typing import List

class Dynarray:
    def __init__(self):
        self.__index_variable = {i: [] for i in range(1, 10)}
        self.__CURRENT_INDEX = None

    def index_object(self, value: str) -> "Dynarray":
        first_digit = int(str(value)[0])
        if first_digit in self.__index_variable:
            self.__CURRENT_INDEX = first_digit
        return self     

    def set(self, value: tuple) -> None:
        if self.__CURRENT_INDEX:
            self.__index_variable[self.__CURRENT_INDEX].append(value)

    def get(self) -> List[tuple] | None:
        if self.__CURRENT_INDEX:
            return self.__index_variable[self.__CURRENT_INDEX]
