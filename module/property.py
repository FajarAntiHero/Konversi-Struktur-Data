import os
import time as tm
from termcolor import colored
from colorama import init

init()

class Property:
    singleLine: str = "-"*100
    doubleLine: str = "="*100
    
    @classmethod
    def dynamicHeader(cls, headerName: str) -> None:
        print(Property.doubleLine)
        print(colored("{:^100}".format(headerName.upper()), 'green'))
        print(Property.doubleLine)

    @classmethod
    def dynamicSubHeader(cls, headerName: str) -> None:
        print(Property.singleLine)
        print(colored("{:^100}".format(headerName.upper()), "green"))
        print(Property.singleLine)

    @classmethod
    def writeDescription(cls, information: str, limit: int) -> None:
        while len(information) > limit:
        # Find the last space before the character limit to avoid cutting words
            split_index = information.rfind(' ', 0, limit)
            if split_index == -1:
                split_index = limit  # If there's no space, split at the limit
            print((information[:split_index]))
            information = information[split_index:].lstrip()

        print(information)  # Print the remaining part that is shorter than the limit

    @classmethod
    def clearTerminal(cls) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @classmethod
    def pauseProgram(cls, time: int) -> None:
        tm.sleep(time)

    @classmethod
    def customPrint(cls, value: str, color: str):
        print(colored(value, color))

    
