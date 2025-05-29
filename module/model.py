class Model:
    
    def __init__(self, data: list = []):
        self.__data: list = data

    @property
    def getData(self) -> list:
        return self.__data
    
    @getData.setter
    def setData(self, value: int) -> None:
        self.__data.append(value)