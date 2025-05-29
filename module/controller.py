from .property import Property
from .model import Model
from .stack import Stack as st
from .queue import Queue as qu
import colorama
import termcolor

class Controller:

    def __init__(self) -> None:
        self.__assignObject = Model([])
        self.__object = None

    def main(self) -> None:
        while True:
            Property.clearTerminal()
            Property.dynamicHeader("program konversi struktur data")
            Property.dynamicSubHeader("input data")
            try:
                self.jumlahData = int(input("{:<50}".format("Masukkan Jumlah Data yang akan dikonversi : ")))
                print(Property.singleLine)
                if self.jumlahData > 0 :
                    for jumlahData in range(self.jumlahData):
                        inputData = int(input("{:<50}".format(f"Masukkan nilai data ke {jumlahData + 1} : ")))
                        print(Property.singleLine)
                        self.__assignObject.setData = inputData
                    Property.pauseProgram(2)
            except TypeError:
                print()
            
            Property.clearTerminal()
            Property.dynamicHeader("program konversi struktur data")
            Property.dynamicSubHeader("pilih jenis data yang akan dikonversi")
            Property.customPrint("{:<100}".format("1. Matrix"),  (255, 0, 255))
            Property.customPrint("{:<100}".format("2. Linked List"), 'light_yellow')
            Property.customPrint("{:<100}".format("3. Stack"), 'cyan')
            Property.customPrint("{:<100}".format("4. Queue"), 'light_blue')
            Property.customPrint("{:<100}".format("5. Graph"), 'light_red')
            print(Property.singleLine)

            while True:
                inputJenisData = str(input("{:<50}".format("Pilih jenis data [1/2/3/4/5] : ")))
                if inputJenisData == "1" or inputJenisData == "2" or inputJenisData == "3" or inputJenisData == "4" or inputJenisData == "5":
                    break
                else:
                    Property.customPrint("{:^100}".format("pilihan anda tidak sesuai!".upper()), 'red')

            match inputJenisData:
                case "1":
                    self.__object = ""
                case "2":
                    self.__object = ""
                case "3":
                    self.__object = qu(self.__assignObject.getData)
                case "4":
                    self.__object = st(self.__assignObject.getData)
                case "5":
                    self.__object = ""

            self.__object.main()
            break