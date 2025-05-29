import os
import time as tm

class Property:
    singleLine: str = "-"*100
    doubleLine: str = "="*100
    __database: list = []

    def __init__(self):
        self.jumlahData = 0

    
    @classmethod
    def dynamicHeader(cls, headerName: str) -> None:
        print(Property.doubleLine)
        print("{:^100}".format(headerName.upper()))
        print(Property.doubleLine)

    @classmethod
    def dynamicSubHeader(cls, headerName: str) -> None:
        print(Property.singleLine)
        print("{:^100}".format(headerName.upper()))
        print(Property.singleLine)

    @classmethod
    def writeDescription(cls, information: str, limit: int) -> None:
        while len(information) > limit:
        # Find the last space before the character limit to avoid cutting words
            split_index = information.rfind(' ', 0, limit)
            if split_index == -1:
                split_index = limit  # If there's no space, split at the limit
            print(information[:split_index])
            information = information[split_index:].lstrip()

        print(information)  # Print the remaining part that is shorter than the limit

    @classmethod
    def clearTerminal(cls) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @classmethod
    def pauseProgram(cls, time: int) -> None:
        tm.sleep(time)

    @property
    def getDatabase(self) -> list:
        return Property.__database
    
    @getDatabase.setter
    def setDatabase(self, value: int) -> None:
        Property.__database.append(value)

    def main(self) -> None:
        while True:
            Property.clearTerminal()
            Property.dynamicHeader("program konversi struktur data")
            Property.dynamicSubHeader("input data")
            try:
                self.jumlahData = int(input("{:<50}".format("Masukkan Jumlah Data yang akan dikonversi : ")))
                for jumlahData in range(self.jumlahData):
                    inputData = int(input("{:<50}".format(f"Masukkan data ke {jumlahData} : ")))
                    self.setDatabase = inputData
            except TypeError:
                print()
            
            Property.clearTerminal()
            Property.dynamicHeader("program konversi struktur data")
            Property.dynamicSubHeader("pilih  jenis data yang akan dikonversi")
            print("{:<100}".format("1. Matrix"))
            print("{:<100}".format("2. Linked List"))
            print("{:<100}".format("3. Stack"))
            print("{:<100}".format("4. Queue"))
            print("{:<100}".format("5. Graph"))
            print(Property.singleLine)

            while True:
                inputJenisData = str(input("{:<50}".format("Pilih jenis data [1/2/3/4/5] : ")))
                if inputJenisData == "1" or inputJenisData == "2" or inputJenisData == "3" or inputJenisData == "4" or inputJenisData == "5":
                    break
                else:
                    print("{:^100}".format("pilihan anda tidak sesuai!".upper()))

            match inputJenisData:
                case "1":
                    object = ""
                    break
                case "2":
                    object = ""
                    break
                case "3":
                    object = ""
                    break
                case "4":
                    object = ""
                    break
                case "5":
                    object = ""
                    break
