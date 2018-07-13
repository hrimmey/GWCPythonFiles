#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
numbers = ["1", "2", "3", "5", "6", "7", "9"]
numbersE = ["2", "4", "6", "8"]
numbersO = ["1", "3","5", "7", "9"]
list = []


def main():
    print("Only Even Numbers Wanted.")
    print(printEvens(numbers))

def printEvens(numbers):
    for x in numbers:
        if isEven(x):
            list.append(x)
        if not isEven(x):
            continue
    return list

def isEven(x):
    if x in numbersE:
        return True
    elif x in numbersO:
        return False


if __name__ == "__main__":
  main()

print("Barack and Michelle are actual life goals")
print("Tsemaye should stop trying to make me a positive person")
